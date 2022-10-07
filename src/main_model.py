from sklearn.svm import SVC
from sentence_transformers import SentenceTransformer
import pickle
import os
import argparse


def predict_flood(description, title):
    #loading the tokenizer
    filename = 'deep_model.sav'
    if not os.path.exists(filename):
        os.system("gdown 1Vd1TV-MFHqC4IWbJCGcmKreCf5Jx_au_")
    loaded_model = pickle.load(open(filename, 'rb'))

    #loading the model
    filename = 'svm_model.sav'
    if not os.path.exists(filename):
        os.system("gdown  1lg3_Ni8r5p1CK9W3DAPsJuM1lyNt8U4a")
    svm_model = pickle.load(open(filename, 'rb'))

    input_txt = loaded_model.encode(description)
    input_title = loaded_model.encode(title)
    input_list = input_txt.tolist() + input_title.tolist()

    result = svm_model.predict([input_list])

    if result[0] == 1:
        return(1)
        print('The post signifies flood')
    else:
        return(0)
        print('The post does not signify a flood')
 
if __name__ == '__main__':
    #Take inputs
    parser = argparse.ArgumentParser(description='Flood detection')

    parser.add_argument('--description', type=str, default='It is a flood')
    parser.add_argument('--title', type=str, default='')

    args = parser.parse_args()

    description = args.description
    title = args.title

    out = predict_flood(description, title)
    
