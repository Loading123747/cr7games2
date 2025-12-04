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
    st.header("Proxys:")
    st.subheader("there will me more soon")
    st.markdown("""
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
    - https://selfstudybrain.com/
    - https://universityequality.com/
    - https://websitebridge.com/
    - https://newalgebra.com/
    - https://virtualstudybrain.com/
    - https://acb.basketballrandom.net/demo/
    - https://xn--31byd1i.net/
    - https://nowgg.usercontent.motorcycles/
    - https://next-level.is-very.fun/
    - https://mathwork-for-science-class.tutorz0.usercontent.motorcycles/
    - https://shuttle.lol/apps/roblox-corporation/5349/roblox.html
    - https://v3.now.gg/
    - https://beta1.apktbg.com/demo
    - https://beta2.apktbg.com/demo
    - https://beta3.apktbg.com/demo
    - https://beta4.apktbg.com/demo
    - https://beta5.apktbg.com/demo
    - https://beta6.apktbg.com/demo
    - https://beta7.apktbg.com/demo
    - https://qtec.7s.com.tr/
    - https://use.bsfa.info/
    - https://use.gurdit.com/
    - https://edu.bsfa.info/
    - https://edu.gurdit.com/
    - https://progresslearning.7s.com.tr/
    - https://e-learning.7s.com.tr/
    - https://lunar.myclarevision.com/
    - https://mathpdf.chanka.com/
    - https://gogglechemistry.chanka.com/
    - https://mydogatemyhw.chanka.com/a
    - https://empirehsgames.eroeasy.com/
    - https://meow.ajhurst.org/edu/
    - http://foxes.fuzzylookups.com
    - https://sites.google.com/view/dsgf-ttsd-45-bsd-7888-pot?usp=sharing
    - https://toike.easterndns.com/rx
    - https://subway.mcfrappe.radicalnetworks.org/
    - https://learningabout.uhaneingenieria.com/
    - https://google-images.global.ssl.fastly.net/
    - https://ezmoney.global.ssl.fastly.net/
    - https://honors.classicalmusicfortheworld.org/
    - https://rammerhead.gokartprix.se
    - https://interstellar.global.ssl.fastly.net
    - https://grimace-shake.skibidi-rizz-gyatt-fanum-tax-sigma-ohio.ct.ws/
    - https://rammer.myclarevision.com/
    - https://jmew.hkieca.com/
    - https://howto.books.youngchurch.org/
    - https://well-did-you-go-to-sakura-site-link-freddys-internet.bloggernow.net/
    - https://nextgensoccer.oldsouthmarlinclub.com/
    - https://guide.edu.bdeuronews.com/
    - https://zenithisthebest.jemix.sg/?page=%2Fgames.html
    - https://plex.bryongaskin.net/games/roblox/
    - https://lupinevault.com/
    - https://frutiger.flyingpenguin.aero/
    - https://fresh.stlh.im/
    - https://submit.videoartfestival.ro/
    - https://classroom.quuqle.com/
    - https://griefed.worldpaste.com/
    - https://zxyp.02.garmanage.com/
    - https://i-like-my-cheese-drippy.bruh.isoluxltda.cl/
    - https://hardalgebraproblems.thebrittainlawfirm.com/
    """)
def games():
    st.header("nothing here yet😒")
    st.subheader("expected date for fix 12/10/25")

def chat():
    st.header("Nothing here yet")
    st.subheader("expected date for fix 12/10/25")

if __name__ == '__main__':
    main()
