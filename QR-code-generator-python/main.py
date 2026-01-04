import qrcode

def get_input():
    input_for_qr = input("Enter the text or url for generating QR: ").strip()
    return input_for_qr

def get_file():
    input_file = input("Enter the name of file: ").strip()
    return input_file

def generate_qr():
    data = get_input()
    filename = get_file()

    img= qrcode.make(data)

    fn = filename or "qrcode"
    
    if not fn.lower().endswith(".png"):
      fn += ".png"
    img.save(fn)    

    
generate_qr()