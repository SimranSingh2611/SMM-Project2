import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import sklearn
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


#reading the csv files of the bots and non-bots
bot =  pd.read_csv('C:\\Users\\Simran Singh\\Desktop\\bots_data.csv', encoding='latin1');
nonbot = pd.read_csv('C:\\Users\\Simran Singh\\Desktop\\nonbots_data.csv', encoding='latin1');

#combining bots and non-bots into a single dataframe
all_users = pd.concat([bot, nonbot])
all_users.fillna('', inplace = True);

#splitting the dataframe into training data and testing data
y = all_users.bot;
x = all_users.drop(['id', 'id_str', 'url', 'default_profile', 'default_profile_image', 'screen_name', 'location',
              'has_extended_profile', 'status', 'lang', 'description', 'created_at', 'name','bot'], axis=1)
X_train, X_test, y_train, y_test = tts(x, y,test_size=0.25);

dt = DecisionTreeClassifier(criterion='gini', min_samples_leaf=5, min_samples_split=3)

dt = dt.fit(X_train, y_train);

y_pred = dt.predict(X_test)

#print("Accuracy of Decison Tree test {}".format(metrics.accuracy_score(X_test, y_pred)))
print("Accuracy of Decison Tree  {}".format(metrics.accuracy_score(y_test, y_pred)))

