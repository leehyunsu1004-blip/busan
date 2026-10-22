import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import math

# 웹 앱 제목
st.title("🚇 부산 지하철역별 이용객 수 지도 분석")

# 호선별 색상 딕셔너리 설정
line_colors = {
    '1호선': 'orange',  # 주황
    '2호선': 'green',  # 초록
    '3호선': 'brown',  # 갈색
    '4호선': 'blue'  # 파랑
}

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader("busan_subway.csv 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded_file)

    # 데이터 호선 열 문자열 정리 (숫자나 공백이 섞여 있을 경우를 대비)
    df['호선'] = df['호선'].astype(str)

    # 2. 호선 필터 (multiselect)
    all_lines = sorted(df['호선'].unique())
    selected_lines = st.multiselect(
        "확인할 호선을 선택하세요 (여러 개 선택 가능)",
        options=all_lines,
        default=all_lines
    )

    # 선택된 호선만 필터링
    filtered_df = df[df['호선'].isin(selected_lines)]

    # 3. 이용객 상위 5개 역 표 표시
    st.subheader("🏆 이용객 수 상위 5개 역")
    top5_df = filtered_df.sort_values(by='이용객수', ascending=False).head(5)
    st.dataframe(top5_df[['호선', '역명', '이용객수']])

    # 4. 지도 생성 (부산 중심 좌표)
    st.subheader("🗺️ 역별 이용객 수 지도")
    m = folium.Map(location=[35.1795543, 129.0756416], zoom_start=11)

    # 5. 필터링된 역들을 지도에 CircleMarker로 표시
    for _, row in filtered_df.iterrows():
        lat = row['위도']
        lon = row['경도']
        station_name = row['역명']
        passengers = row['이용객수']
        line = row['호선']

        # 호선별 색상 가져오기 (지정되지 않은 호선은 기본 회색 처리)
        marker_color = line_colors.get(line, 'gray')

        # 면적이 이용객 수에 비례하도록 반지름을 제곱근으로 계산
        radius = math.sqrt(passengers) * 0.05

        # 마커 추가
        folium.CircleMarker(
            location=[lat, lon],
            radius=radius,
            tooltip=f"[{line}] {station_name}",  # 마우스 올렸을 때: [호선] 역명
            popup=f"이용객수: {passengers:,}명",  # 클릭했을 때: 이용객수
            color=marker_color,  # 테두리 색상
            fill=True,
            fill_color=marker_color,  # 채우기 색상
            fill_opacity=0.6  # 투명도
        ).add_to(m)

    # 6. Streamlit에 지도 출력
    st_folium(m, width=700, height=500)

else:
    st.info("CSV 파일을 업로드하면 분석 결과가 나타납니다.")