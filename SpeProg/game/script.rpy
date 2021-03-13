
image mapRegionGrise = im.Scale("mapRegionsGrise.jpg", 1280, 720)
image carre = "carre.jpg"
image regionBeige = im.Scale("regionBeige.png", 1280, 720)
image regionBleue = im.Scale("regionBleue.png", 1280, 720)
image regionGrise = im.Scale("regionGrise.png", 1280, 720)
image regionJaune = im.Scale("regionJaune.png", 1280, 720)
image regionOrange = im.Scale("regionOrange.png", 1280, 720)
image regionRose = im.Scale("regionRose.png", 1280, 720)
image regionRouge = im.Scale("regionRouge.png", 1280, 720)
image regionVerte = im.Scale("regionVerte.png", 1280, 720)
image regionViolette = im.Scale("regionViolette.png", 1280, 720)



# Le jeu commence ici
label start:
    $ region1Active = True
    $ region2Active = True
    $ region3Active = True
    $ region4Active = True
    $ region5Active = True
    $ region6Active = True
    $ region7Active = True
    $ region8Active = True
    $ region9Active = True
    "Choisissez une région avec laquelle interagir"
    scene mapRegionGrise
    call screen vueTerritoire


screen vueTerritoire:
    if region1Active==True:
        imagebutton:
            idle "regionBeige.png"
            xpos 715
            ypos 26
            action Jump("regionBeige")
    if region2Active==True:
        imagebutton:
            idle "regionBleue.png"
            xpos 415
            ypos 280
            action Jump("regionBleue")
    if region3Active==True:
        imagebutton:
            idle "regionGrise.png"
            xpos 265
            ypos 45
            action Jump("regionGrise")
    if region4Active==True:
        imagebutton:
            idle "regionJaune.png"
            xpos 370
            ypos 90
            action Jump("regionJaune")
    if region5Active==True:
        imagebutton:
            idle "regionOrange.png"
            xpos 155
            ypos 309
            action Jump("regionOrange")
    if region6Active==True:
        imagebutton:
            idle "regionRose.png"
            xpos 73
            ypos 104
            action Jump("regionRose")
    if region7Active==True:
        imagebutton:
            idle "regionRouge.png"
            xpos 720
            ypos 295
            action Jump("regionRouge")
    if region8Active==True:
        imagebutton:
            idle "regionVerte.png"
            xpos 711
            ypos 422
            action Jump("regionVerte")
    if region9Active==True:
        imagebutton:
            idle "regionViolette.png"
            xpos 42
            ypos 383
            action Jump("infoRegionViolette")


label regionBeige:
    "regionBeige"
    return

label regionBleue:
    "regionBleue"
    return

label regionGrise:
    "regionGrise"
    return

label regionJaune:
    "regionJaune"
    return

label regionOrange:
    "regionOrange"
    return

label regionRose:
    "regionRose"
    return

label regionRouge:
    "regionRouge"
    return

label regionVerte:
    "regionVerte"
    return

label infoRegionViolette:
    "infoRegionViolette"
    return
