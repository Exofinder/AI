import formula
from sklearn.metrics.pairwise import euclidean_distances
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import gaussian_kde

def calculate_habitable_percent(
        #maxDensity: float,
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
        distance = euclidean_distances([[plObeccen, plDens/19.7]], [[0.0167, 5.51/19.7]])
        #Divide pldense to the largest value of planets in habitable areas for normalization
        habitablePercent = 1 / (1 + distance)
        habitablePercent = f"{habitablePercent[0][0]:.2f}"

    

    ########## AI logic ##########

    return {
        "planet": plName,
        "habitablePercent": habitablePercent
    }


import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde

def calculate_corona(
    pl_orbsmax: str,
    st_rad: str,
    pl_rade: str,
    sy_dist: str,
    D: str  # 기본값 6미터
):
    # CSV 파일 경로 설정
    file_path = "./NASA_final.csv"

    # CSV 파일 읽기
    data = pd.read_csv(file_path)

    # 필요한 열 선택
    features = ['pl_orbsmax', 'st_rad', 'pl_rade', 'sy_dist']
    df = data[features].copy()

    # 결측치 제거
    df = df.dropna()

    # 상수 및 변수 설정
    SNR0 = 100  # 기준 SNR 값

    # 입력된 행성의 변수 설정
    try:

        ES = float(sy_dist)          # 지구-항성 거리 (파섹 단위)
        PS = float(pl_orbsmax)       # 행성-항성 장반경 (AU 단위)
        R = float(st_rad)            # 항성 반경 (태양 반경 단위)
        RP = float(pl_rade)          # 행성 반경 (지구 반경 단위)
        D = float(D)                 # 망원경 지름 (미터)
    except ValueError:
        return 0  # 입력 값이 올바르지 않으면 0 반환

    # 입력된 행성의 SNR과 ESmax 계산
    try:
        intermediate_value_input = (R * RP * (D / 6)) / ((ES / 10) * PS)
        if intermediate_value_input <= 0:
            return 0  # 물리적으로 의미 없는 값이므로 0 반환
    except ZeroDivisionError:
        return 0  # 0으로 나누는 경우 0 반환
    except Exception:
        return 0  # 기타 예외 발생 시 0 반환

    SNR_input = SNR0 * (intermediate_value_input ** 2)
    ESmax_input = 15 * (D / 6) / PS

    # CSV 데이터로부터 Imaging 행성들의 SNR과 ESmax 계산
    df_imaging = df[df['discoverymethod'] == 'Imaging'].copy()

    # SNR과 ESmax 계산
    df_imaging['SNR'] = SNR0 * ((df_imaging['st_rad'] * df_imaging['pl_rade'] * (D / 6)) / ((df_imaging['sy_dist'] / 10) * df_imaging['pl_orbsmax'])) ** 2
    df_imaging['ESmax'] = 15 * (D / 6) / df_imaging['pl_orbsmax']

    # SNR과 ESmax가 0보다 큰 값만 선택
    df_imaging = df_imaging[(df_imaging['SNR'] > 0) & (df_imaging['ESmax'] > 0)]

    # 로그 변환
    df_imaging['log_SNR'] = np.log10(df_imaging['SNR'])
    df_imaging['log_ESmax'] = np.log10(df_imaging['ESmax'])

    # 로그 변환 후 결측치 제거
    df_imaging = df_imaging.dropna(subset=['log_SNR', 'log_ESmax'])

    if df_imaging.empty:
        return 0  # KDE를 수행할 데이터가 부족한 경우 0 반환

    # KDE를 사용하여 밀도 추정
    values = np.vstack([df_imaging['log_SNR'], df_imaging['log_ESmax']])
    kde = gaussian_kde(values)

    # Imaging 행성들의 밀도 값 계산
    density_values = kde(values)

    # 임계 밀도 수준 설정 (예: 하위 10% 퍼센타일)
    threshold = np.percentile(density_values, 10)  # 필요에 따라 퍼센타일 조정 가능

    # 입력된 행성의 로그 SNR과 로그 ESmax 계산
    try:
        log_SNR_input = np.log10(SNR_input)
        log_ESmax_input = np.log10(ESmax_input)
    except ValueError:
        return 0  # SNR_input 또는 ESmax_input이 0 이하인 경우 0 반환

    # 입력된 행성의 밀도 계산
    input_values = np.array([[log_SNR_input], [log_ESmax_input]])
    density_input = kde(input_values)[0]

    # 입력된 행성이 임계 밀도 이상인지 확인
    if density_input >= threshold:
        return 1  # 밀집 영역 내에 있으므로 1 반환
    else:
        return 0  # 밀집 영역 밖에 있으므로 0 반환

    