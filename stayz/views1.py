from django.views.static import serve
from django.shortcuts import get_object_or_404
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import csv
import json
from collections import defaultdict

def shre (request) :
	print("func started")
	x = request.GET.get('str2','')
	print(x)
	response = ''
	m=open("/Users/raghavrastogi/nltk_data/corpora/webtext/hackathon_chat_data.csv", 'a')
	m.write(x)
	m.close()
	#('hello')
	response = HttpResponse("hellokgrlmkl")
	return (response)