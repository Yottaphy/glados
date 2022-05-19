from colorama import Fore
from .nucleus import Nucleus, Channel
from math import log
from colorama import Fore, Style


def printinfo(input):
    print('---------------------------------------------------------------------------------------------------')
    print('Nucleus', '\t', 'Intensity (%)', '\t', 'Energy (keV)', '\t', 'Half-life', '\t', 'log(Half-life (s))')
    print('---------------------------------------------------------------------------------------------------')

    if type(input) is Nucleus:
        input = [input]
    
    for nucleus in input:
        if len(nucleus.channels) < 1:
            print(nucleus.name, '\n\t\t NO ALPHA INFORMATION ABOUT THIS NUCLEUS')
        else: 
            print(nucleus.name)
            for channel in nucleus.channels: 
                if channel.intensity >100:
                    print('\t\t', "ESTIMATED", '\t', int(channel.energy), '±', int(channel.deltaenergy), '\t', channel.showTime(), '\t\t', "{:.2f}".format(lo(channel.halflife)))
                else:
                   print('\t\t', "{:.1f}".format(channel.intensity), '±', "{:.1f}".format(channel.deltaintensity), '\t', int(channel.energy), '±', int(channel.deltaenergy), '\t', channel.showTime(), '\t\t', "{:.2f}".format(log(channel.halflife))) 

    print('---------------------------------------------------------------------------------------------------')
    print('\n')