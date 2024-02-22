__version__='0.0.3'
#txtParser
#python 3.10.12


t = "example"
txt = f"{t}.txt"
txt2 = f"{t}2.txt"
# Read contents of file
with open(txt, 'r') as f:
    textFile = f.read()

# Replace the target string
textFile1 = textFile.replace('. ', '\n')

# Write to the new file
with open(txt2, 'w') as f:
    f.write(textFile1)