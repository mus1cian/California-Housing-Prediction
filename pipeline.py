from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

def num_pipeline():
    return Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler())
    ])

def fetch_pipeline():
    housing = pd.read_csv("datasets/housing/housing.csv")
    housing_labels = housing["median_house_value"].copy()
    housing = housing.drop("median_house_value", axis=1)
    housing_num = housing.drop("ocean_proximity", axis=1)

    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]

    num_transformer = num_pipeline()
    full_pipeline = ColumnTransformer([
        ("num", num_transformer, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs)
    ])

    full_pipeline.fit(housing)

    return full_pipeline

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
  def __init__(self, add_bedrooms_per_room=True):
    self.add_bedrooms_per_room=add_bedrooms_per_room
  
  def fit(self, X, y=None):
    return self
  
  def transform(self, X):
    rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
    population_per_household = X[:, population_ix] / X[:, households_ix]
    if self.add_bedrooms_per_room:
      bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
      return np.c_[X, rooms_per_household, population_per_household,
                   bedrooms_per_room]
    else:
      return np.c_[X, rooms_per_household, population_per_household]
