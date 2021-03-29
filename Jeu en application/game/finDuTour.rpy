label actionsIA:
    $ chanceAttaqueBeige = renpy.random.randint(1, 4)
    $ chanceAttaqueBleue = renpy.random.randint(1, 4)
    $ chanceAttaqueGrise = renpy.random.randint(1, 4)
    $ chanceAttaqueJaune = renpy.random.randint(1, 4)
    $ chanceAttaqueOrange = renpy.random.randint(1, 4)
    $ chanceAttaqueRose = renpy.random.randint(1, 4)
    $ chanceAttaqueRouge = renpy.random.randint(1, 4)
    $ chanceAttaqueVerte = renpy.random.randint(1, 4)
    $ chanceAttaqueViolette = renpy.random.randint(1, 4)

    #possibilité region beige
    if regionBeigeActive == False and regionJauneActive == True:
        if armeeRegionBeige > armeeRegionJaune and chanceAttaqueBeige == 2:
            $ armeeRegionBeige = armeeRegionBeige - armeeRegionJaune
            $ armeeRegionJaune = 0
            $ regionJauneActive = False
            $ niveauRegionBeige += 1
            g "La région Jaune a été libéré par la région beige"
            nvl clear
    if regionBeigeActive == False and regionGriseActive == True:
        if armeeRegionBeige > armeeRegionGrise and chanceAttaqueBeige == 2:
            $ armeeRegionBeige = armeeRegionGrise - armeeRegionJaune
            $ armeeRegionGrise = 0
            $ regionGriseActive = False
            $ niveauRegionBeige += 1
            g "La région Cyan a été libéré par la région beige"
            nvl clear

    #possibilité region grise dans le code cyan en image
    if regionGriseActive == False and regionJauneActive == True:
        if armeeRegionGrise > armeeRegionJaune and chanceAttaqueGrise == 2:
            $ armeeRegionGrise = armeeRegionGrise - armeeRegionJaune
            $ armeeRegionJaune = 0
            $ regionJauneActive = False
            $ niveauRegionGrise += 1
            g "La région Jaune a été libéré par la région Cyan"
            nvl clear
    if regionGriseActive == False and regionBeigeActive == True:
        if armeeRegionGrise > armeeRegionBeige and chanceAttaqueGrise == 2:
            $ armeeRegionGrise = armeeRegionGrise - armeeRegionBeige
            $ armeeBeigeJaune = 0
            $ regionBeigeActive = False
            $ niveauRegionGrise += 1
            g "La région Beige a été libéré par la région Cyan"
            nvl clear
    if regionGriseActive == False and regionRoseActive == True:
        if armeeRegionGrise > armeeRegionRose and chanceAttaqueGrise == 2:
            $ armeeRegionGrise = armeeRegionGrise - armeeRegionRose
            $ armeeRegionRose = 0
            $ regionRoseActive = False
            $ niveauRegionGrise += 1
            g "La région Rose a été libéré par la région Cyan"
            nvl clear

    #possibilité region Jaune
    if regionJauneActive == False and regionBeigeActive == True:
        if armeeRegionJaune > armeeRegionBeige and chanceAttaqueJaune == 2:
            $ armeeRegionJaune = armeeRegionJaune - armeeRegionBeige
            $ armeeRegionBeige = 0
            $ regionBeigeActive = False
            $ niveauRegionJaune += 1
            g "La région Beige a été libéré par la région Jaune"
            nvl clear
    if regionJauneActive == False and regionBleueActive == True:
        if armeeRegionJaune > armeeRegionBleue and chanceAttaqueJaune == 2:
            $ armeeRegionJaune = armeeRegionJaune - armeeRegionBleue
            $ armeeRegionBleue = 0
            $ regionBleueActive = False
            $ niveauRegionJaune += 1
            g "La région Bleue a été libéré par la région Jaune"
            nvl clear
    if regionJauneActive == False and regionRoseActive == True:
        if armeeRegionJaune > armeeRegionRose and chanceAttaqueJaune == 2:
            $ armeeRegionJaune = armeeRegionJaune - armeeRegionRose
            $ armeeRegionRose = 0
            $ regionRoseActive = False
            $ niveauRegionJaune += 1
            g "La région Rose a été libéré par la région Jaune"
            nvl clear
    if regionJauneActive == False and regionGriseActive == True:
        if armeeRegionJaune > armeeRegionGrise and chanceAttaqueJaune == 2:
            $ armeeRegionJaune = armeeRegionJaune - armeeRegionGrise
            $ armeeRegionGrise = 0
            $ regionGriseActive = False
            $ niveauRegionJaune += 1
            g "La région Cyan a été libéré par la région Jaune"
            nvl clear

    #possibilité region Rose
    if regionRoseActive == False and regionGriseActive == True:
        if armeeRegionRose > armeeRegionGrise and chanceAttaqueRose == 2:
            $ armeeRegionRose = armeeRegionRose - armeeRegionGrise
            $ armeeRegionGrise = 0
            $ regionGriseActive = False
            $ niveauRegionRose += 1
            g "La région Cyan a été libéré par la région Rose"
            nvl clear
    if regionRoseActive == False and regionJauneActive == True:
        if armeeRegionRose > armeeRegionJaune and chanceAttaqueRose == 2:
            $ armeeRegionRose = armeeRegionRose - armeeRegionJaune
            $ armeeRegionJaune = 0
            $ regionJauneActive = False
            $ niveauRegionRose += 1
            g "La région Jaune a été libéré par la région Rose"
            nvl clear
    if regionRoseActive == False and regionBleueActive == True:
        if armeeRegionRose > armeeRegionBleue and chanceAttaqueRose == 2:
            $ armeeRegionRose = armeeRegionRose - armeeRegionBleue
            $ armeeRegionBleue = 0
            $ regionBleueActive = False
            $ niveauRegionRose += 1
            g "La région Bleue a été libéré par la région Rose"
            nvl clear
    if regionRoseActive == False and regionOrangeActive == True:
        if armeeRegionRose > armeeRegionOrange and chanceAttaqueRose == 2:
            $ armeeRegionRose = armeeRegionRose - armeeRegionOrange
            $ armeeRegionOrange = 0
            $ regionOrangeActive = False
            $ niveauRegionRose += 1
            g "La région Orange a été libéré par la région Rose"
            nvl clear
    #possibilité region Orange
    if regionOrangeActive == False and regionRoseActive == True:
        if armeeRegionOrange > armeeRegionRose and chanceAttaqueOrange == 2:
            $ armeeRegionOrange = armeeRegionOrange - armeeRegionRose
            $ armeeRegionRose = 0
            $ regionRoseActive = False
            $ niveauRegionOrange += 1
            g "La région Rose a été libéré par la région Orange"
            nvl clear
    if regionOrangeActive == False and regionBleueActive == True:
        if armeeRegionOrange > armeeRegionBleue and chanceAttaqueOrange == 2:
            $ armeeRegionOrange = armeeRegionOrange - armeeRegionBleue
            $ armeeRegionBleue = 0
            $ regionBleueActive = False
            $ niveauRegionOrange += 1
            g "La région Bleue a été libéré par la région Orange"
            nvl clear
    if regionOrangeActive == False and regionVioletteActive == True:
        if armeeRegionOrange > armeeRegionViolette and chanceAttaqueOrange == 2:
            $ armeeRegionOrange = armeeRegionOrange - armeeRegionViolette
            $ armeeRegionViolette = 0
            $ regionVioletteActive = False
            $ niveauRegionOrange += 1
            g "La région Violette a été libéré par la région Orange"
            nvl clear
    #possibilité region Violette
    if regionVioletteActive == False and regionOrangeActive == True:
        if armeeRegionViolette > armeeRegionOrange and chanceAttaqueViolette == 2:
            $ armeeRegionViolette = armeeRegionViolette - armeeRegionOrange
            $ armeeRegionOrange = 0
            $ regionOrangeActive = False
            $ niveauRegionViolette += 1
            g "La région Orange a été libéré par la région Violette"
            nvl clear
    #possibilité region Bleue
    if regionBleueActive == False and regionOrangeActive == True:
        if armeeRegionBleue > armeeRegionOrange and chanceAttaqueBleue == 2:
            $ armeeRegionBleue = armeeRegionBleue - armeeRegionOrange
            $ armeeRegionOrange = 0
            $ regionOrangeActive = False
            $ niveauRegionBleue += 1
            g "La région Orange a été libéré par la région Bleue"
            nvl clear
    if regionBleueActive == False and regionRoseActive == True:
        if armeeRegionBleue > armeeRegionRose and chanceAttaqueBleue == 2:
            $ armeeRegionBleue = armeeRegionBleue - armeeRegionRose
            $ armeeRegionRose = 0
            $ regionRoseActive = False
            $ niveauRegionBleue += 1
            g "La région Rose a été libéré par la région Bleue"
            nvl clear
    if regionBleueActive == False and regionJauneActive == True:
        if armeeRegionBleue > armeeRegionJaune and chanceAttaqueBleue == 2:
            $ armeeRegionBleue = armeeRegionBleue - armeeRegionJaune
            $ armeeRegionJaune = 0
            $ regionJauneActive = False
            $ niveauRegionBleue += 1
            g "La région Jaune a été libéré par la région Bleue"
            nvl clear
    if regionBleueActive == False and regionRougeActive == True:
        if armeeRegionBleue > armeeRegionRouge and chanceAttaqueBleue == 2:
            $ armeeRegionBleue = armeeRegionBleue - armeeRegionRouge
            $ armeeRegionRouge = 0
            $ regionRougeActive = False
            $ niveauRegionBleue += 1
            g "La région Rouge a été libéré par la région Bleue"
            nvl clear
    if regionBleueActive == False and regionVerteActive == True:
        if armeeRegionBleue > armeeRegionVerte and chanceAttaqueBleue == 2:
            $ armeeRegionBleue = armeeRegionBleue - armeeRegionVerte
            $ armeeRegionVerte = 0
            $ regionVerteActive = False
            $ niveauRegionBleue += 1
            g "La région Verte a été libéré par la région Bleue"
            nvl clear
    #possibilité region Rouge
    if regionRougeActive == False and regionBleueActive == True:
        if armeeRegionRouge > armeeRegionBleue and chanceAttaqueRouge == 2:
            $ armeeRegionRouge = armeeRegionRouge - armeeRegionBleue
            $ armeeRegionBleue = 0
            $ regionBleueActive = False
            $ niveauRegionRouge += 1
            g "La région Bleue a été libéré par la région Rouge"
            nvl clear
    if regionRougeActive == False and regionVerteActive == True:
        if armeeRegionRouge > armeeRegionVerte and chanceAttaqueRouge == 2:
            $ armeeRegionRouge = armeeRegionRouge - armeeRegionVerte
            $ armeeRegionVerte = 0
            $ regionVerteActive = False
            $ niveauRegionRouge += 1
            g "La région Verte a été libéré par la région Rouge"
            nvl clear
    #possibilité region Verte
    if regionVerteActive == False and regionBleueActive == True:
        if armeeRegionVerte > armeeRegionBleue and chanceAttaqueVerte == 2:
            $ armeeRegionVerte = armeeRegionVerte - armeeRegionBleue
            $ armeeRegionBleue = 0
            $ regionBleueActive = False
            $ niveauRegionVerte += 1
            g "La région Bleue a été libéré par la région Verte"
            nvl clear
    if regionVerteActive == False and regionRougeActive == True:
        if armeeRegionVerte > armeeRegionRouge and chanceAttaqueVerte == 2:
            $ armeeRegionVerte = armeeRegionVerte - armeeRegionRouge
            $ armeeRegionRouge = 0
            $ regionRougeActive = False
            $ niveauRegionVerte += 1
            g "La région Rouge a été libéré par la région Verte"
            nvl clear
    jump victoire




label victoire:
    $ jour +=1
    if jour == 30:
        default nombreTerritoire = 0
        if regionBeigeActive == True:
            $ nombreTerritoire += 1

        if regionBleueActive == True:
            $ nombreTerritoire += 1

        if regionGriseActive == True:
            $ nombreTerritoire += 1

        if regionJauneActive == True:
            $ nombreTerritoire += 1

        if regionOrangeActive == True:
            $ nombreTerritoire += 1

        if regionRoseActive == True:
            $ nombreTerritoire += 1

        if regionRougeActive == True:
            $ nombreTerritoire += 1

        if regionVerteActive == True:
            $ nombreTerritoire += 1

        if regionVioletteActive == True:
            $ nombreTerritoire += 1

        if nombreTerritoire < 5:
            g "Vous avez échoué vous n'avez pas réussi à conquérir assez de territoires ..."
            g "Retentez votre chance!"
        elif nombreTerritoire == 5:
            g "Félicitations vous avez gagné !"
            g "Vous avez obtenu le rang D"
        elif nombreTerritoire == 6:
            g "Félicitations vous avez gagné !"
            g "Vous avez obtenu le rang C"
        elif nombreTerritoire == 7:
            g "Félicitations vous avez gagné !"
            g "Vous avez obtenu le rang B"
        elif nombreTerritoire == 8:
            g "Félicitations vous avez gagné !"
            g "Vous avez obtenu le rang A"
        elif nombreTerritoire == 9:
            g "Félicitations vous avez gagné !"
            g "Vous avez obtenu le rang S"
            g "Le rang S est le rang maximum vous êtes un stratège hors pair"
        return
    elif regionBeigeActive == False and regionBleueActive == False and regionGriseActive == False and regionJauneActive == False and regionOrangeActive == False and regionRoseActive == False and regionRougeActive == False and regionVerteActive == False and regionVioletteActive == False:
        g "Vous avez perdu le contrôle de toutes vos régions"
        g "GAME OVER "
        return
    else:
        $ regionBeigeActionFaite = False
        $ regionBleueActionFaite = False
        $ regionGriseActionFaite = False
        $ regionJauneActionFaite = False
        $ regionOrangeActionFaite = False
        $ regionRoseActionFaite = False
        $ regionRougeActionFaite = False
        $ regionVerteActionFaite = False
        $ regionVioletteActionFaite = False
        jump gestionRevenu

label gestionRevenu:

    #Beige
    if niveauRegionBeige == 2:
        $ multiplierBeige = 0.2

    elif niveauRegionBeige == 3:
        $ multiplierBeige = 0.3

    elif niveauRegionBeige == 4:
        $ multiplierBeige = 0.4

    elif niveauRegionBeige == 5:
        $ multiplierBeige = 0.5

    if regionBeigeActive == True:
        $ armeeRegionBeige += armeeRegionBeige * multiplierBeige
        $ argentRegionBeige += argentRegionBeige * multiplierBeige
        $ populationRegionBeige += populationRegionBeige * multiplierBeige
        $ nourritureRegionBeige += nourritureRegionBeige * multiplierBeige
    else:
        $ armeeRegionBeige += armeeRegionBeige * 0.1
        $ argentRegionBeige += argentRegionBeige * 0.1
        $ populationRegionBeige += populationRegionBeige * 0.1
        $ nourritureRegionBeige += nourritureRegionBeige * 0.1


    #Bleue
    if niveauRegionBleue == 2:
        $ multiplierBleue = 0.2

    if niveauRegionBleue == 3:
        $ multiplierBleue = 0.3

    if niveauRegionBleue == 4:
        $ multiplierBleue = 0.4

    if niveauRegionBleue == 5:
        $ multiplierBleue = 0.5

    if regionBleueActive == True:
        $ armeeRegionBleue += armeeRegionBleue * multiplierBleue
        $ armeeRegionBleue += armeeRegionBleue * multiplierBleue
        $ armeeRegionBleue += armeeRegionBleue * multiplierBleue
        $ armeeRegionBleue += armeeRegionBleue * multiplierBleue
    else:
        $ armeeRegionBleue += armeeRegionBleue * 0.1
        $ argentRegionBleue += argentRegionBleue * 0.1
        $ populationRegionBleue += populationRegionBleue * 0.1
        $ nourritureRegionBleue += nourritureRegionBleue * 0.1

    #Grise
    if niveauRegionGrise == 2:
        $ multiplierGrise = 0.2

    if niveauRegionGrise == 3:
        $ multiplierGrise = 0.3

    if niveauRegionGrise == 4:
        $ multiplierGrise = 0.4

    if niveauRegionGrise == 5:
        $ multiplierGrise = 0.5

    if regionGriseActive == True:
        $ armeeRegionGrise += armeeRegionGrise * multiplierGrise
        $ armeeRegionGrise += armeeRegionGrise * multiplierGrise
        $ armeeRegionGrise += armeeRegionGrise * multiplierGrise
        $ armeeRegionGrise += armeeRegionGrise * multiplierGrise
    else:
        $ armeeRegionGrise += armeeRegionGrise * 0.1
        $ argentRegionGrise += argentRegionGrise * 0.1
        $ populationRegionGrise += populationRegionGrise * 0.1
        $ nourritureRegionGrise += nourritureRegionGrise * 0.1

    #Jaune
    if niveauRegionJaune == 2:
        $ multiplierJaune = 0.2

    if niveauRegionJaune == 3:
        $ multiplierJaune = 0.3

    if niveauRegionJaune == 4:
        $ multiplierJaune = 0.4

    if niveauRegionJaune == 5:
        $ multiplierJaune = 0.5

    if regionJauneActive == True:
        $ armeeRegionJaune += armeeRegionJaune * multiplierJaune
        $ armeeRegionJaune += armeeRegionJaune * multiplierJaune
        $ armeeRegionJaune += armeeRegionJaune * multiplierJaune
        $ armeeRegionJaune += armeeRegionJaune * multiplierJaune
    else:
        $ armeeRegionJaune += armeeRegionJaune * 0.1
        $ argentRegionJaune += argentRegionJaune * 0.1
        $ populationRegionJaune += populationRegionJaune * 0.1
        $ nourritureRegionJaune += nourritureRegionJaune * 0.1

    #Orange
    if niveauRegionOrange == 2:
        $ multiplierOrange = 0.2

    if niveauRegionOrange == 3:
        $ multiplierOrange = 0.3

    if niveauRegionOrange == 4:
        $ multiplierOrange = 0.4

    if niveauRegionOrange == 5:
        $ multiplierOrange = 0.5
    if regionOrangeActive == True:
        $ armeeRegionOrange += armeeRegionOrange * multiplierOrange
        $ armeeRegionOrange += armeeRegionOrange * multiplierOrange
        $ armeeRegionOrange += armeeRegionOrange * multiplierOrange
        $ armeeRegionOrange += armeeRegionOrange * multiplierOrange
    else:
        $ armeeRegionOrange += armeeRegionOrange * 0.1
        $ argentRegionOrange += argentRegionOrange * 0.1
        $ populationRegionOrange += populationRegionOrange * 0.1
        $ nourritureRegionOrange += nourritureRegionOrange * 0.1

    #Rose
    if niveauRegionRose == 2:
        $ multiplierRose = 0.2

    if niveauRegionRose == 3:
        $ multiplierRose = 0.3

    if niveauRegionRose == 4:
        $ multiplierRose = 0.4

    if niveauRegionRose == 5:
        $ multiplierRose = 0.5

    if regionRoseActive == True:
        $ armeeRegionRose += armeeRegionRose * multiplierRose
        $ armeeRegionRose += armeeRegionRose * multiplierRose
        $ armeeRegionRose += armeeRegionRose * multiplierRose
        $ armeeRegionRose += armeeRegionRose * multiplierRose
    else:
        $ armeeRegionRose += armeeRegionRose * 0.1
        $ argentRegionRose += argentRegionRose * 0.1
        $ populationRegionRose += populationRegionRose * 0.1
        $ nourritureRegionRose += nourritureRegionRose * 0.1

    #Rouge
    if niveauRegionRouge == 2:
        $ multiplierRouge = 0.2

    if niveauRegionRouge == 3:
        $ multiplierRouge = 0.3

    if niveauRegionRouge == 4:
        $ multiplierRouge = 0.4

    if niveauRegionRouge == 5:
        $ multiplierRouge = 0.5

    if regionRougeActive == True:
        $ armeeRegionRouge += armeeRegionRouge * multiplierRouge
        $ armeeRegionRouge += armeeRegionRouge * multiplierRouge
        $ armeeRegionRouge += armeeRegionRouge * multiplierRouge
        $ armeeRegionRouge += armeeRegionRouge * multiplierRouge
    else:
        $ armeeRegionRouge += armeeRegionRouge * 0.1
        $ argentRegionRouge += argentRegionRouge * 0.1
        $ populationRegionRouge += populationRegionRouge * 0.1
        $ nourritureRegionRouge += nourritureRegionRouge * 0.1


    #Verte
    if niveauRegionVerte == 2:
        $ multiplierVerte = 0.2

    if niveauRegionVerte == 3:
        $ multiplierVerte = 0.3

    if niveauRegionVerte == 4:
        $ multiplierVerte = 0.4

    if niveauRegionVerte == 5:
        $ multiplierVerte = 0.5

    if regionVerteActive == True:
        $ armeeRegionVerte += armeeRegionVerte * multiplierVerte
        $ armeeRegionVerte += armeeRegionVerte * multiplierVerte
        $ armeeRegionVerte += armeeRegionVerte * multiplierVerte
        $ armeeRegionVerte += armeeRegionVerte * multiplierVerte
    else:
        $ armeeRegionVerte += armeeRegionVerte * 0.1
        $ argentRegionVerte += argentRegionVerte * 0.1
        $ populationRegionVerte += populationRegionVerte * 0.1
        $ nourritureRegionVerte += nourritureRegionVerte * 0.1

    #Violette
    if niveauRegionViolette == 2:
        $ multiplierViolette = 0.2

    if niveauRegionViolette == 3:
        $ multiplierViolette = 0.3

    if niveauRegionViolette == 4:
        $ multiplierViolette = 0.4

    if niveauRegionViolette == 5:
        $ multiplierViolette = 0.5

    if regionVioletteActive == True:
        $ armeeRegionViolette += armeeRegionViolette * multiplierViolette
        $ armeeRegionViolette += armeeRegionViolette * multiplierViolette
        $ armeeRegionViolette += armeeRegionViolette * multiplierViolette
        $ armeeRegionViolette += armeeRegionViolette * multiplierViolette
    else:
        $ armeeRegionViolette += armeeRegionViolette * 0.1
        $ argentRegionViolette += argentRegionViolette * 0.1
        $ populationRegionViolette += populationRegionViolette * 0.1
        $ nourritureRegionViolette += nourritureRegionViolette * 0.1



    if regionBeigeActive == True:
        hide screen infoRegionBeige
        $ regionsActives +=1
    if regionGriseActive == True:
        hide screen infoRegionGrise
        $ regionsActives +=1
    if regionJauneActive == True:
        hide screen infoRegionJaune
        $ regionsActives +=1
    if regionBleueActive == True:
        hide screen infoRegionBleue
        $ regionsActives +=1
    if regionOrangeActive == True:
        hide screen infoRegionOrange
        $ regionsActives +=1
    if regionRoseActive == True:
        hide screen infoRegionRose
        $ regionsActives +=1
    if regionRougeActive == True:
        hide screen infoRegionRouge
        $ regionsActives +=1
    if regionVerteActive == True:
        hide screen infoRegionVerte
        $ regionsActives +=1
    if regionVioletteActive == True:
        hide screen infoRegionViolette
        $ regionsActives +=1


    $ armeeGeneral += 15* regionsActives
    $ argentGeneral += 20* regionsActives
    $ populationGeneral += 15* regionsActives
    $ regionsActives=0
    call screen vueTerritoire with fade
