def main():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    quotes=''.join(quotes)
    quotes=quotes.strip('\n')
    f.close()


    print(quotes)

if __name__== "__main__":
  main()
