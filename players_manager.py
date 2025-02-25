import os

# server imports
import redis
from jinja2 import Environment, FileSystemLoader
# Werkzeug App imports
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.urls import url_parse

from data_manager import DataManager
from team_builder import TeamBuilder


def base36_encode(number):
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


class Players(object):

    def __init__(self, config):
        self.data_manager = DataManager()
        self.builder = TeamBuilder()
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)
        self.host = os.getenv('HOST', '0.0.0.0:5000')

        self.url_map = Map([
            Rule('/', endpoint='home'),
            Rule('/players', endpoint='players'),
            Rule('/players/results', endpoint='result'),
            Rule('/teams', endpoint='team_builder'),
            Rule('/teams/results', endpoint='team_results'),
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
        return self.render_template('players.html', host=self.host)

    def on_result(self, request):
        name = request.args.get('name', None)
        nationality = request.args.get('nationality', None)
        club = request.args.get('club', None)
        data = self.data_manager.get_data_from_db(name=name, club=club, nationality=nationality)

        parameters = {"name": name if name is not None else '',
                      "club": club if club is not None else '',
                      "nationality": nationality if nationality is not None else ''
                      }
        return self.render_template('players-results.html', data=data, parameters=parameters, host=self.host)

    def on_home(self, request):
        return self.render_template('home.html',host=self.host)

    def on_about(self, request):
        return self.render_template('about.html', host=self.host)

    def on_team_builder(self, request):
        return self.render_template('teams.html', host=self.host)

    def on_team_results(self, request):
        budget = int(request.args.get('budget', 1000000000))
        data = self.builder.team_builder(budget)
        data = data[['Name', 'Age', 'Nationality', 'Club', 'Photo', 'Overall', 'Value', 'Position']]
        data = data.to_json()
        return self.render_template('team-result.html', data=data, budget=budget, host=self.host)


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
    port = int(os.getenv('PORT',5000))
    run_simple('0.0.0.0', port, app, use_debugger=True, use_reloader=True)