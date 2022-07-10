import streamlit as st

st.set_page_config(page_title = '도움말 - 통계 간편 조회 서비스', page_icon = '❓')

st.title('❓ 도움말')
''
''
''
st.subheader('추천 통계로 시작하기')
with st.form('추천 통계로 시작하기'):
    st.image('assets/photos/추천 통계로 시작하기.png',)
    '📊 홈에서 추천 통계 중 하나를 선택해 보세요. 위 사진은 추천 통계 중 **도별 인구**를 선택한 화면입니다.'
    if st.form_submit_button('시도해 보기'):
        st.session_state['recommendation_population'] = ['인구 - 강원도', '인구 - 경기도', '인구 - 경상남도',
            '인구 - 경상북도', '인구 - 전라남도', '인구 - 전라북도', '인구 - 충청남도', '인구 - 충청북도']
        st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요.')
''
''
''
st.subheader('세부 사항 설정하고, 그래프 움직이기')
with st.form('세부 사항 설정하고, 그래프 움직이기'):
    st.image('assets/photos/세부 사항 설정하고, 그래프 움직이기.png',)
    '차트 종류를 선택하고, 연도 범위를 조정해보세요. 차트뿐 아니라 데이터 시트까지 유동적으로 조정됩니다.'
    '그래프 점 위에 마우스를 올리면 세부 사항을 확인할 수 있고, 드래그와 확대/축소도 지원합니다.'
    if st.form_submit_button('시도해 보기'):
        st.session_state['recommendation_population'] = ['인구 - 강원도', '인구 - 경기도', '인구 - 경상남도',
            '인구 - 경상북도', '인구 - 전라남도', '인구 - 전라북도', '인구 - 충청남도', '인구 - 충청북도']
        st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요.')
''
''
''
st.subheader('잘못 해석할 걱정 덜기')
with st.form('잘못 해석할 걱정 덜기'):
    st.image('assets/photos/잘못 해석할 걱정 덜기.png',)
    '그래프를 해석할 때 주의할 사항이 있다면 이를 감지해서 지능적으로 알려줍니다.'
    if st.form_submit_button('시도해 보기'):
        st.session_state['recommendation_population'] = ['인구 - 서울특별시', '인구 - 경기도']
        st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요. **바 차트**를 선택하세요.')
''
''
''
st.subheader('전체 데이터 사용하기')
with st.form('전체 데이터 사용하기'):
    st.image('assets/photos/전체 데이터 사용하기.png',)
    '그래프를 정상적으로 표시하기 위해 데이터 시트가 자동으로 조절됩니다. (선택한 데이터 모두가 가지고 있는 시계열 자료만 불러옵니다.) 예를 들어, 인구 범주는 5년 단위고 취업자 범주는 1년 단위이므로 기본적으로 조회되는 자료는 5년 단위로 조정된 자료입니다.'
    '전체 데이터를 조회하고 싶다면, **도움말** 항목에서 **전체 데이터 사용하기**를 클릭하세요.'
    if st.form_submit_button('시도해 보기'):
        st.session_state['recommendation_population'] = ['인구 - 총 인구', '취업자 - 총 취업자']
        st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요.')
''
''
''
st.subheader('데이터 간편하게 다운로드하기')
with st.form('데이터 간편하게 다운로드하기'):
    st.image('assets/photos/데이터 간편하게 다운로드하기.png',)
    '그래프 아래에 데이터 시트 조회 기능과 함께 데이터 다운로드 기능을 지원합니다. 데이터 시트는 스크롤이 가능합니다. 데이터는 CSV 파일이며, 아주 빠르게 다운로드됩니다!'
    if st.form_submit_button('시도해 보기'):
        st.session_state['recommendation_population'] = ['인구 - 광주광역시', '인구 - 대구광역시',
            '인구 - 대전광역시', '인구 - 부산광역시', '인구 - 울산광역시', '인구 - 인천광역시']
        st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요.')
''
''
''
st.subheader('소비자물가지수로 가격 비교하기')
with st.form('소비자물가지수로 가격 비교하기'):
    st.image('assets/photos/소비자물가지수로 가격 비교하기.png')
    '📈 물가 통계에서 **소비자물가지수**를 선택해 보세요. 간단하게 원하는 구간의 가격을 비교할 수 있습니다.'
    if st.form_submit_button('시도해 보기'):
            st.session_state['recommendation_money'] = ['소비자물가지수']
            st.success('이제 왼쪽 사이드바를 열고 📈 물가 통계를 선택하세요. 그래프 아래의 **소비자물가지수 가격 계산기**를 클릭하세요.')
''
''
''
st.subheader('사이트 테마 변경하기')
with st.form('사이트 테마 변경하기'):
    st.image('assets/photos/사이트 테마 변경하기.png')
    '우측 상단의 메뉴 버튼을 누르고 **Settings**를 선택하세요. 사이트를 더 넓게 보거나, 사이트의 테마를 조정할 수 있습니다.'
    if st.form_submit_button('시도해 보기'):
        st.warning('아직 지원하지 않는 기능입니다. 직접 해 보세요!')