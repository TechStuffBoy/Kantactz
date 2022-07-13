"""
Originaly code was taken from http://djangosnippets.org/snippets/290/
I was made some improvements like print URL from what queries was
and don't show queries from URLs starts with MEDIA_URL
"""
from django.db import connection
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
import os


def terminal_width():
    """
    Function to compute the terminal width.
    WARNING: This is not my code, but I've been using it forever and
    I don't remember where it came from.
    """
    width = 0
    try:
        import struct, fcntl, termios
        s = struct.pack('HHHH', 0, 0, 0, 0)
        x = fcntl.ioctl(1, termios.TIOCGWINSZ, s)
        width = struct.unpack('HHHH', x)[1]
    except:
        pass
    if width <= 0:
        try:
            width = int(os.environ['COLUMNS'])
        except:
            pass
    if width <= 0:
        width = 80
    return width

class SqlPrintingMiddleware(MiddlewareMixin):
    """
    Middleware which prints out a list of all SQL queries done
    for each view that is processed.  This is only useful for debugging.
    """

    # def __init__(self, get_response):
    #     self.get_response = get_response
    #     print('Init: Middleware called!')
    #     # One-time configuration and initialization.

    # def __call__(self, request):
    #     # Code to be executed for each request before
    #     # the view (and later middleware) are called.

    #     response = self.get_response(request)

    #     # Code to be executed for each request/response after
    #     # the view is called.

    #     return response

    def process_response(self, request, response):
        # if not settings.DEBUG or len(connection.queries) == 0 or request.path_info.startswith(settings.MEDIA_URL):
        #     return response
        
        indentation = 2  
        print("\n\n%s\033[1;35m[SQL Queries for]\033[1;34m %s\033[0m\n" % (" "*indentation, request.path_info))
        width = terminal_width()
        total_time = 0.0
        for query in connection.queries:
            nice_sql = query['sql'].replace('"', '').replace(',',', ')
            sql = "\033[1;31m[%s]\033[0m %s" % (query['time'], nice_sql)
            total_time = total_time + float(query['time'])
            while len(sql) > width-indentation:
                print ("%s%s" % (" "*indentation, sql[:width-indentation]))
                sql = sql[width-indentation:]
            print( "%s%s\n" % (" "*indentation, sql))
        replace_tuple = (" "*indentation, str(total_time))
        print ("%s\033[1;32m[TOTAL TIME: %s seconds]\033[0m" % replace_tuple)
        return response