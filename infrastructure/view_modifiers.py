# https://github.com/talkpython/data-driven-web-apps-with-flask/blob/master/app/ch05_jinja_templates/final/pypi_org/infrastructure/view_modifiers.py

from functools import wraps

import flask
import werkzeug
import werkzeug.wrappers


def response(*, mimetype: str = None, template_file: str = None):  # type:ignore
    def response_inner(f):
        @wraps(f)
        def view_method(*args, **kwargs):
            response_val = f(*args, **kwargs)

            if isinstance(response_val, werkzeug.wrappers.Response):
                return response_val

            if isinstance(response_val, flask.Response):
                return response_val

            if isinstance(response_val, dict):
                model = dict(response_val)
            else:
                model = dict()

            if template_file and not isinstance(response_val, dict):
                raise Exception(
                    "Invalid return type {}, we expected a dict as the return value.".format(
                        type(response_val)
                    )
                )

            if template_file:
                response_val = flask.render_template(template_file, **response_val)

            resp = flask.make_response(response_val)
            resp.model = model  # type:ignore
            if mimetype:
                resp.mimetype = mimetype

            return resp

        return view_method

    return response_inner
