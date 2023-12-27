import urllib.request
from nltk.tokenize import sent_tokenize
from inscriptis import get_text
from PyQt5 import QtCore, QtGui, QtWidgets
from urlaction import URLCheck
import math
import pymysql.cursors
from CountWords import CountWords
import sys
import os
class TFIDF:

	def process(url):
		try:

			print("in process")
			cont= "python java"
			html = urllib.request.urlopen(url).read().decode('utf-8')
			text = get_text(html)
			#print(text)
			stmnts=sent_tokenize(text)
			TFIDF.main(stmnts,cont)
		except Exception as e:
			print("try1")
			print(e.args[0])
			tb = sys.exc_info()[2]
			print(tb.tb_lineno)

	@staticmethod
	def main(stmnts,cont):
		d = {}
		try:

			for st in stmnts:
				l=len(cont)
				tot=0
				import re
				x=[a for a in re.split(r'(\s|\,)', cont.strip()) if a]
				sp=x.count(' ')
				for i in range(0,sp):
					x.remove(' ')
				com=x.count(',')
				for i in range(0,com):
					x.remove(',')
				#print(x)

				for w in x:
					c=CountWords.countOccurences(st,w)
					tot=tot+c
				tot=tot/l
				idf=math.log(l)
				d[st]=tot*idf

			f=open("output.html",'w')
			p=""
			for x in d:
				#print(x)
				if(d[x]>0) :
					txt=x
					txt=txt.replace("\n","")
					for i in range (0,len(txt)):
						if(txt[i].isalpha()):
							txt=txt[i:]
							break
					p=p+txt
					p=p+"\n"
			#print("OUTPUT = "+p)
			head="<html><head><title>Extraction</title><style>pre{   word-wrap: break-word; font-size: 25px; }</style></head><body><h2><center>Result</center></h2><pre>"
			para=p
			#print(para)
			ps=(para.split("\n"))
			le=len(ps)
			i=0
			pa=[]
			while (i+3)<le:
				pr=""
				pr=pr+ps[i]+ps[i+1]+ps[i+2]+ps[i+3]
				i=i+4
				pa.append(pr)
			#print(len(pa),pa)

			text=""
			for i in pa:
				text=text+"\t"+i+"\n\n"
			#print(text)
			if text!="":
				head=head+text
			else:
				head=head+p
			head=head+"</pre></body></html>"
			f.write(head)
			f.close()
			
		except Exception as e:
			print("trY3")
			print(e.args[0])
			tb = sys.exc_info()[2]
			print(tb.tb_lineno)

		return d






if __name__=="__main__":
	TFIDF.process("https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python")
