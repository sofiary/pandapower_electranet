import json
from numpy import true_divide
import pandapower as pp
import pandas as pd

class NetworkBuilder:

    def __init__(self, *, name: str, f_hz: float, sn_mva: int):
        self.net = pp.create_empty_network(name=name, f_hz=f_hz, sn_mva=sn_mva)

    def __repr__(self):
        pass

    def parse_data(self, import_rules) -> pd.DataFrame:
        with open(import_rules) as ir:
            json_rules = json.load(ir)
        assert json_rules is not None, "Failed to load json config."
        worksheets = json_rules["worksheet_relevancy"]
        ignored_rows = json_rules["ignored_rows"]
        self.data = pd.read_excel(f"data/{json_rules['workbook_name']}",
                      sheet_name=[key for key,val in worksheets.items() if val],
                      skiprows=lambda x: x+1 in ignored_rows)

    def build_nodes(self):
        assert self.data is not None, "Please parse necessary data first."
        for index in (df := self.data["ConnectionPoints"]).index:
            node_data = {
                "name": df.loc[index, "Connection Point"],
                "index": None,
                "vn_kv": df.loc[index, "Voltage level"],
                "geodata": (df.loc[index, "Latitude"], df.loc[index, "Longitude"]),
                "zone": None,
                "in_service": True,
            }
            pp.create_bus(self.net, **node_data)

