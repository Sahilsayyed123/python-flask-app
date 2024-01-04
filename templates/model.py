import warnings
import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
df = pd.read_csv("C:/Users/USER/Downloads/health_data.csv")
warnings.filterwarnings(action='ignore')
y = df['cardio']
X = df.drop(["smoke", "id", "alco", "cardio", "Unnamed: 0"], axis=1)
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, shuffle=True, random_state=1)
model = GradientBoostingClassifier()
model.fit(X_train, y_train)
pickle.dump(model, open("model.pkl", "wb"))
