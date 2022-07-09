import streamlit as st

st.set_page_config(page_title = '통계 간편 조회 서비스', page_icon = 'random')

st.title('통계 간편 조회 서비스')
st.markdown('안녕하세요! 좌측 사이드바에서 원하는 통계를 선택하세요. 모든 자료의 출처는 국가통계포털입니다.')
''
''
''
st.subheader('추천 통계를 살펴보세요:')
''
st.subheader('👩 인구 통계')
if st.button('총 인구'):
    st.session_state['recommendation'] = ['총 인구']
    st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요.')
if st.button('서울특별시 인구 vs 경기도 인구'):
    st.session_state['recommendation'] = ['서울특별시 인구', '경기도 인구']
    st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요.')
if st.button('광역시별 인구'):
    st.session_state['recommendation'] = ['광주광역시 인구', '대구광역시 인구', '대전광역시 인구',
        '부산광역시 인구', '울산광역시 인구', '인천광역시 인구']
    st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요.')
if st.button('도별 인구'):
    st.session_state['recommendation'] = ['강원도 인구', '경기도 인구', '경상남도 인구',
        '경상북도 인구', '전라남도 인구', '전라북도 인구', '충청남도 인구', '충청북도 인구']
    st.success('이제 왼쪽 사이드바를 열고 👩 인구 통계를 선택하세요.')