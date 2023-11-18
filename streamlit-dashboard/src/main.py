import streamlit as st

from tabs.tab1 import tab1
from tabs.tab2 import tab2
from functions.helpers import func


st.set_page_config(layout="wide")


def main():
    st.sidebar.title("Zakładki")
    st.session_state.current_page = st.session_state.get(
        "current_page", "Tab 1")

    # Tab 1
    if st.sidebar.button("Tab 1"):
        st.session_state.current_page = "Tab 1"

    # Tab 2
    if st.sidebar.button("Tab 2"):
        st.session_state.current_page = "Tab 2"

    if st.session_state.current_page == "Tab 1":
        tab1()
    elif st.session_state.current_page == "Tab 2":
        tab2()


if __name__ == "__main__":
    main()
