#爬猫？
import urllib.request as req

response=req.urlopen("http://placekitten.com.s3.amazonaws.com/homepage-samples/200/287.jpg")
cat_img=response.read()
f=open('cat_no,2.jpg','wb')
try:
    f.write(cat_img)
finally:
    f.close()
print(response.geturl())
print(response.info())
print(response.getcode())
