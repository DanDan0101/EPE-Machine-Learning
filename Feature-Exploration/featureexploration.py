import numpy as np
import h5py

# Read data file
data_path = '.\\processed-pythia82-lhc13-all-pt1-50k-r1_h022_e0175_t220_nonu_withPars_truth.z'
f = h5py.File(data_path, 'r')
dset = f['t_allpar_new']

def countjets():
    g = q = w = z = t = undef = 0
    for jet in dset:
        # Read truth labels and increment
        g += jet[-6]
        q += jet[-5]
        w += jet[-4]
        z += jet[-3]
        t += jet[-2]
        undef += jet[-1]
    
    # Final results
    print("Total: " + str(g + q + w + z + t + undef))
    print("q: " + str(q))
    print("g: " + str(g))
    print("w: " + str(w))
    print("z: " + str(z))
    print("t: " + str(t))
    print("undef: " + str(undef))

countjets()