from urllib import request
google_url="https://finance.yahoo.com/quote/GOOG/history?ltr=1"

def download_web_data(google_url):
    response=request.urlopen(google_url)
    text=response.read()
    text_string=str(text)
    lines=text_string.split("\\n")
    filename= r'googleurl.txt'
    f=open(filename,"w")
    for x in lines:
        f.write(x +"\n")
    f.close()

download_web_data(google_url)