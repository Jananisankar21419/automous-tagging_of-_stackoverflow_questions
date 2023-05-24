import joblib
joblib_file="tagPredictor.pkl"
joblib.dump(clf,joblib_file)

tagPredictorModel=joblib.load('tagPredictor.pkl')