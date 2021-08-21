import json
from numpy import true_divide
import pandapower as pp
import pandas as pd

class NetworkBuilder:

    def __init__(self, *, name: str, f_hz: float, sn_mva: int):
        self.net = pp.create_empty_network(name=name, f_hz=f_hz, sn_mva=sn_mva)
        self.bus_data = None
        self.line_data = None

    def __repr__(self):
        pass
    
    def _assert_json(self, json_obj):
        assert json_obj is not None, "Failed to load json config."

    def parse_bus_data(self, import_rules: str) -> pd.DataFrame:
        with open(import_rules) as ir:
            json_rules = json.load(ir)
        self._assert_json(json_rules)

        worksheets = json_rules["worksheet_relevancy"]
        ignored_rows = json_rules["ignored_rows"]
        self.bus_data = pd.read_excel(f"data/{json_rules['workbook_name']}",
                      sheet_name=[key for key,val in worksheets.items() if val],
                      skiprows=lambda x: x+1 in ignored_rows)

    def parse_line_data(self, general: str, types: str = None):
        with open(general) as g:
            json_general = json.load(g)
        self._assert_json(json_general)

    def build_buses(self):
        assert self.bus_data is not None, "Please parse necessary data first."
        for index in (df := self.bus_data["ConnectionPoints"]).index:
            bus_data = {
                "name": df.loc[index, "Connection Point"],
                "index": None,
                "vn_kv": df.loc[index, "Voltage level"],
                "geodata": (df.loc[index, "Latitude"], df.loc[index, "Longitude"]),
                "zone": None,
                "in_service": True,
            }
            pp.create_bus(self.net, **bus_data)
    
    def build_lines(self):
        
        pass

    def build_line_type(self):
        pass

