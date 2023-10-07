from model import Model, InterpModel

dirs = [
  "./text/text.txt",
  "./text/text1.txt",
  "./text/text2.txt",
  "./text/text3.txt",
  "./text/text5.txt",
]

data = ""
for dir in dirs:
  with open(dir, "r") as f:
    data += f.read()
    data += ""



model = InterpModel(data, 1, 50)

while True:
  s = input("Enter a sentence: ")
  print(model.generate(s, 5))


