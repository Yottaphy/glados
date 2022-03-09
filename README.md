# General Lookup of α-Decay for Optimised Search (GLαDOS) #

GLαDOS is an alpha chain constructor, which can help in discerning possible summed energies due to fast decays.

## Setup
### Pre-requisites
The `GLαDOS` package is a python package. It requires Python3 to be installed and `pip` to be up to date. It also requires the `argparse` package to be installed, but it will be automatically installed.

### Install
You can install the package directly through `pip`: 

>`$ pip install GLaDOS-alpha==2.0`

Or, alternatively, you can clone the package's `git` repository:

>`$ git clone https://github.com/Yottaphy/glados.git`

and then enter the directory that was created and install

> `$ cd glados`\
> `$ pip install .`

## Usage
Once installed, GLαDOS can be used directly from the terminal. Some flags have to be included for the calculation to take place:
> `$ glados_alpha [-h] -i INPUTFILE [-z zmin zmax] [-n nmin nmax] -p PARENTENERGY [-l lnTau] [-c CHILDENERGY] [-s SUMPEAK] [-t THIRDDECAY]`

Flags in square brackets are optional. The rest are mandatory. `-l` triggers [energy-lifetime search](#energy-lifetime-search) and `-c` triggers [chain search](#chain-search). `-c` overrules `-l`.

### Energy-lifetime Search
`PARENTENERGY` is treated as the energy of the alpha decay, and `lnTau` is the natural log of the decay lifetime. 

### Chain Search
`SUMPEAK` is a number: 1 for summing in the first decay, 2 for summing in the second decay. Anything else will not assume summing.

If the `-t` option is passed, no matter with what argument, the parent to the heaviest nucleus in the search will also be shown if it was found in the range.

## Output

The output shows a list of possible chains, each in their own table. They can be saved into an output file like:

> `$ glados_alpha [...] > outputname.txt`

where `[...]` are the relevant flags and `outputname.txt` is the output file name, saved at the directory from which you launch GLαDOS.
