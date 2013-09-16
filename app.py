#!/usr/bin/env python
import os
from flask import Flask, render_template
import tmdb
import settings

app = Flask(__name__)

themoviedb = tmdb.TMDB(settings.API_KEY)

@app.route('/')
def index():
    movies = themoviedb.now_playing()
    return render_template('index.html', movies=movies)

@app.route('/movie/')
@app.route('/movie/<id>')
def movie(id=None):
    movie = None
    if id is not None:
        movie = themoviedb.movie_info(id)
        cast = themoviedb.movie_casts(id)
    return render_template('movie.html', movie=movie, cast=cast)

@app.route('/person/<id>')
def person(id):
    person = themoviedb.person_info(id)
    return render_template('person.html', person=person)

@app.context_processor
def inject_globals():
    return dict(urls=themoviedb.image_urls)

if __name__ == "__main__":
    app.debug = True
    # app.run()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
