from .nucleus import Nucleus
from math import log

def printinfo(input):
    print('--------------------------------------------------------------------')
    print('Nucleus', '\t', 'Energy (keV)', '\t', 'Half-life', '\t', 'log(Half-life (s))')
    print('--------------------------------------------------------------------')

    if type(input) is Nucleus:
        input = [input]
    
    for nucleus in input:
        if nucleus.halflife == -1:
            print(nucleus.name, '\t\t', int(nucleus.alpha), '±', int(nucleus.delta_alpha), '\t', 'STABLE/UNKNOWN', '\t\t', " ")
        else:
            print(nucleus.name, '\t\t', int(nucleus.alpha), '±', int(nucleus.delta_alpha), '\t', nucleus.showTime(), '\t\t', "{:.2f}".format(log(nucleus.halflife)))
    
    print('--------------------------------------------------------------------')
    print('\n')