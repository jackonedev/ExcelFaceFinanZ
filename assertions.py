try:
    raise valueError("sample value error")
except Exception as e:
    print str(e)    

try:
    raise valueError("sample value error")
except Exception,exception:
    print str(exception)


try:
    raise valueError("sample value error")
except exception:
    print str(exception)


try:
    raise valueError("sample value error")
except Exception:
    print str(Exception) # it prints only the object reference