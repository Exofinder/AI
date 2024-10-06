import numpy as np 

spectral_type_mapping = {'O': 0, 'B': -2.0, 'A': -0.3, 'F': -0.15, 'G': -0.4, 'K': -0.8, 'M': -2.0}

# 스펙트럼 타입을 float으로 변환하는 함수 수정
def spectral_type_to_float(spectral_type):
    """
    스펙트럼 타입(예: "F5", "G2")을 Bolometric 보정값으로 변환하는 함수.
    F5 -> -0.15 (F가 3), G2 -> -0.4 (G가 4)
    """
    if isinstance(spectral_type, str) and len(spectral_type) > 0:
        # 스펙트럼 타입의 첫 글자만 사용하여 매핑 (숫자는 무시)
        base_value = spectral_type_mapping.get(spectral_type[0].upper(), np.nan)
        return base_value
    return np.nan  # 변환이 불가능한 경우 NaN 반환


# Bolometric 보정값을 계산
#bolometric_correction = spectral_type_to_float(spectralType)


def calculate_absolute_magnitude(apparent_magnitude, distance_pc):
    """
    겉보기 등급과 거리(파섹)를 이용하여 절대 등급을 계산하는 함수
    절대 등급 공식: M = m - 5 * (log10(d) - 1)
    """

    return apparent_magnitude - 5 * (np.log10(distance_pc) - 1)

def calculate_bolometric_magnitude(absolute_magnitude, bolometric_correction):
    """
    절대 등급과 Bolometric 보정값을 이용하여 절대 복사 등급을 계산하는 함수
    """
    return absolute_magnitude + bolometric_correction

def calculate_luminosity(absolute_bolometric_magnitude, sun_bolometric_magnitude=4.74, sun_luminosity=3.828*1026):
    """
    항성의 절대 복사 등급을 이용하여 항성의 광도를 계산하는 함수
    공식: L = L_sun * 10^((M_sun - M_bol) / 2.5)
    """
    return (10 ** ((absolute_bolometric_magnitude-sun_bolometric_magnitude) / (-2.5)))

def calculate_habitable_zone_boundaries(luminosity):
    """
    항성의 광도를 이용하여 생명가능지대의 내부 및 외부 반경을 계산하는 함수
    공식: r_inner = sqrt(L / 1.1), r_outer = sqrt(L / 0.53)
    """
    r_inner = np.sqrt(luminosity / 1.1)
    r_outer = np.sqrt(luminosity / 0.53)
    return r_inner, r_outer

def calculate_habitable_zone(r_inner,r_outer,au):
    if(au>=r_inner and au<=r_outer):
        return 1
    else:
        return 0
    
    
