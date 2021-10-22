from flask import Flask, request
import json
import requests
import requests_cache

requests_cache.install_cache('pokedex_cache')

ORIGINAL_POKE_API = "https://pokeapi.co/api/v2"

app = Flask(__name__)
app.url_map.strict_slashes = False


def proxy_request(req):
    response = requests.get(ORIGINAL_POKE_API + req.path, params=req.args)
    forwarded_response = response.text.replace(
        ORIGINAL_POKE_API, "http://192.168.0.197:5000")
    return forwarded_response


@app.route("/pokemon/<id>/")
def pokemon_by_id(id):
    return proxy_request(request)


@app.route("/pokemon")
def pokemon_list():
    return proxy_request(request)
