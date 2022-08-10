from flask import Blueprint, jsonify, make_response


errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def error_404(error):
    return make_response(jsonify(error=str(error)), 404)


@errors.app_errorhandler(500)
def error_500(error):
    return make_response(jsonify(error=str(error)), 500)


@errors.app_errorhandler(401)
def error_401(error):
    return make_response(jsonify(error=str(error)), 401)


@errors.app_errorhandler(405)
def error_405(error):
    return make_response(jsonify(error=str(error)), 405)
