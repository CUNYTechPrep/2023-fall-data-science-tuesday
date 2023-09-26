# Importing required functions
from flask import Flask, render_template
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import io
import base64

# Flask constructor
app = Flask(__name__)

df = pd.read_csv("cats_vs_dogs.csv")

# Function to create and save Matplotlib figures
def create_and_save_figures():
    x = df['state']
    y = df['n_pet_households']
    fig, ax = plt.subplots(figsize =(16, 9))
    ax.barh(x, y)
    plt.xlabel("Number of Pet Households")
    plt.ylabel("State")
    plt.title('States and their Pet Households')
    graph1_filename = 'static/graph1.png'
    plt.savefig(graph1_filename)
    x = df['dog_population']
    y = df['cat_population']
    fig, ax = plt.subplots(figsize =(16, 9))
    plt.scatter(x, y)
    plt.xlabel("Dog Population")
    plt.ylabel("Cat Population")
    plt.title('Dog and Cat Population Comparison')
    graph2_filename = 'static/graph2.png'
    plt.savefig(graph2_filename)

    return graph1_filename, graph2_filename

# Route to display the graphs
@app.route('/')
def display_graphs():
    # Create and save Matplotlib figures
    graph1_filename, graph2_filename = create_and_save_figures()
    
    # Read the saved images as binary data
    with open(graph1_filename, 'rb') as graph1_file:
        graph1_data = base64.b64encode(graph1_file.read()).decode('utf-8')

    with open(graph2_filename, 'rb') as graph2_file:
        graph2_data = base64.b64encode(graph2_file.read()).decode('utf-8')

    return render_template('index.html', graph1_data=graph1_data, graph2_data=graph2_data)

if __name__ == '__main__':
    app.run(debug=True)