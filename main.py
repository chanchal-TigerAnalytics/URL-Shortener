from url_package import getShortURL, getLongURL

if __name__ == "__main__":
    url = 'https://www.codezax.com/'

    # generates the shortURL from url
    short = getShortURL(url, 'home')
    print("Short URL: ", short)

    # fetch the long url from short url   
    long = getLongURL(short)
    print(long)