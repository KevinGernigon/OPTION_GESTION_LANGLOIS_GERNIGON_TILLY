
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
image logoAttaque = im.Scale("logoAttaque.png", 50, 50)
image btnFindeTour = "btnFinDeTour.png"



define p = Character(_('Pythie'), color="#c8ffc8")
define a = Character(_('Ministre des armées'), color="#c8ffc8")
define h = Character(_('Ministre de l"agriculture'), color="#c8ffc8")
define c = Character(_('Ministre des civils'), color="#c8ffc8")
define r = Character(_('Ministre des religions'), color="#c8ffc8")
define a = Character(_('Ambassadeur'), color="#c8ffc8")
define g = Character(_('Maitre du jeu'), color="#c8ffc8", kind = nvl)

default popUpInfoRegionOn=False


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

default jour = 0


label start:
    $ config.has_autosave = False
    $ jour += 1

    scene mapRegionGrise
    call screen vueTerritoire



transform icons :
    zoom 1



label interactionBeige :
    hide screen infoRegionBeige
    scene office
    show pythie at left
    show screen statsInteractionBeige
    call screen interactionBeige




screen statsInteractionBeige:
    image "../images/blackbox.png"
    text "Région Beige" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionBeige :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionBeige :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionBeige:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionBeige:
        xpos 1150
        ypos 20
screen interactionBeige:


    imagebutton :
        idle "boxInteragir1"
        xpos 300
        ypos 100
        action  Jump("ministreArmeeBeige")
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 100
        action  Jump("ministreAgricultureBeige")
    imagebutton :
        idle "boxInteragir3"
        xpos 300
        ypos 400
        action  Jump("ministreCivilsBeige")
    imagebutton :
        idle "boxInteragir4"
        xpos 680
        ypos 400
        action  Jump("ministreFinancesBeige")
    imagebutton :
        idle "boxInteragir5"
        xpos 490
        ypos 250
        action  Jump("ministreAmbassadeurBeige")
#armees
label ministreArmeeBeige:
    p "Assistante convoquer moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeBeige2
label ministreArmeeBeige2 :
    call screen ministreArmeeBeige2

screen ministreArmeeBeige2:
    imagebutton :
        idle "boxInteragir1"
        xpos 300
        ypos 100
        action  Jump("requisitionTroupesArmeeBeige")
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 100
        action  Jump("donTroupesArmeeBeige")

label requisitionTroupesArmeeBeige:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionBeige < 31 :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += 30
                $ armeeRegionBeige -=  30
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeBeige:
            if armeeGeneral < 31 :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionBeige += 30
                $ armeeGeneral -= 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire





#agriculture
label ministreAgricultureBeige:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureBeige2
label ministreAgricultureBeige2 :
    call screen ministreAgricultureBeige2

screen ministreAgricultureBeige2:
    imagebutton :
        idle "boxInteragir1"
        xpos 300
        ypos 100
        action  Jump("requisitionNourritureAgricultureBeige")
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 100
        action  Jump("donNourritureAgricultureBeige")

label requisitionNourritureAgricultureBeige:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionBeige < 31 :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += 30
                $ nourritureRegionBeige -= 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureBeige:
            if nourritureGeneral < 31 :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= 30
                $ nourritureRegionBeige += 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire





#civils


label ministreCivilsBeige:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsBeige2
label ministreCivilsBeige2 :
    call screen ministreCivilsBeige2

screen ministreCivilsBeige2:
    imagebutton :
        idle "boxInteragir1"
        xpos 300
        ypos 100
        action  Jump("requisitionCivilsBeige")
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 100
        action  Jump("donCivilsBeige")

label requisitionCivilsBeige:
            p "Je souhaite requisitionner des civils"
            if populationRegionBeige < 31 :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += 30
                $ populationRegionBeige -= 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsBeige:
            if populationGeneral < 31 :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= 30
                $ populationRegionBeige += 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire










#finances
label ministreFinancesBeige:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesBeige2
label ministreFinancesBeige2 :
    call screen ministreFinancesBeige2

screen ministreFinancesBeige2:
    imagebutton :
        idle "boxInteragir1"
        xpos 300
        ypos 100
        action  Jump("requisitionFinancesBeige")
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 100
        action  Jump("donFinancesBeige")

label requisitionFinancesBeige:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionBeige < 31 :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += 30
                $ argentRegionBeige -= 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesBeige:
            if argentGeneral < 31 :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= 30
                $ argentRegionBeige += 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurBeige:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurBeige2

label ministreAmbassadeurBeige2 :
    call screen ministreAmbassadeurBeige2

screen ministreAmbassadeurBeige2:
    imagebutton :
        idle "boxInteragir1"
        xpos 300
        ypos 100
        action  Jump("augmenterArmeeEmbassadeurBeige")
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 100
        action  Jump("augmenterNourritureAmbassadeurBeige")
    imagebutton :
        idle "boxInteragir2"
        xpos 300
        ypos 400
        action  Jump("vendreNourritureAmbassadeurBeige")
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 400
        action  Jump("reintegrerSoldatsAmbassadeurBeige")


label augmenterArmeeEmbassadeurBeige:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionBeige < 31 :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionBeige -= 30
                $ armeeRegionBeige += 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurBeige:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionBeige < 16 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionBeige < 16 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += 30
                $ populationRegionBeige -= 15
                $ argentRegionBeige -= 15
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurBeige:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionBeige < 31 :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionBeige += 30
                $ nourritureRegionBeige -= 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurBeige:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionBeige < 31 :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionBeige += 30
                $ armeeRegionBeige -= 30
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire









label attaqueBeige:
    hide screen infoRegionBeige
    call screen attaqueBeige
screen attaqueBeige:
    if regionJauneActive==False:
        imagebutton:
            idle "regionJauneRouge.png"
            xpos 370
            ypos 90
            action Jump("beigeAttaqueJaune")
        image "logoAttaque":
            xpos 575
            ypos 200
    if regionGriseActive==False:
        imagebutton:
            idle "regionGriseRouge.png"
            xpos 265
            ypos 45
            action Jump("beigeAttaqueGrise")
        image "logoAttaque":
            xpos 450
            ypos 50

label beigeAttaqueGrise:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionGrise :
        $ armeeRegionBeige -=armeeRegionGrise
        $ armeeRegionGrise = 0
        $ regionGriseActive=True
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionGrise:
        $ armeeRegionGrise-=armeeRegionBeige
        $ armeeRegionBeige =0
        call screen vueTerritoire

label beigeAttaqueJaune:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionJaune :
        $ armeeRegionBeige -=armeeRegionJaune
        $ armeeRegionJaune = 0
        $ regionJauneActive=True
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionJaune:
        $ armeeRegionJaune-=armeeRegionBeige
        $ armeeRegionBeige =0
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
        if (regionJauneActive==False or regionGriseActive==False) and regionBeigeActionFaite==False:
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueBeige")
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
transform dezoom_icons_generales:
    zoom 0.2


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

    imagebutton :
        idle "btnFindeTour"
        xpos 1021
        ypos 635
        action  Jump("victoire")







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

    $ armeeRegionBeige += armeeRegionBeige * multiplier
    $ argentRegionBeige += argentRegionBeige * multiplier
    $ populationRegionBeige += populationRegionBeige * multiplier
    $ nourritureRegionBeige += nourritureRegionBeige * multiplier


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
