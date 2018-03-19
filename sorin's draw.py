def draw(canvas):
    global interactions , addedInteractions, numberOfPlatforms , framecount,numberOfGoats,goats
    lv1background.update(canvas)
    platforms.draw(canvas)
    if not addedInteractions:
        for i in range(len(platforms.getCoords()) ):
            interaction = Interaction(player1, platforms.coords[i])
            interactions.append(interaction)
        addedInteractions = True
    for i in range(len(platforms.getCoords())):
        platforms.coords[i].p1 = Vector(platforms.coords[i].getp1().getP()[0],platforms.coords[i].getp1().getP()[1] + 1)
        platforms.coords[i].p2 = Vector(platforms.coords[i].getp2().getP()[0],platforms.coords[i].getp2().getP()[1] + 1)
        tempPlatform = Platform2(0)
        if platforms.coords[i].p1.y > 700:
            platforms.coords.pop(i)
            if i > 1:
                while not (abs(tempPlatform.getx1() -platforms.coords[i-1].getx1()) > platforms.DISTANCE*platforms.difficulty or \
                    abs(tempPlatform.getx2() - platforms.coords[i - 1].getx2()) > platforms.DISTANCE * platforms.difficulty):
                        tempPlatform = Platform2(0)
            platforms.coords.insert(i,tempPlatform)
            tempInteraction = Interaction(player1, tempPlatform)
        else:
            tempInteraction = Interaction(player1, platforms.coords[i])
        interactions.pop(i)
        interactions.insert(i,tempInteraction)
        if random.randint(0,1) > 0.5 and framecount %360 == 0 and numberOfGoats<3 and platforms.coords[i].p1.y < player1.pos.y: #numberOfPlatforms % 5 == 0 and not madeGoat
            makeGoat(platforms.coords[i])
            numberOfGoats+=1
            madeGoat = True
        #print("len monsters:",len(monsters))
        goatsToPop = []
        for j in range(len(goats)):
            print("len monsters:",len(goats))
            if platforms.coords[i] ==goats[j].platform:
                goats[j].pos = Vector(goats[j].pos.x,platforms.coords[i].p1.y-platforms.coords[i].thickness-goats[j].frameHeight/2)
                goats[j].update(canvas)
                if goats[j].isColliding(player1) and goats[j].harmsPlayer(player1):
                    player1.lifePoints -= 1
                    print("rekt")
                    goatsToPop.append(goats[j])
                    numberOfGoats -= 1
            #print("pos y:",monsters[j].pos.y)
            if goats[j].pos.y > 630:
                goatsToPop.append(goats[j])
                numberOfGoats-=1
        print("monsters to pop:",goatsToPop)
        for j in range(len(goatsToPop)):
            goats.remove(goatsToPop[j])
    framecount += 1


    for i in range(len(interactions)):
        if platforms.coords[i].covers(player1.pos):
            interactions[i].update()

    platforms.draw(canvas)

    player1.update(canvas)

