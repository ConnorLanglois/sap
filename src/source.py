from googletrans import Translator
from newspaper import news_pool
from nltk import Tree

import newspaper
import nltk
import tzlocal
import utils

class Source():
	def __init__(self, url, articles, stocks, callback):
		self.url = url
		self.articles = articles
		self.stocks = stocks
		self.callback = callback

		newspaper.build(self.url)

	def refresh(self):
		paper = newspaper.build(self.url, **{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'})

		news_pool.set([paper], threads_per_source=2)
		news_pool.join()

		for article in paper.articles:
			article.parse()

			if all(source_article.title != article.title for source_article in self.articles):
				if article.publish_date is not None:
					article.publish_date = article.publish_date.astimezone(tzlocal.get_localzone())

				if any(stock_term.lower() in article.title.lower() for stock_terms in self.stocks.values() for stock_term in stock_terms) and all(old_article.title.lower() != article.title.lower() for old_article in self.articles):
					self.articles.append(article)
					self.callback(article)
