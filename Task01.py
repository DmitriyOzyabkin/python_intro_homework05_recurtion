def user_request() -> str | int:
    max_depth = None
    key = input('Enter key: ')
    max_depth_request = input(
        'Do you wanna enter depth od search? (Y/N): ').lower()
    if max_depth_request == 'y':
        max_depth = int(input('Enter max depth: '))
    return key, max_depth


def find_key(structure: dict, key: str, max_depth=None, depth=1):
    result = None
    if max_depth and max_depth < depth:
        return result

    if key in structure:
        return structure[key]
    
    for sub_structure in structure.values():
        if isinstance(sub_structure, dict):
            result = find_key(sub_structure, key, max_depth, depth=depth + 1)
        if result:
            return result
        continue
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


while True:
    key, max_depth = user_request()
    answer = find_key(site, key, max_depth)
    print(answer)