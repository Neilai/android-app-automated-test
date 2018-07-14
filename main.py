import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self,input):

        self.render('./dynamicTest/dynamic.html')


class dynamicHandler(tornado.web.RequestHandler):
    def get(self,input):
        if input =='0':
            self.render('./dynamicTest/dynamic0.html')
        elif input=='1':
            self.render('./dynamicTest/dynamic1.html')
        elif input == '2':
            self.render('./dynamicTest/dynamic2.html')
        elif input == '3':
            self.render('./dynamicTest/dynamic3.html')

class reverseHandler(tornado.web.RequestHandler):
    def get(self,input):
        if input =='0':
            self.render('./reverseTest/reverse0.html')
        elif input =='1':
            self.render('./reverseTest/reverse1.html')
        elif input=='2':
            self.render('./reverseTest/reverse2.html')
        elif input == '3':
            self.render('./reverseTest/reverse3.html')

class staticHandler(tornado.web.RequestHandler):
    def get(self,input):
        if  input =='0':
            self.render('./staticTest/static0.html')
        elif input =='1':
            self.render('./staticTest/static1.html')
        elif  input=='2':
            self.render('./staticTest/static2.html')
        elif input == '3':
            self.render('./staticTest/static3.html')


class introductionHandler(tornado.web.RequestHandler):
    def get(self,input):
        if  input =='0':
            self.render('./introduction/about.html')
        elif input =='1':
            self.render('./introduction/select.html')




if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/dynamicTest/(\w+)', dynamicHandler),
                  (r'/reverseTest/(\w+)', reverseHandler),
                  (r'/staticTest/(\w+)', staticHandler),
                  (r'/introduction/(\w+)', introductionHandler),
             ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

