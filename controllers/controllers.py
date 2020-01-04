# -*- coding: utf-8 -*-
import json
import urllib.request
from html.parser import HTMLParser

from odoo import http

class MyHTMLParser(HTMLParser):
    res = ['Error', 'No description found!', '/renderlistcontent/static/src/img/404PageNotFound.png']
    def handle_starttag(self, tag, attrs):
        if tag == 'meta' and 'property' in attrs[0]:
            if 'title' in attrs[0][1]:
                self.res[0] = attrs[1][1]
            elif 'description' in attrs[0][1]:
                self.res[1] = attrs[1][1]
            elif 'image' in attrs[0][1]:
                self.res[2] = attrs[1][1]

class RenderListContent(http.Controller):
    @http.route('/render/<string:url>', auth='public')
    def content(self, url):
        fp = urllib.request.urlopen('https://' + url)
        
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

        parser = MyHTMLParser()
        parser.res = ['Error', 'No description found!', '/renderlistcontent/static/src/img/404PageNotFound.png']
        parser.feed(mystr)
        
        obj = {'res': parser.res}
        tmp = json.dumps(obj)

        return tmp
