import numpy as np
from .nucleus import Nucleus, Channel, elements

dicNuc = {}

def fillDictionary(filename, nmin, nmax, zmin, zmax, INTENSITY_THRESHOLD, HALFLIFE_THRESHOLD):
    protons, neutrons, halflives, energies, energydeltas, intensities,intensityerrs = np.genfromtxt( filename, unpack=True, skip_header=1, skip_footer=0, #delimiter=','
    )
    dicNuc = {}

    for i in range(len(protons)):
        if neutrons[i] > nmin and neutrons[i] < nmax and protons[i] > zmin and protons[i] < zmax:
            
            if not elements[protons[i]] + str(int(protons[i]+neutrons[i])) in dicNuc.keys():
                dicNuc[elements[protons[i]] + str(int(protons[i]+neutrons[i]))] = Nucleus(neutrons[i],protons[i]) 
           
            if intensities[i] > INTENSITY_THRESHOLD and halflives[i] < HALFLIFE_THRESHOLD:
                dicNuc[elements[protons[i]] + str(int(protons[i]+neutrons[i]))].addChannel(halflives[i], energies[i], energydeltas[i], intensities[i], intensityerrs[i])

    return dicNuc

