def search(obj, item, depth):
    if depth == 0:
        return None
    
    if item in obj:
        return obj[item]
    else:
        for key in obj.keys():
            if type(obj[key]) is dict:
                returned_value = search(obj[key], item, depth - 1)
                if returned_value is not None:
                    return returned_value
    return None
    


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

key = input("Введите искомый ключ: ")
has_depth = True if input("Хотите ввести максимальную глубину? Y/N: ").lower() == "y" else False
depth = int(input("Введите максимальную глубину: ")) if has_depth else float("inf")

print(f"Значение ключа: {search(site, key, depth)}")