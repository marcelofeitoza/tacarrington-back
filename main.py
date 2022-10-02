from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
import pickle, pandas, numpy


app = Flask(__name__)


def runModel():
    data = pandas.read_csv('data.csv')

    x_entrada = df2[['Bx','By','Bz', 'Storm range', 'Epoch',
                    'S/C operational mode', 'WIND/MFI operational mode']].values

    y_saida = df2['Magnetic field magnitude'].values
    X_train, X_test, Y_train, Y_test = train_test_split(x_entrada, y_saida, 
                                                        test_size = 0.3, 
                                                        random_state = 42)

    # Load the model
    model = pickle.load(open('model.pkl', 'rb'))

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict(X_train)

    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)


@app.route('/')
def index():
    return jsonify({"message": "Hello NASA!"})



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        return jsonify({"message": runModel()})
    else:
        return jsonify({"message": "Wrong request method"})



if __name__ == '__main__':
    app.run(debug=True)
