from bisect import bisect_left
from bisect import bisect_right


def binclude_count(arr :List[int], start :int, end :int, sort=True) -> int :

	"""
		Count how many elements from ["start","end"] range is in "arr".
		"sort" flag regulates wether "arr" must be sorted or not (already sorted).
	"""

	if sort : arr.sort()
	return bisect_right(arr,start) - bisect_left(arr,end)

