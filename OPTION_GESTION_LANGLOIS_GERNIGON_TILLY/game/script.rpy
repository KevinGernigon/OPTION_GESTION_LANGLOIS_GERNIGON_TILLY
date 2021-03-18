
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
image boxInteragir1 = "boxInteragir1.png"
image boxInteragir2 = "boxInteragir2.png"
image boxInteragir3 = "boxInteragir3.png"
image boxInteragir4 = "boxInteragir4.png"
image boxInteragir5 = "boxInteragir5.png"



define p = Character(_('Pythie'), color="#c8ffc8")
define a = Character(_('Ministre des armées'), color="#c8ffc8")
define h = Character(_('Ministre de l"agriculture'), color="#c8ffc8")
define c = Character(_('Ministre des civils'), color="#c8ffc8")
define r = Character(_('Ministre des religions'), color="#c8ffc8")
define a = Character(_('Ambassadeur'), color="#c8ffc8")

default popUpInfoRegionOn=False

default armeeGeneral = 0
default argentGeneral = 0
default populationGeneral = 0
default nourritureGeneral = 0

default armeeRegionBeige = 100
default argentRegionBeige = 100
default populationRegionBeige = 150
default nourritureRegionBeige = 100

default armeeRegionBleue = 150
default argentRegionBleue = 100
default populationRegionBleue = 85
default nourritureRegionBleue = 100

default armeeRegionGrise = 100
default argentRegionGrise = 100
default populationRegionGrise = 60
default nourritureRegionGrise = 100

default armeeRegionJaune = 120
default argentRegionJaune = 100
default populationRegionJaune = 110
default nourritureRegionJaune = 100

default armeeRegionOrange = 100
default argentRegionOrange = 0
default populationRegionOrange = 70
default nourritureRegionOrange = 100

default armeeRegionRose = 120
default argentRegionRose = 100
default populationRegionRose = 120
default nourritureRegionRose = 100

default armeeRegionRouge = 80
default argentRegionRouge = 130
default populationRegionRouge = 0
default nourritureRegionRouge = 100

default armeeRegionVerte = 80
default argentRegionVerte = 100
default populationRegionVerte = 140
default nourritureRegionVerte = 100

default armeeRegionViolette = 60
default argentRegionViolette = 150
default populationRegionViolette = 100
default nourritureRegionViolette = 100

default regionBeigeActive = True
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

transform dezoomInteractionChoix:
    zoom 0.5
label start:
    $ config.has_autosave = False
    $ jour = 1
    "test"
    scene mapRegionGrise
    call screen vueTerritoire










label interactionBeige :
    hide screen infoRegionBeige
    scene office
    show pythie at left
    call screen interactionBeige
screen interactionBeige:
#armees
     imagebutton :
            idle "boxInteragir1"
            at dezoomInteractionChoix
            xpos 300
            ypos 100
            action  Jump("ministreArmeeBeige")
     imagebutton :
            idle "boxInteragir2"
            at dezoomInteractionChoix
            xpos 680
            ypos 100
            action  Jump("ministreAgricultureBeige")
     imagebutton :
            idle "boxInteragir3"
            at dezoomInteractionChoix
            xpos 300
            ypos 400
            action  Jump("ministreCivilsBeige")
     imagebutton :
            idle "boxInteragir4"
            at dezoomInteractionChoix
            xpos 680
            ypos 400
            action  Jump("ministreFinancesBeige")
     imagebutton :
            idle "boxInteragir5"
            at dezoomInteractionChoix
            xpos 490
            ypos 250
            action  Jump("ministreAmbassadeurBeige")

label ministreArmeeBeige:
    p "Assistante convoquer moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    menu:
        "Requisitionner des troupes pour l'armée générale(30)":
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            a "Très bien commandant "
            $ armeeGeneral += 30
            $ armeeRegionBeige -=  30
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
        "Donner des soldats à la région(30)":
            p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
            a "Merci commandant"
            $ armeeRegionBeige += 30
            $ armeeGeneral -= 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
#agriculture
label ministreAgricultureBeige:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    menu:
        "Requistionner de la nourriture pour la nourriture générale(30)":
            p "Je souhaite requisitionner de la nourriture"
            a "Très bien commandant "
            $ nourritureGeneral += 30
            $ nourritureRegionBeige -= 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
        "Donner de la nourriture(30)":
            p "Je vous envoie de la nourriture"
            a "Merci commandant"
            $ nourritureGeneral -= 30
            $ nourritureRegionBeige += 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
#civils
label ministreCivilsBeige:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    menu:
        "Requistionner des civils pour les civils généraux(30)":
            p "Je souhaite requisitionner des civils"
            a "Très bien commandant "
            $ populationGeneral += 30
            $ populationRegionBeige -= 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
        "Donner des civils(30)":
            p "Je vous envoie des civils"
            a "Merci commandant"
            $ populationGeneral -= 30
            $ populationRegionBeige += 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
#finances
label ministreFinancesBeige:
    p "Assistante convoquer moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    menu:
        "Requistionner de l'argent pour les caisses générales(30)":
            p "Je souhaite requisitionner de l'argent"
            a "Très bien commandant "
            $ argentGeneral += 30
            $ argentRegionBeige -= 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
        "Donner de l'argent(30)":
            p "Je vous envoie de l'argent"
            a "Merci commandant"
            $ argentGeneral -= 30
            $ argentRegionBeige += 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
#ambassadeur
label ministreAmbassadeurBeige:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    menu :
        "Augmenter la taille de l'armée de cette région(+30 armee / -30 population)":
            p "Je souhaite que vous entrainez des civils en soldats"
            a "Très bien commandant "
            $ populationRegionBeige -= 30
            $ armeeRegionBeige += 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
        "Acheter de la nourriture(+30 nourriture / -15 argent -15 population)":
            p "Je souhaite que vous produisiez plus de nourriture"
            a "Très bien commandant "
            $ nourritureGeneral += 30
            $ populationRegionBeige -= 15
            $ argentRegionBeige -= 15
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
        "Vendre de la nourriture(+30 argent / -30 nourriture)":
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            a "Très bien commandant "
            $ argentRegionBeige += 30
            $ nourritureRegionBeige -= 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire
        "Réintégrer des soldats dans la vie civile(+30 population / -30 armee)":
            p "Je souhaite que des soldats retournent au statut de civil"
            a "Très bien commandant "
            $ populationRegionBeige += 30
            $ armeeRegionBeige -= 30
            $ regionBeigeActionFaite = True
            hide screen interactionBeige
            scene mapRegionGrise
            call screen vueTerritoire

###################################################################################################################











#############################################
##################BEIGE######################


label declarerGuerreRegionBeige:
    call screen declarerGuerreRegionBeige
screen declarerGuerreRegionBeige :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionBeige :
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionBeige :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionBeige :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionBeige:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionBeige:
            xpos 910
            ypos 170
        if(regionBeigeActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionBeige")
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("declarerGuerreRegionBeige")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90
            action  Hide("infoRegionBeige")



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

label declarerGuerreRegionJaune:
    call screen declarerGuerreRegionJaune
screen declarerGuerreRegionJaune :
    $ popUpInfoRegionOn=False
    image "../images/attaque.jpg"

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
























# Le jeu commence ici



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
