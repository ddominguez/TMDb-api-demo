#!/usr/bin/env python
import json
import urllib2
from urllib import urlencode

class TMDB:
    api_url = 'http://api.themoviedb.org/3/'
    image_urls = {'poster': {}, 'profile': {}, 'backdrop': {}}

    def __init__(self, api_key):
        self.api_key = api_key
        self.configuration()

    def api_call(self, url):
        req = urllib2.Request(url)
        req.add_header('Accept', 'application/json')
        return json.load(urllib2.urlopen(req))

    def configuration(self):
        ''' sets image urls '''
        params = {'api_key': self.api_key}
        config = self.api_call(self.api_url+'configuration?%s' % urlencode(params))
        for poster in config['images']['poster_sizes']:
            self.image_urls['poster'][poster] = config['images']['base_url']+poster
        for profile in config['images']['profile_sizes']:
            self.image_urls['profile'][profile] = config['images']['base_url']+profile
        for backdrop in config['images']['backdrop_sizes']:
            self.image_urls['backdrop'][backdrop] = config['images']['base_url']+backdrop

    def get_params(self, extras=None):
        params = {'api_key': self.api_key}
        if isinstance(extras, dict):
            params.update(extras)
        return urlencode(params)

    def movie_search(self, q):
        ''' search for movies by title '''
        p = {'query': q}
        return self.api_call(self.api_url+'search/movie?%s' % self.get_params(p))

    def movie_info(self, id):
        ''' Get the basic movie information for a specific movie id '''
        return self.api_call(self.api_url+'movie/%s?%s' % (id, self.get_params()))

    def movie_casts(self, id):
        ''' Get the cast information for a specific movie id '''
        return self.api_call(self.api_url+'movie/%s/casts?%s' % (id, self.get_params()))

    def movie_trailers(self, id):
        ''' Get the trailers for a specific movie id '''
        return self.api_call(self.api_url+'movie/%s/trailers?%s' % (id, self.get_params()))

    def movie_images(self, id):
        ''' Get the images (posters and backdrops) for a specific movie id '''
        return self.api_call(self.api_url+'movie/%s/images?%s' % (id, self.get_params()))

    def movie_similar(self, id):
        ''' Get the similar movies for a specific movie id '''
        return self.api_call(self.api_url+'movie/%s/similar_movies?%s' % (id, self.get_params()))

    def person_search(self, q):
        ''' search for people by name '''
        p = {'query': q}
        return self.api_call(self.api_url+'search/person?%s' % self.get_params(p))

    def person_info(self, id):
        ''' Get the general person information for a specific id '''
        return self.api_call(self.api_url+'person/%s?%s' % (id, self.get_params()))

    def person_credits(self, id):
        ''' Get the credits for a specific person id '''
        return self.api_call(self.api_url+'person/%s/credits?%s' % (id, self.get_params()))

    def person_images(self, id):
        ''' Get the images for a specific person id '''
        return self.api_call(self.api_url+'person/%s/images?%s' % (id, self.get_params()))

    def now_playing(self):
        ''' Get the list of movies playing in theatres.
            This list refreshes every day.
            The maximum number of items this list will include is 100. '''
        return self.api_call(self.api_url+'movie/now-playing?%s' % self.get_params())

    def upcoming_movies(self):
        ''' Get the list of upcoming movies.
            This list refreshes every day.
            The maximum number of items this list will include is 100. '''
        return self.api_call(self.api_url+'movie/upcoming?%s' % self.get_params())
