import streamlit as st
st.set_page_config(page_title="Projects - Arnav", 
                   page_icon="💀",
                   menu_items=None
                   )
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

footer = """<style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;text-align: center;}</style><div class='footer'><p>Developed with 💖 by AffirmativeGuy.</p></div>"""
st.markdown(footer, unsafe_allow_html=True)


st.title("💀 Projects")
st.write('''This page shows all of my repos(projects) which I have made. These all mainly consist of Python since I am currently learning Python. There is not much projects in my github since I am a beginner.
         Thanks for viewing my projects page.''')

st.html('''<p align="right">
    <a href="https://github.com/AffirmativeGuy/affirmative-cogs"><img width="500" src="https://stats-cop.vercel.app/api/pin/?username=AffirmativeGuy&repo=affirmative-cogs&theme=tokyonight" alt="Affirmative-Cogs"></a>
    </p>
        ''')

st.html('''<p align="left">
    <a href="https://github.com/AffirmativeGuy/Simp-Calculator"><img width="500" src="https://stats-cop.vercel.app/api/pin/?username=AffirmativeGuy&repo=Simp-Calculator&theme=tokyonight" alt="Simp Calc"></a>
    </p>''')

st.html('''<p align="right">
        <a href="https://github.com/AffirmativeGuy/Portfolio"><img width="500" src="https://stats-cop.vercel.app/api/pin?username=AffirmativeGuy&repo=Portfolio&theme=tokyonight" alt="Portfolio"></a>
        </p>''')

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


css = "styles/main.css"
with open(css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)