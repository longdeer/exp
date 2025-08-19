from os			import rename
from os			import path
from sys		import argv
from datetime	import datetime








def trim_CR(pwd :str, *targets :str):


	if	path.isabs(pwd):
		for file in targets:


			if not path.isabs(file): file = path.join(pwd, file)
			target = path.join(pwd, str(datetime.now().timestamp()))


			with open(target, "w") as tmp:
				with open(file) as ent:
					for line in ent : tmp.write(f"{line.strip('\r').strip('\n')}\n")


			rename(target, file)
			print(f"info: trimmed {file}")
	else:	print("error: working directory must be an absolute path")








if	__name__ == "__main__":


	try:	trim_CR(argv[1], *argv[2:])
	except	IndexError : print("error: arguments must be target directory and file names")
	except	Exception as E : print(f"{E.__class__.__name__}: {E}")







