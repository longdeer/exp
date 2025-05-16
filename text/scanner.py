from os				import access	as osaccess
from os				import path		as ospath
from os				import R_OK
from pathlib		import Path
from typing			import Tuple








def byte_scan(path :str | Path) -> Tuple[bool,str] :

	"""
		Reads "path" file in byte mode and recreates whole text. If any not utf-8 symbol will be
		encountered, it will be substituted with "*" and "broken" flag will be set to True.
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

						case "\r":	text += "\n"
						case _:		text += symbol

				except:	text,broken = text + "*",True


		return	broken,	text
	return		True,	text







