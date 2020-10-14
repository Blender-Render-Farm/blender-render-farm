from flask import Flask
from os import system
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


def render(file_location: str, frames: list, output: str):
    if len(frames) == 1:
        system('blender -b {}  -o {} -f -{}'.format(file_location, output, frames[0]))
    else:
        system('blender -b {}  -o {} -s {} -t {}'.format(file_location, output, frames[0], frames[1]))
