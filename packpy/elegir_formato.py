def elegir_moneda_sistema(Europa=True):
    if Europa:
        America = False
        mon_sym = '€'
    elif not Europa:
        America = True
        mon_sym = '$'
    return mon_sym