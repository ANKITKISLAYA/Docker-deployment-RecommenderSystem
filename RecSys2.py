# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:31:07 2020

@author: Ankit
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:30:37 2020

@author: Ankit
"""

import pandas as pd
from pymongo import MongoClient 
from collections import defaultdict
from operator import itemgetter 


class RecSys2:
    
    def rec(self,itemid,number,wid):
        
        citem = int(itemid)
        number = int(number)
        wid = int(wid)
        l=[]
        l1=[]
        conn = MongoClient('192.168.1.101', 27017)
        mydb = conn.ML
        mydb1 = conn.ankit_database
        collection = mydb.RecSysItem
        collection1 = mydb1.ItemWarehouse

        dfw = pd.DataFrame(list(collection1.find({ 'WarehouseId' :wid })))
        lw = dfw.iloc[0,2]
                
        df1 = pd.DataFrame(list(collection.find( { 'itemid' :23 })))
        df2 = df1.drop(['_id' , 'itemid'], axis = 1)
        df3 = df2.sort_values(0, axis=1, ascending=False, inplace=False, kind='quicksort', na_position='last')
        l1 = list(df3.columns.values)
        
        #lcolumn = list(df1.columns.values)
        #lcolumn = lcolumn[:-2]
        #lcolumn = lcolumn[2:]
        l1 = [int(i) for i in l1]
        
        
        
        
        if (citem in l1):  
            df = pd.DataFrame(list(collection.find( { 'itemid' : citem })))
            df12 = df.drop(['_id' , 'itemid'], axis = 1)
            df13 = df12.sort_values(0, axis=1, ascending=False, inplace=False, kind='quicksort', na_position='last')
            l12 = list(df13.columns.values)
            l12 = [int(i) for i in l12]
            
            pos = 0
            for itemID in l12:
                if ((itemID != citem) & (itemID in lw)):
                    l.append(itemID)
                    pos += 1
                    if (pos > number-1):
                        break
                l = [int(i) for i in l]  
            return tuple(l)
        
        else:
            for i in l1:
                if (i in lw):
                    l.append(i)
            
                if (len(l) > number):
                    break
            return tuple(l)





