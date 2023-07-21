import numpy as np  # Import the NumPy library for numerical computing
import pandas as pd  # Import the Pandas library for data manipulation and analysis
import matplotlib.pyplot as plt  # Import the Matplotlib library for plotting
import torch  # Import the PyTorch library for deep learning
from datasets import load_dataset, concatenate_datasets  # Import the datasets library for loading and processing datasets

# Load the SCIQ dataset
dataset = load_dataset("sciq")

# Concatentate the train, validation, and test sets
dataset = concatenate_datasets([dataset['train'], dataset['validation'], dataset['test']])

# Select the first 500 examples from the dataset
dataset = dataset.select(range(500))

# Remove all columns except for the question and correct answer columns
dataset = dataset.remove_columns(set(dataset.column_names) - {'question', 'correct_answer'})

# Convert the dataset to a Pandas DataFrame
data = pd.DataFrame(dataset)

# Set the column names of the DataFrame
data.columns = ['prompt', 'response']

# Add a prompt to each example that asks for a concise and specific answer
data['prompt'] = data['prompt'].map(lambda x: "Give me a concise and specific answer to the following question: {}".format(x))

# Import the AutoTokenizer and AutoDistributedModelForCausalLM classes from the Transformers library
from transformers import AutoTokenizer, AutoDistributedModelForCausalLM

# Set the model name
model_name = "enoch/llama-65b-hf"

# Create a tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name, tuning_mode='deep_ptune', pre_seq_len=3)

# Move the model to the GPU
model = model.cuda()

# Define a function to get a response from the model
def get_response(question):
    """Get a response from the model for a given question."""

    prompt = "Be consise and give straight answer for this question: {}".format(question)

    tokenized = tokenizer(prompt, return_tensors="pt")["input_ids"].cuda()
    outputs = model.generate(tokenized, max_new_tokens=50)

    return tokenized.decode(outputs[0])