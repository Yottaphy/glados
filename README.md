# General Lookup of α-Decay for Optimised Search (GLαDOS) #

GLαDOS is a terminal-based alpha chain constructor, which can help in discerning possible summed energies due to fast decays. It can be used to search the nuclear chart for an energy-lifetime combination or to construct an alpha chain from a series of successive energies in coincidence, including possible sum peaks. 

## Setup
### Pre-requisites
The `GLαDOS` package is a python package. It requires Python3 to be installed and `pip` to be up to date. It also requires the `argparse` and `engineering_notation` packages to be installed, but they will be automatically installed. If they are not, install them using `pip install argparse` and `pip install engineering_notation`, respectively.

### Install
You can install the package directly through `pip`: 

>`$ pip install GLaDOS-alpha==2.1`

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
## Input

The input file must contain 5 columns: n, z, alpha energy (keV), alpha energy error (keV) and lifetime (s). Stable isotopes are assigned -1 s lifetimes, but any negative value would serve the same purpose. 

The file `alpha.dat` provided in the Git repo can serve as an example or be used directly. It contains data taken from [Nudat3](https://www.nndc.bnl.gov/nudat3/), in the National Nuclear Data Center (Brookhaven National Laboratory, USA). The data was retrieved in March 2022. 

## Output

Output data are shown with the same units as they are input with. Lifetimes are shown with usual units (seconds, ms, us, hours, minutes, etc.).

The output shows a list of possible chains, each in their own table. They can be saved into an output file like:

> `$ glados_alpha [...] > outputname.txt`

where `[...]` are the relevant flags and `outputname.txt` is the output file name, saved at the directory from which you launch GLαDOS.
