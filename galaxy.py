import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="은하의 종류",
    page_icon="🌌",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- 제목 및 소개 ---
st.title("🌌 은하의 종류 탐험하기")
st.write(
    "우주에는 수천억 개의 은하가 있으며, 천문학자들은 이 은하들을 모양에 따라 분류합니다."
    "가장 널리 쓰이는 분류법 중 하나인 **허블 순서(Hubble Sequence)**에 대해 알아봅니다."
)

# 허블 튜닝 포크 이미지 (시각적 도움)
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Hubble_sequence_photo.png/1024px-Hubble_sequence_photo.png",
    caption="허블의 '튜닝 포크' 다이어그램. 은하 분류의 기준을 보여줍니다.",
)

st.header("🔭 주요 은하의 종류")
st.write("관심 있는 은하의 종류를 탭에서 선택해 보세요.")

# --- 탭 구성 ---
tab1, tab2, tab3, tab4 = st.tabs(
    ["나선 은하 (Spiral)", "막대 나선 은하 (Barred Spiral)", "타원 은하 (Elliptical)", "불규칙 은하 (Irregular)"]
)

# --- 1. 나선 은하 탭 ---
with tab1:
    st.subheader("🌀 나선 은하 (Spiral Galaxy)")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Andromeda_Galaxy_%28with_h-alpha%29.jpg/1200px-Andromeda_Galaxy_%28with_h-alpha%29.jpg",
        caption="대표적인 나선 은하, 안드로메다 은하 (M31)",
    )
    
    st.markdown(
        """
        나선 은하는 가장 잘 알려진 형태의 은하입니다.

        **주요 특징:**
        * **중심 팽대부 (Bulge):** 은하 중심의 둥글고 밝은 부분으로, 주로 늙은 별들로 이루어져 있습니다.
        * **원반 (Disk):** 팽대부를 둘러싼 납작한 원반입니다.
        * **나선팔 (Spiral Arms):** 원반 내에서 뻗어 나오는 나선 형태의 팔입니다. 이 팔에는 가스와 먼지가 풍부하여 **새로운 별이 활발하게 탄생**합니다.
        
        **분류:** 나선팔이 감긴 정도와 중심 팽대부의 크기에 따라 **Sa** (팔이 빽빽함), **Sb**, **Sc** (팔이 느슨함) 등으로 세분화됩니다.
        """
    )

# --- 2. 막대 나선 은하 탭 ---
with tab2:
    st.subheader("S̅ 막대 나선 은하 (Barred Spiral Galaxy)")
    st.image(
