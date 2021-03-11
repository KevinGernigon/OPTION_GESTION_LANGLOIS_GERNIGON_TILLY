# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.

image drapeauFrance = im.Scale("drapeauFrance.png", 1280, 720)
image carre = "carre.jpg"

# Le jeu commence ici
label start:
    $ region1Active = True
    $ region2Active = True
    $ region3Active = True
    $ region4Active = False
    $ region5Active = True
    $ region6Active = True
    $ region7Active = True
    $ region8Active = True
    $ region9Active = True
    "Choisissez une région avec laquelle interagir"
    scene drapeauFrance
    call screen vueTerritoire


screen vueTerritoire:
    if region1Active==True:
        imagebutton:
            idle "carre.jpg"
            action Jump("infoRegion1")
    if region2Active==True:
        imagebutton:
            idle "carre.jpg"
            xpos 500
            action Jump("infoRegion2")
    if region3Active==True:
        imagebutton:
            idle "carre.jpg"
            xpos 1000
            action Jump("infoRegion3")
    if region4Active==True:
        imagebutton:
            idle "carre.jpg"
            ypos 250
            action Jump("infoRegion4")
    if region5Active==True:
        imagebutton:
            xpos 500
            ypos 250
            idle "carre.jpg"
            action Jump("infoRegion5")
    if region6Active==True:
        imagebutton:
            idle "carre.jpg"
            xpos 1000
            ypos 250
            action Jump("infoRegion6")
    if region7Active==True:
        imagebutton:
            idle "carre.jpg"
            ypos 500
            action Jump("infoRegion7")
    if region8Active==True:
        imagebutton:
            idle "carre.jpg"
            xpos 500
            ypos 500
            action Jump("infoRegion8")
    if region9Active==True:
        imagebutton:
            idle "carre.jpg"
            xpos 1000
            ypos 500
            action Jump("infoRegion9")


label infoRegion1:
    "region1"
    return

label infoRegion2:
    "region2"
    return

label infoRegion3:
    "region3"
    return

label infoRegion4:
    "region4"
    return

label infoRegion5:
    "region5"
    return

label infoRegion6:
    "region6"
    return

label infoRegion7:
    "region7"
    return

label infoRegion8:
    "region8"
    return

label infoRegion9:
    "region9"
    return

