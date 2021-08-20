import pandapower as pp
import pandapower.networks as pn
from pandapower.plotting.plotly import pf_res_plotly
#from preparation import 

if __name__ == "__main__":
    net = pn.case118()
    print(net.__class__)
    #pplt.simple_plot(net)
    pp.runpp(net)
    pf_res_plotly(net)
