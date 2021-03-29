
image mapRegionGrise = im.Scale("mapRegionsGrise.jpg", 1280, 720)
image office = im.Scale ("bg office.png", 1280, 720)
image carre = "carre.jpg"
image regionBeige = im.Scale("regionBeige.png", 1280, 720)
image regionBleue = im.Scale("regionBleue.png", 1280, 720)
image regionGrise = im.Scale("regionGrise.png", 1280, 720)
image regionJaune = im.Scale("regionJaune.png", 1280, 720)
image regionOrange = im.Scale("regionOrange.png", 1280, 720)
image regionRose = im.Scale("regionRose.png", 1280, 720)
image regionRouge = im.Scale("regionRouge.png", 1280, 720)
image regionVerte = im.Scale("regionVerte.png", 1280, 720)
image regionBeigeAttaque = im.Scale("regionBeigeRouge.png", 1280, 720)
image regionBleueAttaque = im.Scale("regionBleueRouge.png", 1280, 720)
image regionGriseAttaque = im.Scale("regionGriseRouge.png", 1280, 720)
image regionJauneAttaque = im.Scale("regionJauneRouge.png", 1280, 720)
image regionOrangeAttaque = im.Scale("regionOrangeRouge.png", 1280, 720)
image regionRoseAttaque = im.Scale("regionRoseRouge.png", 1280, 720)
image regionRougeAttaque = im.Scale("regionRougeRouge.png", 1280, 720)
image regionVerteAttaque = im.Scale("regionVerteRouge.png", 1280, 720)
image boxInteragir1 = "helm.png"
image boxInteragir2 = "leaf.png"
image boxInteragir3 = "desk.png"
image boxInteragir4 = "coins.png"
image boxInteragir5 = "talk.png"
image upgradeRegionButton = "talk.png"
image logoAttaque = im.Scale("logoAttaque.png", 50, 50)
image imageMoins = im.Scale("moinsImage.png", 100, 100)
image imagePlus = im.Scale("plusImage.png", 200, 200)
image imagePlusTen = im.Scale("plusTen.png", 100, 100)
image checkbox = im.Scale("checkbox.png", 100, 100)
image modifyJauge = im.Scale("modifyVariableJauge.png", 200, 200)
image btnFindeTour = "btnFinDeTour.png"
image upgrade1 = im.Scale("upgrade1.png", 200, 200)
image upgrade2 = im.Scale("upgrade2.png", 200, 200)
image accepter = im.Scale("accept.png", 200, 200)
image refus = im.Scale("refuse.png", 200, 200)


define p = Character(_('Pythie'), color="#c8ffc8")
define a = Character(_('Ministre des armées'), color="#c8ffc8")
define h = Character(_('Ministre de l"agriculture'), color="#c8ffc8")
define c = Character(_('Ministre des civils'), color="#c8ffc8")
define r = Character(_('Ministre des religions'), color="#c8ffc8")
define a = Character(_('Ambassadeur'), color="#c8ffc8")
define g = Character(_('Maitre du jeu'), color="#c8ffc8", kind = nvl)


#image des armées différentes
image armyGeneral = "army.png"
image armyBeige = "armeeBeige.png"
image armyRouge = "armeeRouge.png"
image armyViolette = "armeeViolette.png"
image armyVerte = "armeeVerte.png"
image armyGrise = "armeeGrise.png"
image armyRose = "armeeRose.png"
image armyJaune = "armeeJaune.png"
image armyOrange = "armeeOrange.png"
image armyBleue = "armeeBleue.png"

#images des finances différentes
image financesGeneral = "coins.png"
image financesBeige = "coinsBeige.png"
image financesRouge = "coinsRouge.png"
image financesViolette = "coinsViolette.png"
image financesVerte = "coinsVerte.png"
image financesGrise = "coinsGrise.png"
image financesRose = "coinsRose.png"
image financesJaune = "coinsJaune.png"
image financesOrange = "coinsOrange.png"
image financesBleue = "coinsBleue.png"

#images des populations différentes
image popGeneral = "desk.png"
image popBeige = "populationBeige.png"
image popRouge = "populationRouge.png"
image popViolette = "populationViolette.png"
image popVerte = "populationVerte.png"
image popGrise = "populationGrise.png"
image popRose = "populationRose.png"
image popJaune = "populationJaune.png"
image popOrange = "populationOrange.png"
image popBleue = "populationBleue.png"

#images des nourritures différentes
image foodGeneral = "leaf.png"
image foodBeige = "nourritureBeige.png"
image foodRouge = "nourritureRouge.png"
image foodViolette = "nourritureViolette.png"
image foodVerte = "nourritureVerte.png"
image foodGrise = "nourritureGrise.png"
image foodRose = "nourritureRose.png"
image foodJaune = "nourritureJaune.png"
image foodOrange = "nourritureOrange.png"
image foodBleue = "nourritureBleue.png"

default lastScreen=""

default popUpInfoRegionOn=False

default regionsActives = 0

default armeeGeneral = 0
default argentGeneral = 0
default populationGeneral = 0
default nourritureGeneral = 0

default armeeRegionBeige = 100
default argentRegionBeige = 90
default populationRegionBeige = 150
default nourritureRegionBeige = 60

default armeeRegionBleue = 150
default argentRegionBleue = 90
default populationRegionBleue = 85
default nourritureRegionBleue = 75

default armeeRegionGrise = 100
default argentRegionGrise = 100
default populationRegionGrise = 60
default nourritureRegionGrise = 140

default armeeRegionJaune = 120
default argentRegionJaune = 90
default populationRegionJaune = 110
default nourritureRegionJaune = 80

default armeeRegionOrange = 100
default argentRegionOrange = 110
default populationRegionOrange = 70
default nourritureRegionOrange = 120

default armeeRegionRose = 120
default argentRegionRose = 90
default populationRegionRose = 120
default nourritureRegionRose = 70

default armeeRegionRouge = 80
default argentRegionRouge = 90
default populationRegionRouge = 130
default nourritureRegionRouge = 100

default armeeRegionVerte = 80
default argentRegionVerte = 90
default populationRegionVerte = 140
default nourritureRegionVerte = 90

default armeeRegionViolette = 60
default argentRegionViolette = 100
default populationRegionViolette = 100
default nourritureRegionViolette = 140

default regionBeigeActive = False
default regionBleueActive = False
default regionGriseActive = False
default regionJauneActive = False
default regionOrangeActive = False
default regionRoseActive = False
default regionRougeActive = False
default regionVerteActive = False
default regionVioletteActive = False

default regionBeigeActionFaite = False
default regionBleueActionFaite = False
default regionGriseActionFaite = False
default regionJauneActionFaite = False
default regionOrangeActionFaite = False
default regionRoseActionFaite = False
default regionRougeActionFaite = False
default regionVerteActionFaite = False
default regionVioletteActionFaite = False

default niveauRegionBeige = 1
default niveauRegionBleue = 1
default niveauRegionGrise = 1
default niveauRegionJaune = 1
default niveauRegionOrange = 1
default niveauRegionRose = 1
default niveauRegionRouge = 1
default niveauRegionVerte = 1
default niveauRegionViolette = 1

default multiplierBeige = 0.1
default multiplierBleue = 0.1
default multiplierGrise = 0.1
default multiplierJaune = 0.1
default multiplierOrange = 0.1
default multiplierRose = 0.1
default multiplierRouge = 0.1
default multiplierVerte = 0.1
default multiplierViolette = 0.1

default chanceAttaqueBeige = 0
default chanceAttaqueBleue = 0
default chanceAttaqueGrise = 0
default chanceAttaqueJaune = 0
default chanceAttaqueOrange = 0
default chanceAttaqueRose = 0
default chanceAttaqueRouge = 0
default chanceAttaqueVerte = 0
default chanceAttaqueViolette = 0

default variableJauge=0
default variableJaugeDiv2= 0

default jour = 1


label start:
    $ config.has_autosave = False

    "Dans quelle région voulez vous commencer?"
    nvl clear
    scene mapRegionGrise
    call screen choixRegionDepart










###################################################################################################################











#############################################
##################BEIGE######################





#############################################
##################Bleue######################
label actionRegionBleue:
    call screen actionRegionBleue
screen actionRegionBleue:
    $ popUpInfoRegionOn=False
    image "../images/diplomatie.jpg"

label declarerGuerreRegionBleue:
    call screen declarerGuerreRegionBleue
screen declarerGuerreRegionBleue :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionBleue :
    #if(popUpInfoRegionOn==False):
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 450
            ypos 280
        text "Armee :" :
            xpos 460
            ypos 280
        text "%d" % armeeRegionBleue :
            xpos 610
            ypos 280
        text "Argent :" :
            xpos 460
            ypos 310
        text "%d" % argentRegionBleue :
            xpos 610
            ypos 310
        text "Population :":
            xpos 460
            ypos 340
        text "%d" % populationRegionBleue:
            xpos 610
            ypos 340
        text "Nourriture :":
            xpos 460
            ypos 370
        text "%d" % nourritureRegionBleue:
            xpos 610
            ypos 370
        imagebutton :
            idle "../images/interagir.png"
            xpos 500
            ypos 420
            action Jump("interactionBeige")
        imagebutton :
            idle "../images/attaquer.png"
            xpos 500
            ypos 480
            action  Jump("declarerGuerreRegionBleue")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 700
            ypos 290
            action  Hide("infoRegionBleue")




#############################################
##################Grise######################
label actionRegionGrise:
    call screen actionRegionGrise
screen actionRegionGrise:
    $ popUpInfoRegionOn=False
    image "../images/diplomatie.jpg"

label declarerGuerreRegionGrise:
    call screen declarerGuerreRegionGrise
screen declarerGuerreRegionGrise :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionGrise :
    #if(popUpInfoRegionOn==False):
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 400
            ypos 10
        text "Armee :" :
            xpos 410
            ypos 10
        text "%d" % armeeRegionGrise :
            xpos 550
            ypos 10
        text "Argent :" :
            xpos 410
            ypos 40
        text "%d" % argentRegionGrise :
            xpos 550
            ypos 40
        text "Population :":
            xpos 410
            ypos 70
        text "%d" % populationRegionGrise:
            xpos 550
            ypos 70
        text "Nourriture :":
            xpos 410
            ypos 100
        text "%d" % nourritureRegionGrise:
            xpos 550
            ypos 100
        imagebutton :
            idle "../images/interagir.png"
            xpos 450
            ypos 150
            action Jump("actionRegionGrise")
        imagebutton :
            idle "../images/attaquer.png"
            xpos 450
            ypos 210
            action  Jump("declarerGuerreRegionGrise")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 650
            ypos 20
            action  Hide("infoRegionGrise")



#############################################
##################Jaune######################
label actionRegionJaune:
    call screen actionRegionJaune
screen actionRegionJaune:
    $ popUpInfoRegionOn=False
    image "../images/diplomatie.jpg"



transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionJaune :
    #if(popUpInfoRegionOn==False):
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 450
            ypos 100
        text "Armee :" :
            xpos 460
            ypos 100
        text "%d" % armeeRegionJaune :
            xpos 600
            ypos 100
        text "Argent :" :
            xpos 460
            ypos 130
        text "%d" % argentRegionJaune :
            xpos 600
            ypos 130
        text "Population :":
            xpos 460
            ypos 160
        text "%d" % populationRegionJaune:
            xpos 600
            ypos 160
        text "Nourriture :":
            xpos 460
            ypos 190
        text "%d" % nourritureRegionJaune:
            xpos 600
            ypos 190
        imagebutton :
            idle "../images/interagir.png"
            xpos 500
            ypos 240
            action Jump("actionRegionJaune")
        imagebutton :
            idle "../images/attaquer.png"
            xpos 500
            ypos 300
            action  Jump("declarerGuerreRegionJaune")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 700
            ypos 110
            action  Hide("infoRegionJaune")




#############################################
##################Orange######################
label actionRegionOrange:
    call screen actionRegionOrange
screen actionRegionOrange:
    $ popUpInfoRegionOn=False
    image "../images/diplomatie.jpg"

label declarerGuerreRegionOrange:
    call screen declarerGuerreRegionOrange
screen declarerGuerreRegionOrange :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionOrange :
    #if(popUpInfoRegionOn==False):
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 200
            ypos 300
        text "Armee :" :
            xpos 210
            ypos 300
        text "%d" % armeeRegionOrange :
            xpos 350
            ypos 300
        text "Argent :" :
            xpos 210
            ypos 330
        text "%d" % argentRegionOrange :
            xpos 350
            ypos 330
        text "Population :":
            xpos 210
            ypos 360
        text "%d" % populationRegionOrange:
            xpos 350
            ypos 360
        text "Nourriture :":
            xpos 210
            ypos 390
        text "%d" % nourritureRegionOrange:
            xpos 350
            ypos 390
        imagebutton :
            idle "../images/interagir.png"
            xpos 250
            ypos 440
            action Jump("actionRegionOrange")
        imagebutton :
            idle "../images/attaquer.png"
            xpos 250
            ypos 500
            action  Jump("declarerGuerreRegionOrange")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 450
            ypos 310
            action  Hide("infoRegionOrange")



#############################################
##################Rose######################
label actionRegionRose:
    call screen actionRegionRose
screen actionRegionRose:
    $ popUpInfoRegionOn=False
    image "../images/diplomatie.jpg"

label declarerGuerreRegionRose:
    call screen declarerGuerreRegionRose
screen declarerGuerreRegionRose :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionRose :
    #if(popUpInfoRegionOn==False):
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 150
            ypos 100
        text "Armee :" :
            xpos 160
            ypos 100
        text "%d" % armeeRegionRose :
            xpos 300
            ypos 100
        text "Argent :" :
            xpos 160
            ypos 130
        text "%d" % argentRegionRose :
            xpos 300
            ypos 130
        text "Population :":
            xpos 160
            ypos 160
        text "%d" % populationRegionRose:
            xpos 300
            ypos 160
        text "Nourriture :":
            xpos 160
            ypos 190
        text "%d" % nourritureRegionRose:
            xpos 300
            ypos 190
        imagebutton :
            idle "../images/interagir.png"
            xpos 200
            ypos 240
            action Jump("actionRegionRose")
        imagebutton :
            idle "../images/attaquer.png"
            xpos 200
            ypos 300
            action  Jump("declarerGuerreRegionRose")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 400
            ypos 110
            action  Hide("infoRegionRose")


#############################################
##################Rouge######################
label actionRegionRouge:
    call screen actionRegionRouge
screen actionRegionRouge:
    $ popUpInfoRegionOn=False
    image "../images/diplomatie.jpg"

label declarerGuerreRegionRouge:
    call screen declarerGuerreRegionRouge
screen declarerGuerreRegionRouge :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionRouge :
    #if(popUpInfoRegionOn==False):
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 800
            ypos 275
        text "Armee :" :
            xpos 810
            ypos 275
        text "%d" % armeeRegionRouge :
            xpos 950
            ypos 275
        text "Argent :" :
            xpos 810
            ypos 305
        text "%d" % argentRegionRouge :
            xpos 950
            ypos 305
        text "Population :":
            xpos 810
            ypos 335
        text "%d" % populationRegionRouge:
            xpos 950
            ypos 335
        text "Nourriture :":
            xpos 810
            ypos 365
        text "%d" % nourritureRegionRouge:
            xpos 950
            ypos 365
        imagebutton :
            idle "../images/interagir.png"
            xpos 850
            ypos 415
            action Jump("actionRegionRouge")
        imagebutton :
            idle "../images/attaquer.png"
            xpos 850
            ypos 475
            action  Jump("declarerGuerreRegionRouge")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1050
            ypos 285
            action  Hide("infoRegionRouge")





#############################################
##################Verte######################
label actionRegionVerte:
    call screen actionRegionVerte
screen actionRegionVerte:
    $ popUpInfoRegionOn=False
    image "../images/diplomatie.jpg"

label declarerGuerreRegionVerte:
    call screen declarerGuerreRegionVerte
screen declarerGuerreRegionVerte :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionVerte :
    #if(popUpInfoRegionOn==False):
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 800
            ypos 400
        text "Armee :" :
            xpos 810
            ypos 400
        text "%d" % armeeRegionVerte :
            xpos 950
            ypos 400
        text "Argent :" :
            xpos 810
            ypos 430
        text "%d" % argentRegionVerte :
            xpos 950
            ypos 430
        text "Population :":
            xpos 810
            ypos 460
        text "%d" % populationRegionVerte:
            xpos 950
            ypos 460
        text "Nourriture :":
            xpos 810
            ypos 490
        text "%d" % nourritureRegionVerte:
            xpos 950
            ypos 490
        imagebutton :
            idle "../images/interagir.png"
            xpos 850
            ypos 540
            action Jump("actionRegionVerte")
        imagebutton :
            idle "../images/attaquer.png"
            xpos 850
            ypos 600
            action  Jump("declarerGuerreRegionVerte")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1050
            ypos 410
            action  Hide("infoRegionVerte")




#############################################
##################Violette######################
label actionRegionViolette:
    call screen actionRegionViolette
screen actionRegionViolette:
    $ popUpInfoRegionOn=False
    image "../images/diplomatie.jpg"

label declarerGuerreRegionViolette:
    call screen declarerGuerreRegionViolette
screen declarerGuerreRegionViolette :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionViolette :
    #if(popUpInfoRegionOn==False):
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 100
            ypos 400
        text "Armee :" :
            xpos 110
            ypos 400
        text "%d" % armeeRegionViolette :
            xpos 250
            ypos 400
        text "Argent :" :
            xpos 110
            ypos 430
        text "%d" % argentRegionViolette :
            xpos 250
            ypos 430
        text "Population :":
            xpos 110
            ypos 460
        text "%d" % populationRegionViolette:
            xpos 250
            ypos 460
        text "Nourriture :":
            xpos 110
            ypos 490
        text "%d" % nourritureRegionViolette:
            xpos 250
            ypos 490
        imagebutton :
            idle "../images/interagir.png"
            xpos 150
            ypos 540
            action Jump("actionRegionViolette")
        imagebutton :
            idle "../images/attaquer.png"
            xpos 150
            ypos 600
            action  Jump("declarerGuerreRegionViolette")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 350
            ypos 410
            action  Hide("infoRegionViolette")





















screen choixRegionDepart:
        #$ popUpInfoRegionOn=False
        imagebutton:
            idle "regionBeige.png"
            focus_mask True
            xpos 715
            ypos 26
            action Jump("startRegionBeige")
        imagebutton:
            idle "regionBleue.png"
            focus_mask True
            xpos 415
            ypos 280
            action Jump("startRegionBleue")
        imagebutton:
            idle "regionGrise.png"
            focus_mask True
            xpos 265
            ypos 45
            action Jump("startRegionGrise")
        imagebutton:
            idle "regionJaune.png"
            focus_mask True
            xpos 370
            ypos 90
            action Jump("startRegionJaune")
        imagebutton:
            idle "regionOrange.png"
            focus_mask True
            xpos 155
            ypos 309
            action Jump("startRegionOrange")
        imagebutton:
            idle "regionRose.png"
            focus_mask True
            xpos 73
            ypos 104
            action Jump("startRegionRose")
        imagebutton:
            idle "regionRouge.png"
            focus_mask True
            xpos 720
            ypos 295
            action Jump("startRegionRouge")
        imagebutton:
            idle "regionVerte.png"
            focus_mask True
            xpos 711
            ypos 422
            action Jump("startRegionVerte")
        imagebutton:
            idle "regionViolette.png"
            focus_mask True
            xpos 42
            ypos 383
            action Jump("startRegionViolette")


transform variableJaugeText:
    zoom 4


label variableJauge:
    $ variableJauge = 0
    call screen variableJauge

screen variableJauge:
    text "%d" % variableJauge:
        at variableJaugeText
        yalign 0.5
        xalign 0.5
    imagebutton :
        idle "imageMoins"
        yalign 0.5
        xalign 0.35
        action  Jump("variableJaugeMoins")
    imagebutton :
        idle "imagePlus"
        yalign 0.5
        xalign 0.65
        action  Jump("variableJaugePlus")
    imagebutton :
        idle "checkbox"
        yalign 0.75
        xalign 0.5
        action  Jump(lastScreen)
    imagebutton :
        idle "imagePlusTen"
        yalign 0.5
        xalign 0.80
        action  Jump("variableJaugePlusTen")


label variableJaugePlus:

    $ variableJauge+=1
    $ variableJaugeDiv2+=0.5
    call screen variableJauge

label variableJaugePlusTen:
    $ variableJauge+=10
    $ variableJaugeDiv2 +=5
    call screen variableJauge

label variableJaugeMoins:
    $ variableJauge-=1
    if variableJauge < 0 :
        $ variableJauge = 0
    $ variableJaugeDiv2-=0.5
    if variableJaugeDiv2 < 0 :
        $ variableJaugeDiv2 = 0
    call screen variableJauge
