import pandapower as pp
from psseparser import parseraw

# The RAW file is composed of the following columns,
# based on the PSS/E v30 RAW format schema
### Buses
# I, NAME, BASKV, IDE, GL, BL, AREA, ZONE, VM, VA, OWNER
### Loads
# I, ID, STATUS, AREA, ZONE, PL, QL, IP, IQ, YP, YQ, OWNER
### Fixed Shunts
# 
### Generators
# I, ID, PG, QG, QT, QB, VS, IREG, MBASE, ZR, ZX, RT, XT,
# GTAP, STAT, RMPCT, PT, PB, O1, F1, ..., O4, F4

if __name__ == "__main__":
    net = pp.create_empty_network()
    b1 = pp.create_bus(net, vn_kv=20.)
    b2 = pp.create_bus(net, vn_kv=20.)
    pp.create_line(net, from_bus=b1, to_bus=b2, length_km=2.5, std_type="NAYY 4x50 SE")   
    pp.create_ext_grid(net, bus=b1)
    pp.create_load(net, bus=b2, p_mw=20.)

    pp.runpp(net)
    print(net.res_bus.vm_pu)
    print(net.res_line.loading_percent)

    parseraw()