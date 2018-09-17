import _func

if __name__ == '__main__':

    _username = input('Enter a username: ')

    if _username != None:
        _func.get_count(_username)
        _end = int(input('How many items would you like to retrieve? '))
        _func.get_page(_username, 1, _end)
    else:
        quit()
