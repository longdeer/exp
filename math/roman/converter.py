

def int_to_roman(self, num: int) -> str:

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

