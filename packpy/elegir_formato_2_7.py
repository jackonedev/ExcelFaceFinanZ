def elegir_moneda_sistema(Europa=True):
    if Europa:
        America = False
        mon_sys = 'euro'
    elif not Europa:
        America = True
        mon_sys = '$'
    return mon_sys