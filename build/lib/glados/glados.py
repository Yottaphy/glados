import argparse

from .nucleus import Nucleus, elements
from .filldictionary import fillDictionary 
from .daughter import alphaDaughter
from .searcher import lookup, possibleSums
import numpy as np

from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})

def get_parser():

    parser = argparse.ArgumentParser(description= "General Lookup of α-Decay for Optimised Search (GLαDOS)")

    parser.add_argument('-i', '--inputfile',
                        type=str,
                        required=True,
                        help='Input file where information is stored. In order: dummy column, N, Z, E, deltaE')
    parser.add_argument('-z', '--zrange',
                        nargs=2,
                        metavar=('zmin','zmax'),
                        type=int,
                        default=(83,103),
                        help='Range of Z to be searched, from min to max')
    parser.add_argument('-n', '--nrange',
                        nargs=2,
                        metavar=('nmin','nmax'),
                        type=int,
                        default=(126,156),
                        help='Range of N to be searched, from min to max')
    parser.add_argument('-p', '--parentenergy',
                        type=int,
                        required=True,
                        help='Energy of the first decay')
    parser.add_argument('-c', '--childenergy',
                        type=int,
                        required=True,
                        help='Energy of the second decay')
    parser.add_argument('-s', '--sumpeak',
                        type=int,
                        required=True,
                        help='Where is the sum peak. 1 = parent decay, 2 = child decay. Everything else = No sum peak')
    

    args = parser.parse_args()
    return args, parser

def main():
    args, parser = get_parser()   
    
    dicNuc = fillDictionary(args.inputfile, *args.nrange, *args.zrange)
    
    sumInParent = False
    sumInChild  = False
    if args.sumpeak == 1:
        sumInParent = True    
    if args.sumpeak == 2:
        sumInChild = True

    candidates = []

    if(sumInParent):
        listofParents       = possibleSums(args.parentenergy, dicNuc)
        listofGrandchildren = lookup(args.childenergy, dicNuc)
        for parent in listofParents:
            if parent.z-4 > args.zrange[0] and parent.n - 4 > args.nrange[0]:
                if alphaDaughter(alphaDaughter(parent, dicNuc), dicNuc) in listofGrandchildren:
                    daughter      = alphaDaughter(parent, dicNuc)
                    granddaughter = alphaDaughter(alphaDaughter(parent, dicNuc), dicNuc)
                    candidates.append((parent,daughter,granddaughter))

    elif(sumInChild):
        listofParents  = lookup(args.parentenergy, dicNuc)
        listofChildren = possibleSums(args.childenergy, dicNuc)
        for parent in listofParents:
            if parent.z-2 > args.zrange[0] and parent.n-2 > args.nrange[0]:
                if alphaDaughter(parent, dicNuc) in listofChildren:
                    daughter      = alphaDaughter(parent, dicNuc)
                    granddaughter = alphaDaughter(alphaDaughter(parent, dicNuc), dicNuc)
                    candidates.append((parent,daughter,granddaughter))               

    else:
        listofParents  = lookup(args.parentenergy, dicNuc)
        listofChildren = lookup(args.childenergy, dicNuc)
        for parent in listofParents:
            if parent.z-2 > args.zrange[0] and parent.n-2 > args.nrange[0]:
                if alphaDaughter(parent, dicNuc) in listofChildren:
                    daughter      = alphaDaughter(parent, dicNuc)
                    candidates.append((parent,daughter))

    for tuple in candidates:
        print('------------------------------')
        print('Nucleus', '\t', 'Energy (keV)')
        print('------------------------------')
        for nucleus in tuple:
            print(nucleus.name, '\t\t', int(nucleus.alpha), '±', int(nucleus.delta_alpha))
        print('------------------------------')
        print('\n')
if __name__ == '__main__':
    main()