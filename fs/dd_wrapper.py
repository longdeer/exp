#!/usr/bin/env python3
import subprocess
import re
import os
import json
from argparse import ArgumentParser

def shell_exec(cmd: str):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', shell=True)
	ret_code = proc.wait()
	if ret_code != 0:
		raise RuntimeError(f'"{cmd}" return {ret_code}')
	return proc.communicate()

def get_device_size(dev: str):
	stdout, stderr = shell_exec(f"blockdev --getsize64 '{dev}'")
	return int(stdout)

def maybe_wipe_fs(dev: str, warning: str):
	print(warning)
	print(f'Script WILL DESTROY the file system, partitions or any data on testing device.')
	agree = input("Are you sure you want to continue (yes/no)? ")
	if (agree != 'yes'):
		raise RuntimeError('aborted')
	shell_exec(f"wipefs --all '{dev}'")

def is_mounted(cmd: str, device: dict):
	NOT_FOUND = object()
	mnt = device.get("mountpoints", device.get("mountpoint", NOT_FOUND))
	if mnt == NOT_FOUND:
		raise RuntimeError(f'Failed to get device mountpoint, check: "{cmd}"')
	if mnt not in ([], [None], None):
		return True
	if device.get("children") not in ([], [None], None):
		for child in device.get("children"):
			if is_mounted(cmd, child):
				return True
	return False

def check_device(dev: str):
	cmd = f"lsblk -J -i '{dev}'"
	stdout, stderr = shell_exec(cmd)
	data = json.loads(stdout)

	if "blockdevices" not in data or len(data["blockdevices"]) != 1:
		raise RuntimeError(f'Failed to get blockdevice, check: "{cmd}"')

	device = data["blockdevices"][0]

	if device.get("type") != "disk":
		raise RuntimeError(f'Device is not disk, check: "{cmd}"')

	if is_mounted(cmd, device):
		raise RuntimeError(f'Device "{dev}" is mounted, check: "{cmd}"')

	if device.get("children") not in ([], [None], None):
		maybe_wipe_fs(dev, f'Disk device have children (partitions), check: "{cmd}"')

	cmd = f"file --special-files '{dev}'"
	stdout, stderr = shell_exec(cmd)
	if stdout.strip() != f'{dev}: data':
		maybe_wipe_fs(dev, f'Device "{dev}" possible contains filesystem, check: "{cmd}"')

def parse_dd_size(size: str):
	# parse subset of possible suffixes of dd tool
	units = {"K": 2 ** 10, "KB": 10 ** 3,
			 "M": 2 ** 20, "MB": 10 ** 6,
			 "G": 2 ** 30, "GB": 10 ** 9,
			 "T": 2 ** 40, "TB": 10 ** 12}

	match = re.fullmatch(r'([0-9]+)([KMGT]B?)?', size)
	if not match:
		raise RuntimeError(f'Failed to parse bs "{size}"')
	number, unit = match.group(1), match.group(2)
	result = int(number)
	if unit is not None:
		result = result * units[unit]
	return result

def make_step(args, seek: int, dev_size : int):
	dd_cmd = f'dd if=/dev/zero of="{args.device}" bs={args.bs} count={args.bc} oflag=direct,seek_bytes seek={seek}'
	stdout, stderr = shell_exec(dd_cmd)
	percent = seek / dev_size * 100
	out = stderr.split(sep='\n')[2]
	print(f"seek={seek} ({percent:.1f}%): {out}")

def check_is_positive(name: str, val: int):
	if val <= 0:
		raise RuntimeError(f'"{name}" must be greater then 0')

if __name__ == "__main__":
	try:
		parser = ArgumentParser(description='Storage test. Script WILL DESTROY the file system, partitions or any data on testing device!')
		parser.add_argument('device', help='device for test, i.e /dev/sdb')
		parser.add_argument('--bs', help='block size for dd. Default is 2M.', default='2M')
		parser.add_argument('--bc', help='block count for dd. Default is 10000.', type=int, default=10000)
		parser.add_argument('--steps', help='number of steps exclude last. Default is 20.', type=int, default=20)
		parser.add_argument('--alignment', help='alignment of write operations. Default is 1024.', type=int, default=1024)
		args = parser.parse_args()

		args.bs = parse_dd_size(args.bs)
		check_is_positive("bs", args.bs)
		check_is_positive("bc", args.bc)
		check_is_positive("steps", args.steps)
		check_is_positive("alignment", args.alignment)

		if os.geteuid() != 0:
			raise RuntimeError('Script must be run as root')

		check_device(args.device)

		dev_size = get_device_size(args.device)
		for step in range(0, args.steps):
			seek = step * (dev_size // args.steps)
			seek = seek - (seek % args.alignment)
			make_step(args, seek, dev_size)

		write_size = args.bs * args.bc
		last_seek = dev_size - write_size
		last_seek = last_seek - (last_seek % args.alignment)
		make_step(args, last_seek, dev_size)

	except Exception as ex:
		print(f'ERROR: {ex}')
		exit(1)
	except KeyboardInterrupt as ex:
		print(f'\nERROR: interrupted')
		exit(1)