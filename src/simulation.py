import os
import pandapower as pp
import pandapower.networks as pn
from pandapower.plotting.plotly import pf_res_plotly
from preparation import NetworkBuilder

import_rules = dict()
import_rules["aemo"] = r"data/aemo_import_rules.json"
import_rules["electranet"] = r"data/electranet_import_rules.json"
if __name__ == "__main__":
    builder = NetworkBuilder(name="ElectraNet", f_hz=50.0, sn_mva=100)
    builder.parse_data(import_rules=import_rules["electranet"])
    builder.build_nodes()
    breakpoint()
    print(builder)
    #pf_res_plotly(net)
