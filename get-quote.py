import random
def primary():
    print("Keep it logically awesome.")
    f = open("quotes.txt")
    quotes = f.readlines()
    last=len(quotes)
    rnd=random.randint(0,last)
    #quotes=''.join(quotes)

    #quotes=quotes.strip('\n')
    f.close()

    for i in range(5):
        if rnd+i>=len(quotes):
            #print(rnd+i)
            rnd-=len(quotes)+i     
        print(quotes[rnd+i].strip())

if __name__== "__main__":
  primary()
