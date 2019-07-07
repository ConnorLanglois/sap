from sources import Sources

import winsound

def on_new(article):
	winsound.Beep(600, 250)

	print(article.title, '\t' + article.publish_date, '\t\t' + article.url, '\t\t\t' + article.summary, sep='\n')
	print()
	print()
	print()
	print()

if __name__ == '__main__':
	Sources('../resources/sources.txt', '../resources/stocks.txt', 30, on_new).start()
