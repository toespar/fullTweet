#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import math
import twitter
from termcolor import colored
import os
import pip


__author__ 		= "@toespar"
__version__ 	= "1.0.0"
__maintainer__ 	= "toespar"
__email__ 		= "toespar@gmail.com"
__status__ 		= "Stable"

class FullTweet:
	
	def __init__(self):
		pass
	
	def requeriments(self):
		installed_packages = pip.get_installed_distributions()
		installed_packages_list = sorted(["%s==%s" % (i.key, i.version)for i in installed_packages])
		if not any("python-twitter" in s for s in installed_packages_list):
			script = """
					pip install python-twitter
					"""
			os.system("bash -c '%s'" % script)
		if not any("termcolor" in s for s in installed_packages_list): 
			script = """
					pip install termcolor
					"""
			os.system("bash -c '%s'" % script)
			
	def write_tweet(self):
		api = twitter.Api(consumer_key='YOUR CONSUMER KEY', consumer_secret='YOUR CONSUMER SECRET', access_token_key='YOUR ACCESS TOKEN KEY', access_token_secret='YOUR ACCESS TOKEN SECRET')
		count = 0
		tweet = ""
		complete = ""
		looseWord = ""
		text = raw_input(colored("Write here you tweet: ", 'green'))
		numTweets = math.ceil(len(text) / 140)
		if len(text)>140:
			for word in text.split():
				complete = tweet+word+" "
				if len(complete) < 136:
					tweet += looseWord+word+" "
					looseWord=""
				else:
					looseWord=word+" "
					count+=1
					update = tweet+" "+str(count)+"/"+str(int(numTweets))
					status = api.PostUpdate(update)
					print update
					tweet = ""
		else:
			status = api.PostUpdate(text)
    
if __name__ == "__main__":
	print
	print colored("#== fullTweet ========================#", 'blue')
	print colored("#   Author: "+__author__+"                  #", 'blue')
	print colored("#   Version: "+__version__+"                    #", 'blue')
	print colored("#=====================================#\n", 'blue')
	tweet = FullTweet()
	tweet.requeriments()
	tweet.write_tweet()
	