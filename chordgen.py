import os
import openai
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("ORG_ID")

app = Flask(__name__)

def generate_song(genre, theme, style):
    prompt = f"Generate the lyrics and chord notation of a {genre} song about {theme} with the {style} style. You must put the chords over the lyrics where the chord change should occur."
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
    genre = req_data['genre']
    theme = req_data['theme']
    style = req_data['style']

    response = generate_song(genre, theme, style)

    print(response['content'].split('\n'))

    return {'music': response['content'].split('\n')}


app.run(host='0.0.0.0', port=5000)