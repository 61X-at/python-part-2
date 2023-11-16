def create_site(count):
    res = []
    for _ in range(count):
        item = input('Введите название продукта для нового сайта: ')
        current = {
                    'html': {
                        'head': {
                            'title': f'Куплю/продам {item} недорого'
                        },
                        'body': {
                            'h2': f'У нас самая низкая цена на {item}',
                            'div': 'Купить',
                            'p': 'Продать'
                        }
                    }
                }

        res.append(current)
        print(res)

create_site(int(input('Сколько сайтов: ')))