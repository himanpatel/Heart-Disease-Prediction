import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\Himanshu Patel\Downloads\cardiovascular-disease-dataset\Cleansed_MyData.csv')

print(df)
df.columns = ['Unnamed','AGE','CHOLESTEROL','GLUCOSE','PHYSICAL_ACTIVITY','HEIGHT','WEIGHT_GAINED','CARDIO_DISEASE','SMOKE','ALCOHOL','AP_HIGH','AP_LOW','GENDER','Gender_Formatted']
print(df.WEIGHT_GAINED.head(10))

df.drop('''''',axis=1,inplace=True)
print(df.head(15))


### grouping by true and flase weight
#print(df.groupby('CARDIO_DISEASE').WEIGHT_GAINED)
#print('heart disease',df[df.CARDIO_DISEASE=='1'].WEIGHT_GAINED)
#print('No heart disease',df[df.CARDIO_DISEASE=='0'].WEIGHT_GAINED)

groupby_cardiodisease = df['WEIGHT_GAINED'].groupby(df['CARDIO_DISEASE']).plot(kind='bar')
plt.show()
print("this is it",groupby_cardiodisease)

print(len(list(df['WEIGHT_GAINED'].groupby(df['CARDIO_DISEASE']))))
print(sum(list(df['WEIGHT_GAINED'].groupby(df['CARDIO_DISEASE']))[0][1]))
