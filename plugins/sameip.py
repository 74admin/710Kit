#!/usr/bin/env python
#encoding: utf-8
#code by zer0cloud
import requests
from BeautifulSoup import BeautifulSoup

def same_ip(url):	
	'''
	查询同IP网站
	'''
	print "Find Domain in Same IP for %s.." % url
	try:
		source = requests.get('http://i.links.cn/sameip/' + url + '.html')
		soup = BeautifulSoup(source.text)
		divs = soup.findAll(style="word-break:break-all")
		
		if divs == []: #抓取结果为空
			print 'Sorry! Not found!'
			return 
		for div in divs:
			print div.a.string
	except:
		print '\nSome error!!.'
		return True
