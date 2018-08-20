from . import web


@web.route('/user')
def login():
    return 'User'

