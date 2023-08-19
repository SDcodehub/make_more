import os
import streamlit as st

st.title("Intro")

st.write("")
st.write("")

st.subheader("Available Models")
st.markdown(
    "Random Model -  generates the name randomly"
)
st.markdown(
    "Bigram model -  character level model, 2 character understanding"
)

st.markdown(
            "[repo link](https://github.com/SDcodehub/make_over.git)"
)

st.markdown(
            "[Dataset](https://github.com/SDcodehub/make_over/blob/main/data/names.txt)"
)


st.subheader("Ref")
st.markdown(
    "https://youtu.be/PaCmpygFfXo?si=MjyUM2oBykhJNuy1"
)

st.subheader("Credit to")
st.markdown(
    "Andrej Karpathy"
)
