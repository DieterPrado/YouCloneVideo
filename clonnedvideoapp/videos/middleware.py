def ip_is_valid(get_response):

    def middleware(request):

        print('testmmiddleware')
        response = get_response(request)

        return response

    return middleware