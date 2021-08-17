import pandapower as pp
import pandapower.networks as pn
import pandapower.plotting as pplt

if __name__ == "__main__":
    net = pn.case118()
    print(net)
    pplt.simple_plot(net)