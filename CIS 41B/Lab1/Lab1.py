from io import BytesIO
from bs4 import BeautifulSoup
from collections import defaultdict
from urllib.request import urlopen
import csv
import sqlite3
import pandas as pd
import os
import pickle

sqliteConnection = None

def openHtmlFile(htmlfile):
    f = open(htmlfile, "r")
    contents = f.read()
    return BeautifulSoup(contents, 'html.parser')
header = []
results = []
r=[]
e = []
d = defaultdict(list)

soupf = openHtmlFile("Co2.html") #local file
arr = soupf.findAll('td')
for i in range(9,len(arr),84):
    header.append(int(arr[i].text))
    
#finding the average value per month and finding the average value for each year
for i in range(12, len(arr), 7):
    results.append(float(arr[i].text))
for j in range(0, len(results),12):
    r.append(round(sum(results[j:j+12])/12, 2))
for k in range(0, len(header)):
    e.append((header[k], r[k]))
    
#creating defaultdict d to hold the values    
for hed, res in e:
    d[hed]=res
    


dt = []
df = pd.read_csv('SeaLevel.csv', comment='#')
specific_columns=df[["year","TOPEX/Poseidon"]]
s = specific_columns.to_dict('list')
o = defaultdict(list)
p = defaultdict(list)
g= []

#finding the average value for each year by adding the values for each year and dividing by the times added
for i in range(0,len(s['year'])):
    dt.append((int(s['year'][i]),float(s['TOPEX/Poseidon'][i])))
for y, t in dt:
    o[y].append(t)
for name in o:
    n = round(sum(o[name])/len(o[name]),2)
    p[name] = n
print(s)
print(dt)
print(o)
print(p)


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
        
    '''
    this is my query builder for inserting values,
    input: dict of column name = cmd (data ie. 24)
    returns: insert query string
    '''
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
                    c.append(a[i] +" == "+"\""+ b[i]+"\"")                
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
                    c.append(a[i] +" = "+ "\""+b[i]+ "\"")                
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
#build database and queries, please work (UPDATE: IT WORKED YESSSSSSS, I AM SO HAPPY WORDS CANNOT DESCRIBE MY FEELINGS CURRENTLY)
dtb = Database("Lab1.db", "Database")        

tqb= dtb.query_builder(op = "table", ID = "INTEGER PRIMARY KEY", NAME="TEXT NOT NULL", YEAR = "TEXT NOT NULL", AVG = "TEXT NOT NULL")
dtb.table(tqb)

print(tqb)

#placeholder values for datatypes
iqb = dtb.query_builder(op = "insert", ID = 0, NAME="name", YEAR = 1234, AVG = 1234)
print(iqb)

q=0
#now we run thru the values in each table and add it to the sql database
for i in d:
    q= q+1
    data_t = (q, "CO2",i, d[i])
    dtb.insert(iqb,data_t)
for j in p:
    q= q+1
    data_t = (q, "Sea Level",j, p[j])
    dtb.insert(iqb,data_t)
    
#read
print(dtb)
records = dtb.readTable()
[print(r) for r in records]


#shut-down
dtb.close()

'''
Table query:  CREATE TABLE Database (ID INTEGER PRIMARY KEY, NAME TEXT NOT NULL, YEAR TEXT NOT NULL, AVG TEXT NOT NULL)
SQLite table created
CREATE TABLE Database (ID INTEGER PRIMARY KEY, NAME TEXT NOT NULL, YEAR TEXT NOT NULL, AVG TEXT NOT NULL)
INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
Search query:  INSERT INTO Database (ID, NAME, YEAR, AVG) VALUES (?, ?, ?, ?)
Inserted successfully into table
<__main__.Database object at 0x0000020E14BB0E50>
Search query:  SELECT * from Database
ToTotal rows are:   89
(1, 'CO2', '1959', '315.97')
(2, 'CO2', '1960', '316.91')
(3, 'CO2', '1961', '317.64')
(4, 'CO2', '1962', '318.45')
(5, 'CO2', '1963', '318.99')
(6, 'CO2', '1964', '214.41')
(7, 'CO2', '1965', '320.04')
(8, 'CO2', '1966', '321.38')
(9, 'CO2', '1967', '322.16')
(10, 'CO2', '1968', '323.04')
(11, 'CO2', '1969', '324.62')
(12, 'CO2', '1970', '325.68')
(13, 'CO2', '1971', '326.32')
(14, 'CO2', '1972', '327.45')
(15, 'CO2', '1973', '329.68')
(16, 'CO2', '1974', '330.18')
(17, 'CO2', '1975', '295.23')
(18, 'CO2', '1976', '332.04')
(19, 'CO2', '1977', '333.83')
(20, 'CO2', '1978', '335.4')
(21, 'CO2', '1979', '336.84')
(22, 'CO2', '1980', '338.75')
(23, 'CO2', '1981', '340.1')
(24, 'CO2', '1982', '341.45')
(25, 'CO2', '1983', '343.05')
(26, 'CO2', '1984', '307.42')
(27, 'CO2', '1985', '346.12')
(28, 'CO2', '1986', '347.42')
(29, 'CO2', '1987', '349.19')
(30, 'CO2', '1988', '351.57')
(31, 'CO2', '1989', '353.12')
(32, 'CO2', '1990', '354.39')
(33, 'CO2', '1991', '355.61')
(34, 'CO2', '1992', '356.45')
(35, 'CO2', '1993', '357.1')
(36, 'CO2', '1994', '358.83')
(37, 'CO2', '1995', '360.82')
(38, 'CO2', '1996', '362.61')
(39, 'CO2', '1997', '363.73')
(40, 'CO2', '1998', '366.7')
(41, 'CO2', '1999', '368.38')
(42, 'CO2', '2000', '369.55')
(43, 'CO2', '2001', '371.14')
(44, 'CO2', '2002', '373.28')
(45, 'CO2', '2003', '375.8')
(46, 'CO2', '2004', '377.52')
(47, 'CO2', '2005', '379.8')
(48, 'CO2', '2006', '381.9')
(49, 'CO2', '2007', '383.79')
(50, 'CO2', '2008', '385.6')
(51, 'CO2', '2009', '387.43')
(52, 'CO2', '2010', '389.9')
(53, 'CO2', '2011', '391.65')
(54, 'CO2', '2012', '393.85')
(55, 'CO2', '2013', '396.52')
(56, 'CO2', '2014', '398.65')
(57, 'CO2', '2015', '400.83')
(58, 'CO2', '2016', '404.24')
(59, 'CO2', '2017', '406.55')
(60, 'CO2', '2018', '408.52')
(61, 'CO2', '2019', '377.13')
(62, 'Sea Level', '1992', '-17.12')
(63, 'Sea Level', '1993', '-17.05')
(64, 'Sea Level', '1994', '-13.45')
(65, 'Sea Level', '1995', '-9.94')
(66, 'Sea Level', '1996', '-6.58')
(67, 'Sea Level', '1997', '-4.81')
(68, 'Sea Level', '1998', '-5.27')
(69, 'Sea Level', '1999', '-3.59')
(70, 'Sea Level', '2000', '-1.34')
(71, 'Sea Level', '2001', '3.67')
(72, 'Sea Level', '2002', '7.61')
(73, 'Sea Level', '2003', '11.93')
(74, 'Sea Level', '2004', '12.88')
(75, 'Sea Level', '2005', '14.17')
(76, 'Sea Level', '2006', '17.78')
(77, 'Sea Level', '2007', '17.86')
(78, 'Sea Level', '2008', '22.19')
(79, 'Sea Level', '2009', '25.63')
(80, 'Sea Level', '2010', '26.86')
(81, 'Sea Level', '2011', '25.22')
(82, 'Sea Level', '2012', '36.12')
(83, 'Sea Level', '2013', '36.89')
(84, 'Sea Level', '2014', '40.76')
(85, 'Sea Level', '2015', '49.55')
(86, 'Sea Level', '2016', '51.8')
(87, 'Sea Level', '2017', '53.73')
(88, 'Sea Level', '2018', '57.19')
(89, 'Sea Level', '2019', '63.09')


'''