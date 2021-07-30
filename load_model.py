import joblib

loaded_model = joblib.load('dib_79.pkl')

pred = loaded_model.predict([[10, 20, 30, 40, 10, 20, 10, 10]])

if pred[0] == 1:
    print('Patient is diabetic')
else:
    print('Patient is not diabetic')