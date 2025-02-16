import os
import mlflow
import pandas as pd
from sklearn.metrics import confusion_matrix


def init():
    global g_model

    model_dir = os.environ['AZUREML_MODEL_DIR']
    model_rootdir = os.listdir(model_dir)[0]
    model_path = os.path.join(model_dir, model_rootdir)

    g_model = mlflow.sklearn.load_model(model_path)


def run(data):
    predict_result = []

    print('type:', type(data))
    print(data)

    for file in data:
        df = pd.read_csv(file, engine='c')
        print(df.head())

        try:
            df.loc[df['target']=='setosa', 'target'] = '0'
            df.loc[df['target']=='versicolor', 'target'] = '1'
            df.loc[df['target']=='virginica', 'target'] = '2'

            # ランダムフォレスト
            predict_result = g_model.predict(df.drop('target', axis=1))
            df['pred'] = predict_result
            print('df.shape:', df.shape)
            print('df.clumns:', len(df.columns))
            print(pd.DataFrame(data=[df.columns], columns=df.columns))

            print('confusion matrix')
            print(confusion_matrix(df['target'], predict_result))

            df = pd.concat([pd.DataFrame(data=[df.columns], columns=df.columns), df], ignore_index=True)


        except Exception as e:
            raise e
    
    # return df
    return pd.DataFrame(data=[df.columns], columns=df.columns)

