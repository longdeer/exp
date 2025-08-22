from os			import access	as osaccess
from os			import path		as ospath
from os			import R_OK
from pathlib	import Path
from typing		import Tuple








def utf8_broken_byte_scan(path :str | Path, carriage :bool =False) -> Tuple[bool,str] :

	"""
		Reads "path" file in byte mode and recreates whole text. If any not utf-8 symbol will be
		encountered, it will be substituted with "*" and "broken" flag will be set to True.
		Optional flag "carriage" allows treating carriage return symbol "\\r" as new line.
		Returns the tuple of "broken" flag and recreated text string. Doesn't handle any
		possible Exceptions, but ensures "path" is accessible file.
	"""

	text	= str()
	broken	= False

	if	isinstance(path, str | Path) and ospath.isfile(path) and osaccess(path, R_OK):

		with open(path, "rb") as file:
			while(B := file.read(1)):

				try:

					match (symbol := B.decode()):

						case "\r":	text += "\n" if carriage else ""
						case _:		text += symbol

				except:	text,broken = text + "*",True


		return	broken,	text
	return		True,	text








def utf8_byte_scan_collection(path :str | Path) -> str :

	"""
		Applies "utf8_broken_byte_scan" on the file at "path" and returns string
		which is set of lexicographically sorted symbols obtained from resulted text.
	"""

	scan = utf8_broken_byte_scan(path)
	return str().join(sorted(set(scan[1]))) + (" (broken)" if scan[0] else "")







