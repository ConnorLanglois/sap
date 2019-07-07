import nltk

def toggle_print(func):
	def wrapper(self):
		import os
		import sys

		sys.stdout = open(os.devnull, 'w')
		
		func(self)

		sys.stdout = sys.__stdout__

	return wrapper

def get_entities(text):
	entities = {}

	for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
		if isinstance(chunk, Tree):
			if chunk.label() in entities:
				entities[chunk.label()].extend([word for word, tag in chunk])
			else:
				entities[chunk.label()] = [word for word, tag in chunk]
		else:
			if '' in entities:
				entities[''].extend(chunk[0])
			else:
				entities[''] = [chunk[0]]

	return entities
