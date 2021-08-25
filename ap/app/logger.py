import logging
import ulid
from datetime import datetime

from flask import g, request


logger = logging.getLogger('commonLogger')


def logging_request():
    try:
        request_id = ulid.new().str
        g.request_id = request_id
        logger.info(("<<Request Log>> Request Id: <%s> %s %s, Request host: <%s>, query: <%s>"),
                    request_id,
                    request.method,
                    request.path,
                    request.host,
                    request.args.get('query'))
        g.start_time = datetime.now()
    except Exception as error:
        logger.error(("before_app_request error, method: %s, url: %s, params: %s, error_detail: %s"),
                     request.method,
                     request.path,
                     request.args.get('query'),
                     error)
        raise error


def logging_response(response):
    try:
        current_user = g.get('current_user', None)
        if current_user:
            logger.info("<<Response Log>> Request Id: <%s>, %s %s, user_id: <%s>, ip: <%s>, response: %s, (%0.3fs)",
                        g.request_id,
                        request.method,
                        request.path,
                        current_user.user_id,
                        request.remote_addr,
                        response.data.decode(),
                        (datetime.now() - g.start_time).total_seconds())
        else:
            logger.info("<<Response log>> Request Id: <%s>, ip: <%s>, %s %s, response: %s, (%0.3fs)",
                        g.request_id,
                        request.remote_addr,
                        request.method,
                        request.path,
                        response.data.decode(),
                        (datetime.now() - g.start_time).total_seconds())

    except Exception as error:
        logger.error(("after_app_request error, method: %s, url: %s, params: %s, response: %s, error_detail: %s"),
                     request.method,
                     request.path,
                     response.data.decode(),
                     error)
        raise error
    else:
        return response
