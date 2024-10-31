from io import BytesIO
from bs4 import BeautifulSoup
import sqlite3
from collections import defaultdict
import socket
from urllib.request import urlopen
import pandas as pd
import os
import re
from pathlib import Path
from tkinter import ttk
import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import json
import time

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
        
    def deleteRecord(self, query):
        try:
            sqliteConnection = self.db
            cursor = sqliteConnection.cursor()
            print("Delete query: ",query)
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

    def query_builder(self, op, *args,**kw_attr):
        try:
            if op == "insert":
                cols, vals = self._escape(zip(*kw_attr.items()))
                self._cmd_string = 'INSERT INTO {table_name} ({column_names}) VALUES ({param_marks})'
                self._fmt_params['column_names'] = ', '.join(cols)
                self._fmt_params['param_marks'] = ', '.join('?' for _ in range(len(cols))) 
                self._values['cmd'] = vals
                self._cmd_string = 'INSERT INTO {table_name} ({column_names}) VALUES ({param_marks})'.format(table_name = self._fmt_params['table_name'], column_names =self._fmt_params['column_names'], param_marks =self._fmt_params['param_marks'])
            elif op == "table":
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
            elif op == "select":
                cols, vals = self._escape(zip(*kw_attr.items()))
                self._cmd_string = 'SELECT {ID} FROM {table_name} WHERE {condition}'
                self._fmt_params['column_names'] = ', '.join(cols)
                self._values['cmd'] = vals 
                a = []
                b=[]
                c=[]
                if str(args) == "()":
                    args = "*"
                for i in range(0, len(cols)):
                    a.append(self._fmt_params['column_names'].split(", ")[i])
                    b.append(self._values['cmd'][i])
                    c.append(a[i] +" == "+"\'"+ b[i]+"\'")                
                self._cmd_string = 'SELECT {ID} FROM {table_name} WHERE {condition}'.format(table_name = self._fmt_params['table_name'],ID = str(args), condition = ", ".join(map(str,c)))
            elif op == "delete":
                cols, vals = self._escape(zip(*kw_attr.items()))
                self._cmd_string = 'DELETE FROM {table_name} WHERE {condition}'
                self._fmt_params['column_names'] = ', '.join(cols)
                self._values['cmd'] = vals  
                a = []
                b=[]
                c=[]
                for i in range(0, len(cols)):
                    a.append(self._fmt_params['column_names'].split(", ")[i])
                    b.append(self._values['cmd'][i])
                    c.append(a[i] +" = "+ "\'"+b[i]+ "\'")                
                self._cmd_string = 'DELETE FROM {table_name} WHERE {condition}'.format(table_name = self._fmt_params['table_name'], condition = ", ".join(map(str,c)))
            return self._cmd_string
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
class data():
    
    def __init__(self, *query):
        self.query = query
        self.r = defaultdict(list)
        self.v = []
        self.s = defaultdict(list)
        self.dtb = Database("Lab2.db", "Database")  
    def buildDTB(self):
        dt = []
        arr= ["State"]
        for i in range(1970, 2021):
            arr.append(str(i))
        df = pd.read_csv('USAStatesCO2.csv', skiprows = 4,nrows= 51, encoding="ISO-8859-1")
        
        specific_columns=df[arr]
        self.s = specific_columns.to_dict('list')
        g= []
        y=0
        #print(s)
        for j in self.s:
            if j != "State":
                self.v.append(j)
                
                #print(s[j])
                for i in range(0, len(self.s[j])):
                    g.append(self.s[j][int(i)])
                    
        for l in range(0, len(self.v)):
            
            for k in range(l, len(g), 51):
                self.r[(self.s["State"][y])].append(g[k])
            y=y+1
        #print(r)
        #print(v)
        
              
        dicti = {'ID':"INTEGER PRIMARY KEY", 'STATE':"TEXT NOT NULL"}
        dicti2 = {'ID': 0 , 'STATE':"name"}
        for a in self.v:
            dicti["yr"+a] = "INTEGER NOT NULL"
            dicti2["yr"+a] = 1234
        
        tqb= self.dtb.query_builder(op = "table", **dicti)
        self.dtb.table(tqb)
        
        #print(tqb)
        
        iqb = self.dtb.query_builder(op = "insert", **dicti2)
        #print(iqb)
        
        q=0
        tupl = []
        #now we run thru the values in each table and add it to the sql database
        for i in self.r:
            q= q+1
            for c in range(len(self.r[i])):
                tupl.append(float(self.r[i][c]))
            data_t = (q,i, *tupl)
            tupl.clear()
            self.dtb.insert(iqb,data_t)
        
    def close(self):
        self.dtb.close()
    def getStates(self):
        j = (self.s["State"][0:51])
        return ",".join(j)
    def getValues(self):
        for i in self.v:
            return i
    def getDTB(self):
        return self.dtb
    


dat = data()
dat.buildDTB()
sta = dat.getStates()
d = dat.getDTB()

import socket            
 
s = socket.socket()        
print ("Socket successfully created")



port = 11111               
s.bind(('', port))        
print ("socket binded to %s" %(port))
 

s.listen(5)    
print ("socket is listening")

while True:
 
    c, addr = s.accept()    
    print ('Got connection from', addr )
    
    c.send(json.dumps(sta).encode()) 
    
    inpu = c.recv(1024).decode()
    
    

    while(inpu != 'END'):
        requestedData = d.Search(d.query_builder(op = "select", STATE= inpu))
        sendingData = list()
        for i in range(2, len(requestedData[0])): #remove state name which is first element
            sendingData.append(float(requestedData[0][i]))
        c.send(json.dumps(sendingData).encode())
        inpu = c.recv(1024).decode() 
        
    c.close()
    break

dat.close()

