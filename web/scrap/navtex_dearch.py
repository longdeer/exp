import	os
import	re
from	sys						import exit
from	time					import sleep
from	datetime				import datetime
from	datetime				import timedelta
from	pygwarts.magical.spells	import patronus
from	pygwarts.irma.contrib	import LibraryContrib
from	requests				import get as GET
from	bs4						import BeautifulSoup








Y		= 2019
RUNNING	= set()
FOLDER	= "/mnt/container/NavtexArchive"
ROOT	= "https://www.navtex.net/Navtex_Archive"
NAMEP	= re.compile(r"(?P<name>[A-Za-z]{2}\d\d)\.txt$")
LOGGER	= LibraryContrib(init_name="dearch", handler=os.path.join(FOLDER, f"dearch-{Y}.loggy"))


def LOGGY(message):

	LOGGER.info(message)
	print(message)


def get_message(url :str) -> str | None :

	try:

		chunks = GET(url).text.split("\n")

		while not chunks[0].startswith("ZCZC"):		chunks.pop(0)
		while not chunks[-1].startswith("NNNN"):	chunks.pop()

	except	Exception as E : LOGGY(f"crit {patronus(E)}")
	else:	return "".join(chunks)


def save_message(text :str, path :str) -> bool :

	try:

		os.makedirs(os.path.dirname(path), exist_ok=True)
		with open(path, "w") as file : file.write(str(text))

	except	Exception as E : LOGGY(f"fail {path} with {patronus(E)}")
	else:	return True


for m in range(1,13):

	tpoint = datetime(Y,m,1)
	mf = str(m).zfill(2)

	while tpoint.month == m:

		d	= tpoint.day
		df	= str(d).zfill(2)
		day_point = f"{Y}-{mf}-{df}"
		catalog = f"{ROOT}/{Y}%20/{Y}-{mf}%20/{day_point}"
		current = dict()

		LOGGY(f"going {catalog}")
		page = GET(catalog).text

		LOGGY(f"got {len(page)} symbols page")
		soup = BeautifulSoup(page, "html.parser")

		for link in soup.find_all("a"):
			if	(href := link.get("href")).startswith(day_point) and (match := NAMEP.search(href)):

				name = match.group("name").upper()
				load = f"{catalog}/{href}"
				current[name] = load

		fetched = set(current)
		operate = fetched - RUNNING
		expired = RUNNING - fetched

		for name in expired: RUNNING.remove(name)
		for name in operate:

			load = current[name]
			LOGGY(f"trying {load}")

			if	isinstance(message := get_message(load), str):
				if	(result := save_message(

					message,
					os.path.join(FOLDER, str(Y), mf, df, name)
				)):
					LOGGY(f"hit {name}")
					RUNNING.add(name)

			sleep(.6)

		tpoint += timedelta(days=1)







