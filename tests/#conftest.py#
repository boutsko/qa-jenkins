import pytest
import multiprocessing
from flask import url_for
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from src.flask_app.app import create_app


@pytest.fixture(autouse=True, scope="class")
def chrome():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM).install()),
            options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def vm_controls(live_server, chrome):
    live_server.start()
    chrome.get(url_for('controls.controls', _external=True))
    return chrome


@pytest.fixture(scope="session")
def app():
    app = create_app('flask_test.cfg')
    multiprocessing.set_start_method("fork")
    return app


@pytest.fixture(scope="session")
def test_client():
    flask_app = create_app('flask_test.cfg')
    return flask_app.test_client()

