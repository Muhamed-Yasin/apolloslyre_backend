from __init__ import create_app

flask_app = create_app()
celery_app = flask_app.extensions["celery"]