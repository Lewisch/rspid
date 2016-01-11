# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#Taken directly from https://github.com/zbef3825/scraPYwithDatabase/

import httplib
import requests
import ast

class httpreqpipeline(object):


	def __init__(self):

		r1 = requests.post('https://calm-springs-9697.herokuapp.com/login', auth=('USERNAME', 'PASSWORD'))
		tokendict = ast.literal_eval(r1.text)
		token = tokendict['token']
		headers = {'Content-Type': 'application/json', 'Authorization': token}
		print "Pipeline Initiated!"

	def process_items(self, items, spider):
		print "Reorganizing json files..."
		post_num = {}
		postcount = 0
		value_count = 0
		key_count = 0
		#add postnumber index

		for value in items['post_title']:
			
			if requests.get('https://calm-springs-9697.herokuapp.com/database/reddit').text.startswith('Unauthorized'):
				pass
			if postcount == 0:
				pass
			else:
				post_num.pop('post'+str(postcount), None)

			postcount += 1
			post_num['post'+str(postcount)] = {}

			for key in items:
				post_num['post'+str(postcount)][key] = items[key][value_count]



			value_count += 1
			post_request = requests.post('https://calm-springs-9697.herokuapp.com/database/reddit', data = dict(post_num), headers=headers)
			post_request

		print "Saving jsons to database"

		
		


		
		return post_num
