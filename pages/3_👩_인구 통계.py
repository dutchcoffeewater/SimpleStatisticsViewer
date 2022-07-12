import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title = '인구 통계 - 통계 간편 조회 서비스', page_icon = '👩')

if 'recommendation_population' not in st.session_state:
    st.session_state['recommendation_population'] = []
if 'original_chart' not in st.session_state:
    st.session_state['original_chart'] = False
if 'sign_in' not in st.session_state:
    st.session_state['sign_in'] = []



st.title('👩 인구 통계')
st.markdown('국가통계포털([kosis.kr](https://kosis.kr))의 인구 통계를 선택적으로 제공합니다.  \n국가통계포털에서 실시간으로 데이터를 가져오는 서비스가 **아닙니다**.  \n원하는 통계가 있거나 업데이트가 필요하다면, 왼쪽 사이드바의 😎 **정보**에 의견을 남겨주세요.')
''
''
''
os.chdir('data/인구 통계')
raw_list = sorted(os.listdir())
os.chdir('../../')
data_list = []
for i in raw_list:
    data_list.append(i[:-4])
selection = st.multiselect('조회할 데이터를 선택하세요.', data_list,
    default = st.session_state['recommendation_population'])

if selection:
    classification = set()
    for i in selection:
        classification.add(i[:3])

    ''
    if '인구 ' in classification and '취업자' in classification and not st.session_state['original_chart']:
        data2 = []
        for i in selection:
            data2.append(pd.read_csv(f'data/인구 통계/{i}.csv', encoding = 'CP949'))
        dataset2 = data2[0]
        for i in range(1,len(data2)):
            dataset2 = pd.merge(dataset2, data2[i])
        dataset2 = dataset2.set_index('시점')
        dataset2 = dataset2.sort_index()
        dataset2 = dataset2.sort_index(axis = 1)
        dataset2 = dataset2.reset_index()

        co1, co2 = st.columns(2)
        with co1:
            chart_selection = st.radio('차트 선택:', ('선 차트', '영역 차트', '바 차트'))
        with co2:
            year = st.slider('연도 범위:', min(dataset2['시점']), max(dataset2['시점']), ())

        dataset2 = dataset2.loc[(year[0] <= dataset2['시점']) & (dataset2['시점'] <= year[1])]
        dataset2 = dataset2.set_index('시점')
        if chart_selection == '선 차트':
            st.line_chart(dataset2)
        elif chart_selection == '영역 차트':
            st.area_chart(dataset2)
        elif chart_selection == '바 차트':
            if year[0] <= 2010 and 2016 <= year[1]:
                st.warning('인구 범주의 경우 2015년부터 매년 통계를 내기 때문에 이를 전후로 X축 스케일이 다릅니다. 해석에 주의해주세요.')
            st.bar_chart(dataset2)
        
        st.warning('현재 표시되는 그래프와 데이터는 축약된 형태입니다!')
        with st.expander('도움말'):
            '그래프를 정상적으로 표시하기 위해 데이터를 축약하였습니다.'
            '필요하다면 전체 데이터를 다시 불러올 수 있습니다.'
            if st.button('전체 데이터 사용하기'):
                st.session_state['original_chart'] = True
                st.experimental_rerun()
            if '취업자 - 비임금근로자' in selection:
                st.warning('비임금근로자는 자영업자와 무급가족종사자의 합입니다.')
        ''
        ''
        '데이터 시트'
        dataset2
        st.download_button(label = '📄 데이터 다운로드', data = dataset2.to_csv().encode('CP949'),
        file_name = 'data.csv', mime = 'text/csv',
        help = 'CSV 파일을 다운로드합니다. 그게 뭐냐고요? 걱정하지 마세요! 엑셀에서 열 수 있습니다.')
    
    else:
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
            if year[0] <= 2010 and 2016 <= year[1] and '인구 ' in classification:
                st.warning('인구 범주의 경우 2015년부터 매년 통계를 내기 때문에 이를 전후로 X축 스케일이 다릅니다. 해석에 주의해주세요.')
            st.bar_chart(dataset)
        
        if '인구 ' in classification and '취업자' in classification:
            with st.expander('그래프가 제대로 표시되지 않나요?'):
                st.write('인구 범주는 5년 단위로 작성된 반면 취업자 범주는 1년 단위로 작성되었기 때문에, '
                + '현재 인구 범주와 취업자 범주를 함께 조회하면 인구 범주가 제대로 표시되지 않습니다.')
                '축약된 형태로 로드하면 이 문제를 해결할 수 있지만, 일부 데이터가 제외됩니다.'
                if st.button('축약된 형태로 로드하기'):
                    st.session_state['original_chart'] = False
                    st.experimental_rerun()

        if '취업자 - 비임금근로자' in selection:
            with st.expander('도움말'):
                st.warning('비임금근로자는 자영업자와 무급가족종사자의 합입니다.')
        
        ''
        ''
        '데이터 시트'
        dataset
        st.download_button(label = '📄 데이터 다운로드', data = dataset.to_csv().encode('CP949'),
        file_name = 'data.csv', mime = 'text/csv',
        help = 'CSV 파일을 다운로드합니다. 그게 뭐냐고요? 걱정하지 마세요! 엑셀에서 열 수 있습니다.')
