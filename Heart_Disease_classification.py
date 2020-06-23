
###Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import f1_score,accuracy_score
from sklearn.ensemble import AdaBoostClassifier
import pickle
from sklearn.preprocessing import MinMaxScaler



###Load in the dataset
#heart_disease_dataset = pd.read_csv("cardiovascular_diseases_dv3.csv",sep=';')
heart_disease_dataset = pd.read_csv(r'C:\Users\Himanshu Patel\Downloads\cardiovascular-disease-dataset\Cleansed_MyData_Train.csv')

print(heart_disease_dataset.info())
print(heart_disease_dataset.head())
##check for duplicates in the data
print(format(heart_disease_dataset.duplicated().sum()))


##Explore the duplicates
duplicated = heart_disease_dataset[heart_disease_dataset.duplicated(keep=False)]
duplicated = duplicated.sort_values(by=['AGE','GENDER','HEIGHT'], ascending= False)

duplicated.head(6)

#drop duplicates
heart_disease_dataset.drop_duplicates(inplace=True)
print(format(heart_disease_dataset.duplicated().sum()))

heart_disease_dataset.describe()


#heart_disease_dataset["BMI"] = heart_disease_dataset["WEIGHT"] / (heart_disease_dataset["HEIGHT"]/100)**2
#out_filter = ((heart_disease_dataset["AP_HIGH"]>250) | (heart_disease_dataset["AP_LOW"]>200))
#data = heart_disease_dataset[~out_filter]
#len(data)

#out_filter2 = ((heart_disease_dataset["AP_HIGH"] < 0) | (heart_disease_dataset["AP_LOW"] < 0))
#heart_disease_dataset = heart_disease_dataset[~out_filter2]



###Distributions of age,height and weight variables
fig, axes = plt.subplots(1,3, figsize=(18,4))
sns.distplot(heart_disease_dataset.AGE, bins=10, kde= True, ax=axes[0])
sns.distplot(heart_disease_dataset.WEIGHT, bins=10, kde=True, ax=axes[2])
sns.boxplot(heart_disease_dataset.WEIGHT)

correlation = heart_disease_dataset.corr()
###plot heatmap of the correlated features
plt.figure(figsize=(14,12))
heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1,cmap="RdBu_r")
plt.show()

###Prepararing the train and test models
from sklearn.model_selection import train_test_split

y = heart_disease_dataset['CARDIO_DISEASE']
X = heart_disease_dataset.drop(['CARDIO_DISEASE'],axis =1 ,inplace=False)
X.head()

#Split the data into training and testing sets
X_train,X_test, y_train,y_test = train_test_split(X,y,
                                                  test_size = 0.25,
                                                  random_state = 0)

# Show the results of the split
print("Training set has {} samples.".format(X_train.shape[0]))
print("Testing set has {} samples.".format(X_test.shape[0]))

###Decision tree predictor

#Import decision tree classification model from sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

DT_predictor = DecisionTreeClassifier(max_depth=3, min_samples_split=50,min_samples_leaf=50,random_state=13)
DT_predictor.fit(X_train, y_train)
y_predicted = DT_predictor.predict(X_test)
print(y_predicted)

# Evaluate the model
print("------------------------------------------------------")
print("Confussion Matrix")
print("------------------------------------------------------")
print(confusion_matrix(y_test,y_predicted))
print("------------------------------------------------------")
print("Classification Report")
print("------------------------------------------------------")
print(classification_report(y_test,y_predicted))
print("------------------------------------------------------")
DT_accuracy = round(accuracy_score(y_test, y_predicted), 2)
print("Overall accuracy score: " + str(DT_accuracy))
print("------------------------------------------------------")


# Import Random Forest classification model from sklearn
from sklearn.ensemble import RandomForestClassifier

RF_predictor = RandomForestClassifier(n_estimators=50, random_state=17)
RF_predictor.fit(X_train, y_train)
y_predicted = RF_predictor.predict(X_test)
print(y_predicted)

# Evaluate the model
print("------------------------------------------------------")
print("Confussion Matrix")
print("------------------------------------------------------")
print(confusion_matrix(y_test,y_predicted))
print("------------------------------------------------------")
print("Classification Report")
print("------------------------------------------------------")
print(classification_report(y_test,y_predicted))
print("------------------------------------------------------")
RF_accuracy = round(accuracy_score(y_test, y_predicted), 2)
print("Overall accuracy score: " + str(RF_accuracy))
print("------------------------------------------------------")

# Feature Scaling, required by SVM and KNN algorithms
from sklearn.preprocessing import StandardScaler

sc = MinMaxScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Import SVM classification model from sklearn
from sklearn.svm import SVC

SV_classifier = SVC(kernel='linear')
SV_classifier.fit(X_train, y_train)

y_predicted = SV_classifier.predict(X_test)

print(y_predicted)



# Evaluate the model
print("------------------------------------------------------")
print("Confussion Matrix")
print("------------------------------------------------------")
print(confusion_matrix(y_test,y_predicted))
print("------------------------------------------------------")
print("Classification Report")
print("------------------------------------------------------")
print(classification_report(y_test,y_predicted))
print("------------------------------------------------------")
SV_accuracy = round(accuracy_score(y_test, y_predicted), 2)
print("Overall accuracy score: " + str(SV_accuracy))
print("------------------------------------------------------")

# Import KNN classification model from sklearn
from sklearn.neighbors import KNeighborsClassifier

KNN_classifier = KNeighborsClassifier(n_neighbors=25)
KNN_classifier.fit(X_train, y_train)
y_predicted = KNN_classifier.predict(X_test)
print(y_predicted)

# Evaluate the model
print("------------------------------------------------------")
print("Confussion Matrix")
print("------------------------------------------------------")
print(confusion_matrix(y_test,y_predicted))
print("------------------------------------------------------")
print("Classification Report")
print("------------------------------------------------------")
print(classification_report(y_test,y_predicted))
print("------------------------------------------------------")
KNN_accuracy = round(accuracy_score(y_test, y_predicted), 2)
print("Overall accuracy score: " + str(KNN_accuracy))
print("------------------------------------------------------")


#from xgboostcode import XGBClassifier
from xgboost import XGBClassifier

model = XGBClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
print(y_pred)

# Evaluate the model
print("------------------------------------------------------")
print("Confussion Matrix")
print("------------------------------------------------------")
print(confusion_matrix(y_test,y_pred))
print("------------------------------------------------------")
print("Classification Report")
print("------------------------------------------------------")
print(classification_report(y_test,y_pred))
print("------------------------------------------------------")
XGB_accuracy = round(accuracy_score(y_test, y_pred), 2)
print("Overall accuracy score: " + str(XGB_accuracy))
print("------------------------------------------------------")

from catboost import CatBoostClassifier

#features = list(X_train.columns)
#Checking for any categorical features
cat_features_index = np.where(X_train.dtype != np.float)[0]
#cat_features = ["CARDIO_DISEASE","GENDER","SMOKE","ALCOHOL","PHYSICAL_ACTIVITY","CHOLESTEROL"]
print(cat_features_index)

clf = CatBoostClassifier(
   task_type = "CPU",
    iterations=50,
    random_state = 2021,
    learning_rate=0.1,
    eval_metric = "F1",
    loss_function='CrossEntropy'
)


clf.fit(X_train, y_train,
       cat_features=cat_features_index,
        plot=True,
        eval_set=(X_test, y_test),
        verbose=False
)
#X_test = pd.DataFrame(X_test)
y_pred_catboost = clf.predict(X_test)
preds_proba = clf.predict_proba(X_test)
#y_pred_catboost = catboost.predict_prob(pd.DataFrame(X_test))
print("proba:",preds_proba)
print(f1_score(y_test,y_pred))
print(accuracy_score(y_test,y_pred))

print('CatBoost model is fitted: ' + str(clf.is_fitted()))
print('CatBoost model parameters:')
print(clf.get_params())

catboost_accuracy = round(accuracy_score(y_test, y_pred_catboost), 2)
print("Overall accuracy score: " + str(catboost_accuracy))
pickle.dump(clf,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
#create adaboost classifer object
AdaModel = AdaBoostClassifier(n_estimators=150,learning_rate=1)

Adamodel1 = AdaModel.fit(X_train,y_train)
y_pred_adamodel = Adamodel1.predict(X_test)

print("Accuracy :",accuracy_score(y_test,y_pred_adamodel))
Ada_accuracy = round(accuracy_score(y_test, y_pred_adamodel), 2)
print("Overall accuracy score: " + str(Ada_accuracy))

pickle.dump(SV_classifier,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))





# Compare accuracy of the four classification models
compare_scores = {'Decission Tree': DT_accuracy, 'Random Forest': RF_accuracy, 'Support Vector Machine (SVM)': SV_accuracy, 'K Nearest Neighbors (KNN)': KNN_accuracy,'XGBoost (XGB)':XGB_accuracy,'AdaBoost':Ada_accuracy,'Catboost':catboost_accuracy}
print(compare_scores)