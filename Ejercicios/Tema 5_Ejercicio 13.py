try:
    if '1' != 1:
        raise "algún error"
    else:
        print("no se ha producido algún error")
except "algún error":
    print ("se ha producido algún error")
    
