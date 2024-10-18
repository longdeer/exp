from typing	import Any
from typing	import List




def powerset(arr :List[Any]) -> List[Any] :

	if	not arr : return [[]]

	next_part	= powerset(arr[1:])
	first_part	= [[ arr[0] ] + part for part in next_part ]

	return	first_part + next_part



