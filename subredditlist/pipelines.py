# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#Taken directly from https://github.com/zbef3825/scraPYwithDatabase/

import httplib
import requests
import ast
import json

class httpreqpipeline(object):

	def __init__(self):
		#Logging in with scrapy info
		r1 = requests.post('https://calm-springs-9697.herokuapp.com/login', json = {"userID":"scrapy", "password":"cheesecake"})
		
		#if failed to logging in, set allowed variable as false and print what went wrong
		if r1.status_code != 200:
			self.allowed = False
			print r1.text
		
		#if logged in sucessfully, save token in token variable and get it as header
		else:
			self.allowed = True
			tokendict = ast.literal_eval(r1.text)
			token = tokendict['token']
			self.headers = {'Content-Type': 'application/json', 'Authorization': "bearer " + token}
			print "Pipeline Initiated!"

	def process_item(self, items, spider):
		
		#if we cannot log in we pass this condition and nothing happens
		if self.allowed == False:
			pass

		#after successfully logging in, sort data into individual web post and save it to the database
		else:
			post = {}
			post_col = []
			postnum = len(items["postLink"])
			for num in range(postnum):
				post_col.append(post)
			print "Reorganizing json files..."
			#add postnumber index
			for key, value in items.iteritems():
				for num in range(postnum):
					post_col[num][key] = value[num]
				
			
			r2 = requests.post('https://calm-springs-9697.herokuapp.com/api/save/reddit', data = json.dumps(post_col), headers=self.headers)
			if r2.status_code != 200:
				print "Failed to save"
			else:
				print "Saving jsons to database"

		
		


		
		return items
	
