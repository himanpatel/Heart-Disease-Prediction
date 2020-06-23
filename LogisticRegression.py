import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
heart_disease_dataset = pd.read_csv(r'C:\Users\Himanshu Patel\Downloads\cardiovascular-disease-dataset\Cleansed_MyData_Train.csv')

y = heart_disease_dataset['CARDIO_DISEASE']
X = heart_disease_dataset.drop(['CARDIO_DISEASE'],axis =1 ,inplace=False)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.25)
clf = LogisticRegression(penalty='l2')
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)
print(accuracy)

coeff_df = pd.DataFrame([X.columns, clf.coef_[0]]).T
print(coeff_df)

pickle.dump(clf,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))