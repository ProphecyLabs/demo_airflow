
import pandas as pd
import utils.ml_pipeline_config as config

def load_data():
	
	data_path = config.params['data_path']
	data = pd.read_csv(data_path)

	raw_data_path = config.params['raw_data_path']
	data.to_csv(raw_data_path, index=None)
