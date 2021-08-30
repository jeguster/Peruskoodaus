import stdnum.fi.hetu

import hetutarkistus2

def main():
    while True:
        hetu = input("Anna HETU: ")
        if stdnum.fi.hetu.is_valid(hetu):
            print("Oikeanlainen HETU")
            print(hetutarkistus2.sukupuoli(hetu))
            print("Syntymäpäivä:", hetutarkistus2.syntymapaiva(hetu))
            print("ikä", hetutarkistus2.ika(hetu))
            break
        else:
            print("vääränlainen HETU")

if __name__ == '__main__':
    main()