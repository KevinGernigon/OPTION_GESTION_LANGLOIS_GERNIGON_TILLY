
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
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionGrise :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionGrise :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionGrise:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionGrise:
            xpos 910
            ypos 170
        if(regionGriseActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionGrise")
        if (regionJauneActive==False or regionBeigeActive==False or regionRoseActive==False ) and regionGriseActionFaite==False:
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueGrise")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90
            action  Hide("infoRegionGrise")










########################################################################################################################
########################################################################################################################







label interactionGrise :
    hide screen infoRegionGrise
    scene office
    show pythie at left
    show screen statsInteractionGrise
    call screen interactionGrise
screen statsInteractionGrise:
    image "../images/blackbox.png"
    text "Région Grise" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionGrise :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionGrise :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionGrise:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionGrise:
        xpos 1150
        ypos 20

screen interactionGrise:
    imagebutton :
        idle "boxInteragir1"
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeGrise")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureGrise")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsGrise")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesGrise")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurGrise")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionGrise")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeGrise:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeGrise2
label ministreArmeeGrise2 :
    call screen ministreArmeeGrise2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeGrise2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeGrise2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeGrise")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGrise"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeGrise")
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
        idle "armyGrise"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeGrise")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeGrise")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeGrise:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionGrise < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionGrise -=  variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire

label donTroupesArmeeGrise:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionGrise += variableJauge
                $ armeeGeneral -= variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire










#agriculture
label ministreAgricultureGrise:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureGrise2
label ministreAgricultureGrise2 :
    call screen ministreAgricultureGrise2


screen ministreAgricultureGrise2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureGrise2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureGrise")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGrise"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureGrise")
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
        idle "foodGrise"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureGrise")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureGrise")
    text " -%d" % variableJauge:
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureGrise:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionGrise < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionGrise -= variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire

label donNourritureAgricultureGrise:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionGrise += variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire


#civils


label ministreCivilsGrise:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsGrise2
label ministreCivilsGrise2 :
    call screen ministreCivilsGrise2

screen ministreCivilsGrise2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsGrise2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsGrise")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGrise"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsGrise")
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
        idle "popGrise"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsGrise")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsGrise")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsGrise:
            p "Je souhaite requisitionner des civils"
            if populationRegionGrise < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionGrise -= variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire

label donCivilsGrise:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionGrise += variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire



#finances
label ministreFinancesGrise:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesGrise2
label ministreFinancesGrise2 :
    call screen ministreFinancesGrise2

screen ministreFinancesGrise2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesGrise2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesGrise")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGrise"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesGrise")
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
        idle "financesGrise"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesGrise")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesGrise")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesGrise:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionGrise < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionGrise -= variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire

label donFinancesGrise:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionGrise += variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurGrise:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurGrise2

label ministreAmbassadeurGrise2 :
    call screen ministreAmbassadeurGrise2

screen ministreAmbassadeurGrise2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurGrise2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGrise"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurGrise")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGrise"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurGrise")
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
        idle "foodGrise"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurGrise")
    text " +%d" % variableJauge:
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGrise"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurGrise")
    text " -%d" % variableJaugeDiv2:
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGrise"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurGrise")
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
        idle "financesGrise"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurGrise")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGrise"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurGrise")
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
        idle "popGrise"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurGrise")
    text " +%d" % variableJauge:
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGrise"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurGrise")
    text " -%d" % variableJauge:
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurGrise:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionGrise < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionGrise -= variableJauge
                $ armeeRegionGrise += variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire

label augmenterNourritureAmbassadeurGrise:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionGrise < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            if populationRegionGrise < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionGrise -= variableJaugeDiv2
                $ argentRegionGrise -= variableJaugeDiv2
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire

label vendreNourritureAmbassadeurGrise:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionGrise < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionGrise += variableJauge
                $ nourritureRegionGrise -= variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurGrise:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionGrise < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionGrise += variableJauge
                $ armeeRegionGrise -= variableJauge
                $ regionGriseActionFaite = True
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire



label attaqueGrise:
    hide screen infoRegionGrise
    call screen attaqueGrise
screen attaqueGrise:
    if regionJauneActive==False:
        imagebutton:
            idle "regionJauneRouge.png"
            xpos 370
            ypos 90
            action Jump("griseAttaqueJaune")
        image "logoAttaque":
            xpos 575
            ypos 200
    if regionBeigeActive==False:
        imagebutton:
            idle "regionBeigeRouge.png"
            xpos 265
            ypos 45
            action Jump("griseAttaqueBeige")
        image "logoAttaque":
            xpos 450
            ypos 50

#negociation guerre de grise vers grise
screen negociationGriseBeige:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationGriseBeige")
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
        action  Jump("refusNegociationGriseBeige")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationGriseBeige:
    if armeeRegionGrise>=armeeRegionBeige :
        $ armeeRegionGrise -=armeeRegionBeige
        $ armeeRegionBeige = 0
        $ regionBeigeActive=True
        hide screen statsInteractionGrise
        hide screen negociationGriseBeige
        scene mapRegionBeige
        call screen vueTerritoire
    elif armeeRegionGrise<armeeRegionBeige:
        $ armeeRegionBeige-=armeeRegionGrise
        $ armeeRegionGrise =0
        $ regionGriseActive = False
        hide screen statsInteractionGrise
        hide screen negociationGriseBeige
        scene mapRegionBeige
        call screen vueTerritoire

label acceptationNegociationGriseBeige:
    if armeeRegionGrise>=armeeRegionBeige :
        $ argentRegionGrise += argentRegionBeige//4
        $ argentRegionBeige -= argentRegionBeige//4
        hide screen statsInteractionGrise
        hide screen negociationGriseBeige
        scene mapRegionBeige
        call screen vueTerritoire
    elif armeeRegionGrise<armeeRegionBeige:
        $ argentRegionGrise -= argentRegionGrise//2
        $ argentRegionBeige += argentRegionGrise//2
        hide screen statsInteractionGrise
        hide screen negociationGriseBeige
        scene mapRegionBeige
        call screen vueTerritoire

label griseAttaqueBeige:
    $regionGriseActionFaite=True
    if armeeRegionGrise>=armeeRegionBeige :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionGrise
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationGriseBeige
    elif armeeRegionGrise<armeeRegionBeige:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionGrise
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationGriseBeige

#negociation guerre de grise vers jaune
screen negociationGriseJaune:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationGriseJaune")
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
        action  Jump("refusNegociationGriseJaune")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationGriseJaune:
    if armeeRegionGrise>=armeeRegionJaune :
        $ armeeRegionGrise -=armeeRegionJaune
        $ armeeRegionJaune = 0
        $ regionJauneActive=True
        hide screen statsInteractionGrise
        hide screen negociationGriseJaune
        scene mapRegionBeige
        call screen vueTerritoire
    elif armeeRegionGrise<armeeRegionJaune:
        $ armeeRegionJaune-=armeeRegionGrise
        $ armeeRegionGrise =0
        hide screen statsInteractionGrise
        hide screen negociationGriseJaune
        scene mapRegionBeige
        call screen vueTerritoire

label acceptationNegociationGriseJaune:
    if armeeRegionGrise>=armeeRegionJaune :
        $ argentRegionGrise += argentRegionJaune//4
        $ argentRegionJaune -= argentRegionJaune//4
        hide screen statsInteractionGrise
        hide screen negociationGriseJaune
        scene mapRegionBeige
        call screen vueTerritoire
    elif armeeRegionGrise<armeeRegionJaune:
        $ argentRegionGrise -= argentRegionGrise//2
        $ argentRegionJaune += argentRegionGrise//2
        hide screen statsInteractionGrise
        hide screen negociationGriseJaune
        scene mapRegionBeige
        call screen vueTerritoire

label griseAttaqueJaune:
    $regionGriseActionFaite=True
    if armeeRegionGrise>=armeeRegionJaune :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionGrise
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationGriseJaune
    elif armeeRegionGrise<armeeRegionJaune:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionGrise
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationGriseJaune


#------------------------------------------------------------------------------------------------------

label upgradeRegionGrise:
    hide screen infoRegionGrise
    call screen upgradeRegionGrise
screen upgradeRegionGrise:
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

label upgradeChoixGrise1:
    if argentRegionGrise >  50 and populationRegionGrise > 50 and nourritureRegionGrise > 25 :
        if niveauRegionGrise<6 :
            $regionGriseActionFaite=True
            $ argentRegionGrise -= 50
            $ populationRegionGrise -=50
            $ nourritureRegionGrise-=25
            $ niveauRegionGrise+=1
            hide screen statsInteractionGrise
            scene mapRegionBeige
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"
    else :
        a "Il vous manque des ressources "
        hide screen statsInteractionGrise
        scene mapRegionBeige
        call screen vueTerritoire

label upgradeChoixGrise2:
            if argentRegionGrise > 130 and populationRegionGrise > 130 and nourritureRegionGrise > 65 :
                if niveauRegionGrise<6 :
                    $regionGriseActionFaite=True
                    $ argentRegionGrise -= 130
                    $ populationRegionGrise -= 130
                    $ nourritureRegionGrise-=35
                    $ niveauRegionGrise+=3
                    hide screen statsInteractionGrise
                    scene mapRegionBeige
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"
            else :
                a "Il vous manque des ressources "
                hide screen statsInteractionGrise
                scene mapRegionBeige
                call screen vueTerritoire
