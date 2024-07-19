import streamlit as st
st.set_page_config(page_title="About Me - Arnav", 
                   page_icon="🧊",
                   initial_sidebar_state="expanded",
                   menu_items=None
                   )

socials = {
    "YouTube": "https://www.youtube.com/@AffirmativeGuy",
    "GitHub": "https://github.com/AffirmativeGuy",
    "Discord": "https://discord.gg/4pQ5TtRcft",
}

# Thanks to medium(a website) for this part
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title("🎈 About Me")
st.write(
    "Hi there 👋🏻! I'm Arnav Singh a random tech-savy teenager from India lost in the world of computers. I love spending my leisure time in learning or making(tinkering most of the time) projects in Python."
)

# Thanks to coding is fun for this part of code
st.write('\n')
cols = st.columns(len(socials))
for index, (platform, link) in enumerate(socials.items()):
    cols[index].write(f"[{platform}]({link})")

css = "styles/main.css"
with open(css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
