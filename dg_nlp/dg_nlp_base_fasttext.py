import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("D:\\new_data\\new_data\\train_set.csv")
data = data.loc[:,['word_seg','class']]
data['label'] = data.apply(lambda x:'label'+str(x[1]),axis=1)
x_train,x_test = train_test_split(data, test_size=0.3, random_state=42)

x_train.loc[:,['word_seg','label']].to_csv("D:\\new_data\\new_data\\train_set1.txt",index=False,header=None,sep='\t')
x_test.loc[:,['word_seg','label']].to_csv("D:\\new_data\\new_data\\test_set1.txt",index=False,header=None,sep='\t')

import fastText.FastText as ff

classifier = ff.train_supervised('D:\\new_data\\new_data\\train_set1.txt',label = "label")

result = classifier.test("D:\\new_data\\new_data\\test_set1.txt")