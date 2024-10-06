import formula
from sklearn.metrics.pairwise import euclidean_distances


maxDnsity=51
plName='kepler-1649 c'
plDens=5.2
plOrbeccen= 0.72#0.04
plOrbsmax= 0.812
stSpectype= 'G'
stMass= 0.857
stTeff=5596
syDist= 194
syVmag= 12

habitablePercent=-1

bolometric_correction = formula.spectral_type_to_float(stSpectype)
absolute_magnitude = formula.calculate_absolute_magnitude(syVmag, syDist)
bolometric_magnitude = formula.calculate_bolometric_magnitude(absolute_magnitude,bolometric_correction)
luminosity=formula.calculate_luminosity(bolometric_magnitude)
r_inner, r_outer = formula.calculate_habitable_zone_boundaries(luminosity)
result= formula.calculate_habitable_zone(r_inner, r_outer, plOrbsmax)


if(result==0):
    habitablePercent=0
else:
    distance = euclidean_distances([[plObeccen,plDens/51]], [[0.0167, 5.51/51]])
    habitablePercent = 1 / (1 + distance)
    habitablePercent=habitablePercent[0][0]

    
print(habitablePercent)
    ########## AI logic ##########
