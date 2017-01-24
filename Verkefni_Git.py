#Davíð Bjarki Jónsson 24-01-17

#Liður 1

'''
tala1 = int(input("Sláðu inn fyrstu tölu: "))
tala2 = int(input("Sláðu inn næstu tölu: "))
print(tala1 + tala2, "er summan af tölunum")
print(tala1 * tala2, "er margfeldið af tölunum")
'''


#Liður 2

'''
nafn1 = input("Sláðu inn fornafn: ")
nafn2 = input("Sláðu inn eftirnafn: ")
print("Halló", nafn1, nafn2)
'''


#Liður 3

setning = input("Sláðu inn setningu: ")

capital = 0
lowcase = 0
lowhigh = 0

for x in range(len(setning)):
    if setning[x].isupper():
        capital += 1

    elif setning[x].islower():
        lowcase += 1

        if x>0:
            if setning[x-1].isupper():
                lowhigh += 1