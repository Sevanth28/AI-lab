locA="Dirty"
locB="Dirty"
loc=1
dir="left"
print("Starting form left :")
while loc:
    if(dir=="left"):
        if(locA=="Dirty"):
            print("clean A")
            locA="Clean"
            dir="right"
            print("Move right")
        if(locA=="Clean" and locB=="Clean"):
            loc=0
    elif(dir=="right"):
        if(locB=="Dirty"):
            print("clean B")
            locB="Clean"
            dir="left"
            print("Move left")
        if(locA=="Clean" and locB=="Clean"):
             loc=0
print("A and B cleaned")
