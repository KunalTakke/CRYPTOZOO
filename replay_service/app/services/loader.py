import csv 
from pathlib import Path
from typing import List,Dict
from datetime import datetime

class CSVLoader:
    def __init__(self,data_dir:str):
        self.data_dir = Path(data_dir)
    
    def load_crypto_data(self,filename:str):
        file_path = self.data_dir/filename
        if not file_path.exists():
            raise FileNotFoundError(f"File not found {file_path}")
        
        records =[]
        with file_path.open(mode='r',newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                record = {
                    "symbol":row["Symbol"],
                    "date": self._parse_date(row["Date"]),
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low": float(row["Low"]),
                    "close": float(row["Close"]),
                    "volume": float(row["Volume"]),
                    "market_cap": float(row["Marketcap"]),
                }
                records.append(record)
                # sort by date 
                records.sort(key=lambda r: r["date"]) 

            return records

    def _parse_date(self,raw_data):
        """
        Docstring for _parse_date
        returns datetime object
        :param self: Description
        :param date: Description
        """
        try:
            return datetime.strptime(raw_data,"%Y-%m-%d %H:%M:%S")
        except:
            raise ValueError(f"Invalid date format: {raw_data}")
        

        



