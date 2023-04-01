import os
import openai
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("ORG_ID")

app = Flask(__name__)


def get_prompt(lang, genre, theme, key=None, style=None, mood=None):
    if lang == 'en':
        return get_english_prompt(genre, theme, key, style, mood)

    if lang == 'pt-br' or lang == 'pt':
        return get_portuguese_prompt(genre, theme, key, style, mood)


def get_english_prompt(genre, theme, key=None, style=None, mood=None):

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
                 Put the metadata of the song between [], such as [Verse 1], [Chorus].

                 The format must follow the example below:

                    Key: Cm

                    [Intro]
                    G,  D,  Em,  C

                    [Verse 1]
                    Cm,                            G#, 
                    >I see you there, lying so peaceful 
                    Bb,                             G#, 
                    >As if you were just taking a nap
                    Cm,                               G#,
                    >But you left me here, full of anger 
                    Bb,                       G#,
                    >And there's no way that I'm gonna let that pass

                    [Pre-Chorus]
                    Ab,                      Bb,
                    >Every time I close my eyes 
                    G#,                      Ab,
                    >I see you and I realize 

              """

    return prompt


def get_portuguese_prompt(genre, theme, key=None, style=None, mood=None):

    key_prompt = ""
    if key:
        key_prompt = f"O Tom da música deve ser em {key}. "

    style_prompt = ""
    if style:
        style_prompt = f", com o estilo de {style}"

    mood_prompt = ""
    if mood:
        mood_prompt = f", com um humor {mood}"

    prompt = f"""Gere a letra e a progressão de acordes de uma música do gênero {genre} sobre {theme}{style_prompt}{mood_prompt}. 
                 {key_prompt}Você deve colocar os acordes SOBRE as letras onde a mudança de acorde deve ocorrer. 
                 Adicione o tom que gerou a progressão de acordes no início da saída.
                 Adicione > antes de cada verso.
                 Coloque os metadados da música entre [], como [Verso 1], [Refrão].

                 O formato deve seguir o exemplo abaixo:
                    Tom: G
                    
                    [Intro]
                    G,  D,  Em,  C
                    
                    [Verso 1]
                    G,               D,
                    >Eu sei que já me esqueceu
                    Em,              C,
                    >Mas eu ainda penso em você
                    G,               D,
                    >A gente viveu um sonho
                    Em,               C,
                    >Que agora virou pesadelo
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


@app.route("/generate", methods=['POST'])
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
    app.run(host='0.0.0.0', port=5001)
