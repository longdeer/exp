from bs4 import BeautifulSoup as BS

def pars_page(file :"name with extension", name :"for output file, with extension") ->"no return, only creating txt file with text of html content":

	with open(file, "r") as to_soup: # open html file
		to_parse = BS(to_soup, "html.parser") # create a bs4 object from opened file for parsing

	question_numbers, questions, answers = [], [], [] # three lists for mark number of question, the question and the answer for the question

	test_body = to_parse.contents[0].contents[8].contents[13].contents[5].contents[0].contents[1] # digging to the table of that html files with the test content

	for i in range(3, len(test_body), 2):
		current_answer = [] # list for gathering answer by peaces
		for p in test_body.contents[i].contents[5]:
			try:
				current_answer.append(p.get_text()) # search a cell with the answer for <br> tags
			except AttributeError:
				continue # skipping <br> tags

		question_numbers.append(test_body.contents[i].contents[1].get_text()) # add string - number of question to list
		questions.append(test_body.contents[i].contents[3].get_text()) # add string - the question to list
		answers.append(";".join(current_answer)) # add string - the question answer to list, with ";;;" inplace of <br>'s where was multiple answer

	with open(name, "w", encoding="utf-8") as to_file: # saving test text to a .txt file
		# creating a list of processed trios "number of question, question, answer" to join from by linebreaks
		parsed_body = [ "Вопрос {qn}:\n{q}\nОтвет: {a}".format(qn=n, q=q, a=a.strip(";").replace(";;;", ", ")) for n, q, a in zip(question_numbers, questions, answers) ]
		to_file.write("\n\n".join(parsed_body)) # writing file down

pars_page("GOC.html", "GOC.txt")
pars_page("ROC.html", "ROC.txt")
pars_page("GMDSS_utcsb_549_Английский 1 1-Err.html", "ENG.txt")