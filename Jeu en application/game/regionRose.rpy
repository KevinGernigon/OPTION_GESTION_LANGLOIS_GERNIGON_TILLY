

transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionRose :
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionRose :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionRose :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionRose:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionRose:
            xpos 910
            ypos 170
        if(regionRoseActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionRose")
        if (regionJauneActive==False or regionGriseActive==False or regionOrangeActive==False or regionBleueActive==False) and regionRoseActionFaite==False:
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueRose")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90
            action  Hide("infoRegionRose")










########################################################################################################################
########################################################################################################################







label interactionRose :
    hide screen infoRegionRose
    scene office
    show pythie at left
    show screen statsInteractionRose
    call screen interactionRose
screen statsInteractionRose:
    image "../images/blackbox.png"
    text "Région Rose" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionRose :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionRose :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionRose:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionRose:
        xpos 1150
        ypos 20

screen interactionRose:
    imagebutton :
        idle "boxInteragir1"
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeRose")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureRose")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsRose")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesRose")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurRose")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionRose")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeRose:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeRose2
label ministreArmeeRose2 :
    call screen ministreArmeeRose2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeRose2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeRose2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeRose")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyRose"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeRose")
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
        idle "armyRose"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeRose")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeRose")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeRose:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionRose < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionRose -=  variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeRose:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionRose += variableJauge
                $ armeeGeneral -= variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire










#agriculture
label ministreAgricultureRose:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureRose2
label ministreAgricultureRose2 :
    call screen ministreAgricultureRose2


screen ministreAgricultureRose2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureRose2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureRose")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodRose"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureRose")
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
        idle "foodRose"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureRose")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureRose")
    text " -%d" % variableJauge:
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureRose:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionRose < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionRose -= variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureRose:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionRose += variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire


#civils


label ministreCivilsRose:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsRose2
label ministreCivilsRose2 :
    call screen ministreCivilsRose2

screen ministreCivilsRose2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsRose2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsRose")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popRose"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsRose")
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
        idle "popRose"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsRose")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsRose")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsRose:
            p "Je souhaite requisitionner des civils"
            if populationRegionRose < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionRose -= variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsRose:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionRose += variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire



#finances
label ministreFinancesRose:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesRose2
label ministreFinancesRose2 :
    call screen ministreFinancesRose2

screen ministreFinancesRose2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesRose2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesRose")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesRose"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesRose")
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
        idle "financesRose"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesRose")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesRose")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesRose:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionRose < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionRose -= variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesRose:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionRose += variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurRose:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurRose2

label ministreAmbassadeurRose2 :
    call screen ministreAmbassadeurRose2

screen ministreAmbassadeurRose2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurRose2"), Jump("variableJauge")]
    imagebutton :
        idle "armyRose"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurRose")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popRose"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurRose")
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
        idle "foodRose"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurRose")
    text " +%d" % variableJauge:
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popRose"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurRose")
    text " -%d" % variableJaugeDiv2:
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesRose"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurRose")
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
        idle "financesRose"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurRose")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodRose"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurRose")
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
        idle "popRose"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurRose")
    text " +%d" % variableJauge:
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyRose"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurRose")
    text " -%d" % variableJauge:
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurRose:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionRose < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionRose -= variableJauge
                $ armeeRegionRose += variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurRose:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionRose < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionRose < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionRose -= variableJaugeDiv2
                $ argentRegionRose -= variableJaugeDiv2
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurRose:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionRose < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionRose += variableJauge
                $ nourritureRegionRose -= variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurRose:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionRose < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionRose += variableJauge
                $ armeeRegionRose -= variableJauge
                $ regionRoseActionFaite = True
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire



label attaqueRose:
    hide screen infoRegionRose
    call screen attaqueRose
screen attaqueRose:
    if regionJauneActive==False:
        imagebutton:
            idle "regionJauneRouge.png"
            xpos 370
            ypos 90
            action Jump("roseAttaqueJaune")
        image "logoAttaque":
            xpos 575
            ypos 200
    if regionGriseActive==False:
        imagebutton:
            idle "regionGriseRouge.png"
            xpos 265
            ypos 45
            action Jump("roseAttaqueGrise")
        image "logoAttaque":
            xpos 450
            ypos 50
    if regionBleueActive==False:
        imagebutton:
            idle "regionBleueRouge.png"
            xpos 420
            ypos 280
            action Jump("roseAttaqueBleue")
        image "logoAttaque":
            xpos 550
            ypos 350
    if regionOrangeActive==False:
        imagebutton:
            idle "regionOrangeRouge.png"
            xpos 160
            ypos 302
            action Jump("roseAttaqueOrange")
        image "logoAttaque":
            xpos 350
            ypos 350

#negociation guerre de rose vers grise
screen negociationRoseGrise:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationRoseGrise")
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
        action  Jump("refusNegociationRoseGrise")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationRoseGrise:
    if armeeRegionRose>=armeeRegionGrise :
        $ armeeRegionRose -=armeeRegionGrise
        $ armeeRegionGrise = 0
        $ regionGriseActive=True
        hide screen statsInteractionRose
        hide screen negociationRoseGrise
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionRose<armeeRegionGrise:
        $ armeeRegionGrise-=armeeRegionRose
        $ armeeRegionRose =0
        $ regionRoseActive = False
        hide screen statsInteractionRose
        hide screen negociationRoseGrise
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationRoseGrise:
    if armeeRegionRose>=armeeRegionGrise :
        $ argentRegionRose += argentRegionGrise//4
        $ argentRegionGrise -= argentRegionGrise//4
        hide screen statsInteractionRose
        hide screen negociationRoseGrise
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionRose<armeeRegionGrise:
        $ argentRegionRose -= argentRegionRose//2
        $ argentRegionGrise += argentRegionRose//2
        hide screen statsInteractionRose
        hide screen negociationRoseGrise
        scene mapRegionGrise
        call screen vueTerritoire

label roseAttaqueGrise:
    $regionRoseActionFaite=True
    if armeeRegionRose>=armeeRegionGrise :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionRose
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationRoseGrise
    elif armeeRegionRose<armeeRegionGrise:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionRose
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationRoseGrise

#negociation guerre de rose vers jaune
screen negociationRoseJaune:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationRoseJaune")
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
        action  Jump("refusNegociationRoseJaune")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationRoseJaune:
    if armeeRegionRose>=armeeRegionJaune :
        $ armeeRegionRose -=armeeRegionJaune
        $ armeeRegionJaune = 0
        $ regionJauneActive=True
        hide screen statsInteractionRose
        hide screen negociationRoseJaune
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionRose<armeeRegionJaune:
        $ armeeRegionJaune-=armeeRegionRose
        $ armeeRegionRose =0
        hide screen statsInteractionRose
        hide screen negociationRoseJaune
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationRoseJaune:
    if armeeRegionRose>=armeeRegionJaune :
        $ argentRegionRose += argentRegionJaune//4
        $ argentRegionJaune -= argentRegionJaune//4
        hide screen statsInteractionRose
        hide screen negociationRoseJaune
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionRose<armeeRegionJaune:
        $ argentRegionRose -= argentRegionRose//2
        $ argentRegionJaune += argentRegionRose//2
        hide screen statsInteractionRose
        hide screen negociationRoseJaune
        scene mapRegionGrise
        call screen vueTerritoire

label roseAttaqueJaune:
    $regionRoseActionFaite=True
    if armeeRegionRose>=armeeRegionJaune :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionRose
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationRoseJaune
    elif armeeRegionRose<armeeRegionJaune:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionRose
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationRoseJaune





label upgradeRegionRose:
    hide screen infoRegionRose
    call screen upgradeRegionRose
screen upgradeRegionRose:
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

label upgradeChoixRose1:
    if argentRegionRose >  50 and populationRegionRose > 50 and nourritureRegionRose > 25 :
        if niveauRegionRose<6 :
            $regionRoseActionFaite=True
            $ argentRegionRose -= 50
            $ populationRegionRose -=50
            $ nourritureRegionRose-=25
            $ niveauRegionRose+=1
            hide screen statsInteractionRose
            scene mapRegionGrise
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"
    else :
        a "Il vous manque des ressources (il vous faut 50 d'argent, 50 de population et 25 de nourriture pour améliorer votre territoire(niv max : 6))"
        hide screen statsInteractionRose
        scene mapRegionGrise
        call screen vueTerritoire

label upgradeChoixRose2:
            if argentRegionRose > 130 and populationRegionRose > 130 and nourritureRegionRose > 65 :
                if niveauRegionRose<6 :
                    $regionRoseActionFaite=True
                    $ argentRegionRose -= 130
                    $ populationRegionRose -= 130
                    $ nourritureRegionRose-=65
                    $ niveauRegionRose+=3
                    hide screen statsInteractionRose
                    scene mapRegionGrise
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"
            else :
                a "Il vous manque des ressources (il vous faut 130 d'argent, 130 de population et 65 de nourriture pour améliorer votre territoire de trois niveaux (niv max : 6))"
                hide screen statsInteractionRose
                scene mapRegionGrise
                call screen vueTerritoire
