
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










########################################################################################################################
########################################################################################################################







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
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeBeige")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureBeige")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsBeige")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesBeige")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurBeige")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionBeige")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeBeige:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeBeige2
label ministreArmeeBeige2 :
    call screen ministreArmeeBeige2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeBeige2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeBeige2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeBeige")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyBeige"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeBeige")
    text " -%d" % variableJauge:
        xpos 400
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Réquisition de soldats":
        xpos 250
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "armyBeige"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeBeige")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeBeige")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeBeige:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionBeige < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionBeige -=  variableJauge
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeBeige:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionBeige += variableJauge
                $ armeeGeneral -= variableJauge
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
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureBeige2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureBeige")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodBeige"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureBeige")
    text " -%d" % variableJauge:
        xpos 400
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Réquisition de nourriture":
        xpos 250
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "foodBeige"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureBeige")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureBeige")
    text " -%d" % variableJauge:
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureBeige:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionBeige < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionBeige -= variableJauge
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureBeige:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionBeige += variableJauge
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
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsBeige2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsBeige")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBeige"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsBeige")
    text " -%d" % variableJauge:
        xpos 400
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Réquisition de civils":
        xpos 270
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "popBeige"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsBeige")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsBeige")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsBeige:
            p "Je souhaite requisitionner des civils"
            if populationRegionBeige < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionBeige -= variableJauge
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsBeige:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionBeige += variableJauge
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
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesBeige2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesBeige")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesBeige"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesBeige")
    text " -%d" % variableJauge:
        xpos 400
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Réquisition d'argent":
        xpos 260
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "financesBeige"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesBeige")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesBeige")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesBeige:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionBeige < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionBeige -= variableJauge
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesBeige:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionBeige += variableJauge
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
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurBeige2"), Jump("variableJauge")]
    imagebutton :
        idle "armyBeige"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurBeige")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBeige"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurBeige")
    text " -%d" % variableJauge:
        xalign 0.38
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    text "Entraînement de soldats":
        xpos 310
        yalign 0.45
        outlines [ (3, "#000", 0, 0) ]

#choix haut-droite
    imagebutton :
        idle "foodBeige"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurBeige")
    text " +%d" % variableJauge:
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBeige"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurBeige")
    text " -%d" % variableJaugeDiv2:
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesBeige"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurBeige")
    text " -%d" % variableJaugeDiv2:
        xalign 0.78
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    text "Production de nourriture":
        xpos 750
        yalign 0.45
        outlines [ (3, "#000", 0, 0) ]

#choix bas-gauche
    imagebutton :
        idle "financesBeige"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurBeige")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodBeige"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurBeige")
    text " -%d" % variableJauge:
        xalign 0.38
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Vente de nourriture":
        xpos 330
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]

#choix bas-droite
    imagebutton :
        idle "popBeige"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurBeige")
    text " +%d" % variableJauge:
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyBeige"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurBeige")
    text " -%d" % variableJauge:
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurBeige:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionBeige < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionBeige -= variableJauge
                $ armeeRegionBeige += variableJauge
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurBeige:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionBeige < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionBeige < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionBeige -= variableJaugeDiv2
                $ argentRegionBeige -= variableJaugeDiv2
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurBeige:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionBeige < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionBeige += variableJauge
                $ nourritureRegionBeige -= variableJauge
                $ regionBeigeActionFaite = True
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurBeige:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionBeige < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionBeige += variableJauge
                $ armeeRegionBeige -= variableJauge
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

#negociation guerre de beige vers grise
screen negociationBeigeGrise:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBeigeGrise")
    text "Accepter" :
        xpos 280
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "refus"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("refusNegociationBeigeGrise")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBeigeGrise:
    if armeeRegionBeige>=armeeRegionGrise :
        $ armeeRegionBeige -=armeeRegionGrise
        $ armeeRegionGrise = 0
        $ regionGriseActive=True
        hide screen statsInteractionBeige
        hide screen negociationBeigeGrise
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionGrise:
        $ armeeRegionGrise-=armeeRegionBeige
        $ armeeRegionBeige =0
        $ regionBeigeActive = False
        hide screen statsInteractionBeige
        hide screen negociationBeigeGrise
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBeigeGrise:
    if armeeRegionBeige>=armeeRegionGrise :
        $ argentRegionBeige += argentRegionGrise//4
        $ argentRegionGrise -= argentRegionGrise//4
        hide screen statsInteractionBeige
        hide screen negociationBeigeGrise
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionGrise:
        $ argentRegionBeige -= argentRegionBeige//2
        $ argentRegionGrise += argentRegionBeige//2
        hide screen statsInteractionBeige
        hide screen negociationBeigeGrise
        scene mapRegionGrise
        call screen vueTerritoire

label beigeAttaqueGrise:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionGrise :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBeigeGrise
    elif armeeRegionBeige<armeeRegionGrise:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBeigeGrise

#negociation guerre de beige vers jaune
screen negociationBeigeJaune:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBeigeJaune")
    text "Accepter" :
        xpos 280
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "refus"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("refusNegociationBeigeJaune")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBeigeJaune:
    if armeeRegionBeige>=armeeRegionJaune :
        $ armeeRegionBeige -=armeeRegionJaune
        $ armeeRegionJaune = 0
        $ regionJauneActive=True
        hide screen statsInteractionBeige
        hide screen negociationBeigeJaune
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionJaune:
        $ armeeRegionJaune-=armeeRegionBeige
        $ armeeRegionBeige =0
        hide screen statsInteractionBeige
        hide screen negociationBeigeJaune
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBeigeJaune:
    if armeeRegionBeige>=armeeRegionJaune :
        $ argentRegionBeige += argentRegionJaune//4
        $ argentRegionJaune -= argentRegionJaune//4
        hide screen statsInteractionBeige
        hide screen negociationBeigeJaune
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionJaune:
        $ argentRegionBeige -= argentRegionBeige//2
        $ argentRegionJaune += argentRegionBeige//2
        hide screen statsInteractionBeige
        hide screen negociationBeigeJaune
        scene mapRegionGrise
        call screen vueTerritoire

label beigeAttaqueJaune:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionJaune :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBeigeJaune
    elif armeeRegionBeige<armeeRegionJaune:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBeigeJaune

#negociation guerre de beige vers rose
screen negociationBeigeRose:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBeigeRose")
    text "Accepter" :
        xpos 280
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "refus"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("refusNegociationBeigeRose")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBeigeRose:
    if armeeRegionBeige>=armeeRegionRose :
        $ armeeRegionBeige -=armeeRegionRose
        $ armeeRegionRose = 0
        $ regionRoseActive=True
        hide screen statsInteractionBeige
        hide screen negociationBeigeRose
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionRose:
        $ armeeRegionRose-=armeeRegionBeige
        $ armeeRegionBeige =0
        hide screen statsInteractionBeige
        hide screen negociationBeigeRose
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBeigeRose:
    if armeeRegionBeige>=armeeRegionRose :
        $ argentRegionBeige += argentRegionRose//4
        $ argentRegionRose -= argentRegionRose//4
        hide screen statsInteractionBeige
        hide screen negociationBeigeRose
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionRose:
        $ argentRegionBeige -= argentRegionBeige//2
        $ argentRegionRose += argentRegionBeige//2
        hide screen statsInteractionBeige
        hide screen negociationBeigeRose
        scene mapRegionGrise
        call screen vueTerritoire

label beigeAttaqueRose:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionRose :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBeigeRose
    elif armeeRegionBeige<armeeRegionRose:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBeigeRose

#negociation guerre de beige vers orange --------------------------------------------------------------

screen negociationBeigeOrange:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBeigeOrange")
    text "Accepter" :
        xpos 280
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "refus"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("refusNegociationBeigeOrange")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBeigeOrange:
    if armeeRegionBeige>=armeeRegionOrange :
        $ armeeRegionBeige -=armeeRegionOrange
        $ armeeRegionOrange = 0
        $ regionOrangeActive=True
        hide screen statsInteractionBeige
        hide screen negociationBeigeOrange
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionOrange:
        $ armeeRegionOrange-=armeeRegionBeige
        $ armeeRegionBeige =0
        hide screen statsInteractionBeige
        hide screen negociationBeigeOrange
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBeigeOrange:
    if armeeRegionBeige>=armeeRegionOrange :
        $ argentRegionBeige += argentRegionOrange//4
        $ argentRegionOrange -= argentRegionOrange//4
        hide screen statsInteractionBeige
        hide screen negociationBeigeOrange
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionOrange:
        $ argentRegionBeige -= argentRegionBeige//2
        $ argentRegionOrange += argentRegionBeige//2
        hide screen statsInteractionBeige
        hide screen negociationBeigeOrange
        scene mapRegionGrise
        call screen vueTerritoire

label beigeAttaqueOrange:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionOrange :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBeigeOrange
    elif armeeRegionBeige<armeeRegionOrange:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBeigeOrange

#negociation guerre de beige vers Violet --------------------------------------------------------------

screen negociationBeigeViolet:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBeigeViolet")
    text "Accepter" :
        xpos 280
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "refus"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("refusNegociationBeigeViolet")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBeigeViolet:
    if armeeRegionBeige>=armeeRegionViolet :
        $ armeeRegionBeige -=armeeRegionViolet
        $ armeeRegionViolet = 0
        $ regionVioletActive=True
        hide screen statsInteractionBeige
        hide screen negociationBeigeViolet
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionViolet:
        $ armeeRegionViolet-=armeeRegionBeige
        $ armeeRegionBeige =0
        hide screen statsInteractionBeige
        hide screen negociationBeigeViolet
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBeigeViolet:
    if armeeRegionBeige>=armeeRegionViolet :
        $ argentRegionBeige += argentRegionViolet//4
        $ argentRegionViolet -= argentRegionViolet//4
        hide screen statsInteractionBeige
        hide screen negociationBeigeViolet
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionViolet:
        $ argentRegionBeige -= argentRegionBeige//2
        $ argentRegionViolet += argentRegionBeige//2
        hide screen statsInteractionBeige
        hide screen negociationBeigeViolet
        scene mapRegionGrise
        call screen vueTerritoire

label beigeAttaqueViolet:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionViolet :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBeigeViolet
    elif armeeRegionBeige<armeeRegionViolet:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBeigeViolet

#negociation guerre de beige vers Bleue --------------------------------------------------------------

screen negociationBeigeBleue:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBeigeBleue")
    text "Accepter" :
        xpos 280
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "refus"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("refusNegociationBeigeBleue")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBeigeBleue:
    if armeeRegionBeige>=armeeRegionBleue :
        $ armeeRegionBeige -=armeeRegionBleue
        $ armeeRegionBleue = 0
        $ regionBleueActive=True
        hide screen statsInteractionBeige
        hide screen negociationBeigeBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionBleue:
        $ armeeRegionBleue-=armeeRegionBeige
        $ armeeRegionBeige =0
        hide screen statsInteractionBeige
        hide screen negociationBeigeBleue
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBeigeBleue:
    if armeeRegionBeige>=armeeRegionBleue :
        $ argentRegionBeige += argentRegionBleue//4
        $ argentRegionBleue -= argentRegionBleue//4
        hide screen statsInteractionBeige
        hide screen negociationBeigeBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionBleue:
        $ argentRegionBeige -= argentRegionBeige//2
        $ argentRegionBleue += argentRegionBeige//2
        hide screen statsInteractionBeige
        hide screen negociationBeigeBleue
        scene mapRegionGrise
        call screen vueTerritoire

label beigeAttaqueBleue:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionBleue :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBeigeBleue
    elif armeeRegionBeige<armeeRegionBleue:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBeigeBleue

#negociation guerre de beige vers Rouge --------------------------------------------------------------

screen negociationBeigeRouge:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBeigeRouge")
    text "Accepter" :
        xpos 280
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "refus"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("refusNegociationBeigeRouge")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBeigeRouge:
    if armeeRegionBeige>=armeeRegionRouge :
        $ armeeRegionBeige -=armeeRegionRouge
        $ armeeRegionRouge = 0
        $ regionRougeActive=True
        hide screen statsInteractionBeige
        hide screen negociationBeigeRouge
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionRouge:
        $ armeeRegionRouge-=armeeRegionBeige
        $ armeeRegionBeige =0
        hide screen statsInteractionBeige
        hide screen negociationBeigeRouge
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBeigeRouge:
    if armeeRegionBeige>=armeeRegionRouge :
        $ argentRegionBeige += argentRegionRouge//4
        $ argentRegionRouge -= argentRegionRouge//4
        hide screen statsInteractionBeige
        hide screen negociationBeigeRouge
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionRouge:
        $ argentRegionBeige -= argentRegionBeige//2
        $ argentRegionRouge += argentRegionBeige//2
        hide screen statsInteractionBeige
        hide screen negociationBeigeRouge
        scene mapRegionGrise
        call screen vueTerritoire

label beigeAttaqueRouge:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionRouge :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBeigeRouge
    elif armeeRegionBeige<armeeRegionRouge:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBeigeRouge

#negociation guerre de beige vers Verte --------------------------------------------------------------

screen negociationBeigeVerte:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBeigeVerte")
    text "Accepter" :
        xpos 280
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
#choix droite
    imagebutton :
        idle "refus"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("refusNegociationBeigeVerte")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBeigeVerte:
    if armeeRegionBeige>=armeeRegionVerte :
        $ armeeRegionBeige -=armeeRegionVerte
        $ armeeRegionVerte = 0
        $ regionVerteActive=True
        hide screen statsInteractionBeige
        hide screen negociationBeigeVerte
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionVerte:
        $ armeeRegionVerte-=armeeRegionBeige
        $ armeeRegionBeige =0
        hide screen statsInteractionBeige
        hide screen negociationBeigeVerte
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBeigeVerte:
    if armeeRegionBeige>=armeeRegionVerte :
        $ argentRegionBeige += argentRegionVerte//4
        $ argentRegionVerte -= argentRegionVerte//4
        hide screen statsInteractionBeige
        hide screen negociationBeigeVerte
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBeige<armeeRegionVerte:
        $ argentRegionBeige -= argentRegionBeige//2
        $ argentRegionVerte += argentRegionBeige//2
        hide screen statsInteractionBeige
        hide screen negociationBeigeVerte
        scene mapRegionGrise
        call screen vueTerritoire

label beigeAttaqueVerte:
    $regionBeigeActionFaite=True
    if armeeRegionBeige>=armeeRegionVerte :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBeigeVerte
    elif armeeRegionBeige<armeeRegionVerte:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBeige
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBeigeVerte

#------------------------------------------------------------------------------------------------------

label upgradeRegionBeige:
    hide screen infoRegionBeige
    call screen upgradeRegionBeige
screen upgradeRegionBeige:
    imagebutton :
        idle "upgrade1"
        xalign 0.3
        yalign 0.5
        action  Jump("upgradeChoix1")
    imagebutton :
        idle "upgrade2"
        xalign 0.7
        yalign 0.5
        action  Jump("upgradeChoix2")

label upgradeChoix1:
    if argentRegionBeige >  50 and populationRegionBeige > 50 and nourritureRegionBeige > 25 :
        if niveauRegionBeige<6 :
            $regionBeigeActionFaite=True
            $ argentRegionBeige -= 50
            $ populationRegionBeige -=50
            $ nourritureRegionBeige-=25
            $ niveauRegionBeige+=1
            hide screen statsInteractionBeige
            scene mapRegionGrise
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"
    else :
        a "Il vous manque des ressources "
        hide screen statsInteractionBeige
        scene mapRegionGrise
        call screen vueTerritoire

label upgradeChoix2:
            if argentRegionBeige > 130 and populationRegionBeige > 130 and nourritureRegionBeige > 65 :
                if niveauRegionBeige<6 :
                    $regionBeigeActionFaite=True
                    $ argentRegionBeige -= 130
                    $ populationRegionBeige -= 130
                    $ nourritureRegionBeige-=35
                    $ niveauRegionBeige+=3
                    hide screen statsInteractionBeige
                    scene mapRegionGrise
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"
            else :
                a "Il vous manque des ressources "
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire
