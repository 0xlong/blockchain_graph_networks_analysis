import pandas as pd
import json

def unique_ads_list(json_data):
     
    #transform to pandas dataframe from json
    json_to_dataframe = pd.DataFrame.from_dict(json_data)
    
    #select FROM and TO columns, containing addresses and create a list of all addresses
    full_address_list = [*json_to_dataframe['from'].tolist(),*json_to_dataframe['to'].tolist()]
    
    #remove duplicates by encapsulating full_address_list as set
    full_unique_address_list = list(set(full_address_list))

    return full_unique_address_list