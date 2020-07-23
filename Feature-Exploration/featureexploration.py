import os
import numpy as np
from matplotlib import pyplot as plt
import h5py

# Read data file
dirname = os.path.dirname(__file__)
data_path = os.path.join(dirname, 'processed-pythia82-lhc13-all-pt1-50k-r1_h022_e0175_t220_nonu_withPars_truth.z')
f = h5py.File(data_path, 'r')
dset = f['t_allpar_new']

class Jet:
    def __init__(self, name, abbr, color):
        self.name = name
        self.abbr = abbr
        self.color = color
    def count(self):
        """Returns a count of the number of instance of a specific jet type."""
        return dset[self.abbr].sum()
    def get_property(self, property):
        """Returns a 1-D numpy array of all properties of a specific jet type."""
        return dset[property][dset[self.abbr] != 0]

q = Jet("quark", "j_q", "tab:blue")
g = Jet("gluon", "j_g", "tab:orange")
w = Jet("W", "j_w", "tab:green")
z = Jet("Z", "j_z", "tab:red")
t = Jet("top", "j_t", "tab:purple")
undef = Jet("undefined", "j_undef", "k")

jets = np.array([q, g, w, z, t, undef])
total = len(dset)

def countjets():
    print("Total: " + str(total))
    for jet in jets:
        print(jet.name + ": " + str(jet.count()))

def makeplot(property):
    plt.xlabel(property)
    plt.ylabel("Prob. Density (a.u.)")
    for jet in jets:
        properties = jet.get_property(property)
        plt.hist(properties, bins = 100, range = (dset[property].min(), dset[property].max()), weights = np.full_like(properties, 1 / total), histtype = "step", color = jet.color, label = jet.name)
    plt.legend()
    plt.savefig(property + ".svg")
    plt.clf()

jet_kinematics = ["j_mass_mmdt", "j_pt", "j_eta"]
jet_substructures = ["j_zlogz", "j_multiplicity"]
ecf_c1 = ["j_c1_b0_mmdt", "j_c1_b1_mmdt", "j_c1_b2_mmdt"]
ecf_c2 = ["j_c2_b1_mmdt", "j_c2_b2_mmdt"]
ecf_d2 = ["j_d2_b1_mmdt", "j_d2_b2_mmdt", "j_d2_a1_b1_mmdt", "j_d2_a1_b2_mmdt"]
ecf_m2 = ["j_m2_b1_mmdt", "j_m2_b2_mmdt"]
ecf_n2 = ["j_n2_b1_mmdt", "j_n2_b2_mmdt"]
high_level_features = [jet_kinematics, jet_substructures, ecf_c1, ecf_c2, ecf_d2, ecf_m2, ecf_n2]