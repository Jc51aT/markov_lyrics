from flask import Flask, render_template, url_for, redirect, request
import lyricsgeinus as genius
import json 
import os 
import markov_chain

api = genius.Genius(os.environ.get('API_K'))

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/lyrics', methods=['POST'])
def lyrics():
    artist_name = request.form['artist']
    lines = int(request.form['lines'])

    if not artist_name:
        return redirect(url_for('index'))

    
    artist = api.search_artist(artist_name, max_songs=20, take_first_result=True)
    api.save_artists(artist, overwrite=True)

    lyrics = ''
    for lyric_dict in lyric_list:
        lyrics += lyric_dict['snippet'].replace('...', '') + ' '


    mc = markov_chain()
    mc.generateDatabase(lyrics)


    result = []
    for line in range(0, lines):
        result.append(mc.generateString())
    

    return render_template('lyrics.html', result=['hello', 'world'], artist=artist)

if __name__ == '__main__':
    app.run()