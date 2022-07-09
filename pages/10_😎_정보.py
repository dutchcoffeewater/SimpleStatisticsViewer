import streamlit as st

st.set_page_config(page_title = '정보 - 통계 간편 조회 서비스', page_icon = '😎')

st.title('정보')
''
''
''
st.subheader('고객의 소리')
with st.form('Requests',True):
    request = st.text_input('요청사항을 말씀해주세요. (필수)')
    request_email = st.text_input('답변을 이메일로 받으시려면, 이메일을 입력해주세요.')
    if st.form_submit_button('제출'):
        if request:
            try:
                import smtplib
                from email.message import EmailMessage

                smtp_naver = smtplib.SMTP('smtp.naver.com', 587)
                smtp_naver.ehlo()
                smtp_naver.starttls()
                smtp_naver.login(request_sender, request_sender_pw)
                send_request = EmailMessage()
                if request_email:
                    send_request['Subject'] = request_email+'의 새로운 요청'
                else:
                    send_request['Subject'] = 'Anonymous의 새로운 요청'
                send_request.set_content(request)
                send_request['From'] = request_sender
                send_request['To'] = 'solo4emergency@gmail.com'
                smtp_naver.send_message(send_request)

                st.success('접수되었습니다.')
            except:
                st.warning('이런! 무언가 문제가 있었습니다. 다시 시도해 주세요.')

        else:
            st.error('요청사항을 입력해주세요.')

''
'개발자 이메일: solo4emergency@gmail.com'