import streamlit as st
import numpy as np

st.set_page_config(
    page_title="LOS calculater",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={"About": "https://www.linkedin.com/in/manwel-wasfy-537546323/"},
)
k = 4 / 3

# @st.cache_data
# def calculate_distance(h1,h2=0):
#     if(h2!=0):
#         d = 3.57 * (np.sqrt(h1*k) + np.sqrt(h2*k))
#     else:
#         d = 3.57 * (np.sqrt(h1*k))
#     return d

# @st.cache_data
# def radio_horizon(h):
#     return 3.57 * (np.sqrt(h1*k))


st.title("Line of Sight Calculator", text_alignment="center")
st.markdown("\n")
st.write("Enter value, select unit and click on calculate. Result will be displayed.")

if "calculated" not in st.session_state:
    st.session_state.calculated = False


def calculate_los():
    st.session_state.calculated = True


def clear_los():
    st.session_state.calculated = False
    st.session_state.h1_key = 100
    st.session_state.h2_key = 0


def hide_results():
    st.session_state.calculated = False


st.subheader("Inputs: ")
col1, col2 = st.columns(2, border=True)

with col1:
    h1 = st.number_input(
        "Antenna 1 :material/settings_input_antenna: Height : ",
        min_value=0,
        value=100,
        step=1,
        format="%i",
        key="h1_key",
        on_change=hide_results,
    )
with col2:
    h2 = st.number_input(
        "Antenna 2 :material/settings_input_antenna: Height: ",
        min_value=0,
        value=0,
        step=1,
        format="%i",
        key="h2_key",
        on_change=hide_results,
    )


unit = st.radio(":red[**Unit:**]", ("Meters", "Feet"), horizontal=True, index=0)

btn_col1, btn_col2 = st.columns([1, 3])
with btn_col1:
    st.button(
        label="Calculate",
        key="calculate",
        on_click=calculate_los,
        icon=":material/calculate:",
        shortcut="ctrl+k",
    )
with btn_col2:
    st.button(
        label="Clear",
        key="clear",
        on_click=clear_los,
        icon=":material/delete_forever:",
        shortcut="ctrl+d",
    )

st.markdown("---")
st.subheader("Results: ")

if st.session_state.calculated:
    h1 = h1 if unit == "Meters" else h1 * 0.3048
    h2 = h2 if unit == "Meters" else h2 * 0.3048

    rh1 = 3.57 * (np.sqrt(k * h1))
    rh2 = 3.57 * (np.sqrt(k * h2))
    total_los = rh1 + rh2

    col1, col2 = st.columns(2, border=True)
    with col1:
        st.text_input(
            "Radio Horizon 1: ", value=f"{rh1:.2f} Km", disabled=True, key="lol1"
        )
    with col2:
        st.text_input(
            "Radio Horizon 2: ", value=f"{rh2:.2f} Km", disabled=True, key="lol2"
        )
    st.text_input(
        "Total Los of Sight: ", value=f"{total_los:.2f} Km", disabled=True, key="lol3"
    )

else:
    st.text_input("Radio Horizon (1st Station):", value="", disabled=True)
    st.text_input("Radio Horizon (2nd Station):", value="", disabled=True)
    st.text_input("Total Line Of Sight:", value="", disabled=True)
