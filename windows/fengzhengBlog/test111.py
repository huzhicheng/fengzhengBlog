#-*- coding:utf-8 -*-

import os,codecs,json

ROOT = os.path.dirname(__file__)

def getConfigContent():
	jsonfile = file(ROOT+"/ueconfig.json")
	s = json.load(jsonfile)
	return s

def GetConfigValue(key):
	config = getConfigContent()
	return config[key]

from datetime import *
import random

if __name__=="__main__":
	#print GetConfigValue("imageAllowFiles")
	exts = list([".png", ".jpg", ".jpeg", ".gif", ".bmp"])
	name,ext = os.path.splitext("haha.png1")
	print ext in exts
	dt = datetime.now()
	print dt.strftime("%Y%m%d%H%M%S{0}".format(random.randint(1,999999)))
	localpath = ROOT+"/images/gallery/"
	print dict(x=1)

