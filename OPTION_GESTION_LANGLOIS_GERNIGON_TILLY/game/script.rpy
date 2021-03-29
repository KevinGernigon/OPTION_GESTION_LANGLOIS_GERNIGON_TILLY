
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




#############################################
##################Grise######################



#############################################
##################Jaune######################

#############################################
##################Orange######################

#############################################
##################Rose######################


#############################################
##################Rouge######################









#############################################
##################Verte######################




#############################################
##################Violette######################





















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
