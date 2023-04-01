import os
import openai
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("ORG_ID")

app = Flask(__name__)

def get_prompt(lang, genre, theme, key = None, style = None, mood = None):
    if lang == 'en':
        return get_english_prompt(genre, theme, key, style, mood)
    
    if lang == 'pt-br':
        return get_portuguese_prompt(genre, theme, key, style, mood)

def get_english_prompt(genre, theme, key = None, style = None, mood = None):

    key_prompt = ""
    if key:
        key_prompt = f"The key of the chord progression must be in {key}. "

    style_prompt = ""
    if style:
        style_prompt = f", with the {style} style"
    
    mood_prompt = ""
    if mood:
        mood_prompt = f", with a {mood} mood"

    prompt = f"""Generate the lyrics and chord progression of a {genre} song about {theme}{style_prompt}{mood_prompt}.
                 {key_prompt}You must put the chords OVER the lyrics where the chord change should occur. 
                 Add the key that generated the chord progression in the beginning of the output.
              """
    
    return prompt

def get_portuguese_prompt(genre, theme, key = None, style = None, mood = None):
    
    key_prompt = ""
    if key:
        key_prompt = f"O Tom da música deve ser em {key}. "

    style_prompt = ""
    if style:
        style_prompt = f", com o estilo de {style}"
    
    mood_prompt = ""
    if mood:
        mood_prompt = f", com um humor {mood}"

    prompt = f"""Gerar a letra e a notação de acordes de uma música {genre} sobre {theme}{style_prompt}{mood_prompt}.
                 Você deve colocar os acordes sobre a letra onde ocorrer a mudança de acordes.
                 {key_prompt}A música deve ter uma Intro, formada por uma sequencia de acordes.
                 O Tom da música deve ser explicitado na primeira linha.
                 Além disso, por favor, coloque os metadados da música entre colchetes, por exemplo [Verso 1], [Refrão].
              """
    
    return prompt

def generate_song(prompt):
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
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
    lang = req_data.get('lang')
    key = req_data.get('key')

    prompt = get_prompt(lang, genre, theme, key, style, mood)
    response = generate_song(prompt)

    print(response['content'].split('\n'))

    return {'music': response['content'].split('\n')}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)