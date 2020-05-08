import pandas as pd
cuzzine=pd.read_csv('chefmozcuisine.csv')
place=pd.read_csv('geoplaces2.csv')
rating=pd.read_csv('rating_final.csv')
place.drop(['the_geom_meter', 'fax', 'zip',
       'alcohol', 'smoking_area', 'dress_code', 'accessibility',
       'url', 'Rambience', 'franchise', 'area', 'other_services', 'name', 'address', 'city', 'state',
       'country'],axis=1,inplace=True)
print(place.columns)
data=(rating.rating * rating.food_rating * rating.service_rating)/3
data=round(data,1)
rating['ave_rating']=data
list=[]
for i in range(0,1161):
    list.append(i)
#rating.drop([list],axis=1,inplace=True)
rating.drop(['rating','food_rating','service_rating','userID'],axis=1,inplace=True)
print(rating.head())
#rating.set_index('placeID')
result = pd.merge(rating,place,on= 'placeID')
result = pd.merge(result,cuzzine,on= 'placeID')
print(result.head())
import numpy as np
users = result['placeID'].unique()
print(len(users))
count=0
for users in result.placeID:
    while np.equal(users,result.placeID).any():
        count+=result.ave_rating
    #(result.ave_rating.mean())
    print(count)

print(result.placeID.value_counts())
