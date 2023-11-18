import streamlit as st
import matplotlib.pyplot as plt
from datetime import date, timedelta


def tab1():
    st.markdown(
        """
        <style>
            h1 {
                margin-top: -80px;
            }
            
            
        </style>
   """, unsafe_allow_html=True)

    st.title("Tab 1 title")

    proportions = [1, 2, 1]
    item_1_1, item_1_2, item_1_3 = st.columns(proportions)
    item_2_1, item_2_2, item_2_3 = st.columns(proportions)

    with item_1_1:
        select_id = st.session_state.get("select_box_id", 0)
        select_box = st.selectbox("Wybierz", ["a", "b", "c"], select_id)

    with item_1_2:
        start_date = st.session_state.get(
            "start_date", date.today() - timedelta(days=7))

        start_date_input = st.date_input("Wybierz datę", start_date)
        st.session_state.start_date = start_date_input

    with item_1_3:
        st.write("Hello world")

    with item_2_1:
        slider_value = st.session_state.get("slider_input", 1)
        slider_input = st.slider("Wybierz wartość", 1, 10, slider_value)

    with item_2_2:
        multi_select_options = st.session_state.get("multi_input", [123, 234])

        multi_input = st.multiselect("Opcje multiselect", [123, 234, 345],
                                     multi_select_options)

    with item_2_3:
        clicked = st.button("Przycisk")

    if clicked:
        st.session_state.select_box_id = ["a", "b", "c"].index(select_box)
        st.session_state.start_date = start_date_input
        st.session_state.multi_input = multi_input
        st.session_state.slider_input = slider_input

    # ----

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot([1, 2, 3], [2, 5, -3])

    st.pyplot(fig)
