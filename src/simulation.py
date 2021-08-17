import pandapower as pp
import pandapower.networks as pn
from pandapower.plotting.plotly import pf_res_plotly

if __name__ == "__main__":
    net = pn.case118()
    print(net)
    #pplt.simple_plot(net)
    pp.runpp(net)
    pf_res_plotly(net)
