# make_over - Name Generation Application

Welcome to the Name Generation Application! This application allows you to generate names using a character-level language model. There are two models available for experimentation: the Random Model and the Bigram Model.

## Table of Contents
- [Introduction](#introduction)
- [Models](#models)
  - [Random Model](#random-model)
  - [Bigram Model](#bigram-model)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dataset](#dataset)
- [Acknowledgments](#acknowledgments)

## Introduction

The Name Generation Application is a project aimed at generating names using a character-level language model. This type of model focuses on generating names character by character, providing unique and creative name suggestions. The application is built using the Streamlit framework, allowing for an interactive and user-friendly experience.

## Models

### Random Model

The Random Model is a simple name generator that generates names by randomly selecting characters from the available character set. While this model produces purely random names, it can be a fun tool for brainstorming and exploring unconventional name ideas.

### Bigram Model

The Bigram Model is the heart of this application. It is a language model trained on a dataset consisting of 32,033 input names. The model operates at the character level and has learned the statistical relationships between character pairs in the training dataset. As a result, the Bigram Model generates names that exhibit patterns and structures similar to those in the training data.

## Getting Started

To get started with the Name Generation Application, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running:
3. Run the Streamlit application:
4. The application will open in your default web browser, and you can start generating names using the available models.

## Usage

Once you have the application up and running, you can experiment with the two available models: 
[model hosted on hugging face space](https://huggingface.co/spaces/sagarsdesai/make_more)

### Random Model

1. Select the "Random Model" option from the navigation menu.
2. Adjust any desired settings, such as the length of the generated name.
3. Click the "Generate" button to generate a random name.

### Bigram Model

1. Select the "Bigram Model" option from the navigation menu.
2. Enter the desired starting characters for the name in the input field.
3. Adjust any other settings as needed.
4. Click the "Generate" button to generate a name using the Bigram Model.

## Dataset

The Bigram Model is trained on a dataset comprising 32,033 input names. These names have been carefully selected to cover a diverse range of styles and origins. The model has learned from this dataset to generate names that exhibit characteristics observed during training. [dataset](https://github.com/SDcodehub/make_over/blob/main/data/names.txt)

## Acknowledgments

Special thanks to Andrej Karpathy for providing a great series of language model explination videos. [ref](Ref - https://youtu.be/PaCmpygFfXo?si=MjyUM2oBykhJNuy1)

Thanks to hugging face team for providing free hosting

We would like to express our gratitude to the creators of the Streamlit framework, which has enabled us to build this interactive and user-friendly application. Additionally, we acknowledge the importance of the dataset used for training the Bigram Model, as it forms the foundation of the model's ability to generate names.

Feel free to explore and experiment with the Name Generation Application. We hope you enjoy generating creative and inspiring names with our models!

