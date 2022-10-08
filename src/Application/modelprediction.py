from sklearn.svm import SVC
from sentence_transformers import SentenceTransformer
import pickle
import os
import argparse

class ModelPrediction():
    def __init__(self) -> None:
        svm_model = None

    def get_model(self):
        '''filename = 'deep_model.sav'
        if not os.path.exists(filename):
            os.system("python3 -m gdown 1Vd1TV-MFHqC4IWbJCGcmKreCf5Jx_au_")
        loaded_model = pickle.load(open(filename, 'rb'))

        #loading the model
        filename = 'svm_model.sav'
        if not os.path.exists(filename):
            os.system("python3 -m gdown  1lg3_Ni8r5p1CK9W3DAPsJuM1lyNt8U4a")
        svm_model = pickle.load(open(filename, 'rb'))'''

        filename = '/Users/VKANAMA/Downloads/deep_model.sav'
        '''if not os.path.exists(filename):
            print(1)
            os.system("gdown 1Vd1TV-MFHqC4IWbJCGcmKreCf5Jx_au_")'''
        loaded_model = pickle.load(open(filename, 'rb'))

        #loading the model
        filename = '/Users/VKANAMA/Downloads/svm_model.sav'
        '''if not os.path.exists(filename):
            os.system("gdown  1lg3_Ni8r5p1CK9W3DAPsJuM1lyNt8U4a")'''
        self.svm_model = pickle.load(open(filename, 'rb'))
        return loaded_model,self.svm_model

    def get_predictions(self,input_list):
        out = self.svm_model.predict([input_list])
        res = ''
        if out[0] == 1:
            res = 'The post queried signifies flood'
        else:
            res= 'The post queried does not signify a flood'
        return(res)

def main():
    #Take inputs
    parser = argparse.ArgumentParser(description='Flood detection')

    parser.add_argument('--description', type=str, default='It is a flood')
    parser.add_argument('--title', type=str, default='')
    args = parser.parse_args()

    description = args.description
    title = args.title
    loaded_model,svm_model = p.get_model()
    input_txt = loaded_model.encode(title)
    input_title = loaded_model.encode(description)
    input_list = input_txt.tolist() + input_title.tolist()
    out = p.get_predictions(input_list)
    return(out)

if __name__ == '__main__':
    p = ModelPrediction()
    description, title = main()
    