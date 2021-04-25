from flask import Flask

from ci_play.server import app


def test_app():
    assert isinstance(app, Flask)
