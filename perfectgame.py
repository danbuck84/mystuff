print('How to pick the perfect VideoGame!')
brain = str(input('Do you want to avoid using much of your brain (Y/N)? '))
if brain == 'Y':
    reflex = str(input('How are your reflexes (UNREAL/AVERAGE)? '))
    if reflex == 'UNREAL':
        drugs = str(input('Are you on drugs (Y/N)? '))
        if drugs == 'Y':
            print('The best game for you is REZ.')
        elif drugs == 'N':
            feel = str(input('Do you want to feel like you are (Y/N)? '))
            if feel == 'Y':
                print('The best game for you is GEOMETRY WARS 2.')
            elif feel == 'N':
                timing = str(input('How is your timing (SUPERB/AVERAGE)? '))
                if timing == 'SUPERB':
                    rockOut = str(input('You want to rock out (Y/N)? '))
                    if rockOut == 'Y':
                        print('The best game for you is ROCKBAND 3.')
                    elif rockOut == 'N':
                        print('The best game for you is IKARUGA.')
                    else:
                        print("Dude... You can't even follow simple rules. Shame on you!")
                elif timing == 'AVERAGE':
                    twoButtons = str(input('Are 2 buttons too many for you (Y/N)? '))
                    if twoButtons == 'Y':
                        print('The best game for you is MR PACMAN.')
                    elif twoButtons == 'N':
                        print('The best game for you is SUPER PUNCH OUT.')
                    else:
                        print("Dude... You can't even follow simple rules. Shame on you!")
                else:
                    print("Dude... You can't even follow simple rules. Shame on you!")
            else:
                print("Dude... You can't even follow simple rules. Shame on you!")
        else:
            print("Dude... You can't even follow simple rules. Shame on you!")
    elif reflex == 'AVERAGE':
        pointClick = str(input('Do you want to point and click click click click... (Y/N)? '))
        if pointClick == 'Y':
            week = str(input('Do you plan on playing for the next week straight (Y/N)? '))
            if week == 'Y':
                print('The best game for you is WORLD OF WARCRAFT.')
            elif week == 'N':
                print('The best game for you is DIABLO II.')
            else:
                print("Dude... You can't even follow simple rules. Shame on you!")
        elif pointClick == 'N':
            hardest = str(input('Do you want the hardest game ever (Y/N)? '))
            if hardest == 'Y':
                print('The best game for you is DEVIL MAY CRY 3.')
            elif hardest == 'N':
                print('The best game for you is SUPER MONKEY BALL.')
            else:
                print("Dude... You can't even follow simple rules. Shame on you!")
        else:
            print("Dude... You can't even follow simple rules. Shame on you!")
elif brain == 'N':
    creativity = str(input('Maximum Creativity (Y/N)? '))
    if creativity == 'Y':
        print('The best game for you is MINECRAFT.')
    elif creativity == 'N':
        puzzles = str(input('Do you want to solve some puzzles (Y/N)? '))
        if puzzles == 'Y':
            storyline = str(input('Do you feel the need for a storyline as well (Y/N)? '))
            if storyline == 'Y':
                edwardGorey = str(input('Are you an Edward Gorey fan (Y/N)? '))
                if edwardGorey == 'Y':
                    print('The best game for you is LIMBO.')
                elif edwardGorey == 'N':
                    japaneseAwesomeness = str(input('Looking for crazy Japanese awesomeness (Y/N)? '))
                    if japaneseAwesomeness == 'Y':
                        print('The best game for you is KATAMARI DAMACY.')
                    elif japaneseAwesomeness == 'N':
                        shinyOrIndi = str(input('Do you want shiny textures or indi magic (SHINY/INDI)? '))
                        if shinyOrIndi == 'SHINY':
                            print('The best game for you is PORTAL 2.')
                        elif shinyOrIndi == 'INDI':
                            print('The best game for you is BRAID.')
                        else:
                            print("Dude... You can't even follow simple rules. Shame on you!")
                    else:
                        print("Dude... You can't even follow simple rules. Shame on you!")
                else:
                    print("Dude... You can't even follow simple rules. Shame on you!")
            elif storyline == 'N':
                oldschool = str(input('Kick it oldschool (Y/N)? '))
                if oldschool == 'Y':
                    print('The best game for you is TETRIS.')
                elif oldschool == 'N':
                    print('The best game for you is LUMINES.')
                else:
                    print("Dude... You can't even follow simple rules. Shame on you!")
            else:
                print("Dude... You can't even follow simple rules. Shame on you!")
        elif puzzles == 'N':
            simulations = str(input('Do you enjoy simulations (Y/N)? '))
            if simulations == 'Y':
                inCharge = str(input('Do you want to be in charge of a life or an entire city (LIFE/CITY)? '))
                if inCharge == 'LIFE':
                    print('The best game for you is THE SIMS 3.')
                elif inCharge == 'CITY':
                    print('The best game for you is SIM CITY 2000.')
                else:
                    print("Dude... You can't even follow simple rules. Shame on you!")
            elif simulations == 'N':
                localPlayers = str(input('Do you have multiple local players (Y/N)? '))
                if localPlayers == 'Y':
                    buttonMashable = str(input('Button mashable (Y/N)? '))
                    if buttonMashable == 'Y':
                        violence = str(input('Does realistic violence upset you (Y/N)? '))
                        if violence == 'Y':
                            print('The best game for you is SUPER SMASH BROS. MELEE.')
                        elif violence == 'N':
                            weapons = str(input('Do you like big-ass weapons (Y/N)? '))
                            if weapons == 'Y':
                                print('The best game for you is SOULCALIBUR.')
                            elif weapons == 'N':
                                spine = str(input("Do you want to tear out your opponent's spine (Y/N)? "))
                                if spine == 'Y':
                                    print('The best game for you is MORTAL KOMBAT DECEPTION.')
                                elif spine == 'N':
                                    print('The best game for you is SUPER STREET FIGHTER IV.')
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            else:
                                print("Dude... You can't even follow simple rules. Shame on you!")
                        else:
                            print("Dude... You can't even follow simple rules. Shame on you!")
                    elif buttonMashable == 'N':
                        jerseys = str(input('Do you own any official team jerseys (Y/N)? '))
                        if jerseys == 'Y':
                            print('The best game for you is any EA SPORTS game.')
                        elif jerseys == 'N':
                            squealingTires = str(input('Does the sound of squealing tires excite you (Y/N)? '))
                            if squealingTires == 'Y':
                                racingReality = str(input('Should racing games be based in reality (Y/N)? '))
                                if racingReality == 'Y':
                                    badass = str(input('You want to be a badass (Y/N)? '))
                                    if badass == 'Y':
                                        print('The best game for you is BURNOUT PARADISE.')
                                    elif badass == 'N':
                                        trackType = str(input('Rally or Track (RALLY/TRACK)? '))
                                        if trackType == 'RALLY':
                                            print('The best game for you is SEGA RALLY CHAMPIONSHIP.')
                                        elif trackType == 'TRACK':
                                            print('The best game for you is GRAN TURISMO 3 A-SPEC.')
                                        else:
                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                elif racingReality == 'N':
                                    speedShells = str(input('Super speed or turtle shells (SPEED/SHELLS)? '))
                                    if speedShells == 'SPEED':
                                        print('The best game for you is F-ZERO GTX.')
                                    elif speedShells == 'SHELLS':
                                        print('The best game for you is MARIO KART 64.')
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            elif squealingTires == 'N':
                                wrestling = str(input('Do you think professional wrestling is stupid (Y/N)? '))
                                if wrestling == 'Y':
                                    skatePutt = str(input('Skate or putt (SKATE/PUTT)? '))
                                    if skatePutt == 'SKATE':
                                        print("The best game for you is TONY HAWK'S PRO SKATER 3.")
                                    elif skatePutt == 'PUTT':
                                        print("The best game for you is HOT SHOT GOLF.")
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                elif wrestling == 'N':
                                    print("The best game for you is NO MERCY.")
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            else:
                                print("Dude... You can't even follow simple rules. Shame on you!")
                        else:
                            print("Dude... You can't even follow simple rules. Shame on you!")
                    else:
                        print("Dude... You can't even follow simple rules. Shame on you!")
                elif localPlayers == 'N':
                    anotherWorld = str(input('Do you want to lose yourself in another world (Y/N)? '))
                    if anotherWorld == 'Y':
                        levelUp = str(input('Do you yearn to level up your character (Y/N)? '))
                        if levelUp == 'Y':
                            tactician = str(input('Do you fancy yourself a tactician (Y/N)? '))
                            if tactician == 'Y':
                                mobileConsole = str(input('Mobile or console (MOBILE/CONSOLE)? '))
                                if mobileConsole == 'MOBILE':
                                    print('The best game for you is ADVANCE WARS.')
                                elif mobileConsole == 'CONSOLE':
                                    print('The best game for you is FINAL FANTASY TACTICS.')
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            elif tactician == 'N':
                                japanUsa = str(input('Do you want a game made in Japan or America (JAPAN/USA)? '))
                                if japanUsa == 'JAPAN':
                                    largeArmyBattles = str(input('Do you want some large-scale army battles (Y/N)? '))
                                    if largeArmyBattles == 'Y':
                                        print('The best game for you is SUIKODEN II.')
                                    elif largeArmyBattles == 'N':
                                        realTimeBattles = str(input('Looking for real-time battles (Y/N)? '))
                                        if realTimeBattles == 'Y':
                                            print('The best game for you is SECRET OF MANA.')
                                        elif realTimeBattles == 'N':
                                            funOfYourself = str(input('Are you capable of making fun of yourself (Y/N)? '))
                                            if funOfYourself == 'Y':
                                                print('The best game for you is EARTH BOUND.')
                                            elif funOfYourself == 'N':
                                                dragonFetish = str(input('Do you have a serious dragon fetish (Y/N)? '))
                                                if dragonFetish == 'Y':
                                                    print('The best game for you is DRAGON QUEST VIII.')
                                                elif dragonFetish == 'N':
                                                    greatestGame = str(input('Care to play possibly the greatest game of all time (Y/N)? '))
                                                    if greatestGame == 'Y':
                                                        print('The best game for you is CHRONO TRIGGER.')
                                                    elif greatestGame == 'N':
                                                        absCBT = str(input('Active Battle System or Conditional Turn-based Battle (ABS/CBT)? '))
                                                        if absCBT == 'ABS':
                                                            print('The best game for you is FINAL FANTASY VI.')
                                                        elif absCBT == 'CBT':
                                                            print('The best game for you is FINAL FANTASY X.')
                                                        else:
                                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                                    else:
                                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                                else:
                                                    print("Dude... You can't even follow simple rules. Shame on you!")
                                            else:
                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                        else:
                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                elif japanUsa == 'USA':
                                    lightsaber = str(input('Are you cool without getting to use a lightsaber (Y/N)? '))
                                    if lightsaber == 'Y':
                                        print('The best game for you is FALLOUT 2.')
                                    elif lightsaber == 'N':
                                        print('The best game for you is STAR WARS KNIGHTS OF THE OLD REPUBLIC.')
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            else:
                                print("Dude... You can't even follow simple rules. Shame on you!")
                        elif levelUp == 'N':
                            terrified = str(input('Do you like to be terrified (Y/N)? '))
                            if terrified == 'Y':
                                collectWeapons = str(input('Want to collect weapons but be too afraid to use any ammo (Y/N)? '))
                                if collectWeapons == 'Y':
                                    print('The best game for you is RESIDENT EVIL 4.')
                                elif collectWeapons == 'N':
                                    confusedAndHorrified = str(input('Do you want to be confused and horrified the entire time (Y/N)?'))
                                    if confusedAndHorrified == 'Y':
                                        print('The best game for you is SILENT HILL 2.')
                                    elif confusedAndHorrified == 'N':
                                        print('The best game for you is BIOSHOCK.')
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            elif terrified == 'N':
                                cleanJunky = str(input('Is adventure enough for you, or are you an action junky (CLEAN/JUNKY)? '))
                                if cleanJunky == 'CLEAN':
                                    actingPlot = str(input('Want some of the best acting and plot ever put into a game (Y/N)? '))
                                    if actingPlot == 'Y':
                                        print('The best game for you is GABRIEL KNIGHT: SINS OF THE FATHERS.')
                                    elif actingPlot == 'N':
                                        childish = str(input('More childish, or less (MORE/LESS)? '))
                                        if childish == 'MORE':
                                            farfetch = str(input('How far-fetched do you want to get (ABSURD/REGULAR)? '))
                                            if farfetch == 'ABSURD':
                                                print('The best game for you is DAY OF THE TENTACLE.')
                                            elif farfetch == 'REGULAR':
                                                print('The best game for you is THE SECRET OF MONKEY ISLAND.')
                                            else:
                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                        elif childish == 'LESS':
                                            print('The best game for you is GRIM FANDANGO.')
                                        else:
                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                elif cleanJunky == 'JUNKY':
                                    rpg = str(input('Do you want a little role playing with your action (Y/N)? '))
                                    if rpg == 'Y':
                                        disney = str(input('Do you have a fetish for any Disney characters (Y/N)? '))
                                        if disney == 'Y':
                                            print('The best game for you is KINGDOM HEARTS.')
                                        elif disney == 'N':
                                            outerSpace = str(input('What about outer-space (Y/N)? '))
                                            if outerSpace == 'Y':
                                                print('The best game for you is MASS EFFECT 2.')
                                            elif outerSpace == 'N':
                                                fps = str(input('Feel like throwing in some first person shooting (Y/N)? '))
                                                if fps == 'Y':
                                                    print('The best game for you is DEUS EX: HUMAN REVOLUTION.')
                                                elif fps == 'N':
                                                    platforming = str(input('How about some platforming (Y/N)? '))
                                                    if platforming == 'Y':
                                                        print('The best game for you is CASTELVANIA.')
                                                    elif platforming == 'N':
                                                        print('The best game for you is THE ELDER SCROLLS V: SKYRIM.')
                                                    else:
                                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                                else:
                                                    print("Dude... You can't even follow simple rules. Shame on you!")
                                            else:
                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                        else:
                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                    elif rpg == 'N':
                                        maleFemale = str(input('You want a female or male main character (FEMALE/MALE)? '))
                                        if maleFemale == 'FEMALE':
                                            aliensRelics = str(input('Alien conspiracy of lost relics (ALIENS/RELICS)? '))
                                            if aliensRelics == 'ALIENS':
                                                print('The best game for you is BEYOND GOOD & EVIL.')
                                            elif aliensRelics == 'RELICS':
                                                print('The best game for you is TOMB RAIDER: ANNIVERSARY.')
                                            else:
                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                        elif maleFemale == 'MALE':
                                            link = str(input('Link (LINK!/NOPE)? '))
                                            if link == 'LINK!':
                                                oldNew = str(input('Oldschool or Newschool (OLD/NEW)? '))
                                                if oldNew == 'OLD':
                                                    print('The best game for you is THE LEGEND OF ZELDA: A LINK TO THE PAST.')
                                                elif oldNew == 'NEW':
                                                    wiimote = str(input('Do you like gaming with a Wiimote (Y/N)? '))
                                                    if wiimote == 'Y':
                                                        print('The best game for you is THE LEGEND OF ZELDA: TWILIGHT PRINCESS.')
                                                    elif wiimote == 'N':
                                                        print('The best game for you is THE LEGEND OF ZELDA: THE WIND WAKER.')
                                                    else:
                                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                                else:
                                                    print("Dude... You can't even follow simple rules. Shame on you!")
                                            elif link == 'NOPE':
                                                japaneseStory = str(input('Do you want a beautifully crafted Japanese story (Y/N)? '))
                                                if japaneseStory == 'Y':
                                                    artStory = str(input('Do you lean more towards the art or the story (ART/STORY)? '))
                                                    if artStory == 'ART':
                                                        print('The best game for you is OKAMI HD.')
                                                    elif artStory == 'STORY':
                                                        print('The best game for you is ICO.')
                                                    else:
                                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                                elif japaneseStory == 'N':
                                                    openWorld = str(input('Open world (OPEN/CLOSED)? '))
                                                    if openWorld == 'OPEN':
                                                        assassinCriminalCowboy = str(input('Do you want to be an assassin, criminal or cowboy (ASSASSIN/CRIMINAL/COWBOY)? '))
                                                        if assassinCriminalCowboy == 'ASSASSIN':
                                                            print("The best game for you is ASSASSIN'S CREED II.")
                                                        elif assassinCriminalCowboy == 'CRIMINAL':
                                                            print('The best game for you is GRAND THEFT AUTO IV.')
                                                        elif assassinCriminalCowboy == 'COWBOY':
                                                            print('The best game for you is RED DEAD REDEMPTION.')
                                                        else:
                                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                                    elif openWorld == 'CLOSED':
                                                        rewardedStealth = str(input('Do you want stealth to be rewarded (Y/N)? '))
                                                        if rewardedStealth == 'Y':
                                                            batman = str(input('Are you Batman, or do you want to be (Y/N)? '))
                                                            if batman == 'Y':
                                                                print('The best game for you is BATMAN: ARKHAM CITY.')
                                                            elif batman == 'N':
                                                                print('The best game for you is METAL GEAR SOLID 3.')
                                                            else:
                                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                                        elif rewardedStealth == 'N':
                                                            simple = str(input('Keep things simple (Y/N)? '))
                                                            if simple == 'Y':
                                                                print('The best game for you is CASTLE CRASHERS.')
                                                            elif simple == 'N':
                                                                killGods = str(input('Do you want to kill gods (or things decidedly godlike) (Y/N)? '))
                                                                if killGods == 'Y':
                                                                    carnage = str(input('Do you enjoy brutal gratuitous carnage (Y/N)? '))
                                                                    if carnage == 'Y':
                                                                        print('The best game for you is GOD OF WAR.')
                                                                    elif carnage == 'N':
                                                                        print('The best game for you is SHADOW OF THE COLOSSUS.')
                                                                    else:
                                                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                                                elif killGods == 'N':
                                                                    wallsGround = str(input('Do you want to run on walls or keep it a little more grounded (WALLS/GROUND)? '))
                                                                    if wallsGround == 'WALLS':
                                                                        print('The best game for you is PRINCE OF PERSIA: THE SANDS OF TIME.')
                                                                    elif wallsGround == 'GROUND':
                                                                        print('The best game for you is UNCHARTED 2.')
                                                                    else:
                                                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                                                else:
                                                                    print("Dude... You can't even follow simple rules. Shame on you!")
                                                            else:
                                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                                        else:
                                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                                    else:
                                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                                else:
                                                    print("Dude... You can't even follow simple rules. Shame on you!")
                                            else:
                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                        else:
                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            else:
                                print("Dude... You can't even follow simple rules. Shame on you!")
                        else:
                            print("Dude... You can't even follow simple rules. Shame on you!")
                    elif anotherWorld == 'N':
                        facePlatform = str(input('Would you rather jump to platforms, or shoot someone in the face (PLATFORM/FACE)? '))
                        if facePlatform == 'PLATFORM':
                            shootPeople = str(input('Do you want to shoot people while jumping platforms (Y/N)? '))
                            if shootPeople == 'Y':
                                runAndGun = str(input('More run-and-gun, less platforming (Y/N)? '))
                                if runAndGun == 'Y':
                                    print('The best game for you is CONTRA III: THE ALIEN WARS.')
                                elif runAndGun == 'N':
                                    adventure = str(input('Add some adventure to your action/platformer (Y/N)? '))
                                    if adventure == 'Y':
                                        print('The best game for you is SUPER METROID.')
                                    elif adventure == 'N':
                                        print('The best game for you is MEGA-MAN 2.')
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            elif shootPeople == 'N':
                                mario = str(input('Do you have an affection for Italian plumbers (Y/N)? '))
                                if mario == 'Y':
                                    simpleMario = str(input('Do you want the controls kept as simple as possible (Y/N)? '))
                                    if simpleMario == 'Y':
                                        print('The best game for you is SUPER MARIO BROS. 3.')
                                    elif simpleMario == 'N':
                                        dimensions = str(input('Keep it 2D or break into a third dimension (2D/3D)? '))
                                        if dimensions == '2D':
                                            print('The best game for you is SUPER MARIO WORLD.')
                                        elif dimensions == '3D':
                                            throwback2D = str(input('Do you want some 2D throwback levels in the mix (Y/N)? '))
                                            if throwback2D == 'Y':
                                                print('The best game for you is SUPER MARIO 64.')
                                            elif throwback2D == 'N':
                                                print('The best game for you is SUPER MARIO GALAXY 2.')
                                            else:
                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                        else:
                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                elif mario == 'N':
                                    oldCartoons = str(input("Do you yearn for 1980's cartoons (Y/N)? "))
                                    if oldCartoons == 'Y':
                                        print("The best game for you is DISNEY'S DUCKTALES.")
                                    elif oldCartoons == 'N':
                                        underwater = str(input('Do you actually enjoy underwater levels (Y/N)? '))
                                        if underwater == 'Y':
                                            print('The best game for you is DONKEY KONG COUNTRY.')
                                        elif underwater == 'N':
                                            keepIndi = str(input('Want to keep it indi (Y/N)? '))
                                            if keepIndi == 'Y':
                                                print('The best game for you is SUPER MEAT BOY: ULTRA EDITION.')
                                            elif keepIndi == 'N':
                                                print('The best game for you is PSYCHONAUTS.')
                                            else:
                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                        else:
                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            else:
                                print("Dude... You can't even follow simple rules. Shame on you!")
                        elif facePlatform == 'FACE':
                            firstThird = str(input('First or third person view (1ST/3RD)? '))
                            if firstThird == '1ST':
                                singlePlayer = str(input('Are you looking for a single player game (Y/N)? '))
                                if singlePlayer == 'Y':
                                    keysMouse = str(input('Keyboard only or do you want to use a mouse as well (KEYS/MOUSE)? '))
                                    if keysMouse == 'KEYS':
                                        print('The best game for you is DOOM II.')
                                    elif keysMouse == 'MOUSE':
                                        print('The best game for you is HALF-LIFE 2.')
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                elif singlePlayer == 'N':
                                    respawn = str(input('Do you like games without a re-spawn (Y/N)? '))
                                    if respawn == 'Y':
                                        print('The best game for you is COUNTER-STRIKE.')
                                    elif respawn == 'N':
                                        ridiculous = str(input('Ridiculous non-stop action, rocket jumps, laser guns etc. (Y/N)? '))
                                        if ridiculous == 'Y':
                                            print('The best game for you is QUAKE III: ARENA.')
                                        elif ridiculous == 'N':
                                            strategy = str(input('Heavy reliance on team-play and strategy (Y/N)? '))
                                            if strategy == 'Y':
                                                print('The best game for you is TEAM FORTRESS 2.')
                                            elif strategy == 'N':
                                                noob = str(input('Do you like being called a n00b by 8 year olds (Y/N)? '))
                                                if noob == 'Y':
                                                    print('The best game for you is HALO 3.')
                                                elif noob == 'N':
                                                    zombies = str(input('Zombies (Y/N)? '))
                                                    if zombies == 'Y':
                                                        print('The best game for you is LEFT4DEAD 2.')
                                                    elif zombies == 'N':
                                                        print('The best game for you is CALL OF DUTY 4.')
                                                    else:
                                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                                else:
                                                    print("Dude... You can't even follow simple rules. Shame on you!")
                                            else:
                                                print("Dude... You can't even follow simple rules. Shame on you!")
                                        else:
                                            print("Dude... You can't even follow simple rules. Shame on you!")
                                    else:
                                        print("Dude... You can't even follow simple rules. Shame on you!")
                                else:
                                    print("Dude... You can't even follow simple rules. Shame on you!")
                            elif firstThird == '3RD':
                                print('The best game for you is GEARS OF WARD 2.')
                            else:
                                print("Dude... You can't even follow simple rules. Shame on you!")
                        else:
                            print("Dude... You can't even follow simple rules. Shame on you!")
                    else:
                        print("Dude... You can't even follow simple rules. Shame on you!")
                else:
                    print("Dude... You can't even follow simple rules. Shame on you!")
            else:
                print("Dude... You can't even follow simple rules. Shame on you!")
        else:
            print("Dude... You can't even follow simple rules. Shame on you!")
    else:
        print("Dude... You can't even follow simple rules. Shame on you!")
else:
    print("Dude... You can't even follow simple rules. Shame on you!")
