import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde

def calculate_corona(
        PS: float,
        R: float,
        RP: float,
        ES: float,
        D: float  # 기본값 6미터
):
    # CSV 파일 경로 설정
    file_path = "./NASA_filtered_imaging.csv"

    # CSV 파일 읽기
    data = pd.read_csv(file_path)

    # 필요한 열 선택
    features = ['pl_orbsmax', 'st_rad', 'pl_rade', 'sy_dist']
    df = data[features].copy()

    # 결측치 제거
    df = df.dropna()

    # 상수 및 변수 설정
    SNR0 = 100  # 기준 SNR 값

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
    df_imaging = df

    # SNR과 ESmax 계산
    df_imaging.loc[:, 'SNR'] = SNR0 * ((df_imaging['st_rad'] * df_imaging['pl_rade'] * (D / 6)) / (
                (df_imaging['sy_dist'] / 10) * df_imaging['pl_orbsmax'])) ** 2
    df_imaging.loc[:, 'ESmax'] = 15 * (D / 6) / df_imaging['pl_orbsmax']

    # SNR과 ESmax가 0보다 큰 값만 선택
    df_imaging = df_imaging[(df_imaging['SNR'] > 0) & (df_imaging['ESmax'] > 0)]

    # 로그 변환
    df_imaging.loc[:, 'log_SNR'] = np.log10(df_imaging['SNR'])
    df_imaging.loc[:, 'log_ESmax'] = np.log10(df_imaging['ESmax'])

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
