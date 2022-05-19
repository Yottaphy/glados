from .daughter import alphaDaughter
from math import log

SEARCH_WIDTH = 50 #keV

def lookup(energy, dicNuc):
    output = []
    for _,isotope in dicNuc.items():
        for channel in isotope.channels:
            if channel.energy > energy-SEARCH_WIDTH and channel.energy < energy+SEARCH_WIDTH:
                output.append(isotope)
    return output

def possibleSums(energy, dicNuc):
    output = []
    for _,isotope in dicNuc.items():
        if alphaDaughter(isotope, dicNuc) != False:
            candidates = []
            for channel1 in isotope.channels:
                for channel2 in alphaDaughter(isotope, dicNuc).channels:
                    candidate = channel1.energy + channel2.energy
                    if candidate > energy-2*SEARCH_WIDTH and candidate < energy+2*SEARCH_WIDTH:
                        output.append(isotope)
                        break
    return output

def searcher(energy, time, dicNuc):
    output = []
    for _,isotope in dicNuc.items():
        if len(isotope.channels) < 1:
            continue
        for channel in isotope.channels:
            if channel.energy > energy-SEARCH_WIDTH and channel.energy < energy+SEARCH_WIDTH and log(channel.halflife) > time - 1 and log(channel.halflife) < time + 1: 
                if isotope not in output:
                    output.append(isotope)
    return output