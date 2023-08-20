import sys
import time
from flask import Flask, url_for
import pytest
import urllib.request
from urllib.request import urlopen, Request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.flask_app.app import create_app

SLEEP = 3.5

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None


def test_vm_controls_url(vm_controls):
    res = urllib.request.urlopen(url_for('controls.controls', _external=True))
    assert url_for('controls.controls') == "/controls"
    assert res.code == 200

def test_vm_controls_create_button(vm_controls):
    create_btn = WebDriverWait(vm_controls, 10).until(
        EC.presence_of_element_located((By.ID, "create-btn"))
    )
    create_btn.click()
    time.sleep(SLEEP)
    assert "Vm has been created" in vm_controls.page_source


def test_vm_controls_start_button(vm_controls):
    start_btn = WebDriverWait(vm_controls, 10).until(
        EC.presence_of_element_located((By.ID, "start-btn"))
    )
    start_btn.click()
    time.sleep(SLEEP)
    assert "Vm has been started" in vm_controls.page_source


def test_vm_controls_stop_button(vm_controls):
    stop_btn = WebDriverWait(vm_controls, 10).until(
        EC.presence_of_element_located((By.ID, "stop-btn"))
    )
    stop_btn.click()
    time.sleep(SLEEP)
    assert "Vm has been stopped" in vm_controls.page_source


def test_vm_controls_snapshot_button(vm_controls):
    snapshot_btn = WebDriverWait(vm_controls, 10).until(
        EC.presence_of_element_located((By.ID, "snapshot-btn"))
    )
    snapshot_btn.click()
    time.sleep(SLEEP)
    assert "Vm has been snapshotted" in vm_controls.page_source
