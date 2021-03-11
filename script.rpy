
#background placeholder à remplacer
image background = "../images/fond.png"

#fond de la box qui apparait

image fond_info_region = "../images/carre_gris.png"

# ressources


default var_armee_region_1 = 50
default var_argent_region_1 = 50
default var_population_region_1 = 50
default var_nourriture_region_1 = 50

#screen diplomatie placeholder à remplacer

screen diplomatie:
    image "../images/diplomatie.jpg"

screen attaque :
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5

screen info_region_1 :
    image "../images/carre_gris.png":
        at carre_zoom
        xpos 100
        ypos 100
    text "Armee :" :
        xpos 110
        ypos 100
    text "%d" % var_armee_region_1 :
        xpos 300
        ypos 100
    text "Argent :" :
        xpos 110
        ypos 130
    text "%d" % var_argent_region_1 :
        xpos 300
        ypos 130
    text "Population :":
        xpos 110
        ypos 160
    text "%d" % var_population_region_1:
        xpos 300
        ypos 160
    text "Nourriture :":
        xpos 110
        ypos 190
    text "%d" % var_nourriture_region_1:
        xpos 300
        ypos 190
    imagebutton :
        idle "../images/interagir.png"
        xpos 150
        ypos 240
        #TODO action change screen vers interaction
        action [Show("diplomatie")]
    imagebutton :
        idle "../images/attaquer.png"
        xpos 150
        ypos 300
        #TODO action change screen vers attaque
        action  [Show("attaque")]
#pour test
define e = Character()

# Le jeu commence ici
label start:

    scene background

    show screen info_region_1


    e "bonsoir"
return
