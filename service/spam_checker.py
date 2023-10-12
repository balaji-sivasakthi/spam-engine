from service.mail_spam_checker import model, feature_extraction
import pickle
from langdetect import detect
import sys


model_file = 'model.pkl'
pickled_model = pickle.load(open('model.pkl', 'rb'))
input_message = sys.argv[1]

test = detect(input_message)

if test == 'en' or test == 'ta':
    input_mail = [input_message]
    # Convert Text to feature vectors
    input_data_feature = feature_extraction.transform(input_mail)

    # Making Prediction
    prediction = pickled_model.predict(input_data_feature)
    print(prediction)
    print("Message is valid")

else:
    print('0')

