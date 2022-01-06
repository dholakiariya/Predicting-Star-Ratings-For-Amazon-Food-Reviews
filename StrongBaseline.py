import pandas as pd
import csv

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

train_data=pd.read_csv('data/train_data.csv')
dev_data=pd.read_csv('data/dev_data.csv')
test_data=pd.read_csv('data/test_data.csv')
train_data.drop(columns=['Unnamed: 0'])
dev_data.drop(columns=['Unnamed: 0'])
test_data.drop(columns=['Unnamed: 0'])

#Using Count Vectorizer to classify data
def extract_features(df_train, df_dev, df_test):

  count_vect = CountVectorizer()
  X_train = count_vect.fit_transform(train_data["review_body"])
  tfidf_transformer = TfidfTransformer()
  X_train = tfidf_transformer.fit_transform(X_train)

  X_dev = count_vect.transform(dev_data["review_body"])
  X_dev = tfidf_transformer.fit_transform(X_dev)
  X_test = count_vect.transform(test_data["review_body"])
  X_test = tfidf_transformer.fit_transform(X_test)

  y_train = train_data["star_rating"].tolist()
  y_dev = dev_data["star_rating"].tolist()
  y_test = test_data["star_rating"].tolist()

  return X_train, X_dev, X_test, y_train, y_dev, y_test

#Extract features
X_train, X_dev, X_test, y_train, y_dev, y_test = extract_features(train_data, dev_data, test_data)

#Naive Bayes Classifier
clf_nb = MultinomialNB()
clf_nb.fit(X_train, y_train)

#Predict
y_pred = clf_nb.predict(X_test)
rows = zip(y_pred)

with open('prediction_labels.csv', "w") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
