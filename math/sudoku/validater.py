

def isValidSudoku(board :List[List[str]]) -> bool :

	vcol = [ list() for i in range(9) ]
	subs = {

		( "00","01","02", "10","11","12", "20","21","22" ) : list(),
		( "03","04","05", "13","14","15", "23","24","25" ) : list(),
		( "06","07","08", "16","17","18", "26","27","28" ) : list(),
		( "30","31","32", "40","41","42", "50","51","52" ) : list(),
		( "33","34","35", "43","44","45", "53","54","55" ) : list(),
		( "36","37","38", "46","47","48", "56","57","58" ) : list(),
		( "60","61","62", "70","71","72", "80","81","82" ) : list(),
		( "63","64","65", "73","74","75", "83","84","85" ) : list(),
		( "66","67","68", "76","77","78", "86","87","88" ) : list(),
	}

	for r,RAW in enumerate(board):

		vraw = list()

		for C,POINT in enumerate(RAW):

			if	POINT != ".":

				if	POINT in vraw	: return False
				if	POINT in vcol[C]: return False

				vraw.append(POINT)
				vcol[C].append(POINT)
				KEY = f"{r}{C}"

				for sub,box in subs.items():
					if	KEY in sub:

						if	POINT in box: return False
						box.append(POINT)

	return	True

