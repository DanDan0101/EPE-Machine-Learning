import os
import numpy as np
import h5py

# Read data file
dirname = os.path.dirname(__file__)
data_path = os.path.join(dirname, 'processed-pythia82-lhc13-all-pt1-50k-r1_h022_e0175_t220_nonu_withPars_truth.z')
f = h5py.File(data_path, 'r')
dset = f['t_allpar_new']

def countjets():
    g = dset["j_g"].sum()
    q = dset["j_q"].sum()
    w = dset["j_w"].sum()
    z = dset["j_z"].sum()
    t = dset["j_t"].sum()
    undef = dset["j_undef"].sum()
    
    # Final results
    print("Total: " + str(g + q + w + z + t + undef))
    print("q: " + str(q))
    print("g: " + str(g))
    print("w: " + str(w))
    print("z: " + str(z))
    print("t: " + str(t))
    print("undef: " + str(undef))

# countjets()