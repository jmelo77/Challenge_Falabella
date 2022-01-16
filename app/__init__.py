import os
from flask import Flask
from flask_cors import CORS

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'Dev')
print ('Using %s environment' % ENVIRONMENT)

app = Flask(__name__)

CORS(app, resources={ r'/*': {'origins': '*'}}, supports_credentials=True)
app.config.from_object('app.settings.%s' %  ENVIRONMENT)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patent.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import views, helpers

app.register_blueprint(views.blueprint_patent)

helpers.create_patent()
