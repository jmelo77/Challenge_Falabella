from flask import request, jsonify, Response, Blueprint
from .models import Patent
from .models import db

class HTTPStatusCode(object):
    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_200_OK = 200
    HTTP_204_NO_CONTENT = 204
    HTTP_500_SERVER_ERROR = 500

status = HTTPStatusCode()

blueprint_patent = Blueprint('patent', __name__, url_prefix='/patent')

@blueprint_patent.route('/id/<int:id>', methods=['GET'])
def Patent_Id_Resource(id):
    if request.method == 'GET':
        if id is not None:
            result = Patent.query.filter_by(id=id).first()
            if result:
                return jsonify(patent=result.patent), status.HTTP_200_OK
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@blueprint_patent.route('/name/<name>', methods=['GET'])
def Patent_Name_Resource(name):
    if request.method == 'GET':
        if name is not None:
            result = Patent.query.filter_by(patent=name.upper()).first()
            if result:
                return jsonify(id=result.id), status.HTTP_200_OK
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)               