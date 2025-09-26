import pandas as pd
s=pd.Series([10,20,30,40])
print(s)

data = {'Name':['Nicolas','Noah','David','Keifer','Jasper','Felix','Calix',None],'Age':[25,30,22,23,24,None,22,21]}
df = pd.DataFrame(data)
print(df)
print(df.head())  #return first 5 rows
print(df.head(3)) #return first 3 rows
print(df.tail())    #return last 5 rows
print(df.tail(4))   #return last 4 rows
print(df.info())    #info of perticular data
print(df.describe()) 
print(df.columns) #Index(['Name', 'Age'], dtype='object')
print(df.shape) #shows no. of rows and columns

data = {'Name':['Nicolas','Noah','David','Keifer'],
        'Age':[25,30,22,23],
        'Cities':['Mumbai','Goa','Chennai','Banglore']}
df = pd.DataFrame(data,index=[0,1,2,3])
print(df.loc[1])
print(df.loc[:,['Name','Cities']])
print(df.iloc[0])
print(df.iloc[1,0]) # o/p:-Noah
print(df.iloc[:,0:2])
data1 = {'Name':['Nicolas','Noah','David','Keifer','Jasper'],
        'Age':[25,30,22,23,None]}
df = pd.DataFrame(data1)
print(df.isnull())
print(df.dropna())
print(df.fillna(0))
df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)