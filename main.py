from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
import pickle, pandas, numpy

from getDatasets import downloadLatestDataset, downloadAllDatasets

app = Flask(__name__)


def separateTrainValues(df):
    x = df.drop('Magnetic field magnitude', axis=1)
    y = df['Magnetic field magnitude']

    return X, y


def runModel():
    downloadLatestDataset()
    downloadAllDatasets()
    return { "status": "success" }


@app.route('/')
def index():
    return jsonify({"message": "Hello NASA!"})


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # return jsonify({"message": runModel()})
        return runModel()
    else:
        return jsonify({"message": "Wrong request method"})


if __name__ == '__main__':
    app.run(debug=True)
