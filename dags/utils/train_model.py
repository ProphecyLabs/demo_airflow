from sklearn.linear_model import Ridge
import utils.ml_pipeline_config as config
from joblib import dump
import pandas as pd

def train_model(**kwargs):

	scaled_data = pd.read_csv(config.params['scaled_data_path'])
	target = config.params['target_name']
	X,y = scaled_data.drop(target,1), scaled_data[target]
	alpha = kwargs['alpha']

	model = Ridge(alpha=alpha)
	model.fit(X, y)
	predictions = model.predict(X)

	pd.Series(predictions).to_csv(f'./data/predictions_alpha_{alpha}.csv', index=None)
	dump(model, f'./models/Ridge_{alpha}.joblib')
