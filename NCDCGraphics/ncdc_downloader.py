# coding: utf-8
#!usr/bin/python3.4

import sys
import os
import sqlite3

import gzip
from urllib.request import urlretrieve
from urllib.error import URLError


class NcdcDownloader:
    '''The class that load data from ncdc portal'''
    
    def __init__(self, st_number, year):
        self.st_number = st_number
        self.year = year
    
    def ncdc_url_to_sqlite(self, st_number=None, year=None):
        '''
        The function that downloads the ncdc archive,
        decompresses it, and writes it to the sqllite database'''
    
        st_number = str(self.st_number)
        year = str(self.year)
    
    
        try:
        
            file_inp = st_number + '-99999-' +year + '.op.gz'
            url = 'ftp://ftp.ncdc.noaa.gov/pub/data/gsod/' + year + '/' + file_inp
            urlretrieve(url, file_inp)
          
        except URLError:
    
            print('Check station number or year not exists')
    
        try:
    
            with gzip.open(file_inp, 'rb') as f:
        
                file_out = open(st_number + '-99999-' + year + '.txt', 'wb')
                
                for line in f:
                    file_out.write(line)
                    
        except IOError:
            
            print('File will not be writed')
        
        try: 
               
            file_out = open(st_number + '-99999-' + year  + '.txt', 'r') 
        
        except FileNotFoundError:
            
            print ('Unsuccessful session, try again')
               
        self.table_name = 'table '+ st_number + year 
        
        conn = sqlite3.connect('ncdc.db')
        self.c = conn.cursor()
        
        try:
            
            if os.path.exists(st_number + '-99999-' + year  + '.txt'):
                
                self.c.execute('''CREATE TABLE '%s'
                            (stn integer, wban integer,
                            year integer, monthday integer, temp real,
                            dewp real, slp real, stp real, wdsp real, max real,
                            min real, prcp real, sndp real)''' % self.table_name)
                            
                   
                file_out.readline()
                for line in file_out:
                    
                    # Insert values in ncdc.db, see 'gsod-description.txt'
                    self.c.execute('''INSERT INTO '%s' VALUES 
                             ('%i', '%i', '%i', '%i', '%f', '%f', '%f', '%f', 
                             '%f', '%f', '%f', '%f', '%f')''' 
                             % (self.table_name, int(line[0:6]), int(line[7:12]), 
                             int(line[14:18]), int(line[18:22]),
                             float(line[24:30]), float(line[35:41]),\
                             float(line[46:52]), float(line[57:63]),\
                             float(line[78:83]), float(line[102:108]),\
                             float(line[110:116]), float(line[118:123]),\
                             float(line[125:130])))
                             
                conn.commit()
                            
                file_out.close()

            
        # This exception occurs when a table is existing
        
        except (sqlite3.OperationalError, UnboundLocalError):
            
            try:
                os.remove(st_number + '-99999-' + year  + '.txt')
                os.remove(st_number + '-99999-' + year  + '.op.gz')
                
            except FileNotFoundError:
                pass
                    


if __name__ == '__main__':
    ncdc1 = NcdcDownloader(260630, 2000)
    ncdc1.ncdc_url_to_sqlite()
                
    
    
