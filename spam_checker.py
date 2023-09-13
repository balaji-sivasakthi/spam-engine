from mail_spam_checker import model, feature_extraction
import pickle

model_file = 'model.pkl'
pickled_model = pickle.load(open('model.pkl', 'rb'))

#   Building a Predictable System
input_mail = [(input("enter your email "))]
# Convert Text to feature vectors
input_data_feature = feature_extraction.transform(input_mail)

# Making Prediction
prediction = pickled_model.predict(input_data_feature)

print(prediction)



