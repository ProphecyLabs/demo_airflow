from sklearn.preprocessing import StandardScaler
import pandas as pd
import utils.ml_pipeline_config as config

def preprocess_data():

	raw_data_path = config.params['raw_data_path']
	fetched_data = pd.read_csv(raw_data_path)

	fetched_data.fillna(fetched_data.mean(), inplace=True)

	target = config.params['target_name']
	X = fetched_data.drop(target,axis=1)
	
	#dummify categorical data
	cat_cols = [c for c in X.columns if X[c].dtype == 'object']
	X = pd.get_dummies(X, columns = cat_cols)

	X_scaled = pd.DataFrame(StandardScaler().fit_transform(X),
							columns = X.columns)

	X_scaled[target] = fetched_data[target]

	X_scaled.to_csv(config.params['scaled_data_path'], index=None)

	