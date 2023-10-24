# Setting up dev env for HuggingFace


#### First deactive your anaconda env
```
conda deactivate
```

##### Next make sure you have pip installed
try:
```
pip3 list
or 
pip list
```
if you dont have pip yet...
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py
```

### Create virtual env
```
python3 -m venv env

source env/bin/activate

pip3 install --upgrade pip

```


## Installing huggingface dependencies ~10min and 3gb

##### You can do this all at once via installing them via the requirements.txt
```
pip3 install -r requirements.txt
```


##### or installing them manually
```
pip3 install 'transformers[torch]'
pip3 install 'transformers[tf-cpu]'
pip3 install 'transformers[flax]'
pip3 install jupyter
pip3 install scikit-learn
pip3 install plotly-express
pip3 install seaborn
```

### https://huggingface.co/learn/nlp-course/chapter0/1?fw=pt
Above is a course on HuggingFace for NLP specifically


### https://huggingface.co/learn/nlp-course/chapter1/3?fw=pt
Here is a course on using pipelines. 
There are three main steps involved when you pass some text to a pipeline:

0. The text is preprocessed into a format the model can understand.
0. The preprocessed inputs are passed to the model.
0. The predictions of the model are post-processed, so you can make sense of them.


Some of the currently available pipelines are:
```
feature-extraction (get the vector representation of a text)
fill-mask
ner (named entity recognition)
question-answering
sentiment-analysis
summarization
text-generation
translation
zero-shot-classification
```
Let’s have a look at a few of these!