import  base64
import  sys

with open(sys.argv[1], 'r') as encoded_file:
    data = encoded_file.read()

for i in range (50):
    data = base64.b64decode(data)

print(data)
encoded_file.close()
