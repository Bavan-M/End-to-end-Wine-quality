import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model=joblib.load(Path('artifacts/model_trianer/model.joblib'))

    def predict(self,data):
        predction=self.model.predict(data)
        return predction