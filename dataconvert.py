import numpy as np
import pandas as pd
from math import isnan
pd.set_option('display.max_rows', None)

def energyEstimation(Q,n,z):
    return Q/(1 + 4/(n+z-4)) #4 is the mass of the alpha particle and n+z-4 is the total mass of the daughter nucleus

# _,_,n,z,_,_,_,_,_,_,halflife,_,_,_,alpha,deltaalpha,intensity,intensityerr,_,_ = np.genfromtxt("newalpha.dat", skip_header=1, unpack=True)

q       = pd.read_csv("qvalues.csv",    sep=',', names=["n","z","energy"]  , dtype= {"z":int,"n":int, "energy":float})
hl      = pd.read_csv("halflives.csv",  sep=',', names=["n","z","halflife"], dtype= {"z":int,"n":int, "halflife":float})
real    = pd.read_csv("oldalpha.dat",   sep=',', names=["z","n","halflife","energy","DeltaAlpha","intens","DeltaIntens"], header=1)


tvalues = []
for i, row in q.iterrows():
    z, n, e = int(row["z"]), int(row["n"]), row["energy"]
          
    zlist = real.loc[real["z"] == z].index.values
    nlist = real.loc[real["n"] == n].index.values

    if len(set(zlist).intersection(nlist)) != 0:
        print(set(zlist).intersection(nlist))
        for index in set(zlist).intersection(nlist):
            outrow = real.iloc[index]
            print(z, n, "{:.6g}".format(outrow["halflife"]), outrow["energy"], outrow["DeltaAlpha"],outrow["intens"],outrow["DeltaIntens"]) 
    else:
        zlist = hl.loc[hl["z"] == z].index.values
        nlist = hl.loc[hl["n"] == n].index.values
        try:
            halflife = hl["halflife"][(set(zlist).intersection(nlist))].values[0]
        except:
            continue

        if isnan(float(e)): continue
        if n+z == 4: continue
        estim = energyEstimation(float(e), n, z)
        if estim >= 0:
            print(z, n, "{:.6g}".format(halflife), format(estim, '.2f'), 0, 101, 0)
        else:
            print(z, n, "{:.6g}".format(halflife), -1, 0, 0, 0)

   