def tpl_sort(tpl):
    if not all(isinstance(num, int) for num in tpl):
        return tpl
    return tuple(sorted(tpl))

tpl = (6, 3, -1, 8, 4, 10, -5)

print(tpl_sort(tpl))