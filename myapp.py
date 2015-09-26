from uwsgidecorators import *
import tornado.web

# this is our Tornado-managed app
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

t_application = tornado.web.Application([
    (r"/", MainHandler),
])

# here happens the magic, we bind after every fork()
@postfork
def start_the_tornado_servers():
    application.listen(8000 + uwsgi.worker_id())
