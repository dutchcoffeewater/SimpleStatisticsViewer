import streamlit as st

st.set_page_config(page_title = '정보 - 통계 간편 조회 서비스', page_icon = '😎')

st.title('😎 정보')
''
''
''
st.subheader('고객의 소리')
'자료 업데이트가 필요한가요? 다른 통계도 확인하고 싶나요? 버그가 있나요? 추천 통계를 제안하고 싶나요?'
'요청사항은 언제든지 아래에 남겨주시거나, 직접 이메일을 보내주세요!'
'최대한 빠르게 답변드리겠습니다.'
with st.form('Requests',True):
    request = st.text_area('요청사항을 말씀해주세요. (필수)')
    request_email = st.text_input('답변을 이메일로 받으시려면, 이메일을 입력해주세요.')
    import smtplib
    from email.message import EmailMessage
    if st.form_submit_button('제출'):
        if request:
            try:
                smtp_naver = smtplib.SMTP('smtp.naver.com', 587)
                smtp_naver.ehlo()
                smtp_naver.starttls()
                smtp_naver.login(st.secrets['request_sender'], st.secrets['request_sender_pw'])
                send_request = EmailMessage()
                if request_email:
                    send_request['Subject'] = request_email+'의 새로운 요청'
                else:
                    send_request['Subject'] = 'Anonymous의 새로운 요청'
                send_request.set_content(request)
                send_request['From'] = st.secrets['request_sender']
                send_request['To'] = 'solo4emergency@gmail.com'
                smtp_naver.send_message(send_request)

                st.success('접수되었습니다.')
            except:
                st.warning('이런! 무언가 문제가 있었습니다. 다시 시도해 주세요.')

        else:
            st.error('요청사항을 입력해주세요.')

''
'개발자 이메일: solo4emergency@gmail.com'