import random

restaraunts = ["Hai Hong","Vietnam","Asian Noddle House","Little Thai","Oishi Bowl",
"Koko's","The Nines","Apollo's","Jack's","Cafe Pacfic","Subway","Plum Tree","Tango Chicken"
,"Miyake","Four Seasons"]
selection = random.randint(0,len(restaraunts)-1)
print restaraunts[selection]
