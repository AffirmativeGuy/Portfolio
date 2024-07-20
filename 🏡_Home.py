import streamlit as st
st.set_page_config(page_title="About Me - Arnav", 
                   page_icon="🧊",
                   menu_items=None
                   )

socials = {
    "YouTube": "https://www.youtube.com/@AffirmativeGuy",
    "GitHub": "https://github.com/AffirmativeGuy",
    "Discord": "https://discord.gg/4pQ5TtRcft",
    "Email" : "mailto:arnavsin0511@gmail.com"
}

# Thanks to medium(a website) for this part
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """


st.markdown(hide_default_format, unsafe_allow_html=True)

footer = """<style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;text-align: center;}</style><div class='footer'><p>Devloped with 💖 by AffirmativeGuy.</p></div>"""
st.markdown(footer, unsafe_allow_html=True)

st.title("🎈 About Me")
st.write(
    "Hi there 👋🏻! I'm Arnav Singh a random tech-savvy teenager from India lost in the world of computers. I love spending my leisure time in learning or making(tinkering most of the time) projects in Python."
)


 
x = st.sidebar.selectbox(
    'Wish to connect?',
    ('😶 Discord', '🏆 Github', '📧 Email', '🐧 YouTube')
)


if x == "😶 Discord":
    st.sidebar.caption("You can reach me at [my discord server.](https://discord.gg/4pQ5TtRcft)")
elif x == "🏆 Github":
    st.sidebar.caption(f"You can reach me at [my github.](https://github.com/AffirmativeGuy)")
elif x == "📧 Email":
    st.sidebar.caption("You can reach me at [my email address.](mailto:arnavsin0511@gmail.com)")
else:
    st.sidebar.caption("You can reach me at [my youtube channel.](https://www.youtube.com/@AffirmativeGuy)")
# Thanks to coding is fun for this part of code



st.write('\n')
cols = st.columns(len(socials))
for index, (platform, link) in enumerate(socials.items()):
    cols[index].write(f"[{platform}]({link})")

css = "styles/main.css"
with open(css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
