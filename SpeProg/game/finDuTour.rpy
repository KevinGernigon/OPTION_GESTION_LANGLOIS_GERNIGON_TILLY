
label victoire:
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

    $ armeeRegionBeige += armeeRegionBeige * multiplierBeige
    $ argentRegionBeige += argentRegionBeige * multiplierBeige
    $ populationRegionBeige += populationRegionBeige * multiplierBeige
    $ nourritureRegionBeige += nourritureRegionBeige * multiplierBeige


    #Bleue
    if niveauRegionBleue == 2:
        $ multiplierBleue = 0.2

    if niveauRegionBleue == 3:
        $ multiplierBleue = 0.3

    if niveauRegionBleue == 4:
        $ multiplierBleue = 0.4

    if niveauRegionBleue == 5:
        $ multiplierBleue = 0.5

    $ armeeRegionBleue += armeeRegionBleue * multiplierBleue
    $ armeeRegionBleue += armeeRegionBleue * multiplierBleue
    $ armeeRegionBleue += armeeRegionBleue * multiplierBleue
    $ armeeRegionBleue += armeeRegionBleue * multiplierBleue

    #Grise
    if niveauRegionGrise == 2:
        $ multiplierGrise = 0.2

    if niveauRegionGrise == 3:
        $ multiplierGrise = 0.3

    if niveauRegionGrise == 4:
        $ multiplierGrise = 0.4

    if niveauRegionGrise == 5:
        $ multiplierGrise = 0.5

    $ armeeRegionGrise += armeeRegionGrise * multiplierGrise
    $ armeeRegionGrise += armeeRegionGrise * multiplierGrise
    $ armeeRegionGrise += armeeRegionGrise * multiplierGrise
    $ armeeRegionGrise += armeeRegionGrise * multiplierGrise

    #Jaune
    if niveauRegionJaune == 2:
        $ multiplierJaune = 0.2

    if niveauRegionJaune == 3:
        $ multiplierJaune = 0.3

    if niveauRegionJaune == 4:
        $ multiplierJaune = 0.4

    if niveauRegionJaune == 5:
        $ multiplierJaune = 0.5

    $ armeeRegionJaune += armeeRegionJaune * multiplierJaune
    $ armeeRegionJaune += armeeRegionJaune * multiplierJaune
    $ armeeRegionJaune += armeeRegionJaune * multiplierJaune
    $ armeeRegionJaune += armeeRegionJaune * multiplierJaune

    #Orange
    if niveauRegionOrange == 2:
        $ multiplierOrange = 0.2

    if niveauRegionOrange == 3:
        $ multiplierOrange = 0.3

    if niveauRegionOrange == 4:
        $ multiplierOrange = 0.4

    if niveauRegionOrange == 5:
        $ multiplierOrange = 0.5

    $ armeeRegionOrange += armeeRegionOrange * multiplierOrange
    $ armeeRegionOrange += armeeRegionOrange * multiplierOrange
    $ armeeRegionOrange += armeeRegionOrange * multiplierOrange
    $ armeeRegionOrange += armeeRegionOrange * multiplierOrange

    #Rose
    if niveauRegionRose == 2:
        $ multiplierRose = 0.2

    if niveauRegionRose == 3:
        $ multiplierRose = 0.3

    if niveauRegionRose == 4:
        $ multiplierRose = 0.4

    if niveauRegionRose == 5:
        $ multiplierRose = 0.5

    $ armeeRegionRose += armeeRegionRose * multiplierRose
    $ armeeRegionRose += armeeRegionRose * multiplierRose
    $ armeeRegionRose += armeeRegionRose * multiplierRose
    $ armeeRegionRose += armeeRegionRose * multiplierRose

    #Rouge
    if niveauRegionRouge == 2:
        $ multiplierRouge = 0.2

    if niveauRegionRouge == 3:
        $ multiplierRouge = 0.3

    if niveauRegionRouge == 4:
        $ multiplierRouge = 0.4

    if niveauRegionRouge == 5:
        $ multiplierRouge = 0.5

    $ armeeRegionRouge += armeeRegionRouge * multiplierRouge
    $ armeeRegionRouge += armeeRegionRouge * multiplierRouge
    $ armeeRegionRouge += armeeRegionRouge * multiplierRouge
    $ armeeRegionRouge += armeeRegionRouge * multiplierRouge


    #Verte
    if niveauRegionVerte == 2:
        $ multiplierVerte = 0.2

    if niveauRegionVerte == 3:
        $ multiplierVerte = 0.3

    if niveauRegionVerte == 4:
        $ multiplierVerte = 0.4

    if niveauRegionVerte == 5:
        $ multiplierVerte = 0.5

    $ armeeRegionVerte += armeeRegionVerte * multiplierVerte
    $ armeeRegionVerte += armeeRegionVerte * multiplierVerte
    $ armeeRegionVerte += armeeRegionVerte * multiplierVerte
    $ armeeRegionVerte += armeeRegionVerte * multiplierVerte

    #Violette
    if niveauRegionViolette == 2:
        $ multiplierViolette = 0.2

    if niveauRegionViolette == 3:
        $ multiplierViolette = 0.3

    if niveauRegionViolette == 4:
        $ multiplierViolette = 0.4

    if niveauRegionViolette == 5:
        $ multiplierViolette = 0.5

    $ armeeRegionViolette += armeeRegionViolette * multiplierViolette
    $ armeeRegionViolette += armeeRegionViolette * multiplierViolette
    $ armeeRegionViolette += armeeRegionViolette * multiplierViolette
    $ armeeRegionViolette += armeeRegionViolette * multiplierViolette


    call screen vueTerritoire