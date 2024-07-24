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

footer = """<style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;text-align: center;}</style><div class='footer'><p>Developed with 💖 by AffirmativeGuy.</p></div>"""
st.markdown(footer, unsafe_allow_html=True)

st.title("🐱‍🚀 About Me")
st.html('''
        <h1 align="center"><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=995&color=FF0000&center=true&multiline=true&random=false&width=435&lines=Hi+%F0%9F%91%8B%F0%9F%8F%BB%2C+I'm+Arnav+Singh." alt="Typing SVG" /></a></h1>
''')
st.write(
    "Hi there 👋🏻! I'm Arnav Singh a random tech-savvy teenager from India lost in the world of computers. I love spending my leisure time in learning or making(tinkering most of the time) projects in Python."
)

cols = st.columns(len(socials))
for index, (platform, link) in enumerate(socials.items()):
    cols[index].write(f"[{platform}]({link})")
 
x = st.sidebar.selectbox(
    '🐱‍👤 Wish to connect?',
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


st.html('''<h3 align="left">Languages and Tools I'm Tinkering With:</h3>
<p align="left">
  <a href="https://discord.com/invite/WYXqMxnsqa">
    <img src="https://skillicons.dev/icons?i=git,go,py,vscode,arch,github&perline=3&theme=dark" />
  </a>
</p>''')
st.write('''### ❄️ Quote by me:
[![Quote](https://quotes-github-readme.vercel.app/api?theme=catppuccin_mocha&type=horizontal&quote=To%20Be%20The%20Best%20You%20Have%20To%20Work%20Hard,%20But%20To%20Be%20The%20Worst%20You%20Don't.&author=AffirmativeGuy)](https://youtu.be/dQw4w9WgXcQ?si=eoehQUYaFQwPM-Rh)
''')

st.sidebar.write("""### 🍜 My Discord Profile

[![Discord Presence](https://lanyard.cnrad.dev/api/1064034452893863966)](https://discord.com/users/1064034452893863966)""")
st.sidebar.html('''<h3 align="left">My Socials:</h3>
<p align="left">
<a href="https://www.youtube.com/c/https://www.youtube.com/@affirmativeguy" target="blank"><img align="center" src="https://cdn.simpleicons.org/youtube" alt="YouTube" height="50" width="60" /></a> 
<a href="https://discord.com/invite/WYXqMxnsqa"> <img align="center", src="https://skillicons.dev/icons?i=discord", alt="https://discord.com/invite/WYXqMxnsqa"</p>
''')

st.sidebar.html('''
        <h1 align="center"><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=995&color=FF0000&center=true&multiline=true&random=false&width=435&lines=........." alt="Typing SVG" /></a></h1>
''')
st.write('\n')


css = "styles/main.css"
with open(css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
