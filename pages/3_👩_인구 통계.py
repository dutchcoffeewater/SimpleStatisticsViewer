import streamlit as st
import pandas as pd

st.set_page_config(page_title = '인구 통계 - 통계 간편 조회 서비스', page_icon = '👩')

if 'recommendation' not in st.session_state:
    st.session_state['recommendation'] = []

st.title('인구 통계')
st.markdown('국가통계포털([kosis.kr](kosis.kr))의 인구 통계를 선택적으로 제공합니다.')
'국가통계포털에서 실시간으로 데이터를 가져오는 서비스가 **아닙니다**.'
'원하는 통계가 있거나 업데이트가 필요하다면, 왼쪽 사이드바의 😎**정보**에 의견을 남겨주세요.'
''
''
''
data_list = sorted(['총 인구', '서울특별시 인구', '부산광역시 인구', '대구광역시 인구', '인천광역시 인구',
    '광주광역시 인구', '대전광역시 인구', '울산광역시 인구', '세종특별자치시 인구', '경기도 인구',
    '강원도 인구', '충청북도 인구', '충청남도 인구', '전라북도 인구', '전라남도 인구', '경상북도 인구',
    '경상남도 인구', '제주특별자치도 인구'])
selection = st.multiselect('비교할 데이터를 선택하세요.', data_list, default = st.session_state['recommendation'])

if selection:
    ''
    data = []
    for i in selection:
        data.append(pd.read_csv(f'data/{i}.csv', encoding = 'CP949', index_col = 0))
    dataset = pd.concat(data, axis = 1)
    dataset = dataset.sort_index()
    dataset = dataset.sort_index(axis = 1)
    co1, co2 = st.columns(2)
    with co1:
        chart_selection = st.radio('차트 선택:', ('선 차트', '영역 차트', '바 차트'))
    with co2:
        year = st.slider('조회를 원하는 연도 범위를 선택하세요.', 1925, 2020, ())
    dataset = dataset.reset_index()
    dataset = dataset.loc[(year[0] <= dataset['시점']) & (dataset['시점'] <= year[1])]
    dataset = dataset.set_index('시점')
    if chart_selection == '선 차트':
        st.line_chart(dataset)
    elif chart_selection == '영역 차트':
        st.area_chart(dataset)
    elif chart_selection == '바 차트':
        st.warning('2015년부터 매년 통계를 내기 때문에 이를 전후로 x축 스케일이 달라졌습니다. 해석에 주의해주세요.')
        st.bar_chart(dataset)
    st.write(dataset)
    st.download_button(label = '📄 데이터 다운로드', data = dataset.to_csv().encode('CP949'),
        file_name = 'data.csv', mime = 'text/csv',
        help = 'CSV 파일을 다운로드합니다. 그게 뭐냐고요? 걱정하지 마세요! 엑셀로 열립니다.')
