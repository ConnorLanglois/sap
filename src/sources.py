from multiprocessing import Process
from threading import Thread
from time import sleep
from urllib import parse

import logging
import newspaper

from source import Source

import utils

# logging.disable(logging.CRITICAL)

# newspaper.Article.throw_if_not_downloaded_verbose = utils.toggle_print(newspaper.Article.throw_if_not_downloaded_verbose)
# newspaper.Article.throw_if_not_parsed_verbose = utils.toggle_print(newspaper.Article.throw_if_not_parsed_verbose)

class Sources(list):
	def __init__(self, sources_path, stocks_path, delay, callback):
		super().__init__()

		self.sources_path = sources_path
		self.stocks_path = stocks_path
		self.delay = delay
		self.callback = callback

		self.articles = []

		with open(self.sources_path) as file:
			self.urls = [parse.quote(url.strip(), ':/?="&') for url in file.readlines()]

		with open(self.stocks_path) as file:
			self.stocks = {stock.strip().split(':')[0]: stock.strip().split(':')[1].split(',') for stock in file.readlines()}

	def start(self, daemon=False):
		for url in self.urls:
			Process(target=self.run, args=(url,), daemon=False).start()
			sleep(1)

	def run(self, url):
		source = Source(url, self.articles, self.stocks, self.callback)
		
		# self.append(source)

		while True:
			sleep(self.delay)
			
			try:
				source.refresh()
			except Exception as e:
				print(e)
