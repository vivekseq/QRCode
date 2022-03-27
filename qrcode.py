import qrcode
from PIL import Image
from  urllib.parse import urlparse
import sys
def qr(n):
    img = qrcode.make(n)
    source = urlparse(n).netloc
    img.save(source + ".jpg")
    print("saved image"+ source)




if __name__ == '__main__':
    try:
        arg_command = sys.argv[1]
    except IndexError:
        arg_command = ""

    Done = False
    while not Done:
        if arg_command=="":
            print('\nMenu')
            print('U URL')
            print('Q Quit')
            print('----------------')
            command = input('Enter Selection> ').strip()[0].upper()
        else:
            command = arg_command
            #- set arg value to empty to run Menu option again.
            arg_command = ""

        if command == 'U':
            print ("Enter URL:")
            url = input().lower()
            qr(url)
        elif command == "Q":
            break
        else:
            print ("Wrong Selection.")
