import streamlit as st


st.set_page_config(  # 페이지 설정
    page_title="케이팝 데몬 헌터스 팬덤 형성 요인 분석",  # 페이지 Tab의 타이틀
    page_icon="",  # 페이지 Tab의 아이콘
    layout="wide",  # 페이지 레이아웃: centered, wide
    # 사이드바 초기 상태 : auto, collapsed, expanded
    initial_sidebar_state="expanded",
    # 페이지 오른쪽 상부의 메뉴에 추가할 메뉴 항목: Get help, Report a bug, About
    menu_items={
        'Get help': "https://docs.streamlit.io",  # URL만
        'Report a bug': "https://streamlit.io",  # URL만
        'About': "## C321050 이승아"
    }
)
st.set_page_config(
    page_title="Streamlit",
    layout="wide",
    initial_sidebar_state="expanded"
)


# 타이틀 텍스트 출력
st.title("C321050 이승아 데이터 시각화 3차 시험")
st.caption("워드클라우드와 네트워크 시각화는 뉴스의 제목으로만 진행하였다.")
st.caption("위 streamlit의 모든 이미지 및 미디어는 번잡하지 않기 위해 모두 버튼을 누를시에만 나타납니다.")

st.header('워드클라우드 이미지')

st.subheader('워드클라우드 이미지이다.')
st.text('이를 통해 한국 관람, 음식 등 한국의 문화와 영화 내 아이돌 그룹 (헌트릭스), 빌보드 (노래) 등 잘 만들어진 영화 내 노래가 핵심 요인임을 볼 수 있다.')
if st.button('워드클라우드 이미지 기본'):
    st.image("data/wordcloud_square.png", use_container_width=True)

st.subheader('워드클라우드 도형 이미지이다.')
st.caption('데이터 분석 관점에서 필요하진 않으나 시각화의 미적요소를 위해 완성하였다.')
if st.button('워드클라우드 이미지 하트'):
    st.image("data/wordcloud.png", use_container_width=True)

primary_button = st.button('케데헌 헌트릭스 golden 뮤직비디오 보기', type='primary')
if primary_button:
    st.video("https://www.youtube.com/watch?v=yebNIHKAC4A&list=RDyebNIHKAC4A&start_radio=1")  # YouTube 링크

st.header('네트워크 이미지')

st.subheader('기본 네트워크 이미지이다.')
st.text('음식(떡볶이, 김밥, 라면)등이 대체적으로 이어져있고, 라이프스타일, 전통, 호랑이, 관광등이 형성되어있는 것을 보아, 대표적인 한국 라이프스타일과 문화를 볼 수 있는 영화가 팬덤 형성의 핵심 요인이 되었다는 것을 확인할 수 있다.')
if st.button('네트워크 시각화 이미지'):
    st.image("data/naver_news_network.png", use_container_width=True)

st.subheader('네트워크 원형 이미지이다.')
st.text('위에서 언급했던 것과 같이 음식, 전통 등 한국의 라이프 스타일을 볼 수 있는 영화이기 때문에 팬덤이 형성되었다는 것을 확인할 수 있다.')

if st.button('네트워크 시각화 이미지 원형'):
    st.image("data/naver_news_circle_network.png", use_container_width=True)

             
st.caption("seaborn 그래프는 뉴스의 내용으로 진행하였다.")
st.subheader('seaborn 상위 언급 단어이다.')
st.text("애니메이션, 전통과 체험이 가장 상위인 것을 보아 애니메이션 영화를 통해 한국의 전통을 체험할 수 있다는 경험이 팬덤 형성에 영향을 준 것으로 예측된다.")
if st.button('seaborn 상위 언급 단어'):
    st.image("data/top_word_frequency.png", use_container_width=True)

import streamlit.components.v1 as components

st.caption("altair plotly 그래프는 뉴스의 날짜로 진행하였다.")

st.subheader('뉴스에서 언급된 날짜 수이다.')
st.text("2025.6.4일을 기준으로 시작되었고, 가장 두드러지는 변화는 8.20, 10.23, 11.21에 보였다")
# 버튼 ai 도움
if st.button('날짜별 뉴스 수 그래프 plotly'):
    with open('./html/article_trend_plotly.html', 'r', encoding='utf-8') as f:
        html = f.read()
    components.html(html, height=600)

st.subheader('뉴스에서 언급된 날짜 수이다.')
st.text("같은 데이터를 사용했기 때문에 같은 형태의 뉴스량 변화를 볼 수 있다")
# 버튼 ai 도움
if st.button('날짜별 뉴스 수 그래프 altair'):
    with open('./html/article_trend_altair.html', 'r', encoding='utf-8') as f:
        html = f.read()
    components.html(html, height=600)
