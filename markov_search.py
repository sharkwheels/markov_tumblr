#################################
# Markov Search 
# Nadine Lessio 2016 Winter
# IAMD_RI
# V1.0
# your computer is trying to parse some Freud into image / word combos, heres's what its coming up with.
# just make a photo grid w/ the search terms as the hover title or something. 
# do it in flask and put it on heroku or something.
# this can be the bot end of it that runs every hour on scheduler. 
# hmm. maybe i can post this to tumblr...
##################################

import markovify
import random
import re
import os
import sys
from py_ms_cognitive import PyMsCognitiveImageSearch
import pytumblr

"""
consumer_key =  os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
token_key = os.environ['token_key']
token_secret = os.environ['token_secret']

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)
"""

def make_sentence(txt):
	""" Yes I'm using a markov generator because I am lazy. Feed it a lot of text. """
	
	# Get raw text as string.
	with open(txt) as f:
		text = f.read()

	# Build the model.
	text_model = markovify.Text(text)

	# print a short scentence under 200 characters
	for i in range(1):
		s = text_model.make_short_sentence(200)
		su = re.sub(r'[^\w\s]','',s)
		print(su)
		grab_words(su.lower())


def grab_words(s):
	"""split the scentence into words and choose one to search with """

	words = s.split()
	print(words)

	not_words = ["the","of","it","that","us","you","me",
				"in","and","or","maybe","yes","no","but","however",
				"therefore","out","even","her","him","his","hers","they",
				"there","their","thus","this","when","go","a","be","because",
				"all","some","while","an","for","will","also","we","me","you","is",
				"i","with","was","just","as","by","its","it's","so","does","do",
				"go","stop","these","to","too","who","what","where","when","why","been",
				"any","from","has","had","if","at","whilst","can","may","one","could","would",
				"should","not","she","he","since","here","about","once","twice","are",
				"our","your","you're","other","most","less","more","were","we're","my","test","least",
				"which","them","about","such","into","seem","seemed","though","tho","on","off",
				"those","these","than","many","_eg_","up","have","upon","like","appears","same","does","none","_at","_he"
				]

	scrubbed_words = [x for x in words if x not in not_words]
	print(scrubbed_words)

	final_word = random.choice(scrubbed_words)
	final_word_second = random.choice(scrubbed_words)

	final_term = [final_word,final_word_second]
	
	send_result(final_term,s)

def send_result(toJoin,s):
	""" Send the result to someone. Post it somewhere? Make a Pinterest maybe? """
	spacer = " "
	search_term = spacer.join(toJoin)
	number = random.choice(range(0,50))
	print(toJoin)
	try:
		search_service = PyMsCognitiveImageSearch('55bc81d97f72464b839c0dbfd03d454d', search_term)
		first_fifty_result = search_service.search(limit=50, format='json') #1-50
		image_url =  first_fifty_result[number].content_url
		print(image_url)
		print(search_term)
		print(s)
		print(" ")
		client.create_photo('computerfreud', state="published", tags=["computer","freud","bot",search_term], caption=s, source=image_url)
		print("sent to tumblr")
		sys.exit()
	except Exception as e:
		print 'Exception occurred, value:', e

make_sentence("rt.txt")


