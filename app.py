from flask import Flask, render_template, url_for, redirect, request
import lyricsgenius as genius
import json 
import os 
import markov_chain as mc
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
 
# Accessing variables.
api_key = os.getenv('API_KEY')
api = genius.Genius(api_key)
api.verbose = False # Turn off status messages
api.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
api.skip_non_songs = False # Include hits thought to be non-songs (e.g. track lists)
api.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their title

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

    
    artist = api.search_artist(artist_name, max_songs=3)
    artist.save_lyrics('lyrics', overwrite=True)
    # Opening JSON file 
    f = open('lyrics.json',)  
    lyric_list = json.load(f)
    

    lyrics = ''
    songs = lyric_list['songs']
    print(type(songs[0]))
    for lyric_dict in songs:
        lyrics += lyric_dict['lyrics'].replace('...', '') + ' '


    
    result = mc.generate_lyrics(lyrics)


    #result = []
    #for line in range(0, lines):
    #    result.append(mc.generateString())
    

    return render_template('lyrics.html', result=result, artist=artist)

if __name__ == '__main__':
    app.run()