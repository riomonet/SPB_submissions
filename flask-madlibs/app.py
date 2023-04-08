from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretsarecool'
debug = DebugToolbarExtension(app)


@app.route("/form")
def form():
    """we need to just get the input words here"""
    words = story.prompts
    return render_template('form.html',words = words)

@app.route("/output")
def output():
    """Write the text replacing each input with th eniputh from the input"""
    text = story.generate(request.args)
    return render_template('output.html',text=text)
        
