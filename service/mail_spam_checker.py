
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Data Collection and Pre Processing
raw_mail_data = pd.read_csv('service/mail_data.csv')
raw_mail_data.head()

# Replace the null values with a null string
mail_data = raw_mail_data.where(pd.notnull(raw_mail_data),'')

#  Label Encoding
mail_data.loc[mail_data['Category'] == 'spam', 'Category'] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category'] = 1

# Seperating the text as texts and label
X = mail_data['Message']
Y = mail_data['Category']

X_Train,X_test,Y_Train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=3)

feature_extraction = TfidfVectorizer(min_df=1,stop_words='english')

X_train_feature = feature_extraction.fit_transform(X_Train)
X_test_feature = feature_extraction.transform(X_test)

Y_Train = Y_Train.astype('int')
Y_test = Y_test.astype('int')

model = RandomForestClassifier()

model.fit(X_train_feature,Y_Train)

# Evaluating the Trained Model
prediction_on_Training_Data = model.predict(X_train_feature)

# Predition on Training Model
accuracy_on_training_data = accuracy_score(Y_Train,prediction_on_Training_Data)

print("Accuracy for Training : ",accuracy_on_training_data * 100)

# Predict on Test Data
import pickle
pickle.dump(model, open('model.pkl', 'wb'))


