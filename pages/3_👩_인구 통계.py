import streamlit as st
import pandas as pd

st.set_page_config(page_title = '인구 통계 - 통계 간편 조회 서비스', page_icon = '👩')

if 'recommendation_population' not in st.session_state:
    st.session_state['recommendation_population'] = []

st.title('👩 인구 통계')
st.markdown('국가통계포털([kosis.kr](https://kosis.kr))의 인구 통계를 선택적으로 제공합니다.')
'국가통계포털에서 실시간으로 데이터를 가져오는 서비스가 **아닙니다**.'
'원하는 통계가 있거나 업데이트가 필요하다면, 왼쪽 사이드바의 😎**정보**에 의견을 남겨주세요.'
''
''
''
data_list = sorted(['인구 - 총 인구', '인구 - 서울특별시', '인구 - 부산광역시', '인구 - 대구광역시', '인구 - 인천광역시',
    '인구 - 광주광역시', '인구 - 대전광역시', '인구 - 울산광역시', '인구 - 세종특별자치시', '인구 - 경기도',
    '인구 - 강원도', '인구 - 충청북도', '인구 - 충청남도', '인구 - 전라북도', '인구 - 전라남도', '인구 - 경상북도',
    '인구 - 경상남도', '인구 - 제주특별자치도', '취업자 - 총 취업자', '취업자 - 비임금근로자', '취업자 - 자영업자', '취업자 - 임금근로자',
    '취업자 - 무급가족종사자'])
selection = st.multiselect('조회할 데이터를 선택하세요.', data_list,
    default = st.session_state['recommendation_population'])

if selection:
    ''
    data = []
    for i in selection:
        data.append(pd.read_csv(f'data/인구 통계/{i}.csv', encoding = 'CP949', index_col = 0))
    dataset = pd.concat(data, axis = 1)
    dataset = dataset.sort_index()
    dataset = dataset.sort_index(axis = 1)
    dataset = dataset.reset_index()
    co1, co2 = st.columns(2)
    with co1:
        chart_selection = st.radio('차트 선택:', ('선 차트', '영역 차트', '바 차트'))
    with co2:
        year = st.slider('연도 범위:', min(dataset['시점']), max(dataset['시점']), ())
    dataset = dataset.loc[(year[0] <= dataset['시점']) & (dataset['시점'] <= year[1])]
    dataset = dataset.set_index('시점')
    if chart_selection == '선 차트':
        st.line_chart(dataset)
    elif chart_selection == '영역 차트':
        st.area_chart(dataset)
    elif chart_selection == '바 차트':
        if year[0] <= 2010 and 2016 <= year[1]:
            st.warning('인구 통계의 경우 2015년부터 매년 통계를 내기 때문에 이를 전후로 X축 스케일이 다릅니다. 해석에 주의해주세요.')
        st.bar_chart(dataset)

    st.warning('현재 인구 범주와 취업자 범주를 함께 조회하면 인구 통계가 제대로 표시되지 않습니다.'
        + ' 이는 인구 통계가 5년 단위로 작성된 반면 취업자 범주는 1년 단위로 작성되었기 때문입니다.'
        + ' 해결하려 노력하고 있으니 잠시만 기다려주세요.')

    if '취업자 - 비임금근로자' in selection:
        with st.expander('도움말'):
            st.warning('비임금근로자는 자영업자와 무급가족종사자의 합입니다.')

    st.write(dataset)
    st.download_button(label = '📄 데이터 다운로드', data = dataset.to_csv().encode('CP949'),
        file_name = 'data.csv', mime = 'text/csv',
        help = 'CSV 파일을 다운로드합니다. 그게 뭐냐고요? 걱정하지 마세요! 엑셀에서 열 수 있습니다.')