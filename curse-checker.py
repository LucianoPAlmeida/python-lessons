import urllib
def read_text() : 
    quotes = open(r'movie_quotes.txt')
    contents = quotes.read()
    quotes.close()
    return contents 
def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    connection.close()
    return output
contents = read_text()
profanity = check_profanity(contents)
if "true" in profanity:
    print "What your mouth boy!"
else: 
    print "No profanity"
