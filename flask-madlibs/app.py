from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def mad_temp():
    """serves template for mad lib story"""
    return render_template('form.html', prompts=story.prompts)

@app.route('/story')
def gen_story():
    """Generates story with user's input and displays result"""
    text = story.generate(request.args)
    return render_template('story.html', text=text)