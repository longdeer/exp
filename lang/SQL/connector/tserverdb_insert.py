







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


		tserver.execute("INSERT IGNORE INTO navbag (word,state) VALUES ('LOL',0),('KEK',0)")
		tserver.execute("INSERT IGNORE INTO navbag (word,state) VALUES ('CHEBUREK',0),('LONG',0)")


		loggy.info(f"Insertion done")
		connection.commit()
		tserver.close()


	except	mysql.connector.Error as E: print(E)
	else:	connection.close()







