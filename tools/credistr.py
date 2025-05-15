







def cred(creds_file_path :str =None) -> str or None :

	"""
		Opens file and returns content string. It is assumed to be used with special files,
		which contatin single line, like password, token, or somthing similar.
		Only works in silent mode (very silent).
	"""

	try:

		with	open(creds_file_path) as raw:
				return raw.read().rstrip("\n")
	except:		return







