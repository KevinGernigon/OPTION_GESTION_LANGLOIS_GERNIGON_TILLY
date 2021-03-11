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
    $ region4Active = True
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
            xpos 1000
            action Jump("infoRegion2")
    if region3Active==True:
        imagebutton:
            idle "carre.jpg"
            ypos 500
            action Jump("infoRegion3")
    if region4Active==True:
        imagebutton:
            idle "carre.jpg"
            xpos 1000
            ypos 500
            action Jump("infoRegion4")


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