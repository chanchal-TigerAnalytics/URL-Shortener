from url_package import isShortURLPresent, getShortURL, getLongURL, showDatabase, updateLongURL

if __name__ == "__main__":
    fullURL = "https://www.fb.com/"
    
    #get the shortURL from fullURL
    short = getShortURL(fullURL, 'fb')
    print(short)
    
    # get the longURL from corresponding shortURL
    long = getLongURL(short)
    print(long)
    
    
    #update the longURL
    short = updateLongURL(short, "https://www.facebook.com/")
    
    #get the newLong URL
    long = getLongURL(short)
    print(long)
    
    # requests for database (username, password)
    # only admin can see the database
    showDatabase('chanchal', 'chanchal@123')
    
    
    
    
    
    
    
    