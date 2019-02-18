import sys
import calendar

viewCalendar = lambda yy, mm: print("\n\n Calendar > \n %s\n" % calendar.month(yy, mm))

while True:
    if str(input("[+] Start [Y/N]? ")).strip().lower() == "y":
        try:
            viewCalendar(int(input("\nYear: ")), int(input("Month: ")))
        except IndexError:
            print(" --> Try Again! With valid numbers!\n")
    else:
        print("\nSee you soon! :D")
        sys.exit(0)
