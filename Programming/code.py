import hashlib, sys, os

def md5(input):
    return hashlib.md5(input.encode()).hexdigest()

file_name = sys.argv[1]

if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
else:
    print("The file does not exist!")
    sys.exit()

for f in content.split('\n'):
    print(md5(f))