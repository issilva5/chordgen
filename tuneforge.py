import os
import openai
from flask import Flask, request, Response
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
                 The chords must be between dots. Each lyric verse must start with >.

                 The format must follow the example below:

                    Key: Cm

                    [Intro] 
                    .B.  .B11.  .B.  
                    .B.  .B11.  .B.
                    .B.  .F#6(11).  .E7M.  

                    [Verse 1]

                    .B.
                    >Look at the stars
                                        .F#6(11).
                    >Look how the shine for you
                                        .E7M.
                    >And everything you do

                    >Yeah, they were all yellow
                    .B.
                    >I came along
                                    .F#6(11).
                    >I wrote a song for you

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
                 {key_prompt}Coloque os acordes ACIMA da letra da música, na posição em que a mudança de acorde deve ocorrer.
                 Adicione o tom que gerou a progressão de acordes no início da saída.
                 Coloque os metadados da música entre [], como [Verso 1], [Refrão].
                 Os acordes devem estar entre pontos, por exemplo, .F#6(11). .
                 Cada verso da letra deve começar com >.

                 O formato deve seguir o exemplo abaixo:

                    Tom: Cm

                    [Introdução]
                    .B. .B11. .B.
                    .B. .B11. .B.
                    .B. .F#6(11). .E7M.

                    [Verso 1]

                    .B.
                    >Olha as estrelas
                                        .F#6(11).
                    >Olha como o brilho para você
                              .E7M.
                    >E tudo que você faz

                    >Sim, eram todos amarelos
                    .B.
                    >Eu vim junto
                                    .F#6(11).
                    >Escrevi uma musica pra você
              """

    return prompt


def generate_song(prompt, stream = False):

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        stream=stream
    )

    return completion


@app.route("/generate", methods=['GET'])
@cross_origin()
def generate_stream():

    req_data = request.args.to_dict()
    genre = req_data.get('genre')
    theme = req_data.get('theme')
    style = req_data.get('style')
    mood = req_data.get('mood')
    lang = req_data.get('lang')
    key = req_data.get('key')

    prompt = get_prompt(lang, genre, theme, key, style, mood)
    response = generate_song(prompt, stream=True)

    def stream():

        buffer = ''

        for chunk in response:

            delta = chunk['choices'][0]['delta']

            if 'content' in delta:
                buffer += delta['content']
                if len(buffer) >= 50:
                    yield buffer
                    buffer = ''
    
    return Response(stream(), mimetype='text/event-stream')

@app.route("/generate", methods=['POST'])
@cross_origin()
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
    response = response.choices[0].message

    return {'music': response['content'].split('\n')}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
