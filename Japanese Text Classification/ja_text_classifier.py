from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from ja_word_tokenize import Tokenizer
from sklearn.metrics import accuracy_score
from sklearn import svm

me = Tokenizer()

def test_accuracy(xTestvect,yTestvect,model):
    ypred = model.predict(xTestvect)
    score = accuracy_score(yTestvect, ypred)
    return score

def test_text(text,model):
    yPred = model.predict(vect.transform([text]))
    return yPred

def data_details(df):
    print("================DATA DETAILS==============")
    print("TOTAL RECORDS:", len(df))
    print("COUNT OF EACH CATEGORY IN THE DATA")
    print(df.CARETYPE.value_counts())
    print("==" * 20)

def word_tokenize(text):
    return me.tokenize(text)

vect = TfidfVectorizer(tokenizer= lambda x: word_tokenize(x),sublinear_tf=True, encoding='utf-8',
                                  decode_error='ignore',
                                 )

df = pd.read_csv("<path_to_train_csv>")
test_df = pd.read_csv("<path_to_test_csv>")
data_details(df)

X_train_data = vect.fit_transform( df["TEXT"].values.astype('U'))
Y_train_data = df["LABEL"]
xTestvect = vect.transform(test_df['TEXT'].values.astype('U'))
yTestvect = test_df['LABEL']

model = svm.SVC(gamma='scale', decision_function_shape='ovo') #74%
model.fit(X_train_data, Y_train_data)

print ("ACCURACY: ",test_accuracy(xTestvect,yTestvect,model))
while True:
    text = input(">")
    print ("TEST:",test_text(text,model))



