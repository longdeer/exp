

def int_to_roman(num: int) -> str :

	roma,rem = "M" *(num //1000),num %1000

	if		900 <= rem	: roma,rem = roma + "CM",rem %900
	elif	500 <= rem	: roma,rem = roma + "D",rem %500
	elif	400 <= rem	: roma,rem = roma + "CD",rem %400

	roma,rem = roma + "C" *(rem //100),rem %100

	if		90 <= rem	: roma,rem = roma + "XC",rem %90
	elif	50 <= rem	: roma,rem = roma + "L",rem %50
	elif	40 <= rem	: roma,rem = roma + "XL",rem %40

	roma,rem = roma + "X" *(rem //10),rem %10

	if		9 <= rem	: roma,rem = roma + "IX",rem %9
	elif	5 <= rem	: roma,rem = roma + "V",rem %5
	elif	4 <= rem	: roma,rem = roma + "IV",rem %4

	return	roma + "I" *rem


def roman_to_int(s: str) -> int :

	total = 0
	skip = False
	
	for i,c in enumerate(s):
		if skip:

			skip = False
			continue

		match c:

			case "M": total += 1000
			case "D": total += 500
			case "L": total += 50
			case "V": total += 5
			case "C":

				try:
					match s[i+1]:

						case "D":

							total += 400
							skip = True
							continue

						case "M":

							total += 900
							skip = True
							continue

				except IndexError: pass
				total += 100

			case "X":
				try:
					match s[i+1]:

						case "L":

							total += 40
							skip = True
							continue

						case "C":

							total += 90
							skip = True
							continue

				except IndexError: pass
				total += 10

			case "I":
				try:
					match s[i+1]:

						case "V":

							total += 4
							skip = True
							continue

						case "X":

							total += 9
							skip = True
							continue

				except IndexError: pass
				total += 1

	return total

