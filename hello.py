from cgi import parse_qsl

def app(environ, start_response):
    d = parse_qsl(environ['QUERY_STRING'], True)
    
    output = ''
    for key,value in d:
                output = output + key + '=' + value +'\n'

    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return output
