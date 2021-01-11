import joblib
import inflection
import pandas as pd

class Fraud:
    
    def __init__(self):
        self.minmaxscaler = joblib.load('../parameters/minmaxscaler_cycle1.joblib')
        self.onehotencoder = joblib.load('../parameters/onehotencoder_cycle1.joblib')
        
    def data_cleaning(self, df1):
        cols_old = df1.columns.tolist()
        
        snakecase = lambda i: inflection.underscore(i)
        cols_new = list(map(snakecase, cols_old))
        
        df1.columns = cols_new
        
        return df1
    
    def feature_engineering(self, df2):
        # step
        df2['step_days'] = df2['step'].apply(lambda i: i/24)
        df2['step_weeks'] = df2['step'].apply(lambda i: i/(24*7))

        # difference between initial balance before the transaction and new balance after the transaction
        df2['diff_new_old_balance'] = df2['newbalance_orig'] - df2['oldbalance_org']

        # difference between initial balance recipient before the transaction and new balance recipient after the transaction.
        df2['diff_new_old_destiny'] = df2['newbalance_dest'] - df2['oldbalance_dest']

        # name orig and name dest
        df2['name_orig'] = df2['name_orig'].apply(lambda i: i[0])
        df2['name_dest'] = df2['name_dest'].apply(lambda i: i[0])
        
        return df2.drop(columns=['name_orig', 'name_dest', 
                      'step_weeks', 'step_days'], axis=1)
    
    def data_preparation(self, df3):
        # OneHotEncoder
        df3 = self.onehotencoder.transform(df3)

        # Rescaling 
        num_columns = ['amount', 'oldbalance_org', 'newbalance_orig', 'oldbalance_dest', 
                       'newbalance_dest', 'diff_new_old_balance', 'diff_new_old_destiny']
        df3[num_columns] = self.minmaxscaler.transform(df3[num_columns])
        
        # selected columns
        final_columns_selected = ['step', 'oldbalance_org', 'newbalance_orig', 'newbalance_dest', 
                                  'diff_new_old_balance', 'diff_new_old_destiny', 'type_TRANSFER']
        return df3[final_columns_selected]
    
    def get_prediction(self, model, original_data, test_data):
        pred = model.predict(test_data)
        original_data['prediction'] = pred
        
        return original_data.to_json(orient="records", date_format="iso")