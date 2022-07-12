import streamlit as st
from google.oauth2 import service_account
import google_auth_httplib2
import httplib2
from googleapiclient.http import HttpRequest
from googleapiclient.discovery import build
import pandas as pd

st.set_page_config(page_title = '마이 페이지 - 통계 간편 조회 서비스', page_icon = '🥰')

if 'sign_up_show' not in st.session_state:
    st.session_state['sign_up_show'] = False
if 'sign_in' not in st.session_state:
    st.session_state['sign_in'] = []



SPREADSHEET_ID = st.secrets['spreadsheet_id']
SHEET_NAME = "User"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"

def connect_to_gsheet():
    # Create a connection object.
    global credentials
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets['gcp_service_account'],
        scopes = ["https://www.googleapis.com/auth/spreadsheets"],
    )

    # Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http = httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http = httplib2.Http()
    )
    service = build(
        "sheets",
        "v4",
        requestBuilder = build_request,
        http = authorized_http,
        cache_discovery = False
    )
    gsheet_connector = service.spreadsheets()
    return gsheet_connector

@st.cache(ttl = 10)
def get_data(gsheet_connector) -> pd.DataFrame:
    values = (
        gsheet_connector.values()
        .get(spreadsheetId = SPREADSHEET_ID, range = f'{SHEET_NAME}!A:E',)
        .execute()
    )

    df = pd.DataFrame(values['values'])
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def add_row_to_gsheet(gsheet_connector, row) -> None:
    gsheet_connector.values().append(
        spreadsheetId = SPREADSHEET_ID,
        range = f'{SHEET_NAME}!A:E',
        body = dict(values = row),
        valueInputOption = 'USER_ENTERED',
    ).execute()



st.title('🥰 마이 페이지')
''
''
''
if st.session_state['sign_in']:
    st.subheader(f'환영합니다, {st.session_state["sign_in"][1]}님.')
    
    '통계 즐겨찾기 기능은 현재 **준비 중**입니다.'
    ''
    if st.button('로그아웃'):
        st.session_state['sign_in'] = []
        st.experimental_rerun()

else:
    # 로그인 폼
    st.subheader('로그인')
    with st.form('login', True):
        login_id = st.text_input('아이디')
        login_pw = st.text_input('비밀번호', type = 'password')
        if st.form_submit_button('로그인'):
            if login_id and login_pw:
                # 로그인 시작
                try:
                    'start debugging..'
                    gsheet_connector = connect_to_gsheet()
                    '1st complete.'
                    st.write(get_data(gsheet_connector))
                    rows = list(get_data(gsheet_connector).itertuples())
                except:
                    st.warning('이런! 무언가 문제가 있었습니다. 잠시 후 다시 시도해 주세요.')
                else:
                    for row in rows:
                        if row[1] == login_id:
                            if row[2] == login_pw:
                                st.session_state['sign_in'] = row
                                st.experimental_rerun()
                            else:
                                st.error('일치하는 회원 정보를 찾을 수 없습니다.')
                            break
                    else:
                        st.error('일치하는 회원 정보를 찾을 수 없습니다.')
            else:
                st.error('아이디와 비밀번호를 모두 입력해 주세요.')

    # 회원가입
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
                    try:
                        gsheet_connector = connect_to_gsheet()
                        rows = list(get_data(gsheet_connector).itertuples())
                        for row in rows:
                            if row[1] == sign_up_id:
                                st.warning('동일한 아이디가 이미 등록되어 있습니다. 다른 아이디를 사용해주세요.')
                                break
                        else:
                            add_row_to_gsheet(
                                gsheet_connector,
                                [[sign_up_id, sign_up_pw, sign_up_email]],
                            )
                            st.success("회원가입이 완료되었습니다.")
                            st.balloons()
                            st.session_state['sign_up_show'] = False
                    except:
                        st.warning('이런! 무언가 문제가 있었습니다. 잠시 후 다시 시도해 주세요.')