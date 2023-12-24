import numpy as np 
import pandas as pd 
import json
import pickle
import config


class AbaloneAgeDetector():
    def __init__(self,Sex, Length, Diameter, Height, Whole_weight, Shucked_weight, Viscera_weight, Shell_weight):
        self.Sex = Sex
        self.Length = Length
        self.Diameter = Diameter
        self.Height = Height
        self.Whole_weight = Whole_weight
        self.Shucked_weight = Shucked_weight 
        self.Viscera_weight = Viscera_weight
        self.Shell_weight = Shell_weight

    def load_data(self):
        with open(config.model_path, 'rb') as file:
            self.model = pickle.load(file)

        with open(config.scaler_path, 'rb') as file1:
            self.scaler = pickle.load(file1)

        with open(config.features_path, 'r') as file2:
            self.features_data = json.load(file2)

    def predict_age(self):
        self.load_data()
        # Create Input Features Series 
        test_series = pd.Series(np.zeros(len(self.features_data['columns'])),index=self.features_data['columns'])
        test_series['Sex'] = self.features_data['Sex'][self.Sex]
        test_series['Length'] = self.Length
        test_series['Diameter'] = self.Diameter
        test_series['Height'] = self.Height
        test_series['Whole_weight'] = self.Whole_weight
        test_series['Shucked_weight'] = self.Shucked_weight
        test_series['Viscera_weight'] = self.Viscera_weight
        test_series['Shell_weight'] = self.Shell_weight

        # Scaler : Scale The Data 
        input_scaled = self.scaler.transform([test_series])
        y_pred = self.model.predict(input_scaled)[0]
        y_pred = np.around(y_pred,2)
        y_pred = f"Predicted Abalone Age is : {y_pred} Years"

        return y_pred
    


# f = [Sex, Length, Diameter, Height, Whole_weight, Shucked_weight, Viscera_weight, Shell_weight]

