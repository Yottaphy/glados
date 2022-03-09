import numpy as np
from .nucleus import Nucleus, elements

dicNuc = {}
def fillDictionary(filename, nmin, nmax, zmin, zmax):
    neutrons, protons, energies, deltas, halflives = np.genfromtxt( filename, unpack=True, skip_header=1, skip_footer=0, autostrip=True)
    dicNuc = {}
    for i in range(0,6655):
        if neutrons[i] > nmin and neutrons[i] < nmax and protons[i] > zmin and protons[i] < zmax:
            nuc = Nucleus(neutrons[i], protons[i], energies[i], deltas[i], halflives[i])             
            dicNuc[elements[nuc.z] + str(nuc.a)] = nuc
    return dicNuc

