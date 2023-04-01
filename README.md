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
        "E, B, C#m, A ",
        "",
        "[Verse 1]",
        "E,                                        B",
        ">Got a taste of fame, now I can't slow down",
        "C#m,                                       A",
        ">Every move I make, they follow me around",
        "E,                                               B",
        ">Can't even go to lunch without a crowd ",
        "C#m,                                         A",
        ">Every single moment, they're screaming out loud",
        "",
        "[Chorus]",
        "E,                                       B",
        ">Here I am, the one they all love to hate ",
        "C#m,                                          A",
        ">Can't escape, can't get away ",
        "E,                                             B",
        ">Living my life just like a runaway ",
        "C#m,                                          A",
        ">Lost in the fame, can't find my way ",
        "",
        "[Verse 2]",
        "E,                                                B",
        ">Feeling like a puppet, they pull my strings ",
        "C#m,                                          A",
        ">Always in the spotlight, never off the scene ",
        "E,                                                   B",
        ">Can't take a step without a flash machine ",
        "C#m,                                                A",
        ">Every move I make, it's like I'm in a dream ",
        "",
        "[Chorus]",
        "E,                                       B",
        ">Here I am, the one they all love to hate ",
        "C#m,                                          A",
        ">Can't escape, can't get away ",
        "E,                                             B",
        ">Living my life just like a runaway ",
        "C#m,                                          A",
        ">Lost in the fame, can't find my way ",
        "",
        "[Bridge]",
        "C#m,                B,                 A,              E",
        ">Picture perfect, but it's not what it seems ",
        "C#m,                 B,                    A,             E",
        ">Living in the moment, just like a machine ",
        "C#m,               B,                  A,                E",
        ">But somewhere deep inside I'm just like you ",
        "C#m,                 B,                     A,                  E",
        ">Lost in the fame, trying to find the truth ",
        "",
        "[Chorus]",
        "E,                                       B",
        ">Here I am, the one they all love to hate ",
        "C#m,                                          A",
        ">Can't escape, can't get away ",
        "E,                                             B",
        ">Living my life just like a runaway ",
        "C#m,                                          A",
        ">Lost in the fame, can't find my way ",
        "",
        "[Outro]",
        "E, B, C#m, A"
    ]
}
```