With this application, we are able to generate a song according to some *genre*, *theme*, *style*, *mood* and *key*.
<br><br>
How-to:
1. Clone the repository\
`https://github.com/issilva5/chordgen.git`
2. Install the requirements\
`pip install -r requirements.txt`
3. Put the key and id in a `.env`
4. Use it with `python chordgen.py``

<br>
Here are some examples of the parameters: 

**Genre**: `rock, country, pop, samba, blues`\
**Theme**: `love, crime, life`\
**Style**: `an artist/band's name`\
**Mood**: `melancholic, happy, sad`\
**Lang**: `en or pt-br`\
**Key**: `G, E, Bm`

<br>
Also, you can choose the language that you want to use and it will be the same language of the lyrics you will receive. With that, you will receive a full lyric with the given chords and key chord to play and have fun!
Here is an example:

```
{
    "genre": "pop rock",
    "theme": "fame",
    "style": "Miley Cyrus",
    "mood": "powerful",
    "lang": "en",
    "key": "E"
}
```

And the result will be:

```
{
    "music": [
        "Key: E",
        "",
        "[Intro]",
        "E  B  C#m  A",
        "",
        "[Verse 1]",
        "E                            B",
        ">I'm living in a world of lights ",
        "C#m                             A",
        ">Where the cameras follow day and night",
        "E                            B",
        ">People screaming for my name ",
        "C#m                             A",
        ">But do they know who I really am?",
        "",
        "",
        "[Chorus]",
        "E                          B",
        ">Fame, it's a double-edged sword ",
        "C#m                        A",
        ">Bringing joy, but leaving us bored",
        "E                          B",
        ">Money can't buy happiness ",
        "C#m                       A",
        ">We're just prisoners of success",
        "",
        "",
        "[Verse 2]",
        "E                            B",
        ">Tryna keep myself sane ",
        "C#m                           A",
        ">In a world that's gone insane ",
        "E                            B",
        ">Everything's magnified ",
        "C#m                     A",
        ">But my emotions I have to hide",
        "",
        "",
        "[Chorus]",
        "E                          B",
        ">Fame, it's a double-edged sword ",
        "C#m                        A",
        ">Bringing joy, but leaving us bored",
        "E                          B",
        ">Money can't buy happiness ",
        "C#m                       A",
        ">We're just prisoners of success",
        "",
        "",
        "[Bridge]",
        "E                      B",
        ">Everybody wants a piece of me ",
        "C#m               A",
        ">But nobody knows who I can be ",
        "E                   B",
        ">I'm not just a brand ",
        "C#m                     A",
        ">I'm a human with a beating heart",
        "",
        "",
        "[Chorus]",
        "E                          B",
        ">Fame, it's a double-edged sword ",
        "C#m                        A",
        ">Bringing joy, but leaving us bored",
        "E                          B",
        ">Money can't buy happiness ",
        "C#m                       A",
        ">We're just prisoners of success",
        "",
        "[Outro]",
        "E  B  C#m  A"
    ]
}
```