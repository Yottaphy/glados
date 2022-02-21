from .daughter import alphaDaughter

def lookup(energy, dicNuc):
    output = []
    for _,isotope in dicNuc.items():
        if isotope.alpha > energy-150 and isotope.alpha < energy+150:
            output.append(isotope)
    return output

def possibleSums(energy, dicNuc):
    output = []
    for _,isotope in dicNuc.items():
        if alphaDaughter(isotope, dicNuc) != False:
            candidate = isotope.alpha + alphaDaughter(isotope, dicNuc).alpha 
            if candidate > energy-300 and candidate < energy+300:
                output.append(isotope)
    return output