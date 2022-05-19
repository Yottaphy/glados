import argparse
from xmlrpc.client import Boolean

from .nucleus import Nucleus, elements
from .filldictionary import fillDictionary 
from .daughter import alphaDaughter, alphaParent
from .searcher import lookup, possibleSums, searcher
from .printinfo import printinfo
from math import log
from engineering_notation import EngNumber

from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})

def get_parser():

    parser = argparse.ArgumentParser(description= "General Lookup of α-Decay for Optimised Search (GLαDOS)")

    parser.add_argument('-i', '--inputfile',
                        type=str,
                        required=True,
                        help='Input file where information is stored. In order: dummy column, N, Z, E, deltaE')
    parser.add_argument('-e', '--nuclidename',
                        type=str,
                        help='Nuclide name to display in the form XA where X is the element symbol and A is the mass')
    parser.add_argument('-z', '--zrange',
                        nargs=2,
                        metavar=('zmin','zmax'),
                        type=int,
                        default=(50,118),
                        help='Range of Z to be searched, from min to max')
    parser.add_argument('-n', '--nrange',
                        nargs=2,
                        metavar=('nmin','nmax'),
                        type=int,
                        default=(50,200),
                        help='Range of N to be searched, from min to max')
    parser.add_argument('-p', '--parentenergy',
                        type=int,
                        help='Energy of the first decay')
    parser.add_argument('-l', '--lnTau',
                        type=float,
                        help='Natural log of decay half-life')
    parser.add_argument('-c', '--childenergy',
                        type=int,
                        help='Energy of the second decay')
    parser.add_argument('-s', '--sumpeak',
                        type=int,
                        help='Where is the sum peak. 1 = parent decay, 2 = child decay. Everything else = No sum peak')    
    parser.add_argument('-t', '--thirddecay',
                        type=bool,
                        default=False,
                        required=False,
                        help='Is this a second-third combination? If true, the first nucleus will be given')
    parser.add_argument('-Y', '--halflifemax',
                        type=float,
                        default=10E38,
                        required=False,
                        help='Maximum half-life in seconds')
    parser.add_argument('-I', '--intensitythreshold',
                        type=float,
                        default=0,
                        required=False,
                        help='Minimum intensity (%)')

    args = parser.parse_args()
    return args, parser

def main():
    args, parser = get_parser()   
    
    INTENSITY_THRESHOLD = 0.1 #args.intensitythreshold
    HALFLIFE_MAXIMUM    = args.halflifemax

    dicNuc = fillDictionary(args.inputfile, *args.nrange, *args.zrange, INTENSITY_THRESHOLD, HALFLIFE_MAXIMUM)

    #Nuclide info mode
    if args.nuclidename is not None:
        nucleus = dicNuc[args.nuclidename]
        printinfo(nucleus)

    #Setting flags for sumpeaks
    sumInParent = False
    sumInChild  = False
    if args.sumpeak == 1:
        sumInParent = True    
    if args.sumpeak == 2:
        sumInChild = True

    #Chain Search Mode
    candidates = []
    if args.parentenergy is None:
        exit()
    if args.childenergy is not None:
        if(sumInParent): #sum in the first decay
            listofParents       = possibleSums(args.parentenergy, dicNuc)
            listofGrandchildren = lookup(args.childenergy, dicNuc)
            for parent in listofParents:
                #if parent.z-4 > args.zrange[0] and parent.n - 4 > args.nrange[0]:
                    if alphaDaughter(alphaDaughter(parent, dicNuc), dicNuc) in listofGrandchildren:
                        daughter      = alphaDaughter(parent, dicNuc)
                        granddaughter = alphaDaughter(alphaDaughter(parent, dicNuc), dicNuc)
                        candidates.append((parent,daughter,granddaughter))

        elif(sumInChild): #sum in the second decay
            listofParents  = lookup(args.parentenergy, dicNuc)
            listofChildren = possibleSums(args.childenergy, dicNuc)
            for parent in listofParents:
                #if parent.z-2 > args.zrange[0] and parent.n-2 > args.nrange[0]:
                    if alphaDaughter(parent, dicNuc) in listofChildren:
                        daughter      = alphaDaughter(parent, dicNuc)
                        granddaughter = alphaDaughter(alphaDaughter(parent, dicNuc), dicNuc)
                        if (parent,daughter,granddaughter) not in candidates:
                            candidates.append((parent,daughter,granddaughter))               

        else: #no summing mode
            listofParents  = lookup(args.parentenergy, dicNuc)
            listofChildren = lookup(args.childenergy, dicNuc)
            for parent in listofParents:
                if parent.z-2 > args.zrange[0] and parent.n-2 > args.nrange[0]:
                    if alphaDaughter(parent, dicNuc) in listofChildren:
                        daughter      = alphaDaughter(parent, dicNuc)
                        if (parent,daughter) not in candidates:
                            candidates.append((parent,daughter))

        if(args.thirddecay): #Appends the parent of the first candidate at the beginning of the list if thirddecay is selected.
            newcandidates = []
            for tuple in candidates:
                if(not alphaParent(tuple[0], dicNuc)): 
                    print('No parent found in range.')
                else:
                    grandparent = alphaParent(tuple[0], dicNuc)
                    newtuple = (grandparent, *tuple)
                    newcandidates.append(newtuple)
            candidates = newcandidates
        
        for tuple in candidates:
            printinfo(tuple)

    elif args.lnTau is not None: #Energy-lifetime Search mode
        candidates = searcher(args.parentenergy, args.lnTau, dicNuc)
        printinfo(candidates)
    

if __name__ == '__main__':
    main()