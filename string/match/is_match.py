

# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#  '.' Matches any single character.
#  '*' Matches zero or more of the preceding element.
#  The matching should cover the entire input string (not partial).


def isMatch(s: str, p: str, fms=0, fmp=0, dyna=dict()) -> bool:

	dyna = dict()
	def deep(fms, fmp) -> bool:

		if	( fms,fmp ) not in dyna:
			dyna[fms,fmp] = (

				not (len(s) -fms)

			)	if	not (len(p) -fmp) else (

				deep(fms,fmp+2) or
				(fms <len(s) and p[fmp] in ( s[fms],"." )) and
				deep(fms+1,fmp)

			)	if	(fmp +1) <len(p) and p[fmp+1] == "*" else (

				(fms <len(s) and p[fmp] in ( s[fms],"." )) and
				deep(fms+1,fmp+1)

			)

		return	dyna[fms,fmp]
	return		deep(0,0)

