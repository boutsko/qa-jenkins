from flask import Flask
from views import vm_controls_views
from vm_controls import vm_controls_bp


def create_app(config=None):
    app = Flask(
        __name__,
        static_url_path='',
        static_folder='static',
        template_folder='templates',
    )

    if config:
        app.config.from_pyfile(config)

    app.register_blueprint(vm_controls_bp)
    app.register_blueprint(vm_controls_views.vm_controls_page)

    return app


if __name__ == '__main__':
    app = create_app('config.py')
    app.run(debug=True)
