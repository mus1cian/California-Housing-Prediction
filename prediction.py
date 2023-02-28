import joblib
import pipeline as pipe

def predict(data):
    clf = joblib.load("my_model.pkl")
    full_pipeline = pipe.fetch_pipeline()
    data_prepared = full_pipeline.transform(data)
    return clf.predict(data_prepared)
