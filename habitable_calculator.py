import formula
from sklearn.metrics.pairwise import euclidean_distances

def calculate_habitable_percent(
        #maxDensity: float,
        plName: str,
        plDens: str,
        plOrbeccen: str,
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
            "plName": plName,
            "plOrbsmax": plOrbsmax,
            "stSpectype": stSpectype,
            "stBrightness": '',
            "innerBoundHabitableZone": '',
            "outerBoundHabitableZone": '',
            "habitablePercent": -1
        }
    else: 
        plDens=float(plDens)

    if(plOrbeccen==''):
        return {
            "plName": plName,
            "plOrbsmax": plOrbsmax,
            "stSpectype": stSpectype,
            "stBrightness": '',
            "innerBoundHabitableZone": '',
            "outerBoundHabitableZone": '',
            "habitablePercent": -1
        }
    else:
        plOrbeccen=float(plOrbeccen)

    if(plOrbsmax==''):
        return {
            "plName": plName,
            "plOrbsmax": plOrbsmax,
            "stSpectype": stSpectype,
            "stBrightness": '',
            "innerBoundHabitableZone": '',
            "outerBoundHabitableZone": '',
            "habitablePercent": -1
        }
    else:
        plOrbsmax=float(plOrbsmax)

    if(stSpectype==''):
        return {
            "plName": plName,
            "plOrbsmax": plOrbsmax,
            "stSpectype": stSpectype,
            "stBrightness": '',
            "innerBoundHabitableZone": '',
            "outerBoundHabitableZone": '',
            "habitablePercent": -1
        }
    
    if(stMass==''):
        return {
            "plName": plName,
            "plOrbsmax": plOrbsmax,
            "stSpectype": stSpectype,
            "stBrightness": '',
            "innerBoundHabitableZone": '',
            "outerBoundHabitableZone": '',
            "habitablePercent": -1
        }
    else:
        stMass=float(stMass)

    if(stTeff==''):
        return {
            "plName": plName,
            "plOrbsmax": plOrbsmax,
            "stSpectype": stSpectype,
            "stBrightness": '',
            "innerBoundHabitableZone": '',
            "outerBoundHabitableZone": '',
            "habitablePercent": -1
        }
    else:
        stTeff=float(stTeff)
    
    if(syDist==''):
        return {
            "plName": plName,
            "plOrbsmax": plOrbsmax,
            "stSpectype": stSpectype,
            "stBrightness": '',
            "innerBoundHabitableZone": '',
            "outerBoundHabitableZone": '',
            "habitablePercent": -1
        }
    else:
        syDist=float(syDist)
    
    if(syVmag==''):
        return {
            "plName": plName,
            "plOrbsmax": plOrbsmax,
            "stSpectype": stSpectype,
            "stBrightness": '',
            "innerBoundHabitableZone": '',
            "outerBoundHabitableZone": '',
            "habitablePercent": -1
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
        distance = euclidean_distances([[plOrbeccen, plDens/19.7]], [[0.0167, 5.51/19.7]])
        #Divide pldense to the largest value of planets in habitable areas for normalization
        habitablePercent = 1 / (1 + distance)
        habitablePercent = habitablePercent[0][0]

    ########## AI logic ##########

    return {
        "plName": plName,
        "plOrbsmax": plOrbsmax,
        "stSpectype": stSpectype,
        "stBrightness": luminosity,
        "innerBoundHabitableZone": r_inner,
        "outerBoundHabitableZone": r_outer,
        "habitablePercent": habitablePercent
    }