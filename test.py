import openpyxl
import random
import time
from random import *
dsociety = []
dsocnames = []
names = []
dognames = []
catnames = []
catspecies = []
csociety = []
wsociety = []
wildnames = []
wildbreeds = []
wildbreedsa = []
wildspecies = []
allpets = []
itemlist = [['ball',1,10],['chewy',1,10],['rose',20,1],['comb',20,20]]
items = ['ball','chewy','rose','comb']
wildmatchup= {}
book = openpyxl.load_workbook('dog.xlsx')
sheet = book['save']
catspecie = book['cats']
cats = catspecie['A']
inventoryraw = book['inventory']
inventory = []
inventorynames = []
wildspecie = book['wild']
cells = sheet
petlist = []
def load():
    w = 0
    for c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 in wildspecie:
        w += 1
        if w < 11:
            smiley = [c2.value,c3.value,c4.value,c5.value,c6.value,c7.value,c8.value,c9.value,c10.value]
            wildspecies.append(c1.value)
            allpets.append(c1.value)
            wildbreedsa.append(smiley)
    allpets.append('cat')
    allpets.append('dog')
    for x in range(0,len(wildbreedsa)):
        k = []
        for y in range(0,len(wildbreedsa[x])):
            if wildbreedsa[x][y] != 'none':
                k.append(wildbreedsa[x][y])
        wildbreeds.append(k)
    w = 0
    for c1,c2,c3 in inventoryraw:
        a = [c1.value,c2.value,c3.value]
        if 'none' not in a:
            inventory.append(a)
        if 'money' not in a and 'xp' not in a:
            inventorynames.append(a[1])
    w = 0
    for c1 in cats:
        w += 1
        if w > 38:
           pass
        else:
            catspecies.append(c1.value)
        w = -1
    for c1,c2,c3,c4,c5,c6,c7,c8,c9 in cells:
            c = [c1.value,c2.value,c3.value,c4.value,c5.value,c6.value,c7.value,c8.value,c9.value]
            if None not in c and 'Name' not in c:
                petlist.append(c)
                names.append(petlist[w][0])
def save():
    sheet.delete_rows(1,1000)
    sheet.append(['Name','Gender','Species','Breed','Speed','Intelligence','Charisma','Hunger','Thirst'])
    for x in petlist:
        sheet.append(x)

    inventoryraw.delete_rows(1,1000)
    for x in inventory:
        inventoryraw.append(x)
    book.save('dog.xlsx')
def dog_gen():
    global specieslist
    specieslist = ['Chihuahua', 'Pomeranian', 'Maltese', 'Toy Fox Terrier',\
        'Yorkshire Terrier', 'Papillon', 'Miniature Pinscher', 'Italian Greyhound', \
        'Pekingese', 'Silky Terrier', 'English Toy Spaniel', 'Norwich Terrier', 'Norfolk Terrier',\
        'Russell Terrier', 'Tibetan Spaniel', 'Shih Tzu', 'Schipperke', 'Miniature Schnauzer',\
        'Beagle', 'Bichons Frise', 'Cavalier King Charles Spaniel', 'Pug', 'Shetland Sheepdog',\
        'Scottish Terrier', 'Pembroke Welsh Corgi', 'Miniature Bull Terrier', 'Shiba Inu', \
        'Sealyham Terrier', 'Dachshund', 'Tibetan Terrier', 'American Eskimo Dog', 'Miniature American Shepherd',\
        'German Pinscher', 'Polish Lowland Sheepdog', 'Standard Schnauzer', 'Border Collie', 'Bearded Collie', 'Bulldog',\
        'Setter (Irish Red and White)', 'Basset Hound', 'Siberian Husky', 'Samoyed', 'Australian Shepherd', 'Dalmatian',\
        'Retriever (Nova Scotia Duck Tolling)', 'Bull Terrier', 'Pointer (German Wirehaired)', 'Pointer (German Shorthaired)',\
        'Pointer', 'Poodle', 'American Foxhound', 'Collie', 'Greyhound', 'Retriever (Flat-Coated)', 'Setter (Gordon)', \
        'Retriever (Golden)', 'Setter (Irish)', 'Boxer', 'Giant Schnauzer', 'Retriever (Chesapeake Bay)', 'Retriever (Labrador)', \
        'Setter (English)', 'German Shepherd Dog', 'Retriever (Curly-Coated)', 'Old English Sheepdog', 'Weimaraner', 'Rhodesian Ridgeback',\
        'Alaskan Malamute', 'Black and Tan Coonhound', 'Doberman Pinscher', 'Bernese Mountain Dog', 'Akita', 'Rottweiler', 'Irish Wolfhound', \
        'Tibetan Mastiff', 'Greater Swiss Mountain Dog', 'Anatolian Shepherd Dog', 'Neapolitan Mastiff', 'Newfoundland', 'St. Bernard', 'Mastiff']
    galname = ['Allie','Rose','Lucy','Mary','Susan','Lily','Emma','Liv','Sophia','Isabella',\
        'Ava','Mia','Emily','Abigail','Maddie','Charlotte','Harper','Sofia','Avery','Liz','Evelyn',\
        'Ella','Chloe','Victoria','Aubrey','Grace','Zoey','Natalie','Addie','Brooklyn','Hannah','Layla',\
        'Scarlet','Aria','Samantha','Anna','Ariana','Savannah','Gabriella','Claire','Sadie','Riley']
    guyname =['Liam','Noah','William','James','Logan','Ben','Elijah','Elisha','Jacob','Michael',\
        'Alex','Ethan','Daniel','Matt','Aidan','Henry','Jack','Sam','David','Carter','Jayden','John',\
        'Owen','Dylan','Luke','Gabriel','Tony','Isaac','Greyson','Jack','Julian','Levi','Chris','Josh',\
        'Andrew','Mateo','Ryan','Jason','Nathan','Aaron','Isaiah','Tom','Caleb','Josiah','Christian','Hunter']
    gender = ['male','female']
    print('You can adopt:')
    for x in range(0,randint(0,20)):
        k = choice(gender)
        r = choice(specieslist)

        if k == 'male':
            l = choice(guyname)
            print('%s: a %s %s(a dog)' %(l,k,r))
        else:
            l = choice(galname)
            print('%s: a %s %s(a dog)' %(l,k,r))
        m = [l,k,r]
        dsociety.append(m)
        dognames.append(l)
    print('Or you can give away:')
    w = -1
    for x in petlist:
        w+=1
        if x[2] == 'dog':
            print(petlist[w][0])
def newdog(name):
    if name in dognames:
        for x in dsociety:
            if x[0] == name:
                gender = x[1]
                breed = x[2]
                break
        ndog = [name,gender,'dog',breed,randint(10,100),randint(100,1000),randint(10,150),0,0]
        petlist.append(ndog)
        names.append(name)
        ptint(petlist)
def cat_gen():
    galname = ['Allie','Rose','Lucy','Mary','Susan','Lily','Emma','Liv','Sophia','Isabella',\
        'Ava','Mia','Emily','Abigail','Maddie','Charlotte','Harper','Sofia','Avery','Liz','Evelyn',\
        'Ella','Chloe','Victoria','Aubrey','Grace','Zoey','Natalie','Addie','Brooklyn','Hannah','Layla',\
        'Scarlet','Aria','Samantha','Anna','Ariana','Savannah','Gabriella','Claire','Sadie','Riley']
    guyname =['Liam','Noah','William','James','Logan','Ben','Elijah','Elisha','Jacob','Michael',\
        'Alex','Ethan','Daniel','Matt','Aidan','Henry','Jack','Sam','David','Carter','Jayden','John',\
        'Owen','Dylan','Luke','Gabriel','Tony','Isaac','Greyson','Jack','Julian','Levi','Chris','Josh',\
        'Andrew','Mateo','Ryan','Jason','Nathan','Aaron','Isaiah','Tom','Caleb','Josiah','Christian','Hunter']
    gender = ['male','female']
    print('You can adopt:')
    for x in range(0,randint(0,20)):
        k = choice(gender)
        r = choice(catspecies)

        if k == 'male':
            l = choice(guyname)
            print('%s: a %s %s(a cat)' %(l,k,r))
        else:
            l = choice(galname)
            print('%s: a %s %s(a cat)' %(l,k,r))
        m = [l,k,r]
        csociety.append(m)
        catnames.append(l)
    print('Or you can give away:')
    w = -1
    for x in petlist:
        w+=1
        if x[2] == 'cat':
            print(petlist[w][0])
def newcat(name):
    if name in catnames:
        for x in csociety:
            if x[0] == name:
                gender = x[1]
                breed = x[2]
                break
        names.append(name)
        ndog = [name,gender,'cat',breed,randint(10,100),randint(100,1000),randint(10,150),0,0]
        petlist.append(ndog)
def wild_gen():
    galname = ['Allie','Rose','Lucy','Mary','Susan','Lily','Emma','Liv','Sophia','Isabella',\
        'Ava','Mia','Emily','Abigail','Maddie','Charlotte','Harper','Sofia','Avery','Liz','Evelyn',\
        'Ella','Chloe','Victoria','Aubrey','Grace','Zoey','Natalie','Addie','Brooklyn','Hannah','Layla',\
        'Scarlet','Aria','Samantha','Anna','Ariana','Savannah','Gabriella','Claire','Sadie','Riley']
    guyname =['Liam','Noah','William','James','Logan','Ben','Elijah','Elisha','Jacob','Michael',\
        'Alex','Ethan','Daniel','Matt','Aidan','Henry','Jack','Sam','David','Carter','Jayden','John',\
        'Owen','Dylan','Luke','Gabriel','Tony','Isaac','Greyson','Jack','Julian','Levi','Chris','Josh',\
        'Andrew','Mateo','Ryan','Jason','Nathan','Aaron','Isaiah','Tom','Caleb','Josiah','Christian','Hunter']
    gender = ['male','female']
    print('You can adopt:')
    for x in range(0,randint(0,20)):
        n = randint(0,9)
        k = choice(gender)
        r = choice(wildbreeds[n])

        if k == 'male':
            l = choice(guyname)
            print('%s: a %s %s(a %s)' %(l,k,r,wildspecies[n]))
        else:
            l = choice(galname)
            print('%s: a %s %s(a %s)' %(l,k,r,wildspecies[n]))
        m = [l,k,r,wildspecies[n]]
        wsociety.append(m)
        wildnames.append(l)
    print('Or you can give away:')
    w = -1
    for x in petlist:
        w+=1
        if x[2] in wildspecies:
            print(petlist[w][0])
def new_wild(name):
        if name in wildnames:
            for x in wsociety:
                if x[0] == name:
                    gender = x[1]
                    breed = x[2]
                    species = x[3]
                    ndog = [name,gender,species,breed,randint(10,100),randint(100,1000),randint(10,150),0,0]
                    petlist.append(ndog)
                    names.append(name)
                    break
def rename(past,new):
    w = -1
    for x in range(0,len(petlist)):
        w+=1
        if petlist[x][0] == past:
            k = petlist[x]
            del petlist[x]
            k[0] = new
            petlist.insert(x,k)   
            break
def giveaway(name):
    for x in range(0,len(petlist)):
        if petlist[x][0] == name:
            del petlist[x]
    for x in range(0,len(names)):
        if names[x] == name:
            del names[x]
def showstats(name):
    a = ''
    for x in range(0,len(petlist)):
        if petlist[x][0] == name:
            a = petlist[x]
            break
    if bool(a) == True:
        print('name:%s'% name)
        print('gender:%s'% a[1])
        print('species:%s'% a[2])
        print('breed:%s'% a[3])
        print('speed:%s'% a[4])
        print('intelligence:%s' % a[5])
        print('charisma:%s'% a[6])
        print('hunger:%s'% a[7])
        print('thirst:%s'% a[8])
def feed(name):
    if name in names:
        for x in range(0,len(petlist)):
            if name == petlist[x][0]:
                petlist[x][7] = 100
def water(name):
    if name in names:
        for x in range(0,len(petlist)):
            if name == petlist[x][0]:
                petlist[x][8] = 100
def buy(item):
    if item not in inventorynames:
        for x in range(0,len(itemlist)):
            if itemlist[x][0] == item:
                inventory.append([item,1,itemlist[x][2]])
                inventorynames.append(item)
                inventory[0][1]-= itemlist[x][1]
    else:
        for x in range(0,len(itemlist)):
            if itemlist[x][0] == item:
                price = itemlist[x][1]
                uses = itemlist[x][2]
                break
        for x in range(0,len(inventory)):
            if inventory[x][0] == item:
                inventory[x][1] = inventory[x][1]+1
                inventory[x][2] += uses
                inventory[0][1] =inventory[0][1]-price
                break
def game():
    import random
    n = random.randint(1, 99)
    guess = int(input("Enter an integer from 1 to 99: "))
    while n != "guess":
        print()
        if guess < n:
            print("Go higher")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess > n:
            print ("Go lower")
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            print ("you guessed it!")
            inventory[0][1]+= 100
            break      
def custom_pet():
    species = ''
    breed = ''
    gender = ''
    while species not in allpets:
        species = input('Choose a species.')
    if species == 'dog':
        while breed not in specieslist:
            breed = input('Choose a dog breed.')
    elif species == 'cat':
        while breed not in catspecies:
            breed = input('Choose a cat breed.')
    elif species == 'tiger':
        while breed not in wildbreeds[0]:
            breed = input('Choose a tiger breed.')
    elif species == 'lion':
        while breed not in wildbreeds[1]:
            breed = input('Choose a lion breed.')
    elif species == 'wild dog':
        while breed not in wildbreeds[2]:
            breed = input('Choose a wild dog breed.')
    elif species == 'fox':
        while breed not in wildbreeds[3]:
            breed = input('Choose a fox breed.')
    elif species == 'bear':
        while breed not in wildbreeds[4]:
            breed = input('Choose a bear breed.')   
    elif species == 'wild cat':
        while breed not in wildbreeds[5]:
            breed = input('Choose a wild cat breed.') 
    elif species == 'deer':
        breed = 'deer'
    elif species == 'ibex':
        breed = 'ibex'
    elif species == 'rhinoceros':
        breed = 'rhinoceros'
    elif species == 'buffalo':
        while breed not in wildbreeds[8]:
            breed = input('Choose a buffalo breed.')   
    while gender not in ['male','female']:
        gender = input('Choose a gender.(Male or female)')
    name = input('Name it.')
    petlist.append([name,gender,species,breed,randint(10,100),randint(100,1000),randint(10,150),0,0])
    names.append(name)
load()

while True:
    r = input('')
    g = r.rsplit()

    if len(g) == 4:
        if g[0] == 'go' and g[1] =='to' and g[2] == 'Dog' and g[3] == 'Society':
            dog_gen()
        elif g[0] == 'go' and g[1] =='to' and g[2] == 'Cat' and g[3] == 'Society':
            cat_gen()
        elif g[0] == 'go' and g[1] =='to' and g[2] == 'Wild' and g[3] == 'Society':
            wildnames = []
            wsociety = []
            wild_gen()
    elif len(g) == 3:
        if g[0] == 'adopt' and g[1] =='dog'and g[2] in dognames:
            newdog(g[2])
        elif g[0] == 'adopt' and g[1] =='cat'and g[2] in catnames:
            newcat(g[2])
        elif g[0] == 'adopt' and g[1] == 'wild' and g[2] in wildnames:
            print('Finne!')
            new_wild(g[2])
        elif g[0] == 'name' and g[1] in names:
            rename(g[1],g[2])
        elif g[0] == 'give'and g[1] == 'away' and g[2] in names:
            print('OK!')
            giveaway(g[2])
    elif len(g) == 2:
        if g[0] == 'show' and g[1] in names:
            showstats(g[1])
        elif g[0] == 'feed' and g[1] in names:
            feed(g[1])
        elif g[0] == 'show' and g[1] == 'inventory':
            print('Name:Count:Uses')
            for x in inventory:
                print('%s:%s:%s'%(x[0],x[1],x[2]))
        elif g[0] == 'show' and g[1] == 'pets':
            for x in names:
                print(x)
        elif g[0] == 'water' and g[1] in names:
            water(g[1])
        elif g[0] == 'buy'and g[1] in items:
            buy(g[1])
        elif g[0] == 'earn' and g[1] == 'money':
            game()
            print('Done!')
        elif r == 'new pet':
            custom_pet()
    elif len(g) == 1:
        if g[0] == 'save':
            save()
        elif g[0] == 'quit':
            quit()