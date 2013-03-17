#!/usr/bin/env python
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

@app.context_processor
def inject_globals():
    return dict(urls = themoviedb.image_urls)

if __name__ == "__main__":
    app.debug = True
    app.run()