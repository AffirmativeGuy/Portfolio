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
st.write("This page shows all of my repos(projects) which I have made, you can either click on he tabs to get some detailed info about the repos or just click 'Show All' to see all of the repos line-by-line.")
cogs = '[![Affirmative-Cogs](https://github-readme-stats.vercel.app/api/pin/?username=AffirmativeGuy&repo=affirmative-cogs&show_owner=true&theme=tokyonight)](https://github.com/AffirmativeGuy/affirmative-cogs)'
portfolio = '[![Portfolio](https://github-readme-stats.vercel.app/api/pin/?username=AffirmativeGuy&repo=Portfolio&show_owner=true&theme=tokyonight)](https://github.com/AffirmativeGuy/Portfolio)'
simp_calc = '[![Simp Calculator](https://github-readme-stats.vercel.app/api/pin/?username=AffirmativeGuy&repo=Simp-Calculator&show_owner=true&theme=tokyonight)](https://github.com/AffirmativeGuy/Simp-Calculator)'

cog, website, calc, show_all = st.tabs(["Cogs", "Portfolio", "Calculator", "Show all"])

with cog:
   st.header("Affirmative-Cogs")
   st.caption("These are some of my cogs made by me for my discord bot based on the Red-Discord-Bot. This cog includes commands such as a custom made info command, credits command, ping, uptime etc")
   st.write(cogs)

with website:
   st.header("Portfolio")
   st.caption("This is my self-made portfolio's source code which is based on streamlit library in the python language. This website includes pages such as blogs, about me and projects. Which is updated frequently based on my liking.")
   st.write(portfolio)

with calc:
   st.header("Simple Calculator")
   st.caption("A simple terminal based calculator which can multiply, divide, add(💀), subtract and finally it can give power of any number it was made by me as a part of practical based learning.")
   st.write(simp_calc)

with show_all:
 with st.container():
  st.header("Projects")
  st.write("### Affirmative-Cogs")
  st.write(cogs)

  st.write("### Portfolio")
  st.write(portfolio)

  st.write("### Simp-Calculator")
  st.write(simp_calc)




# Adapted from the the official streamlit docs


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