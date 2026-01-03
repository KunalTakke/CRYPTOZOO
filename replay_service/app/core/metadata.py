import csv
from pathlib import Path
from typing import Dict

class MetadataRegistry:
    def __init__(self,metadata_path:str):
        self.metadata_path = Path(metadata_path)
        self.symbol_to_file = {}
        self._load_metadata()

    def _load_metadata(self):
        
        if not self.metadata_path.exists():
            raise FileExistsError(f"Metadata file not found :{self.metadata_path}")
        
        with self.metadata_path.open(mode='r',newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                symbol = row["Symbol"].strip().upper()
                filename = row["FileNames"].strip()
                self.symbol_to_file[symbol] = filename

    def get_file_for_symbol(self,symbol:str):
        symbol = symbol 
        if symbol not in self.symbol_to_file:
            raise KeyError(f"Symbol '{symbol}' not found in metadata registry")
        return self.symbol_to_file[symbol]

    

