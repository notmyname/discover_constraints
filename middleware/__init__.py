try:
    import simplejson as json
except ImportError:
    import json

from swift.common.utils import readconf

class DiscoverConstraints(object):

    def __init__(self, app, conf):
        self.app = app
        try:
            constraints = readconf('/etc/swift/swift.conf',
                                   'swift-constraints')
        except SystemExit:
            self.constraints = None
        else:
            del constraints['__file__']
            del constraints['log_name']
            for k, v in constraints.items():
                constraints[k] = int(v)
            self.constraints = json.dumps(constraints)

    def __call__(self, env, start_response):
        if env['PATH_INFO'] == '/.constraints' and \
                env['REQUEST_METHOD'] == 'GET':
            if self.constraints:
                body = [self.constraints]
            else:
                body = ['Constraints were not loaded']
            start_response('200 Ok',
                [('Content-Length', str(sum(len(b) for b in body))),
                 ('Content-Type', 'application/json')])
            return body

        else:
            return self.app(env, start_response)


def filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)

    def make_filter(app):
        return DiscoverConstraints(app, conf)

    return make_filter
