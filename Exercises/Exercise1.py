import streamlit as st
import random

st.title("Collatz conjecture")

if "value" not in st.session_state:
    st.session_state.value = None
    st.session_state.started = False
    st.session_state.cliks = 0
    button_label = "Start"
else:
    if st.session_state.value == 1:
        button_label = "Success!"
    else:
        if st.session_state.value % 2 == 0:
            button_label = "Half it"
        else:
            button_label = "Triple and add one"


if st.button(button_label, disabled=st.session_state.value == 1):
    if not st.session_state.started:
        st.session_state.value = random.randint(1, 100)
        st.session_state.started = True
    else:
        if st.session_state.value % 2 == 0:
            st.session_state.value = st.session_state.value // 2
        else:
            st.session_state.value = st.session_state.value * 3 + 1

st.dialog("You have cliked the button (st.session_state.cliks) times.")
def dialog():
    st.write("Are you sure about this?")
    if st.button("Yes, I'm sure"):
        st.rerun()

if st.session_state.value > 1 and (st.session_state.cliks > 0 and st.session_state.cliks % 5 == 0):
    dialog()



