from dataclasses import asdict
from urllib.request import urlopen
from bs4 import BeautifulSoup
from os import *    
from requests import *
from tkinter import *
import urllib.request
from idlelib.iomenu import encoding

url = "http://naver.com"

result = BeautifulSoup(url.text,"lxml")
rank = result.find("div",attrs={"class" : "iskeyword"})
print(rank.h4.get_text())
print(len(rank.li))

ranknum = rank.find("span",attrs={"class":"num_rank"})
ranksubject = rank.find("span",attrs={"class":"txt_rank"})
print(ranknum)
print(ranksubject)