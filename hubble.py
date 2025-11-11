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
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/NGC_1300_HST.jpg/1200px-NGC_1300_HST.jpg",
        caption="대표적인 막대 나선 은하, NGC 1300",
    )
    
    st.markdown(
        """
        막대 나선 은하는 나선 은하의 특별한 형태로, 관측되는 나선 은하의 약 3분의 2를 차지합니다.
        
        **주요 특징:**
        * **중심 막대 (Bar):** 은하 중심 팽대부를 가로지르는 밝은 '막대' 구조가 있습니다.
        * **나선팔:** 나선팔이 중심에서 바로 시작하지 않고, 이 **막대의 양 끝에서부터** 뻗어 나옵니다.
        
        **참고:** 우리 은하(Milky Way) 역시 막대 나선 은하로 분류됩니다.
        
        **분류:** 나선 은하와 마찬가지로 **SBa**, **SBb**, **SBc** 등으로 세분화됩니다.
        """
    )

# --- 3. 타원 은하 탭 ---
with tab3:
    st.subheader("⚫ 타원 은하 (Elliptical Galaxy)")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/M87_-_Elliptical_Galaxy.jpg/1200px-M87_-_Elliptical_Galaxy.jpg",
        caption="거대 타원 은하, M87 (중심에 초거대 블랙홀이 있습니다)",
    )
    
    st.markdown(
        """
        타원 은하는 특별한 구조 없이 부드러운 타원체(공 또는 럭비공) 모양을 하고 있습니다.
        
        **주요 특징:**
        * **모양:** 둥근 모양(E0)부터 납작한 타원(E7)까지 다양합니다.
        * **별의 구성:** 주로 **늙은 별들**로 이루어져 있으며, 전체적으로 붉은빛을 띕니다.
        * **별의 탄생:** 성간 가스와 먼지가 거의 없기 때문에, **새로운 별이 거의 태어
        나지 않습니다.**
        * **크기:** 우주에서 가장 작은 은하부터 가장 거대한 은하까지 크기 폭이 매우 넓습니다.
        """
    )

# --- 4. 불규칙 은하 탭 ---
with tab4:
    st.subheader(" irregular 불규칙 은하 (Irregular Galaxy)")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Large_Magellanic_Cloud_2MASS.jpg/1200px-Large_Magellanic_Cloud_2MASS.jpg",
        caption="우리 은하의 위성 은하인 대마젤란 은하 (LMC)",
    )
    
    st.markdown(
        """
        불규칙 은하는 이름 그대로 일정한 나선팔이나 타원 형태를 갖지 않는 은하들입니다.
        
        **주요 특징:**
        * **형태 없음:** 정해진 모양이 없으며, 종종 혼란스러운 모습을 보입니다.
        * **별의 탄생:** 가스와 먼지가 풍부하여 **매우 활발하게 별이 탄생**하는 경우가 많습니다.
        * **원인:** 대부분 다른 은하와의 **중력 상호작용**이나 충돌로 인해 형태가 망가진 경우입니다.
        
        **종류:**
        * **Irr I:** 어느 정도 구조가 남아있지만 불규칙한 형태 (예: 대마젤란 은하)
        * **Irr II:** 완전히 혼란스러운 형태
        """
    )

# --- 꼬리말 ---
st.info("이 앱은 Streamlit을 사용하여 만들어졌습니다. 우주에 대한 호기심을 계속 가져주세요!")
