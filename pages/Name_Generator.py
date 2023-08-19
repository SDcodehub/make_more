import os
from pathlib import Path
import streamlit as st
import torch 
from network.network import NeuralNetwork
import torch.nn.functional as F

# Page title
st.set_page_config(page_title='Name Generator')
st.title('Name Generator')

# Select Model - drop down
model_list = [
    'Random model',
  'Bigram model'
]
model_name = st.selectbox('Select an example query:', model_list)

# Number of outputs - input field
num_results = st.number_input("Number of Names to be Generated", min_value=1, max_value=50) 

# Process
# get weights
with st.form('myform', clear_on_submit=True):

    submitted = st.form_submit_button('Submit')

    if submitted:
        # get current path
        get_cwd = os.getcwd()
        project_dir = get_cwd
        models_path = os.path.join(project_dir, 'models')

        if model_name == 'Bigram model':
            w = torch.load(os.path.join(models_path, 'bigram-USA.pt'))
        elif model_name == 'Random model':
            w = torch.ones(27,27) * 0.01

        for i in range(num_results):
            ix = 0
            name=""
            y = torch.Generator().manual_seed(2147483647)
            while True:
                nn = NeuralNetwork(50, 2147483647)

                xenc = F.one_hot(torch.tensor([ix]), num_classes=27).float() # input to the network one hot encodding
                logits = xenc @ w
                counts = logits.exp()
                probs = counts / counts.sum(1, keepdims=True)

                ix = torch.multinomial(probs, num_samples=1, replacement=True).item()
                name += nn.itos[ix]
                if nn.itos[ix] ==".":
                    break
            st.write(name)




