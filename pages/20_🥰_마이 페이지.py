import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect

st.set_page_config(page_title = '마이 페이지 - 통계 간편 조회 서비스', page_icon = '🥰')

if 'sign_up_show' not in st.session_state:
    st.session_state['sign_up_show'] = False



# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets['gcp_service_account'],
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets'
    ],
)

conn = connect(credentials = credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl = 600)
def run_query(query):
    rows = conn.execute(query, headers = 1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
st.write(rows)
st.write(type(rows))

for row in rows:
    st.write(row)
    st.write(type(row))



st.title('🥰 마이 페이지')
''
''
''
st.subheader('로그인')
with st.form('login', True):
    login_id = st.text_input('아이디')
    login_pw = st.text_input('비밀번호', type = 'password')
    if st.form_submit_button('로그인'):
        if login_id and login_pw:
            for row in rows:
                if row['아이디'] == login_id and row['비밀번호'] == login_pw:
                    f'환영합니다, {login_id}님.'
                    f'회원번호: {row["회원번호"]}'
                    f'이메일: {row["이메일"]}'
                break
            st.warning('아직 구현되지 않은 기능입니다.')
        else:
            st.error('아이디와 비밀번호를 모두 입력해 주세요.')
''
'회원이 되시면 통계 즐겨찾기 등 다양한 기능을 이용하실 수 있습니다.'
if st.button('회원가입'):
    if st.session_state['sign_up_show']:
        st.session_state['sign_up_show'] = False
    else:
        st.session_state['sign_up_show'] = True

if st.session_state['sign_up_show']:
    with st.form('sign_up', True):
        sign_up_id = st.text_input('아이디')
        sign_up_pw = st.text_input('비밀번호', type = 'password')
        sign_up_pw_check = st.text_input('비밀번호 확인', type = 'password')
        sign_up_email = st.text_input('이메일')
        if st.form_submit_button('회원가입'):
            if sign_up_pw != sign_up_pw_check:
                st.error('비밀번호가 틀립니다. 다시 확인해주세요.')
            elif '@' not in sign_up_email:
                st.error('이메일을 다시 확인해 주세요.')
            else:
                st.warning('아직 구현되지 않은 기능입니다.')