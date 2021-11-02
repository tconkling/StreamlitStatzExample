import streamlit as st


@st.experimental_memo
def my_memo(count):
    return [3.14] * count


@st.experimental_singleton
def my_singleton():
    return "there can be only one"


st.write(my_memo(1))
st.write(my_memo(11))
st.write(my_singleton())
