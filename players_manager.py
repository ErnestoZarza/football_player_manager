import os

from sqlalchemy import create_engine
import pymysql
import pandas as pd

# server imports
import redis
from jinja2 import Environment, FileSystemLoader
# Werkzeug App imports
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.urls import url_parse
from werkzeug.utils import redirect


def get_data_from_db(name=None, club=None, nationality=None):
    sql_engine = create_engine('mysql+pymysql://root:Panda@#35@127.0.0.1', pool_recycle=3600)

    db_connection = sql_engine.connect()

    where = ''

    if name:
        where = "WHERE Name={name}".format(name=name)
    if club:
        if "WHERE" in where:
            where += " AND Club={club}".format(club=club)
        else:
            where = "WHERE Club={club}".format(club=club)
    if nationality:
        if "WHERE" in where:
            where += " AND Nationality='{nationality}'".format(nationality=nationality)
        else:
            where = "WHERE Nationality='{nationality}'".format(nationality=nationality)

    frame = pd.read_sql("select * from football_players_db.players {filter}".format(filter=where), db_connection);

    pd.set_option('display.expand_frame_repr', False)

    print(frame)

    db_connection.close()
    return frame.to_json()


# get_data_from_db(nationality='Argentina')

# @Request.application
# def application(request):
#     return Response('Hello, World!')


def base36_encode(self, number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))


def is_valid_url(url):
    parts = url_parse(url)
    return parts.scheme in ('http', 'https')


def get_hostname(url):
    return url_parse(url).netloc


def application(environ, start_response):
    request = Request(environ)
    text = 'Hello %s!' % request.args.get('name', 'Ernesto')
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)


class Players(object):

    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)

        self.url_map = Map([
            Rule('/', endpoint='home'),
            Rule('/players', endpoint='players'),
            Rule('/search', endpoint='search'),
            Rule('/results', endpoint='result'),
            Rule('/teams', endpoint='team_builder'),
            Rule('/builder', endpoint='team_result'),
            Rule('/about', endpoint='about')
        ])

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def on_players(self, request):
        return self.render_template('players.html')

    def on_search(self, request):
        if request.method == 'POST':

            url = request.form['url']
            if not is_valid_url(url):
                error = 'Please enter a valid URL'
            else:
                name = request.args.get('name', None)
                nationality = request.args.get('nationality', None)
                club = request.args.get('club', None)
                result = get_data_from_db(name=name, nationality=nationality, club=club)
                return self.render_template('search-result.html',
                                            name=name,
                                            nationality=nationality,
                                            club=club,
                                            data=result
                                            )
            return self.render_template('players.html', error=error, url=url)

    def on_home(self, request):
        return self.render_template('home.html')

    def on_about(self, request):
        return self.render_template('about.html')

    def on_team_builder(self, request):
        return self.render_template('teams.html')


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Players({
        'redis_host': redis_host,
        'redis_port': redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': os.path.join(os.path.dirname(__file__), 'static')
        })
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)