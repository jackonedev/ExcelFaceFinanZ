def elegir_simbolo_moneda(Europa=True):
    if Europa:
        America = False
        mon_sym = '€'
    elif not Europa:
        America = True
        mon_sym = '$'
    print (f'Simbolo: {mon_sym}')
    return mon_sym