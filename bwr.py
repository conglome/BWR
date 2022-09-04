list = ["fuck"] #here add all of the bad words you can find

inp = input("Enter sentence : ")

for x in list:
    if (x in inp):
        print(inp.replace(x, " [REDACTED] "))
