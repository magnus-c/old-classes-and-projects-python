from collections import defaultdict
from collections import namedtuple
from operator import attrgetter
from io import BytesIO
from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.image as mpim
import re
import csv
import sqlite3
import pandas as pd
import os
import pickle
import numpy as np
import requests
import shutil
import sys

class WebScraping:
   def __init__(self, htmls):
      self.htmls = htmls
   
   def phtml(self):
      print(self.htmlsite)
     
   def openHtmlFile(self):
      f = open(self.htmls, "r")
      contents = f.read()
      return BeautifulSoup(contents, 'html.parser')
  
   def openHtmlSite(self):    
      html = urlopen(self.htmls)
      return BeautifulSoup(html, 'html.parser')    
    
   def children(self):
      [print(child.name) for child in (self.htmls).recursiveChildGenerator() if child.name is not None]        
  
   def findAll(self,tags):
      dict = {}
      for tag in (self.htmls).find_all(tags):
         print("{0}: {1}".format(tag.name, tag.text))
         r = re.compile(r'\s')
         s = r.split(tag.text)
         dict[s[0]] = s[1]
      for k,v in dict.items():
         print('key= ',k,'\tvalue= ',v)    
  
   def appendTag(self,tag,nustr):
      newtag = soupf.new_tag(tag)
      newtag.string=nustr
      ultag = soupf.ul  
      ultag.append(newtag)  
      print(ultag.prettify()) 
  
   def insertAt(self,tag,nustr,index):
      newtag = (self.htmls).new_tag(tag)
      newtag.string = nustr
      ultag = (self.htmls).ul   
      ultag.insert(index, newtag)   
      print(ultag.prettify()) 
  
   def selectIndex(self,index):
      sel = "li:nth-of-type("+str(index)+")"
      print((self.htmls).select(sel))
  
   def selectParagraph(self):
      spanElem = (self.htmls).select('p')
      print(spanElem)
      for i in range(0,len(spanElem)):
         print(str((spanElem)[i]))


class Database:
   
   def __init__(self, db, table_name, escape_hook=None):
      sqliteConnection = sqlite3.connect(db)
      self.db = sqliteConnection
      self.dbn = db
      #I found this snippet online and edited it to fit my purpose
      self._cmd_string = ''
      self._where_string = ''
      if escape_hook:
         self._fmt_params = {'table_name': escape_hook(table_name)}
      else:
         self._fmt_params = {'table_name': table_name}
    
      self._values = {'cmd': None, 'where': None}
      self.escape_hook = escape_hook

   def convert2Blog(self,filename):
      with open(filename, 'rb') as file:
         blobData = file.read()
      return blobData
     
   def connect(self):
      try:
         sqliteConnection = self.db
         cursor = sqliteConnection.cursor()
         print("Database created and Successfully Connected to SQLite")
         select_Query = "select sqlite_version();"
         print("Search query: ",select_Query)
         cursor.execute(select_Query)
         record = cursor.fetchall()
         print("SQLite Database Version is: ", record)
      except sqlite3.Error as error:
         print("Error while connecting to sqlite", error)
     
   def deleteRecord(self,id):
      try:
         sqliteConnection = self.db
         cursor = sqliteConnection.cursor()
         delete_query = "DELETE from Database where id = "+str(id)
         print("Delete query: ",delete_query)
         cursor.execute(delete_query)
         sqliteConnection.commit()
         print("Record deleted successfully ")
      except sqlite3.Error as error:
         print("Failed to delete record from sqlite table", error)
  
   def Search(self, value):
      sqliteConnection = self.db
      cursor = sqliteConnection.cursor()
      sel = 'SELECT id FROM Database WHERE name == "{0}"'.format(value)
      print("Search query: ",sel)
      cursor.execute(sel)
      result = cursor.fetchall()
      return result
  
   def insert(self, query,tup):
      sqliteConnection = self.db
      try:
         cursor = sqliteConnection.cursor()
         cursor.execute(query, tup)
         print("Search query: ",query)
         sqliteConnection.commit()
         print("Inserted successfully into table")
      except sqlite3.Error as error:
         print("Failed to insert: ", error)
  
   def readTable(self):
      sqliteConnection = self.db
      records = None
      try:
         cursor = sqliteConnection.cursor()
         sqlite_select_query = """SELECT * from Database"""
         print("Search query: ",sqlite_select_query)
         cursor.execute(sqlite_select_query)
         records = cursor.fetchall()
         print("Total rows are:  ", len(records))
      except sqlite3.Error as error:
         print("Failed to read data from sqlite table", error)
      return records
  
   def table(self,query):
      sqliteConnection = self.db
      try:
         cursor = sqliteConnection.cursor()
         cursor.execute(query)
         print("Table query: ",query)
         sqliteConnection.commit()
         print("SQLite table created")    
      except sqlite3.Error as error:
         print("Table exists: ", error)
  
   def update(self,id, htext):
      sqliteConnection = self.db
      try:
         cursor = sqliteConnection.cursor()
         update_query = """Update Database set html = ? where id = ?"""
         data = (htext, id)
         cursor.execute(update_query, data)
         print("Update query: ",update_query)
         sqliteConnection.commit()
         print("Record Updated successfully")
      except sqlite3.Error as error:
         print("Failed to update sqlite table", error)
   def close(self):
      sqliteConnection = self.db
      sqliteConnection.close()
      os.remove(self.dbn)     
    
   '''
      this is my query builder for inserting values,
      input: dict of column name = cmd (data ie. 24)
      returns: insert query string
      '''
   def query_builder(self, op, **kw_attr):
      try:
         if op == "table":
            cols, vals = self._escape(zip(*kw_attr.items()))
            self._cmd_string = 'INSERT INTO {table_name} ({column_names}) VALUES ({param_marks})'
            self._fmt_params['column_names'] = ', '.join(cols)
            self._fmt_params['param_marks'] = ', '.join('?' for _ in range(len(cols))) 
            self._values['cmd'] = vals
            self._cmd_string = 'INSERT INTO {table_name} ({column_names}) VALUES ({param_marks})'.format(table_name = self._fmt_params['table_name'], column_names =self._fmt_params['column_names'], param_marks =self._fmt_params['param_marks'])
            return self._cmd_string 
   '''
      this is my query builder for table, a little scuffed
      input: dict of column name = cmd (data type ie. TEXT NOT NULL)
      returns: table query string
      '''
   def table_query_builder(self, **kw_attr):
      cols, vals = self._escape(zip(*kw_attr.items()))
      self._cmd_string = 'CREATE TABLE {table_name} ({column_names, cmd})'
      self._fmt_params['column_names'] = ', '.join(cols)
      self._values['cmd'] = vals
      a = []
      b=[]
      c=[]
      for i in range(0, len(cols)):
         a.append(self._fmt_params['column_names'].split(", ")[i])
         b.append(self._values['cmd'][i])
         c.append(a[i] +" "+ b[i])
      self._cmd_string = 'CREATE TABLE {table_name} ({r})'.format(table_name = self._fmt_params['table_name'], r= ", ".join(map(str,c))) 
      return self._cmd_string 
   def search_query_builder(self, con):
      self._cmd_string = 'SELECT * FROM {table_name} WHERE {condition}'.format(table_name = self._fmt_params['table_name'], condition = con)
      return self._cmd_string

   def delete_query_builder(self, con):
      self._cmd_string = 'DELETE FROM FROM {table_name} WHERE {condition}'.format(table_name = self._fmt_params['table_name'], condition = con)
   except sqlite3.Error as error:
      print(error)
   #for the questionmars in the other thing
   def _qmarks(n):
      if hasattr(n, '__len__'):
         n = len(n)
      return ', '.join('?' for _ in range(n)) 
  
   #taking things out of the zip
   def _escape(self, colvals):
      if self.escape_hook:
         escaped = ((self.escape_hook(col), val)
                             for col, val in zip(*colvals))
         return zip(
                   *filter(lambda x: x[0] is not None, escaped)
                  )
  
      return colvals
   
class namedtup:
   def __init__(self, tup):
      self.tup = tup
   
   def __str__(self,seq):
      st = ', '.join(map(str, seq))
      return st

   def __sort__(self, seq, attr):
      srt = sorted(seq, key=attrgetter(attr))
      return srt
      
   def __search__(self, seq, val):
      
      values = []
      for i in seq:
         if val in i:
            values.append(i)
      
      return values
   
'''   
q = WebScraping('https://en.wikipedia.org/wiki/Greenhouse_gas')    
souph = q.openHtmlSite()
#print(souph)

for caption in souph.find_all('caption'):
   if caption.text.strip() == 'Current greenhouse gas concentrations[57]':
      table = caption.find_parent('table', {'class': 'wikitable'})  
print((table.prettify()))

print((table.prettify()))

cells = list()

filters = str(table)
filters = re.split("<td>", filters)

for result in filters:
   cells += re.findall("\S+[\s]?\S+", result)

print(cells)
	
'''


tup = namedtuple('Row', ["Gas","Pre1750", "Recent", "Absoluteinc", "PercentageInc"])
tups = [tup("A", 2,3,4,5), tup("B", 3,4,5,6), tup("C", 1,1,2,9)]

tupl = namedtup(tup)
print(str(tups))
print(tupl._search(tups, "A"))
print(tupl._sort(tups, "Recent"))

'''
headers = [header.text.split('[', 1)[0].strip("\n") for header in table.find_all('th')]
#tr is the row, td are the numbers we want
results = [{headers[i]: cell for i, cell in enumerate(row.find_all('td'))}
           for row in table.find_all('tr')]

gas= []
pre = []
recent = []
absinc = []
percinc = []
incradfor = []
tupp = []
arr= []
q = 0
for i in range(1,len(results)):
   try:
      gas.append((results[i][headers[0]]).find('a').text.strip("\n"))
   except:
      gas.append((results[i][headers[0]]).text.strip("\n"))
   pre.append((results[i][headers[1]]).text.replace(u"\xa0", u' ').split('[', 1)[0])
   recent.append((results[i][headers[2]]).text.replace(u"\xa0", u' ').split('[', 1)[0].strip("/ "))
   absinc.append((results[i][headers[3]]).text.replace(u"\xa0", u' ').split('[', 1)[0])
   percinc.append((results[i][headers[4]]).text.replace(u"\xa0", u' ').split('[', 1)[0])


for j in range(len(pre)):
   tupp.append(tup(gas[j], pre[j], recent[j], absinc[j], percinc[j]))
 
df = pd.DataFrame(tupp) 
print(df)

df_byte = df.to_json().encode()


dtb = Database("Midterm1.db", "Database") 

tqb = dtb.table_query_builder(ID = "INTEGER PRIMARY KEY", GAS="TEXT NOT NULL", PRE = "TEXT NOT NULL", RECENT = "TEXT NOT NULL", ABSOLUTEINC ="TEXT NOT NULL", PERCENTAGEINC = "TEXT NOT NULL")
dtb.table(tqb)
iqb = dtb.insert_query_builder(ID = 0, GAS="abc", PRE = "abc", RECENT = "abc", ABSOLUTEINC ="abc", PERCENTAGEINC = "abc")

for i in range(len(gas)):
   q = q+1
   data_j = (q, gas[i], pre[i], recent[i], absinc[i], percinc[i])
   dtb.insert(iqb,data_j)

print(dtb)
records = dtb.readTable()
dtb.close()
'''
