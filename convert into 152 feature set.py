# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 09:24:59 2021

@author: Susmita
"""
import pandas as pd 


dataset = pd.read_csv('152 features.csv') 
#print(dataset)
total_feature1=int(20)
featureSetSize=int(19)

# input 
x1 = dataset.iloc[:, 0:total_feature1].values 

dataTrain = pd.read_csv('impense data.csv')

f= open("impense_152.csv","w+")  
        
for i in range (0,1):    
        with open("impense data.csv",'r') as file: 
            
            for line in file:         
                for word in line.split(): 
                    word1, word2=word.split(',')
                    seq=word1
                    #print(seq)
                    for i in range(0,8):
                        if(seq[i]=='A'):
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[0][j]))
                                f.write(",")
                            #print("1")
                        if(seq[i]=='R'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[1][j]))
                                f.write(",")
                        if(seq[i]=='N'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[2][j]))
                                f.write(",")
                        if(seq[i]=='D'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[3][j]))
                                f.write(",")
                        if(seq[i]=='C'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[4][j]))
                                f.write(",")
                        if(seq[i]=='Q'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[5][j]))
                                f.write(",")
                        if(seq[i]=='E'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[6][j]))
                                f.write(",")
                        if(seq[i]=='G'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[7][j]))
                                f.write(",")
                        if(seq[i]=='H'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[8][j]))
                                f.write(",")
                        if(seq[i]=='I'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[9][j]))
                                f.write(",")
                        if(seq[i]=='L'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[10][j]))
                                f.write(",")
                        if(seq[i]=='K'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[11][j]))
                                f.write(",")
                        if(seq[i]=='M'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[12][j]))
                                f.write(",")
                        if(seq[i]=='F'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[13][j]))
                                f.write(",")
                        if(seq[i]=='P'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[14][j]))
                                f.write(",")
                        if(seq[i]=='S'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[15][j]))
                                f.write(",")
                        if(seq[i]=='T'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[16][j]))
                                f.write(",")
                        if(seq[i]=='W'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[17][j]))
                                f.write(",")
                        if(seq[i]=='Y'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[18][j]))
                                f.write(",")
                        if(seq[i]=='V'):  
                            for j in range(1,featureSetSize+1):
                                f.write(str(x1[19][j]))
                                f.write(",")
                                
                f.write(str(word2))             
                f.write('\n')
            
                                          
        f.close()