# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 19:29:55 2018

@author: hasee
"""



import pandas as pd, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score

column = "word_seg"
train = pd.read_csv('D:\\new_data\\train_set.csv',iterator=True)
df_train_data=[]
loop = True
while loop:
    try:
        data_0 = train.get_chunk(50000)
        df_train_data.append(data_0)
    except:
        loop = False
        
train_df = pd.concat(df_train_data, ignore_index=True)
    
    
test = pd.read_csv('D:\\new_data\\test_set.csv',iterator=True)
df_test_data=[]
loop = True
while loop:
    try:
        data_0 = test.get_chunk(50000)
        df_test_data.append(data_0)
    except:
        loop = False
        
test_df = pd.concat(df_test_data, ignore_index=True)

#这里可以调优
vec = TfidfVectorizer(ngram_range=(1,2),min_df=3, max_df=0.9,use_idf=1,smooth_idf=1, sublinear_tf=1,max_features=100000)
#vec = HashingVectorizer(ngram_range=(1, 2), n_features=2**16)

vec_train = vec.fit_transform(train_df[column])
vec_test = vec.transform(test_df[column])
y=(train_df["class"]-1).astype(int)
#这里可以调优
#lin_clf = svm.LinearSVC(C=0.1) #78.01%
#交叉验证
lin_clf = LogisticRegression(C=10,max_iter=1000) #78.40%
scores_count=cross_val_score(lin_clf,vec_train,y,cv=10,scoring='accuracy')
print(scores_count.mean())

lin_clf.fit(vec_train,y)
joblib.dump(lin_clf, "train_model.m")
clf = joblib.load("train_model.m")

preds = lin_clf.predict(vec_test)

test_df["class"] = [x+1 for x in preds]

result = test_df.loc[:,['id','class']].to_csv(r'D:\new_data\result.csv',index=False)

