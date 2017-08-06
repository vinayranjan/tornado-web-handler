"""Hanlder to handle the complete application."""
import tornado.ioloop
import tornado.web
import os
from tornado.web import url

from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")


class MainHandler(tornado.web.RequestHandler):
    """Main handler to render the home page."""

    def get(self):
        """Render the index page."""
        self.render("index.html", handler=self)


class PageHandler(tornado.web.RequestHandler):
    """Page handler to handle pages other than home page."""

    def get(self):
        """Render the page based on url."""
        current_url = self.request.uri.split('?')[0].replace('/', '')
        self.render("{0}.html".format(current_url), handler=self)

if __name__ == "__main__":
    parse_command_line()
    all_templates = []
    for content in os.walk(
            os.path.join(os.path.dirname(__file__), "templates")):
        all_templates = content[2]
    template_handlers = [url(r"/", MainHandler)]
    for file in all_templates:
        if '.html' in file:
            template_handlers.append(
                url(r'/' + file.split('.')[0], PageHandler))

    application = tornado.web.Application(
        template_handlers,
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug)

    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
