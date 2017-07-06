
def get(id):
    if id == 0: # Empty bytearray
        return bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    if id == 1: # Icon 1
        return bytearray(b'\xff\x01\x01\x01\xf1\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\xf1\x01\x01\x01\xff\xff\x00\x00\x00\xff\x00\x00\x00\xff\x01\x01\x01\xf1\x11\x11\x11\x11\x11\x11\xf1\x01\x01\x01\xff\x00\x00\x00\xff\x00\x00\x00\xff\xff\x00\x00\x00\xff\x00\x00\x00\xff\x80\x80\x80\x8f\x88\x88\x88\x88\x88\x88\x8f\x80\x80\x80\xff\x00\x00\x00\xff\x00\x00\x00\xff\xff\x80\x80\x80\x8f\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x8f\x80\x80\x80\xff')

    if id == 2: # Icon 2
        return bytearray(b'\xff\x01\x01\x01\xf1\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\xf1\x01\x01\x01\xff\xff\x00\x00\x00\xff\x00\x00\x00\xff\x01\x01\x01\xf1\x11\x11\x11\x11\x11\x11\xf1\x01\x01\x01\xff\x00\x00\x00\xff\x00\x00\x00\xff\xff\x00\x00\x00\xff\x00\x00\x00\xff\x80\x80\x80\x8f\x88\x88\x88\x88\x88\x88\x8f\x80\x80\x80\xff\x00\x00\x00\xff\x00\x00\x00\xff\xff\x80\x80\x80\x8f\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x8f\x80\x80\x80\xff')



    if id == 'wifi': # Wifi icon
        return bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\xC0\xC0\xC0\xC0\xE0\xE0\xE0\xE0\xE0\xE0\xE0\xE0\xC0\xC0\xC0\xC0\x80\x80\x00\x00\x00\x00\x00\x00\x08\x1C\x3E\x3E\x1F\x1F\x0F\x0F\x07\x87\x83\xC3\xC3\xC3\xC3\xC3\xC3\xC3\xC3\xC3\xC3\x83\x87\x07\x0F\x0F\x1F\x1F\x3E\x3E\x1C\x08\x00\x00\x00\x00\x00\x00\x06\x0F\x1F\x0F\x0F\x07\x87\x83\xC3\xC3\xC3\xC3\x83\x87\x07\x0F\x0F\x1F\x0F\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x07\x0F\x0F\x07\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
