import utils.ml_pipeline_config as config
import pandas as pd

def calculate_result():

	first_model_results = pd.read_csv('./data/predictions_alpha_0.1.csv')
	second_model_results = pd.read_csv('./data/predictions_alpha_0.01.csv')

	final_predictions = (first_model_results+second_model_results)/2
	final_predictions.to_csv(config.params['final_result_path'])
	
