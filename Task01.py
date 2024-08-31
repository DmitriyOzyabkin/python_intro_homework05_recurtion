def user_request() -> str | int:
    max_depth = None
    key = input('Enter key: ')
    max_depth_request = input('Do you wanna enter depth od search? (Y/N): ').lower()
    if max_depth_request == 'y':
        max_depth = int(input('Enter max depth: '))
    return key, max_depth




while True:
    user_request()
