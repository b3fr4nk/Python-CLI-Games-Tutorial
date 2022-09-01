import requests

text = input("enter the text you wish to turn into ascii")
r = requests.get("https://ascii-generator.site/t/")
print(r.text)
print("done")