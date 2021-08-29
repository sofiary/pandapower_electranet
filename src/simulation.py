import os
import pandapower as pp
import pandapower.networks as pn
from pandapower.plotting.plotly import pf_res_plotly
from preparation import NetworkBuilder

import_rules = dict()
aemo_data = r"data/aemo_data_sources.json"
tnsp_buses = r"data/electranet_buses.json"

if __name__ == "__main__":
    builder = NetworkBuilder(name="ElectraNet", f_hz=50.0, sn_mva=100)
    builder.parse_bus_data(import_rules=tnsp_buses)
    builder.build_nodes()
    breakpoint()
    print(builder)
    #pf_res_plotly(net)
