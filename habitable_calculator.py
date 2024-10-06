import formula 
import corona_graph
from sklearn.metrics.pairwise import euclidean_distances

def calculate_habitable_percent(
        plName: str,
        plDens: str,
        plOrbeccen: str,
        plOrbsmax: str,
        plRade: str,
        stSpectype: str,
        stRad: str,
        syDist: str,
        syVmag: str,
        D: float
):
    ########## AI logic ##########
    habitablePercent = -1
    coronaAffect = 0
    h_flag = 1
    c_flag = 1
    s_flag = 1
    if(plName==''):
        plName='Unkown'

    if(plRade=='' or stRad==''):
        c_flag = 0
    else:
        plRade=float(plRade)
        stRad=float(stRad)

    if(plOrbsmax=='' or syDist==''):
        c_flag = 0
        s_flag = 0
    else:
        plOrbsmax=float(plOrbsmax)
        syDist=float(syDist)

    if(s_flag == 0 or plDens=='' or plOrbeccen=='' or stSpectype=='' or syVmag==''):
        h_flag = 0
    else:
        plDens=float(plDens)
        plOrbeccen=float(plOrbeccen)
        syVmag=float(syVmag)





    #density and eccentricity를 보고 특이값 제거
    if (c_flag):
        coronaAffect = corona_graph.calculate_corona(plOrbsmax, stRad, plRade, syDist, D)
    

    luminosity = -1
    r_inner = -1
    r_outer = -1
    #spectral_type_mapping = {'O': 0, 'B': -2.0, 'A': -0.3, 'F': -0.15, 'G': -0.4, 'K': -0.8, 'M': -2.0}
    if (h_flag):
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
        "habitablePercent": habitablePercent,
        "coronaGraphAffect": coronaAffect
    }
