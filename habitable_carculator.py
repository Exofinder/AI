import fomula

def calculate_habitable_percent(
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
    if(plName==''):
        plName='Unkown'

    if(plDens==''):
        plDens=1
    else: 
        plDens=float(plDens)

    if(plObeccen==''):
        plObeccen=1
    else:
        plObeccen=float(plObeccen)

    if(stSpectype==''):
        stSpectype='A'
    

    spectral_type_mapping = {'O': 0, 'B': -2.0, 'A': -0.3, 'F': -0.15, 'G': -0.4, 'K': -0.8, 'M': -2.0}
    absolute_magnitude = fomula.calculate_absolute_magnitude(syVmag, syDist)
    bolometric_magnitude = fomula.calculate_bolometric_magnitude(absolute_magnitude,stSpectype)
    luminosity=fomula.calculate_luminosity(bolometric_magnitude)
    r_inner, r_outer = fomula.calculate_habitable_zone_boundaries(luminosity)
    result= fomula.calculate_habitable_zone(r_inner, r_outer, plOrbsmax)

    if(result==0):
        habitablePercent=0
    else:
        habitablePercent=1

    ########## AI logic ##########

    return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }