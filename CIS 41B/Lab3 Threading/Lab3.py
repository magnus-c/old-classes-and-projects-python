from io import BytesIO
from bs4 import BeautifulSoup
from collections import defaultdict
import urllib.request
from urllib.request import urlopen
import pandas as pd
import json
from collections import defaultdict
from urllib.request import urlopen
import csv
import sqlite3
import os
import pickle
import pprint
import threading
import time
import queue 
import numpy as np
import matplotlib.pyplot as plt
class Database:
    def __init__(self, db, table_name, escape_hook=None):
        sqliteConnection = sqlite3.connect(db, check_same_thread=False)
        self.db = sqliteConnection
        self.dbn = db
        # I found this snippet online and edited it to fit my purpose
        self._cmd_string = ''
        self._where_string = ''
        if escape_hook:
            self._fmt_params = {'table_name': escape_hook(table_name)}
        else:
            self._fmt_params = {'table_name': table_name}

        self._values = {'cmd': None, 'where': None}
        self.escape_hook = escape_hook

    def convert2Blog(self, filename):
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def connect(self):
        try:
            sqliteConnection = self.db
            cursor = sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
            select_Query = "select sqlite_version();"
            print("Search query: ", select_Query)
            cursor.execute(select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    def deleteRecord(self, query):
        try:
            sqliteConnection = self.db
            cursor = sqliteConnection.cursor()
            print("Delete query: ", query)
            cursor.execute(query)
            sqliteConnection.commit()
            print("Record deleted successfully ")
        except sqlite3.Error as error:
            print("Failed to delete record from sqlite table", error)

    def Search(self, query):
        sqliteConnection = self.db
        cursor = sqliteConnection.cursor()
        print("Search query: ", query)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert(self, query, tup):
        sqliteConnection = self.db
        try:
            cursor = sqliteConnection.cursor()
            cursor.execute(query, tup)
            print("Search query: ", query)
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
            print("Search query: ", sqlite_select_query)
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Total rows are:  ", len(records))
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        return records

    def table(self, query):
        sqliteConnection = self.db
        try:
            cursor = sqliteConnection.cursor()
            cursor.execute(query)
            print("Table query: ", query)
            sqliteConnection.commit()
            print("SQLite table created")
        except sqlite3.Error as error:
            print("Table exists: ", error)

    def update(self, id, htext):
        sqliteConnection = self.db
        try:
            cursor = sqliteConnection.cursor()
            update_query = """Update Database set html = ? where id = ?"""
            data = (htext, id)
            cursor.execute(update_query, data)
            print("Update query: ", update_query)
            sqliteConnection.commit()
            print("Record Updated successfully")
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)

    def close(self):
        sqliteConnection = self.db
        sqliteConnection.close()
        os.remove(self.dbn)

    def query_builder(self, op, *args, **kw_attr):
        try:
            if op == "insert":
                cols, vals = self._escape(zip(*kw_attr.items()))
                self._cmd_string = 'INSERT INTO {table_name} ({column_names}) VALUES ({param_marks})'
                self._fmt_params['column_names'] = ', '.join(cols)
                self._fmt_params['param_marks'] = ', '.join(
                    '?' for _ in range(len(cols)))
                self._values['cmd'] = vals
                self._cmd_string = 'INSERT INTO {table_name} ({column_names}) VALUES ({param_marks})'.format(
                    table_name=self._fmt_params['table_name'], column_names=self._fmt_params['column_names'], param_marks=self._fmt_params['param_marks'])
            elif op == "table":
                cols, vals = self._escape(zip(*kw_attr.items()))
                self._cmd_string = 'CREATE TABLE {table_name} ({column_names, cmd})'
                self._fmt_params['column_names'] = ', '.join(cols)
                self._values['cmd'] = vals
                a = []
                b = []
                c = []
                for i in range(0, len(cols)):
                    a.append(self._fmt_params['column_names'].split(", ")[i])
                    b.append(self._values['cmd'][i])
                    c.append(a[i] + " " + b[i])
                self._cmd_string = 'CREATE TABLE {table_name} ({r})'.format(
                    table_name=self._fmt_params['table_name'], r=", ".join(map(str, c)))
            elif op == "select":
                cols, vals = self._escape(zip(*kw_attr.items()))
                self._cmd_string = 'SELECT {ID} FROM {table_name} WHERE {condition}'
                self._fmt_params['column_names'] = ', '.join(cols)
                self._values['cmd'] = vals
                a = []
                b = []
                c = []
                if str(*args) == "()":
                    args = "*"
                for i in range(0, len(cols)):
                    a.append(self._fmt_params['column_names'].split(", ")[i])
                    b.append(self._values['cmd'][i])
                    c.append(a[i] + " == "+"\'" + b[i]+"\'")
                self._cmd_string = 'SELECT {ID} FROM {table_name} WHERE {condition}'.format(
                    table_name=self._fmt_params['table_name'], ID=str(*args), condition=", ".join(map(str, c)))
            elif op == "delete":
                cols, vals = self._escape(zip(*kw_attr.items()))
                self._cmd_string = 'DELETE FROM {table_name} WHERE {condition}'
                self._fmt_params['column_names'] = ', '.join(cols)
                self._values['cmd'] = vals
                a = []
                b = []
                c = []
                for i in range(0, len(cols)):
                    a.append(self._fmt_params['column_names'].split(", ")[i])
                    b.append(self._values['cmd'][i])
                    c.append(a[i] + " = " + "\'"+b[i] + "\'")
                self._cmd_string = 'DELETE FROM {table_name} WHERE {condition}'.format(
                    table_name=self._fmt_params['table_name'], condition=", ".join(map(str, c)))
            return self._cmd_string
        except sqlite3.Error as error:
            print(error)
    # for the questionmars in the other thing

    def _qmarks(n):
        if hasattr(n, '__len__'):
            n = len(n)
        return ', '.join('?' for _ in range(n))

    # taking things out of the zip
    def _escape(self, colvals):
        if self.escape_hook:
            escaped = ((self.escape_hook(col), val)
                       for col, val in zip(*colvals))
            return zip(
                *filter(lambda x: x[0] is not None, escaped)
            )

        return colvals


def openHtmlFile(htmlfile):
    f = open(htmlfile, "r", encoding="utf-8")
    contents = f.read()
    return BeautifulSoup(contents, 'html.parser')


dtb = Database("Lab3.db", "Database")
d = defaultdict(list)
urllib.request.urlretrieve(
    "https://gml.noaa.gov/aggi/aggi.html", "html_file.html")
soupf = openHtmlFile("html_file.html")

arr = soupf.findAll("td")
for i in range(13, len(arr), 11):
    d["year"].append(int(arr[i].text))
    d["CO2"].append(float(arr[i+1].text))
    d["CH4"].append(float(arr[i+2].text))
    d["N2O"].append(float(arr[i+3].text))
    d["CFC"].append(float(arr[i+4].text))
    d["HCFCs"].append(float(arr[i+5].text))
    d["HCFCs2"].append(float(arr[i+6].text))

print
dicti = {'ID': "INTEGER PRIMARY KEY", 'YEAR': "INTEGER NOT NULL", "CO2": "INTEGER NOT NULL",
         "CH4": "INTEGER NOT NULL", "N2O": "INTEGER NOT NULL", "CFC": "INTEGER NOT NULL", "HCFCs": "INTEGER NOT NULL", "HCFCs2": "INTEGER NOT NULL"}
dicti2 = {'ID': 0, 'YEAR': 1234, "CO2": 1234,
          "CH4": 1234, "N2O": 1234, "CFC": 1234, "HCFCs": 1234, "HCFCs2":1234}

tqb = dtb.query_builder(op="table", **dicti)
dtb.table(tqb)
iqb = dtb.query_builder(op="insert", **dicti2)
tupl = []
q=0

for i in range(len(d["year"])):
    q = q+1
    for j in d.keys():
        tupl.append(d[j][i])

    data_t = (q, *tupl)
    print(tupl)
    tupl.clear()
    dtb.insert(iqb, data_t)

listCO2= []  
listCH4= []  
listN2O= []  
listCFC= []  
listHCFCs= []  
listHCFCs2= []  
  
tlock = threading.Lock()
#sqlite3.connect("Lab3.db", check_same_thread=False)
def thread_function(list, elem, yr, dtbs):
    tlock.acquire_lock()
    sqb = dtbs.query_builder('select', elem, year =str(yr))
    list.append(dtb.Search(sqb)[0][0])
    tlock.release()
    

q = queue.Queue()
   


for i in range(1990, 2020):
    q.put(threading.Thread(target=thread_function,args=(listCO2, "CO2", i, dtb,)))
    q.put(threading.Thread(target=thread_function,args=(listCH4, "CH4",i, dtb)))
    q.put(threading.Thread(target=thread_function,args=(listN2O, "N2O",i, dtb)))
    q.put(threading.Thread(target=thread_function,args=(listCFC, "CFC", i, dtb,)))
    q.put(threading.Thread(target=thread_function,args=(listHCFCs, "HCFCs", i, dtb,)))
    q.put(threading.Thread(target=thread_function,args=(listHCFCs2, "HCFCs2", i, dtb,)))
    

for qu in q.queue:
    qu.start() 
    qu.join()
    

listss = (listCO2, listCH4,listN2O,listCFC,listHCFCs,listHCFCs2)
num = 0

plt.figure(figsize=(18, 12))
plt.xlim(1990, 2019)
plt.ylim(0, 3)
plt.xscale("linear")
plt.yscale("linear")
plt.xlabel("Year")
plt.ylabel("Global Radiative Forcing (W m-2)")


for l in listss:
    num = num+1
    print(l)
    x = [i for i in range(1990, 2020)]
    y= l
    coef = np.polyfit(x,y,1)
    poly1d_fn = np.poly1d(coef) 
    plt.plot(x,y, x, poly1d_fn(x), '--k', label= list(d.keys())[num]) 


plt.legend(loc='best')    
plt.show()
    
