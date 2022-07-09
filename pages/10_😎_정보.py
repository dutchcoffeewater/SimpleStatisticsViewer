import streamlit as st

st.set_page_config(page_title = '정보 - 통계 간편 조회 서비스', page_icon = '😎')

st.title('정보')
''
''
''
st.subheader('고객의 소리')
with st.form('Requests',True):
    request = st.text_input('요청사항을 말씀해주세요. (필수)')
    st.text_input('답변을 이메일로 받으시려면, 이메일을 입력해주세요.')
    if st.form_submit_button('제출'):
        if request:
            st.error('아직 구현되지 않은 기능입니다.')
        else:
            st.error('요청사항을 입력해주세요.')

''
'개발자 이메일: solo4emergency@gmail.com'