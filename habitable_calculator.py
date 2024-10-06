import formula
from sklearn.metrics.pairwise import euclidean_distances

def calculate_habitable_percent(
        maxDnsity:float,
        plName: str,
        plDens: str,
        plObeccen: str,
        plOrbsmax: str,
        stSpectype: str,
        stMass: str,
        stTeff: str,
        syDist: str,
        syVmag: str
):
    ########## AI logic ##########
    habitablePercent=-1
    if(plName==''):
        plName='Unkown'

    if(plDens==''):
        return {
        "planet": plName,
        "habitablePercent": habitablePercent
    } 
    else: 
        plDens=float(plDens)

    if(plObeccen==''):
        return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }
    else:
        plObeccen=float(plObeccen)

    if(plOrbsmax==''):
        return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }
    else:
        plOrbsmax=float(plOrbsmax)

    if(stSpectype==''):
        return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }
    
    if(stMass==''):
        return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }
    else:
        stMass=float(stMass)

    if(stTeff==''):
        return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }
    else:
        stTeff=float(stTeff)
    
    if(syDist==''):
        return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }
    else:
        syDist=float(syDist)
    
    if(syVmag==''):
        return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }
    else:
        syVmag=float(syVmag)


    #density and eccentricity를 보고 특이값 제거
    

    #spectral_type_mapping = {'O': 0, 'B': -2.0, 'A': -0.3, 'F': -0.15, 'G': -0.4, 'K': -0.8, 'M': -2.0}
    bolometric_correction = formula.spectral_type_to_float(stSpectype)
    absolute_magnitude = formula.calculate_absolute_magnitude(syVmag, syDist)
    bolometric_magnitude = formula.calculate_bolometric_magnitude(absolute_magnitude,bolometric_correction)
    luminosity=formula.calculate_luminosity(bolometric_magnitude)
    r_inner, r_outer = formula.calculate_habitable_zone_boundaries(luminosity)
    result= formula.calculate_habitable_zone(r_inner, r_outer, plOrbsmax)

    
    if(result==0):
        habitablePercent=0
    else:
        distance = euclidean_distances([[plObeccen,plDens/maxDnsity]], [[0.0167, 5.51/maxDnsity]])
        habitablePercent = 1 / (1 + distance)

    

    ########## AI logic ##########

    return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }