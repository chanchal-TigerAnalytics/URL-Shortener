import random
import string
import pickle

dbname = 'userdatabase.pkl'

def getShortURL(longURL):
    """
        For the given longURL, it returns the Short URL.
    """

    size = random.randint(5,8)
    chars = string.ascii_lowercase + string.digits;

    shortURL = "".join([random.choice(chars) for i in range(size)])
    
    # load the database from 'user_database.pkl'
    DB = {}
    with open(dbname, 'rb') as dbfile:
        try:
            DB = pickle.load(dbfile)
        except:
            pass

    # if this shortURL is already present in DB
    # call this function again
    if shortURL in DB:
        return getShortURL(longURL)

    # otherwise store this shortURL and corresponding longURL to the database
    DB[shortURL] = longURL

    # update the database
    with open(dbname, 'wb') as dbfile:
        pickle.dump(DB, dbfile)
    # formatted shortURL
    res = "ckm.in/" + shortURL
    return res


def getLongURL(shortURL):
    """
        given a short URL, it returns the long URL if exists,
        return "short URL doesn't exists." otherwise.
    """
    key = shortURL.split('/')[-1]
    
    #load database
    DB = {}
    with open(dbname, 'rb') as dbfile:
        try:
            DB = pickle.load(dbfile)
        except:
            pass
        
    # Return longURL if shortURL exits in database, otherwise return '
    try:
        return DB[key]
    except KeyError:
        return "short URL doesn't exists."