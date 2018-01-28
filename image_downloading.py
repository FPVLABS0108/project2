import random
import urllib.request

def download_web_image(url):
    name=random.randrange(1,1000)
    img_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,img_name)


download_web_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsXZ8o7b3rRZ1VpnMNsVU4q8q_vZRD6AEUaGg_YjfOrHrT4YGcLg")
download_web_image("http://wp.production.patheos.com/blogs/loveinshallah/files/2014/05/soulmates.jpg?w=300")
download_web_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQNSyFxUohiUTOtW9aYDmFgFMueHlPraqxdw9v6tnHZ8Ydk9wn0Q")
download_web_image("https://completewellbeing.com/wp-content/uploads/2014/10/soul-mates-cell-mates.jpg")