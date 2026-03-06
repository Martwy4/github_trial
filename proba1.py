def order(cst_name, cst_order, *arg, **kwarg):
    print(cst_name, 'ordered a', cst_order)
    for arg in arg:
        print(' - Add', arg)
    for key, value in kwarg.items():
        print(' - Add', key, ':', value)
order('Tadzia', 'black coffee')
order('Tadea', 'black coffe', milk='whole')
order('Tadeusza','tea','none', sweetener='honey')