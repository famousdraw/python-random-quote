import random
def primary():
    last=13
    rnd=random.randint(0,last)
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    #quotes=''.join(quotes)
    #quotes=quotes.strip('\n')
    f.close()


    print(quotes[rnd])

if __name__== "__main__":
  primary()
