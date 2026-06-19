import requests
import pandas
from bs4 import BeautifulSoup

respons = requests.get("https://www.flipkart.com/ajy/~cs-7d5gd723be/pr?sid=ajy&collection-tab-name=BBD+2024+Noise+Smartwatches&" \
"pageCriteria=default&param=5781&hpid=Y8tEWNmThOXtFwc8qea15Kp7_Hsxr70nj65vMAAFKlc%3D&" \
"ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTEsMDk5Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiU01XR0dLVDVGWVFITlJKUCIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIk5vaXNlIFNtYXJ0d2F0Y2hlcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D")

# print(respons)
soup = BeautifulSoup(respons.content,'html.parser') 
# print(soup)
names = soup.find_all('a',class_="wjcEIp")
# print(names)
name=[]
for i in names[0:10]:
   tex= i.get_text()
   name.append(tex)
# print(emp)   
prices = soup.find_all('div',class_="Nx9bqj")
# print(names_1)
price=[]
for i in prices[0:10]:
    data = i.get_text()
    data_1=data.replace('₹','')
    price.append(data_1)
# print(price)
ratting = soup.find_all('div',class_="XQDdHH")
rate =[]
for i in ratting[0:10]:
    r = i.get_text()
    rate.append(float(r))
# print(rate)      
images = soup.find_all('img',class_="DByuf4")
im=[]
for i in images[0:10]:
    image=i['src']
    im.append(image)
# print(im) 
   
df = pandas.DataFrame()
df['NAMES']= name
df['PRICES'] = price
df['RATTING'] = rate
df['IMAGES_LINK'] = im
# print(df)
df.to_csv('watches.csv')



