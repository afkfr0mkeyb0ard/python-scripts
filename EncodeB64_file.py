#Encode all the lines of a file to base64
import base64

with open('file.txt') as f:
        lines = f.read().splitlines()
B64 = []
for el in lines:
        b = base64.b64encode(bytes(el, 'utf-8'))
        b = b.decode("utf-8")
        B64.append(b)

with open('result.txt','w') as f:
        for el in B64:
                f.write(el + "\n")
