import pandas as pd
import numpy as np

dest_table = 'transactions'
# string column nullable
nullable_string_table_with_fields = {
    "transactions": ["description", "transaction_type"],
    "accounts": ["account_name", "account_type", "branch_location"],
    "customers": ["first_name", "last_name", "email", "address"],
}
# Extended DataFrame with additional columns
df = pd.DataFrame({
    "description": ["nanci","    nan   ","     nan T  ", "nan"],
    "transaction_type": ["Credit", "Debit", "nan","gr"],
    "date": ["2023-01-01", "2023-01-02", None,None],
    "amount": [100.0, np.nan, 300.0,10],  # Numeric column not in tables_data
    "firmd": ["extra1", "extra2", None, None]
})
print(df)
# Check if the table name matches and replace NaN with None for matching columns
if dest_table in nullable_string_table_with_fields: #check if table matching
    for column in df.columns: # take each column from df and interate
        if column in nullable_string_table_with_fields[dest_table]: #match column from dataframe to nullable column from tables_data
            print(f"column ={column} and dest_table = {dest_table}")
            df[column] = df[column].str.strip().replace('nan', "None")
print(df)

