import tornado.ioloop
import tornado.web
import ldap

class IbuttonHandler(tornado.web.RequestHandler):

    def get(self, ibutton):
        # Do the actual work here
        # Call out to ldap, return a json dict
        # contents: entryUUID, username
        response = {
            'username': '',
            'entryUUID': ''
            }

        self.write(response)


def ldap_search(ibutton):
    # Do the ldap search here    
    pass

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", IbuttonHandler),
    ])

    application.listen(6969)
    tornado.ioloop.IOLoop.instance().start()
