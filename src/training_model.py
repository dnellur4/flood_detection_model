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
json_df = pd.DataFrame(data['images'], columns = required_columns)
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
