







if	__name__ == "__main__":


	import	mysql.connector
	from	mysql.connector			import errorcode
	from	pygwarts.irma.contrib	import LibraryContrib


	try:

		loggy = LibraryContrib(init_name="office")
		connection = mysql.connector.connect(

			user="vla",
			password="vla::SQL",
			host="192.168.162.65",
		)
		tserver = connection.cursor()
		loggy.info("Connection established")


		tserver.execute("CREATE DATABASE IF NOT EXISTS office")
		tserver.execute("USE office")


		tserver.execute("DROP TABLE IF EXISTS actsnprots")
		tserver.execute(
			"""
				CREATE TABLE actsnprots (
					id INT NOT NULL AUTO_INCREMENT,
					date DATE,
					category BLOB,
					number CHAR(5),
					content LONGBLOB,
					author BLOB,
					comment LONGBLOB,
					PRIMARY KEY(id)
				)
			"""
		)
		loggy.info("Table actsnprots created")
		tserver.execute(
			"""
				INSERT INTO actsnprots (date, category, content) VALUES
				(
					'2024-6-29',
					'Акт возврата',
					'Акт возврата нежилого помещения к договору №01/01-2021-1 аренды нежилого помещения от 01.01.2021'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO actsnprots (date, category, number, content, author) VALUES
				(
					'2024-7-30',
					'Акт дефектации',
					'06',
					'Замена блока питания в АРМ ARQ',
					'Смирнов Д.Е.'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO actsnprots (date, category, number, content, author) VALUES
				(
					'2024-10-15',
					'Акт дефектации',
					'07',
					'Замена аккумуляторов в ИБП ARQ-C',
					'Смирнов Д.Е.'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO actsnprots (date, category, number, content, author) VALUES
				(
					'2024-10-15',
					'Акт установки',
					'07',
					'Замена аккумуляторов в ИБП ARQ-C',
					'Смирнов Д.Е.'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO actsnprots (date, category, number, content, author) VALUES
				(
					'2024-10-15',
					'Акт дефектации',
					'08',
					'Замена аккумуляторов в ИБП Lenovo2',
					'Смирнов Д.Е.'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO actsnprots (date, category, number, content, author) VALUES
				(
					'2024-10-15',
					'Акт установки',
					'08',
					'Замена аккумуляторов в ИБП Lenovo2',
					'Смирнов Д.Е.'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO actsnprots (date, category, content, author, comment) VALUES
				(
					'2024-10-29',
					'Акт списания',
					'Списание канцелярских принадлежностей',
					'Смирнов Д.Е.',
					'Заявка №12/3-04-035 от 02.09.2024'
				)
			"""
		)
		loggy.info("Table actsnprots populated")


		tserver.execute("DROP TABLE IF EXISTS contracts")
		tserver.execute(
			"""
				CREATE TABLE contracts (
					id INT NOT NULL AUTO_INCREMENT,
					date DATE,
					number CHAR(32),
					eosed CHAR(32),
					content LONGBLOB,
					agent BLOB,
					insigner BLOB,
					outsigner BLOB,
					fmdate DATE,
					todate DATE,
					price LONGBLOB,
					comment LONGBLOB,
					PRIMARY KEY(id)
				)
			"""
		)
		loggy.info("Table contracts created")
		tserver.execute(
			"""
				INSERT INTO contracts
				(date, number, content, agent, insigner, outsigner, fmdate, todate, comment)
				VALUES
				(
					'2024-1-1',
					'01/01-2021-1',
					'ДС - продление договора аренды нежилого помещения от 01.01.2021',
					'ПАО "МТФ"',
					'Мажирин Сергей Иванович, директор',
					'Старков Денис Алексеевич, генеральный директор',
					'2024-1-1',
					'2024-6-30',
					'Ежемесячный платёж 145 943,60 руб.'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO contracts
				(date, number, content, agent, insigner, outsigner, price)
				VALUES
				(
					'2024-2-10',
					'ПФ-0313/24-12',
					'Договор на поставку шлюзов ТРИКОМ GIP-2M',
					'ООО "СТ-Связь"',
					'Филиппов Павел Вячеславович, и.о. директора',
					'Лавренов Юрий Владимирович, генеральный директор',
					'247 542,00 руб. (в т.ч. НДС 20% - 41 257,00)'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO contracts
				(date, number, eosed, content, agent, insigner, outsigner, fmdate, todate, price, comment)
				VALUES
				(
					'2024-12-13',
					'28-25',
					'1879144',
					'Выполнение работ по предоставлению информации в области гидрометеорологии (Навтекс)',
					'ФГБУ "Мурманское УГМС"',
					'Седых Владимир Викторович, и.о. директора',
					'Чаус Оксана Михайловна, начальник',
					'2025-1-1',
					'2024-12-31',
					'574 516,80 руб. (в т.ч. 20% НДС - 95 752,80)',
					'Ежемесячный платёж 47 876,40 руб (в т.ч. НДС 20% - 7 979,40 руб.)'
				)
			"""
		)
		loggy.info("Table contracts populated")


		tserver.execute("DROP TABLE IF EXISTS letters")
		tserver.execute(
			"""
				CREATE TABLE letters (
					id INT NOT NULL AUTO_INCREMENT,
					date DATE,
					number CHAR(32),
					eosed CHAR(32),
					theme LONGBLOB,
					receiver LONGBLOB,
					address LONGBLOB,
					signer BLOB,
					author BLOB,
					comment LONGBLOB,
					PRIMARY KEY(id)
				)
			"""
		)
		loggy.info("Table letters created")
		tserver.execute(
			"""
				INSERT INTO letters
				(date, number, eosed, theme, receiver, address, signer, author, comment)
				VALUES
				(
					'2024-10-23',
					'Ф1050-14/1252-12',
					'1821096',
					'О возврате денежных средств',
					'АО "ЧИП и ДИП", Генеральный директор, Корольков А.С.',
					'sales@chipdip.ru',
					'Седых В.В.',
					'Смирнов Д.Е.',
					'Возврат денежных средств в размере 540,00 руб. в связи с недопоставкой товаров'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO letters
				(date, number, eosed, theme, receiver, address, signer, author, comment)
				VALUES
				(
					'2024-12-4',
					'Ф1050-12/1423-12',
					'1872817',
					'О гарантиях бесперебойного предоставления услуг связи',
					'ПАО «МегаФон»',
					'г. Мурманск, ул. Шмидта, д. 4А',
					'Седых В.В.',
					'Лупандин В.А.',
					'В январе 2025 МТФ должен выгнать всех операторов с крыши, письмом запрашиваем гарантии сохранения связи'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO letters
				(date, number, eosed, theme, receiver, address, signer, author, comment)
				VALUES
				(
					'2024-12-5',
					'Ф1050-08/610-12',
					'1874059',
					'Запрос в ЦА доверенности для аренды Шмидта 43',
					'ЦА',
					'ЦА',
					'Седых В.В.',
					'Трекин В.В.',
					'смена собственникак+ новый директор+ окончание договора аренды'
				)
			"""
		)
		loggy.info("Table letters populated")


		tserver.execute("DROP TABLE IF EXISTS notes")
		tserver.execute(
			"""
				CREATE TABLE notes (
					id INT NOT NULL AUTO_INCREMENT,
					date DATE,
					reg DATE,
					number CHAR(32),
					eosed CHAR(32),
					theme LONGBLOB,
					receiver LONGBLOB,
					signer BLOB,
					author BLOB,
					comment LONGBLOB,
					PRIMARY KEY(id)
				)
			"""
		)
		loggy.info("Table notes created")
		tserver.execute(
			"""
				INSERT INTO notes
				(date, number, theme)
				VALUES
				(
					'2024-1-12',
					'12/3-04-001',
					'ВКС Директору и ЗБМ'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO notes
				(date, number, eosed, theme, receiver, signer, author, comment)
				VALUES
				(
					'2024-8-8',
					'12/3-04-028',
					'1745848',
					'Заявка на закупку кофемашины',
					'Чернушкин Д.А. (замещает Зеленкова Н.К.)',
					'Трекин В.В.',
					'Смирнов Д.Е.',
					'Согласуется'
				)
			"""
		)
		tserver.execute(
			"""
				INSERT INTO notes
				(date, reg, number, eosed, theme, receiver, signer, author, comment)
				VALUES
				(
					'2024-11-26',
					'2024-11-27',
					'12/3-04-045',
					'1863699',
					'На заключение договора с ФГБУ "Мурманское УГМС" на 2025г.',
					'Кукушкин А.Н.',
					'Трекин В.В.',
					'Смирнов Д.Е.',
					'Исполнитель Трекин В.В. СЗ подлежит аннулированию'
				)
			"""
		)
		loggy.info("Table notes populated")


		connection.commit()
		tserver.close()


	except	mysql.connector.Error as E: print(E)
	else:	connection.close()







