from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
import pickle, pandas, numpy


app = Flask(__name__)



def separateTrainValues(df):
    x = df.drop('Magnetic field magnitude', axis=1)
    y = df['Magnetic field magnitude']

    return X, y



def runModel():
    df = pandas.read_csv('data.csv')
    
    X, y = separateTrainValues(df)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    with open('model.pkl', 'wb') as f:
        pickle.dump(regressor, f)

    return regressor                                                       



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
