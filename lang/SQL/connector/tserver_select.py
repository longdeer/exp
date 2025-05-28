







if	__name__ == "__main__":


	import	mysql.connector
	from	mysql.connector			import errorcode
	from	pygwarts.irma.contrib	import LibraryContrib


	try:

		loggy = LibraryContrib(init_name="tserverdb")
		connection = mysql.connector.connect(

			user="vla",
			password="vla::SQL",
			host="192.168.162.65",
			database="tserverdb",
		)
		tserver = connection.cursor()
		loggy.info("Connection established")


		tserver.execute("SELECT word,state FROM navbag WHERE word IN ('JAN', 'FEB', 'MAR', 'APR')")
		for word,state in tserver : loggy.info(f"Selected {word},{state}")


		tserver.execute("SELECT word,state FROM navbag WHERE word IN ('MAY', 'JUN', 'JUL', 'AUG')")
		for word,state in tserver : loggy.info(f"Selected {word},{state}")


		tserver.close()


	except	mysql.connector.Error as E: print(E)
	else:	connection.close()







