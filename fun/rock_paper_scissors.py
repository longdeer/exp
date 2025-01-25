from random import choice








while	True:
	if	(player := input("chose:\n1 - rock\n2 - paper\n3 - scissors\n")) in "123":
		
		print(choice(( "you win", "you loose" )))
		break







