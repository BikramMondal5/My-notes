import requests
url="http://ratings.fide.com/download/standard_rating_list.zip"
result = requests.get(url)
with open("output.zip","wb") as file:
    file.write(result.content)
print("Download complete")