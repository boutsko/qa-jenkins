from flask import Blueprint, jsonify, render_template

vm_controls_bp = Blueprint('controls', __name__)


@vm_controls_bp.route("/controls")
def controls():
    return render_template("index.html")


@vm_controls_bp.route('/ping')
def ping():
    return jsonify(ping='pong')
