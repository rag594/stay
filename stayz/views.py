from django.views.static import serve
from django.shortcuts import get_object_or_404
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import csv
import json
from collections import defaultdict


def akash (request) :

    
	x= request.GET.get('city','')
	print(x)
	response = ''
	m=open("hackathon_chat_data.csv" ,
	     encoding = 'ISO-8859-2'
	     )
	reader = csv.reader(m)
	row=[]
	month=[]#list of all month
	cit=[]#dummy City
	cities=[]#list of all cities
	cid=[]#list of all id's
	hotels=[]#list of all hotels
	i=0
	for row in reader:
		try:
			if '-' and '\\\n' and 'Check in:' in row[1]:
				if row[1].split('-')[1] != '':
					hotels.append(row[1].split(' - ')[0])

				else :
					hotels.append("NULL")  
				cit.append(row[1].split(' - ')[1])
				cities.append(cit[i].split("Check in:")[0])
				
				i+=1                             
		except Exception  :
			continue
	try:
		for row in reader:
			if ':' or '/' in row[3]:
				if ':' in row[3]:
					cid.append(row[3].split(":")[0])
				month.append(row[3].split("/")[1].split("/")[0])
				i+=1
	except Exception:
		pass
	cindex=[]
	k=0
	for c in cities:
		
		if str(x)[1:-2] in c:
			#print("1212")
			cindex.append(k)
		k+=1
	hot=[]
	coun=[]
	frequency=len(cindex)
	print(frequency)
	for ind in cindex:
		hot.append(hotels[ind].strip('\\\n').strip('<br />').strip('option1:\\\n'))
	d=defaultdict(int)
	for h in hot:
		d[h]+=1
	print(d)
	response = HttpResponse(json.dumps({'dict':d, 'freq':frequency}))
	return (response)


