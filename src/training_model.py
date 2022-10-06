#Dataset preparation
import json
import pandas as pd

path = '/content/drive/MyDrive/flood_project/Training_dataset/'
testing_path = '/content/drive/MyDrive/flood_project/test_set/'

#Load the training dataset using metadata and label data.
train_df = pd.read_csv(path + 'devset_images_gt.csv')
train_df.columns=(['image_id', 'label'])
train_df["image_id"] = train_df["image_id"].astype(str)
train_df = train_df[train_df.columns[[0, 1]]]

json_filename = path + "devset_images_metadata.json"
with open(json_filename) as json_file:
    data = json.load(json_file)

required_columns = ['description', 'user_tags', 'image_id', 'title']
json_df = pd.DataFrame(data['images'], columns = required_columns1)
print(json_df.head())
#merge label and json dataframes
train_df = pd.merge(train_df, json_df, how='inner')
train_df.head()


#Load the testing dataset using metadata and label data.
test_df = pd.read_csv(testing_path + 'testset_images_gt.csv')
test_df.columns=(['image_id', 'label'])
test_df["image_id"] = test_df["image_id"].astype(str)
test_df = test_df[test_df.columns[[0, 1]]]

json_filename = testing_path + "testset_images_metadata.json"
with open(json_filename) as json_file:
    data = json.load(json_file)

required_columns = ['description', 'user_tags', 'image_id', 'title']
json_df = pd.DataFrame(data['images'], columns = required_columns)
#merge label and json dataframes
test_df = pd.merge(test_df, json_df, how='inner')
test_df.head()


from sentence_transformers import SentenceTransformer
model = SentenceTransformer('bert-base-nli-mean-tokens')


train_df = train_df.drop(columns=['user_tags','image_id'])
test_df = test_df.drop(columns=['user_tags','image_id'])
train_df = train_df.fillna(" ")
test_df = test_df.fillna(" ")

X_train = train_df[['description', 'title']]
y_train = train_df['label'].tolist()
X_test = test_df[['description', 'title']]
y_test = test_df['label'].tolist()

#Generating the embeddings for description and title
sentence_embeddings_description_train = model.encode(X_train.loc[:,'description'].tolist())
sentence_embeddings_title_train = model.encode(X_train.loc[:,'title'].tolist())

sentence_embeddings_description_test = model.encode(X_test.loc[:,'description'].to_list())
sentence_embeddings_title_test = model.encode(X_test.loc[:,'title'].to_list())


#Concatenating the embeddings
X_train = []
for i in range(len(sentence_embeddings_description_train)):
  X_train.append(sentence_embeddings_description_train[i].tolist() + sentence_embeddings_title_train[i].tolist())
X_test = []
for i in range(len(sentence_embeddings_description_test)):
  X_test.append(sentence_embeddings_description_test[i].tolist() + sentence_embeddings_title_test[i].tolist())
  
  
#Model building and training
from sklearn.svm import SVC
svm = SVC(kernel='rbf')

svm.fit(X_train, y_train)


#Test set evaluation metrics
from sklearn.metrics import classification_report

#predict response using SVM
svm_y_pred = svm.predict(X_test)

# calculate report for svm model
svm_report = classification_report(y_test, svm_y_pred, target_names=['not flooded', 'flooded'])

print('SVM Model classification report is: \n', svm_report)
