from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parent.parent / "app.py")


def test_app_carga_sin_excepciones():
    at = AppTest.from_file(APP, default_timeout=60).run()
    assert not at.exception
