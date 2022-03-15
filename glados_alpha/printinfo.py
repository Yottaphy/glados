from .nucleus import Nucleus
from math import log

def printinfo(input):
    print('--------------------------------------------------------------------')
    print('Nucleus', '\t', 'Energy (keV)', '\t', 'Half-life', '\t', 'log(Half-life (s))')
    print('--------------------------------------------------------------------')

    if type(input) is Nucleus:
        print(input.name, '\t\t', int(input.alpha), '±', int(input.delta_alpha), '\t', input.showTime(), '\t\t', "{:.2f}".format(log(input.halflife)))
    else:
        for nucleus in input:
                print(nucleus.name, '\t\t', int(nucleus.alpha), '±', int(nucleus.delta_alpha), '\t', nucleus.showTime(), '\t\t', "{:.2f}".format(log(nucleus.halflife)))
     
    print('--------------------------------------------------------------------')
    print('\n')