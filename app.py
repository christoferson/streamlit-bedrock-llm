import streamlit as st
import cmn_auth

st.set_page_config(
    page_title="Chat Application",
    page_icon=":coffee:", #"🧊",
    layout="wide", #centered
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://localhost.com/help',
        'Report a bug': "https://www.localhost.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

###### AUTH START #####

if not cmn_auth.check_password():
   st.stop()

######  AUTH END #####

tab1, tab2, tab3 = st.tabs([":blue[**Get Started**]", "Prompt Guide", "Links"])

with tab1:
    st.header("Get Started")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Chat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("Knowlege Base")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("Agents")
        st.image("https://static.streamlit.io/examples/owl.jpg")
   

with tab2:
    st.header("Prompt Guide")
    #st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    st.subheader("Text to Image - Example 1")
    st.markdown(":blue[**prompt:**] breathtaking night street of Tokyo, neon lights. award-winning, professional, highly detailed")
    st.markdown(":red[**negative:**] anime, cartoon, graphic, text, painting, crayon, graphite, abstract glitch, blurry")

with tab3:
    st.header("Useful Links")
    #st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    st.markdown("- :blue-background[name] https://foo/bar.com")

    st.markdown("> blockquote")
    st.markdown("- [x] Write the press release") 
    st.markdown("- [ ] Write the press release  H~2~O X^2^") 