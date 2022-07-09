import streamlit as st
import pandas as pd

st.set_page_config(page_title = '물가 통계 - 통계 간편 조회 서비스', page_icon = '📊')

if 'recommendation_money' not in st.session_state:
    st.session_state['recommendation_money'] = []

st.title('물가 통계')
st.markdown('국가통계포털([kosis.kr](https://kosis.kr))의 인구 통계를 선택적으로 제공합니다.')
'국가통계포털에서 실시간으로 데이터를 가져오는 서비스가 **아닙니다**.'
'원하는 통계가 있거나 업데이트가 필요하다면, 왼쪽 사이드바의 😎**정보**에 의견을 남겨주세요.'
''
''
''
data_list = sorted(['소비자물가지수', '국내총생산(명목)', '국민총소득(명목)', '요소비용국민소득(명목)',
    '국민처분가능소득(명목)', '국민총처분가능소득(명목)', '가계총처분가능소득(명목)',
    '1인당 국내총생산(명목)', '1인당 국민총소득(명목)', '1인당 가계총처분가능소득(명목)',
    '국내총생산(실질성장률)'])
selection = st.multiselect('조회할 데이터를 선택하세요.', data_list,
    default = st.session_state['recommendation_money'])

if selection:
    ''
    data = []
    for i in selection:
        data.append(pd.read_csv(f'data/물가 통계/{i}.csv', encoding = 'CP949', index_col = 0))
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
        st.bar_chart(dataset)

    if '소비자물가지수' in selection:
        if '소비자물가지수' in st.session_state['recommendation_money']:
            st.success('아래의 가격 계산기도 확인해보세요.')
        with st.expander('소비자물가지수 가격 계산기'):
            if min(year) < 1965:
                if max(year) < 1965:
                    st.error('해당 기간에는 소비자물가지수 데이터가 제공되지 않습니다.')
                else:
                    st.warning('소비자물가지수는 1965년부터 산출되기 시작하였으므로, 계산기의 범위도 이에 맞게 조정됩니다.')
            if max(year) >= 1965:
                col1, col2 = st.columns(2)
                with col1:
                    comparison_1 = st.number_input(f'{max(min(year),1965)}년의 가격이 이정도였다면...', 0.0, step = 100.0)
                    st.metric(f'{max(max(year),1965)}년의 가격은',
                        str(round((float(dataset.loc[[max(max(year),1965)], ['소비자물가지수 (2020년 = 100)']].values)*comparison_1)/float(dataset.loc[[max(min(year),1965)], ['소비자물가지수 (2020년 = 100)']].values),2))+'원')
                with col2:
                    comparison_2 = st.number_input(f'{max(max(year),1965)}년의 가격이 이만큼이라면...', 0, step = 1000)
                    st.metric(f'{max(min(year),1965)}년의 가격은',
                        str(round((float(dataset.loc[[max(min(year),1965)], ['소비자물가지수 (2020년 = 100)']].values)*comparison_2)/float(dataset.loc[[max(max(year),1965)], ['소비자물가지수 (2020년 = 100)']].values),2))+'원')

    st.write(dataset)
    st.download_button(label = '📄 데이터 다운로드', data = dataset.to_csv().encode('CP949'),
        file_name = 'data.csv', mime = 'text/csv',
        help = 'CSV 파일을 다운로드합니다. 그게 뭐냐고요? 걱정하지 마세요! 엑셀에서 열 수 있습니다.')