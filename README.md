With this application, we are able to generate a song according to some *genre*, *theme*, *style*, *mood* and *key*.
<br><br>
How-to:
1. Clone the repository\
`https://github.com/issilva5/chordgen.git`
2. Install the requirements\
`pip install -r requirements.txt`
3. Put the key and id in a `.env`
4. Use it with `python chordgen.py``

## How to use it?

### GET /generate

Use the GET request will give an SSE response. To pass the parameter to it, you must use the query string.

Here is an example: `localhost:5001/generate?genre=pop+rock&theme=fame&style=Miley+Cyrus&mood=powerful&lang=en&key=E`

### POST /generate

Make a POST request to the `localhost:5001/generate` URL.

Here are an example of the parameters: 

```json
{
    "genre": "pop rock",
    "theme": "fame",
    "style": "Miley Cyrus",
    "mood": "powerful",
    "lang": "en",
    "key": "E"
}
```

You can choose the language that you want to use and it will be the same language of the lyrics you will receive. With that, you will receive a full lyric with the given chords and key chord to play and have fun!
