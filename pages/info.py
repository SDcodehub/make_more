import os
import streamlit as st

st.title("Name Generation Application")

st.write("Welcome to the Name Generation Application! This application allows you to generate names using a character-level language model. There are two models available for experimentation: the Random Model and the Bigram Model.")

st.subheader("Available Models")
st.markdown("Random Model - generates the name randomly")
st.markdown("Bigram Model - character level model, 2 character understanding")

st.subheader("Getting Started")
st.write("To get started with the Name Generation Application, follow these steps:")
st.write("1. Clone the repository to your local machine.")
st.write("2. Install the required dependencies by running:")
st.code("pip install -r requirements.txt")
st.write("3. Run the Streamlit application:")
st.code("streamlit run Name_Generator.py")
st.write("4. The application will open in your default web browser, and you can start generating names using the available models.")

st.subheader("Usage")
st.write("Once you have the application up and running, you can experiment with the two available models: [model](https://huggingface.co/spaces/sagarsdesai/make_more)")
st.markdown("### Random Model")
st.write("1. Select the 'Random Model' option.")
st.write("2. Adjust any desired settings, such as number of output names.")
st.write("3. Click the 'Generate' button to generate a random name.")
st.write("### Bigram Model")
st.write("1. Select the 'Bigram Model' option from the navigation menu.")
st.write("2. Adjust any desired settings, such as number of output names.")
st.write("4. Click the 'Generate' button to generate a name using the Bigram Model.")

st.subheader("Dataset")
st.write("The Bigram Model is trained on a dataset comprising 32,033 input names. These names have been carefully selected to cover a diverse range of styles and origins. The model has learned from this dataset to generate names that exhibit characteristics observed during training.")
st.markdown("[Dataset](https://github.com/SDcodehub/make_over/blob/main/data/names.txt)")

st.subheader("Acknowledgments")
st.write("Special thanks to Andrej Karpathy for providing a great series of language model explanation videos. [ref](https://youtu.be/PaCmpygFfXo?si=MjyUM2oBykhJNuy1)")
st.write("Thanks to the Hugging Face team for providing free hosting.")
st.write("Feel free to explore and experiment with the Name Generation Application. We hope you enjoy generating creative and inspiring names with our models!")
