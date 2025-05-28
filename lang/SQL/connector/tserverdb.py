







if	__name__ == "__main__":


	import	mysql.connector
	from	mysql.connector			import errorcode
	from	pygwarts.irma.contrib	import LibraryContrib
	from	pygwarts.irma.shelve	import LibraryShelf


	try:

		loggy = LibraryContrib(init_name="tserverdb")
		shelf = LibraryShelf(loggy)
		shelf.grab("/home/vla/ArrestedDevelopment/pygwarts/development/hagrid/Navbag.Shelf")


		connection = mysql.connector.connect(

			user="vla",
			password="vla::SQL",
			host="192.168.162.65",
		)
		tserver = connection.cursor()
		loggy.info("Connection established")


		tserver.execute("CREATE DATABASE IF NOT EXISTS tserverdb")
		tserver.execute("USE tserverdb")
		tserver.execute("DROP TABLE IF EXISTS navbag")
		tserver.execute(
			"""
				CREATE TABLE navbag (
					id INT NOT NULL AUTO_INCREMENT,
					word VARCHAR(255) NOT NULL,
					state INT,
					PRIMARY KEY(id)
				)
			"""
		)
		loggy.info("DB created")


		for word,state in shelf:

			tserver.execute("INSERT INTO navbag (word,state) VALUES (%s,%s)"%(f"'{word}'",f"'{state}'"))
			loggy.info(f"Inserted {word},{state}")


		connection.commit()
		tserver.close()


	except	mysql.connector.Error as E: print(E)
	else:	connection.close()







