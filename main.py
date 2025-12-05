import streamlit as st

PAGES = {
    "Home": "home",
    "Proxys": "p",
    "Games": "g",
    "chat": "c"
}

def main():
    st.link_button("🚨🚨EMERGENCY!(Click if the teacher is near)🚨🚨", "https://www.aleks.com/login")
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    st.session_state.page = PAGES[selection]

    # Load the selected page
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "p":
        proxy()
    elif st.session_state.page == "g":
        games()
    elif st.session_state.page == "c":
        chat()

def home():
    st.title("Welcome to CR7 Games!")
    st.subheader("this is 2nd version of cr7 games. there are no games right now but there will be. till then use the proxys. not all the proxys may work for you so test them all.")

def proxy():
    st.header("Updated Links")

    st.markdown("""
    - https://roughly-classic-ladybug.global.ssl.fastly.net/
    -https://incog.works
    -https://xyz.zaylovesparker.xyz
    - https://rex-web.global.ssl.fastly.net/
    - https://d1wj13dnncr67a.cloudfront.net/
    - https://wqs7ujl.beanweb.qzz.io.cdn.cloudflare.net/
    - https://securly.com.go4it.com.mx/
    - https://loilo3.webredirect.org/
    - https://en.en.www.www.app.ligjtlproxy.home64.de/
    - https://dev.vpn.104-243-45-193.traefik.me/
    - https://samex-5.ipv64.net/
    - https://yuru.haifu.ipv64.net/
    - https://stateexams.statetestingstudies.com/
    - https://lookingfora-job.com.bostoncareercounselor.com/
    - https://mathshelp.lasersoft.com.au/
    - https://alexsgamehub-proxys-16942330.codehs.me/
    - https://selfstudybrain.com/
    - https://universityequality.com/
    - https://newalgebra.com/
    - https://virtualstudybrain.com/
    - https://xn--31byd1i.net/
    - https://ubgroblox.global.ssl.fastly.net/
    - https://mathstutor.life/
    - https://educationbluesky.com/
    - https://maths.news/
    - https://maths.media/
    - https://websitesball.com/
    - https://ngg.798sc.com/
    - https://hotkitchenbag.com/
    - https://websitesbridge.com/
    - https://mathsspot.com/
    """)

def games():
    st.header("nothing here yet😒")
    st.subheader("expected date for fix 12/10/25")

def chat():
    st.header("Nothing here yet")
    st.subheader("expected date for fix 12/10/25")

if __name__ == '__main__':
    main()
