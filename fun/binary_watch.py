

# Leetcode Q401. Binary Watch
# A binary watch has 4 LEDs on the top to represent the hours (0-11),
# and 6 LEDs on the bottom to represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM),
# return all possible times the watch could represent. You may return the answer in any order.
# The hour must not contain a leading zero.
#  For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.
#  For example, "10:2" is not valid. It should be "10:02".



def get_time(combo :List[int]) -> str :

	H = 0
	M = 0

	for c in combo:

		if c <6: M += 1 <<c
		else: H += 1 <<(c -6)
	if	H <12 and M <60: return f"{H}:{str(M).zfill(2)}"

def readBinaryWatch(turnedOn: int) -> List[str]:
	return list(filter(bool,( get_time(c) for c in combinations(range(10), turnedOn) if c ))) if turnedOn else [ "0:00" ]

