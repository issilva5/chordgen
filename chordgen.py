import os
import openai
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("ORG_ID")

app = Flask(__name__)

def get_prompt(genre, theme, style = None, mood = None):

    style_prompt = ""
    if style:
        style_prompt = f", with the {style} style"
    
    mood_prompt = ""
    if mood:
        mood_prompt = f", with a {mood} mood"

    prompt = f"""Generate the lyrics and chord notation of a {genre} song about {theme}{style_prompt}{mood_prompt}. 
                 You must put the chords over the lyrics where the chord change should occur.
                 The song must have an Intro.
                 The key of the song must be explicited in the first line.
                 Also, please put the metadata of the song between [], for example [Verse 1], [Chorus].
              """
    
    return prompt

def generate_song(prompt):
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message


@app.route("/generate", methods = ['POST'])
def generate():

    req_data = request.get_json()
    genre = req_data.get('genre')
    theme = req_data.get('theme')
    style = req_data.get('style')
    mood = req_data.get('mood')

    prompt = get_prompt(genre, theme, style, mood)
    response = generate_song(prompt)

    print(response['content'].split('\n'))

    return {'music': response['content'].split('\n')}


app.run(host='0.0.0.0', port=5000)