import hashlib, sys, os

def md5(input):
    return hashlib.md5(input.encode()).hexdigest() # Function to compute MD5

file_name = sys.argv[1]  # Get the file name

if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        content = f.read() # Read the file's content
else:
    print("The file does not exist!")
    sys.exit()

for f in content.split('\n'): # Loop through each line of the file
    print(md5(f))