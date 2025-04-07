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








ROOT	= "https://www.navtex.net/Navtex_Archive"
FOLDER	= "/mnt/container/NavtexArchive"
NAMEP	= re.compile(r"(?P<name>[A-Za-z]{2}\d\d)\.txt$")
LOGGER	= LibraryContrib(init_name="dearch", handler=os.path.join(FOLDER, "dearch.loggy"))

def LOGGY(message):

	LOGGER.info(message)
	print(message)


def get_message(url :str) -> str :

	if	(response := GET(url)):
		chunks = response.text.split("\n")

		while not chunks[0].startswith("ZCZC"):		chunks.pop(0)
		while not chunks[-1].startswith("NNNN"):	chunks.pop()

		return "".join(chunks)


def save_message(text :str, path :str) -> bool :

	try:

		os.makedirs(os.path.dirname(path), exist_ok=True)
		with open(path, "w") as file : file.write(str(text))

	except	Exception as E : LOGGY(f"fail {path} with {patronus(E)}")
	else:	return True


for Y in range(2016,2025):
	for m in range(1,13):

		tpoint = datetime(Y,m,1)
		mf = str(m).zfill(2)

		while tpoint.month == m:

			d = tpoint.day
			df = str(d).zfill(2)
			day_point = f"{Y}-{mf}-{df}"
			catalog = f"{ROOT}/{Y}%20/{Y}-{mf}%20/{day_point}"

			LOGGY(f"going {catalog}")
			page = GET(catalog).text

			LOGGY(f"got {len(page)} symbols page")
			soup = BeautifulSoup(page, "html.parser")

			for link in soup.find_all("a"):
				if	(href := link.get("href")).startswith(day_point):

					load = f"{catalog}/{href}"
					LOGGY(f"trying {load}")

					if	isinstance(message := get_message(load), str):
						if	(match := NAMEP.search(href)) and (name := match.group("name")):
							if	(result := save_message(

								message,
								os.path.join(FOLDER, str(Y), mf, df, name.upper())
							)):
								LOGGY(f"hit {href}")

				sleep(.6)

			tpoint += timedelta(days=1)







