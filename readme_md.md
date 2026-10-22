# 🚇 부산 지하철역별 이용객 수 지도 분석 앱

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수를 시각화하고 분석할 수 있는 웹 대시보드 프로젝트입니다.

---

## 📌 주요 기능

1. **데이터 업로드 및 확인**:
   - `busan_subway.csv` 파일을 웹 브라우저에서 직접 업로드하여 원본 데이터를 확인합니다.
2. **호선 필터링 (Multiselect)**:
   - 1호선부터 4호선까지 원하는 호선만 선택하여 지도에 표시할 수 있습니다.
3. **호선별 고유 색상 마커**:
   - 1호선: 주황 (`orange`)
   - 2호선: 초록 (`green`)
   - 3호선: 갈색 (`brown`)
   - 4호선: 파랑 (`blue`)
4. **이용객 수 비례 원형 마커 (`CircleMarker`)**:
   - 원의 면적이 이용객 수에 직관적으로 비례하도록 반지름을 제곱근($\sqrt{\text{이용객수}}$)으로 계산하여 표현합니다.
   - 마우스를 올리면(`tooltip`): 역명 표시
   - 마커를 클릭하면(`popup`): 상세 이용객 수 표시
5. **TOP 5 랭킹 표**:
   - 선택된 호선 내에서 이용객 수가 가장 많은 상위 5개 역을 순위표로 요약 표시합니다.

---

## 📂 데이터 형식 (`busan_subway.csv`)

CSV 파일은 다음과 같은 열(Column) 구성을 가집니다.

| 호선 | 역명 | 위도 | 경도 | 이용객수 |
| :--- | :--- | :--- | :--- | :--- |
| 1호선 | 서면 | 35.1578 | 129.0594 | 45000 |
| ... | ... | ... | ... | ... |

---

## 🛠️ 시작하기

### 1. 저장소 복제 (Clone)

```bash
git clone https://github.com/당신의_깃허브_아이디/저장소_이름.git
cd 저장소_이름
```

### 2. 필수 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 3. 앱 실행

```bash
streamlit run app.py
```

브라우저가 자동으로 열리며 로컬 주소(`http://localhost:8501`)로 접속됩니다.

---

## 📁 프로젝트 구조

```text
├── app.py                # Streamlit 메인 애플리케이션 코드
├── requirements.txt      # 프로젝트 의존성 목록
├── README.md             # 프로젝트 설명서
└── busan_subway.csv      # 지하철 데이터셋 (샘플)
```

---

## 💡 기술 스택

- **Language**: Python
- **Framework**: Streamlit
- **Data Analysis**: Pandas
- **Map Visualization**: Folium, streamlit-folium