import pandas as pd
import numpy as np
# Original DataFrame
data = {
    'Number': [1, 2, np.nan, 4, 5, np.nan, 7, 8, 9, 10],
    'Float': [0.1, 0.2, 0.3, np.nan, 0.5, 0.6, np.nan, 0.8, 0.9, 1.0],
    'String': ['A', 'B', 'C', 'D', 'E', 'F', 'G', np.nan, 'I', 'J'],
    'Boolean': [True, False, np.nan, True, np.nan, False, True, np.nan, False, True],
    'DateTime': pd.to_datetime(['2021-01-01', '2021-01-02', np.nan, '2021-01-04', '2021-01-05', np.nan, '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10'])
}
df = pd.DataFrame(data)
print(df)
# Function to replace NaN with empty values while retaining data type
# def replace_nan_with_empty(df):
#     for col in df.columns:
#         if pd.api.types.is_float_dtype(df[col]) or pd.api.types.is_integer_dtype(df[col]):
#             df[col] = df[col].astype('object').replace({np.nan: ''})
#         elif pd.api.types.is_bool_dtype(df[col]):
#             df[col] = df[col].replace({np.nan: ''})
#         elif pd.api.types.is_datetime64_any_dtype(df[col]):
#             df[col] = df[col].astype('object').replace({pd.NaT: ''})
#         else:
#             df[col] = df[col].replace({np.nan: ''})
#     return df
# df_replaced_all = replace_nan_with_empty(df)
# # Convert DataFrame to a numpy array
# data_array = df_replaced_all.values
# # Save the numpy array to a text file
# np.savetxt('/users/prem/Documents/replaced_dataframe.txt', data_array, fmt='%s', delimiter=',')
# # Verify the DataFrame
# print(df_replaced_all)
# print(df_replaced_all.dtypes)
