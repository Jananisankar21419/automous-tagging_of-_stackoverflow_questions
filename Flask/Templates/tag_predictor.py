# IMPORTING MODEL
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer

# READ DATA
df = pd.read_csv('C:/Users/91630/Desktop/stackoverflow/dataset/final-data.csv')
                 
df1 = df.dropna()
import ast
df1['Tags'] = df1['Tags'].apply(lambda x: ast.literal_eval(x))

# Load from file
tagPredictorModel = joblib.load('tagPredictor.pkl')

tfidf=TfidfVectorizer(analyzer= 'word', max_features=10000, ngram_range=(1,3), stop_words='english')
X = tfidf.fit_transform(df1['Body'].values.astype(str))

multilabel = MultiLabelBinarizer()
y=df1['Tags']
y=multilabel.fit_transform(y)

def getTags(question):
 question = tfidf.transform(question)
 multilabel.inverse_transform(tagPredictorModel.predict(question))
 print(tags)
 return tags
