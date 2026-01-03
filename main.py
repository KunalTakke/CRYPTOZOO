import os
import pandas as pd
from replay_service.app.core.metadata import MetadataRegistry
from replay_service.app.services.loader import CSVLoader

def generate_metadata(folder_path):
    """
    Docstring for generate_metadata
    
    :param folder_path: path of the folder
    """
    metadata_dictionary = {} 
    try:
        csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
        for f in csv_files:
            print(f)
        print(f"Total files are {len(csv_files)}")
    except FileNotFoundError as f:
        print(f"Files not Found {f}")
    
    for files in csv_files:
        try:
            df = pd.read_csv(os.path.join(folder_path,files),nrows=1,usecols=['Symbol'])
            symbols_data = df['Symbol'].iloc[0] 
            metadata_dictionary[symbols_data] = files
        except Exception as e:
            print(f"Unexpected error occured with {files}: {e}")
        
    
    
    resultant_list = []
    for sym,fs in metadata_dictionary.items():
        resultant_list.append({'Symbol':sym,'FileNames':folder_path+"/"+fs})

    df_mapping = pd.DataFrame(resultant_list)
    dest_file = os.path.join("./replay_service/data/","metadata.csv")
    df_mapping.to_csv(dest_file,index=False)

    print("Metadata file generated!")

# function call
generate_metadata(folder_path = "crypto_currencies")

registry = MetadataRegistry("./replay_service/data/metadata.csv")
print(registry.get_file_for_symbol("BTC"))
loader = CSVLoader("crypto_currencies")
rows = loader.load_crypto_data("coin_Bitcoin.csv")
print(rows[0])
