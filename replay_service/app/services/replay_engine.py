from typing import Dict,List

class ReplayEngine:
    def __init__(self):
        self._data = {}
        self._pointers = {}


    def register_symbol(self,symbol,records):
        """
        Docstring for register_symbol
        
        :param self: Description
        :param symbol: Description
        :param records: Description
        """
        symbol = symbol.upper()
        if not records:
            raise ValueError(f"No records provided for the symbol {symbol}")
        
        self._data[symbol] = records
        self._pointers[symbol] = 0


    def get_next_event(self,symbol):
        """
        Docstring for get_next_event
        
        :param self: Description
        :param symbol: Description
        """
        symbol = symbol.upper()
        if symbol not in self._data:
            raise KeyError(f"{symbol} is not registered")
        pointer = self._pointers[symbol]
        records = self._data[symbol]

        if pointer>=len(records):
            return None 
        
        event = records[pointer]
        self._pointers[symbol]+=1
        return event

    def is_finished(self,symbol):
        """
        Docstring for is_finished
        
        :param self: Description
        :param symbol: Description
        """
        symbol = symbol.upper()
        return self._pointers.get(symbol,0) >=len(self._data.get(symbol,[]))

