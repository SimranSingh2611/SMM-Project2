import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import sklearn
from sklearn import metrics


#reading the csv files of the bots and non-bots
bot =  pd.read_csv('C:\\Users\\Simran Singh\\Desktop\\bots_data.csv', encoding='latin1');
nonbot = pd.read_csv('C:\\Users\\Simran Singh\\Desktop\\nonbots_data.csv', encoding='latin1');

#combining bots and non-bots into a single dataframe
all_users = pd.concat([bot, nonbot])
all_users.fillna('', inplace = True);

#splitting the dataframe into training data and testing data
y = all_users.bot;
x = all_users.drop('bot', axis = 1)
X_train, X_test, y_train, y_test = tts(x, y,test_size=0.25);

#TF-IDF of the 'description' parameter of the training dataset
#description      	String	       The user-defined UTF-8 string describing their account.
vectorizer = CountVectorizer()  #Converts a collection of text documents to a matrix of token counts
words_count = vectorizer.fit_transform(X_train['description'])  #Learns the vocabulary dictionary and returns term-document matrix.
tf_transformer = sklearn.feature_extraction.text.TfidfTransformer(use_idf=True).fit(words_count)
X_train = tf_transformer.transform(words_count)

clf = sklearn.svm.LinearSVC()
clf.fit(X_train, y_train)

#TF-IDF of the 'description' parameter of the test dataset
test_word_count = vectorizer.transform(X_test['description'])
X_test = tf_transformer.transform(test_word_count)

#Predicting the labels
y_predicted = clf.predict(X_test)

#Printing the accuracy of the SVM classifier
print("Accuracy of SVM  {}".format(metrics.accuracy_score(y_test, y_predicted)))
