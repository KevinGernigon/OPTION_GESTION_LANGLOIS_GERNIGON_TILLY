
# Le jeu commence ici
transform dezoom_icons_generales:
    zoom 0.2

label startRegionBeige:
    $ regionBeigeActive = True
    call screen vueTerritoire
label startRegionBleue:
    $ regionBleueActive = True
    call screen vueTerritoire
label startRegionGrise:
    $ regionGriseActive = True
    call screen vueTerritoire
label startRegionJaune:
    $ regionJauneActive = True
    call screen vueTerritoire
label startRegionOrange:
    $ regionOrangeActive = True
    call screen vueTerritoire
label startRegionRose:
    $ regionRoseActive = True
    call screen vueTerritoire
label startRegionRouge:
    $ regionRougeActive = True
    call screen vueTerritoire
label startRegionVerte:
    $ regionVerteActive = True
    call screen vueTerritoire
label startRegionViolette:
    $ regionVioletteActive = True
    call screen vueTerritoire


screen vueTerritoire:
    #$ popUpInfoRegionOn=False
    if regionBeigeActive==True:
        imagebutton:
            idle "regionBeige.png"
            xpos 715
            ypos 26
            action Show("infoRegionBeige")
    if regionBleueActive==True:
        imagebutton:
            idle "regionBleue.png"
            xpos 415
            ypos 280
            action Show("infoRegionBleue")
    if regionGriseActive==True:
        imagebutton:
            idle "regionGrise.png"
            xpos 265
            ypos 45
            action Show("infoRegionGrise")
    if regionJauneActive==True:
        imagebutton:
            idle "regionJaune.png"
            xpos 370
            ypos 90
            action Show("infoRegionJaune")
    if regionOrangeActive==True:
        imagebutton:
            idle "regionOrange.png"
            xpos 155
            ypos 309
            action Show("infoRegionOrange")
    if regionRoseActive==True:
        imagebutton:
            idle "regionRose.png"
            xpos 73
            ypos 104
            action Show("infoRegionRose")
    if regionRougeActive==True:
        imagebutton:
            idle "regionRouge.png"
            xpos 720
            ypos 295
            action Show("infoRegionRouge")
    if regionVerteActive==True:
        imagebutton:
            idle "regionVerte.png"
            xpos 711
            ypos 422
            action Show("infoRegionVerte")
    if regionVioletteActive==True:
        imagebutton:
            idle "regionViolette.png"
            xpos 42
            ypos 383
            action Show("infoRegionViolette")
    #text pop_up en haut à droite
    image "../images/army.png" :
        yalign 0.02
        xalign 0.94
        at dezoom_icons_generales
    text "%d" % armeeGeneral :
        yalign 0.03
        xalign 0.97
    image "../images/leaf.png" :
        yalign 0.08
        xalign 0.94
        at dezoom_icons_generales
    text "%d" % nourritureGeneral:
        yalign 0.091
        xalign 0.97
    image "../images/desk.png" :
        yalign 0.14
        xalign 0.94
        at dezoom_icons_generales
    text "%d" % populationGeneral :
        yalign 0.15
        xalign 0.97
    image "../images/coins.png" :
        yalign 0.20
        xalign 0.94
        at dezoom_icons_generales
    text "%d" % argentGeneral :
        yalign 0.21
        xalign 0.97
    text "%d" % jour :
        xpos 20
        ypos 20
    imagebutton :
        idle "btnFindeTour"
        xpos 450
        ypos 600
        action  Jump("iadeplacements")
