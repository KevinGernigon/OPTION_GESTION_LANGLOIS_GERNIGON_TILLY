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
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionOrange :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionOrange :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionOrange:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionOrange:
            xpos 910
            ypos 170
        if(regionOrangeActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionOrange")
        if (regionBleueActive==False or regionVioletteActive==False or regionRoseActive==False ) and regionOrangeActionFaite==False:
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueOrange")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90
            action  Hide("infoRegionOrange")










########################################################################################################################
########################################################################################################################







label interactionOrange :
    hide screen infoRegionOrange
    scene office
    show pythie at left
    show screen statsInteractionOrange
    call screen interactionOrange
screen statsInteractionOrange:
    image "../images/blackbox.png"
    text "Région Orange" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionOrange :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionOrange :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionOrange:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionOrange:
        xpos 1150
        ypos 20

screen interactionOrange:
    imagebutton :
        idle "boxInteragir1"
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeOrange")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureOrange")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsOrange")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesOrange")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurOrange")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionOrange")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeOrange:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeOrange2
label ministreArmeeOrange2 :
    call screen ministreArmeeOrange2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeOrange2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeOrange2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeOrange")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyOrange"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeOrange")
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
        idle "armyOrange"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeOrange")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeOrange")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeOrange:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionOrange < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionOrange -=  variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeOrange:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionOrange += variableJauge
                $ armeeGeneral -= variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire










#agriculture
label ministreAgricultureOrange:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureOrange2
label ministreAgricultureOrange2 :
    call screen ministreAgricultureOrange2


screen ministreAgricultureOrange2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureOrange2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureOrange")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodOrange"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureOrange")
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
        idle "foodOrange"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureOrange")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureOrange")
    text " -%d" % variableJauge:
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureOrange:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionOrange < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionOrange -= variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureOrange:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionOrange += variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire


#civils


label ministreCivilsOrange:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsOrange2
label ministreCivilsOrange2 :
    call screen ministreCivilsOrange2

screen ministreCivilsOrange2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsOrange2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsOrange")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popOrange"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsOrange")
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
        idle "popOrange"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsOrange")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsOrange")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsOrange:
            p "Je souhaite requisitionner des civils"
            if populationRegionOrange < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionOrange -= variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsOrange:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionOrange += variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire



#finances
label ministreFinancesOrange:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesOrange2
label ministreFinancesOrange2 :
    call screen ministreFinancesOrange2

screen ministreFinancesOrange2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesOrange2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesOrange")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesOrange"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesOrange")
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
        idle "financesOrange"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesOrange")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesOrange")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesOrange:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionOrange < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionOrange -= variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesOrange:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionOrange += variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurOrange:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurOrange2

label ministreAmbassadeurOrange2 :
    call screen ministreAmbassadeurOrange2

screen ministreAmbassadeurOrange2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurOrange2"), Jump("variableJauge")]
    imagebutton :
        idle "armyOrange"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurOrange")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popOrange"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurOrange")
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
        idle "foodOrange"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurOrange")
    text " +%d" % variableJauge:
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popOrange"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurOrange")
    text " -%d" % variableJaugeDiv2:
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesOrange"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurOrange")
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
        idle "financesOrange"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurOrange")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodOrange"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurOrange")
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
        idle "popOrange"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurOrange")
    text " +%d" % variableJauge:
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyOrange"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurOrange")
    text " -%d" % variableJauge:
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurOrange:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionOrange < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionOrange -= variableJauge
                $ armeeRegionOrange += variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurOrange:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionOrange < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionOrange < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionOrange -= variableJaugeDiv2
                $ argentRegionOrange -= variableJaugeDiv2
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurOrange:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionOrange < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionOrange += variableJauge
                $ nourritureRegionOrange -= variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurOrange:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionOrange < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionOrange += variableJauge
                $ armeeRegionOrange -= variableJauge
                $ regionOrangeActionFaite = True
                hide screen statsInteractionOrange
                scene mapRegionGrise
                call screen vueTerritoire



label attaqueOrange:
    hide screen infoRegionOrange
    call screen attaqueOrange
screen attaqueOrange:
    if regionBleueActive==False:
        imagebutton:
            idle "regionBleueRouge.png"
            xpos 420
            ypos 280
            action Jump("orangeAttaqueBleue")
        image "logoAttaque":
            xpos 550
            ypos 350
    if regionVioletteActive==False:
        imagebutton:
            idle "regionVioletteRouge.png"
            xpos 42
            ypos 380
            action Jump("orangeAttaqueViolette")
        image "logoAttaque":
            xpos 200
            ypos 500
    if regionRoseActive==False:
        imagebutton:
            idle "regionRoseRouge.png"
            xpos 78
            ypos 100
            action Jump("orangeAttaqueRose")
        image "logoAttaque":
            xpos 250
            ypos 200

#negociation guerre de orange vers orange
screen negociationOrangeViolette:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationOrangeViolette")
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
        action  Jump("refusNegociationOrangeViolette")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationOrangeViolette:
    if armeeRegionOrange>=armeeRegionViolette :
        $ armeeRegionOrange -=armeeRegionViolette
        $ armeeRegionViolette = 0
        $ regionVioletteActive=True
        hide screen statsInteractionOrange
        hide screen negociationOrangeViolette
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionOrange<armeeRegionViolette:
        $ armeeRegionViolette-=armeeRegionOrange
        $ armeeRegionOrange =0
        $ regionOrangeActive = False
        hide screen statsInteractionOrange
        hide screen negociationOrangeViolette
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationOrangeViolette:
    if armeeRegionOrange>=armeeRegionViolette :
        $ argentRegionOrange += argentRegionViolette//4
        $ argentRegionViolette -= argentRegionViolette//4
        hide screen statsInteractionOrange
        hide screen negociationOrangeViolette
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionOrange<armeeRegionViolette:
        $ argentRegionOrange -= argentRegionOrange//2
        $ argentRegionViolette += argentRegionOrange//2
        hide screen statsInteractionOrange
        hide screen negociationOrangeViolette
        scene mapRegionGrise
        call screen vueTerritoire

label orangeAttaqueViolette:
    $regionOrangeActionFaite=True
    if armeeRegionOrange>=armeeRegionViolette :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionOrange
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationOrangeViolette
    elif armeeRegionOrange<armeeRegionViolette:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionOrange
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationOrangeViolette

#negociation guerre de orange vers bleue
screen negociationOrangeBleue:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationOrangeBleue")
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
        action  Jump("refusNegociationOrangeBleue")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationOrangeBleue:
    if armeeRegionOrange>=armeeRegionBleue :
        $ armeeRegionOrange -=armeeRegionBleue
        $ armeeRegionBleue = 0
        $ regionBleueActive=True
        hide screen statsInteractionOrange
        hide screen negociationOrangeBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionOrange<armeeRegionBleue:
        $ armeeRegionBleue-=armeeRegionOrange
        $ armeeRegionOrange =0
        hide screen statsInteractionOrange
        hide screen negociationOrangeBleue
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationOrangeBleue:
    if armeeRegionOrange>=armeeRegionBleue :
        $ argentRegionOrange += argentRegionBleue//4
        $ argentRegionBleue -= argentRegionBleue//4
        hide screen statsInteractionOrange
        hide screen negociationOrangeBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionOrange<armeeRegionBleue:
        $ argentRegionOrange -= argentRegionOrange//2
        $ argentRegionBleue += argentRegionOrange//2
        hide screen statsInteractionOrange
        hide screen negociationOrangeBleue
        scene mapRegionGrise
        call screen vueTerritoire

label orangeAttaqueBleue:
    $regionOrangeActionFaite=True
    if armeeRegionOrange>=armeeRegionBleue :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionOrange
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationOrangeBleue
    elif armeeRegionOrange<armeeRegionBleue:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionOrange
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationOrangeBleue
#negociation guerre de orange vers rose
screen negociationOrangeRose:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationOrangeRose")
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
        action  Jump("refusNegociationOrangeRose")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationOrangeRose:
    if armeeRegionOrange>=armeeRegionRose :
        $ armeeRegionOrange -=armeeRegionRose
        $ armeeRegionRose = 0
        $ regionRoseActive=True
        hide screen statsInteractionOrange
        hide screen negociationOrangeRose
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionOrange<armeeRegionRose:
        $ armeeRegionRose-=armeeRegionOrange
        $ armeeRegionOrange =0
        hide screen statsInteractionOrange
        hide screen negociationOrangeRose
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationOrangeRose:
    if armeeRegionOrange>=armeeRegionRose :
        $ argentRegionOrange += argentRegionRose//4
        $ argentRegionRose -= argentRegionRose//4
        hide screen statsInteractionOrange
        hide screen negociationOrangeRose
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionOrange<armeeRegionRose:
        $ argentRegionOrange -= argentRegionOrange//2
        $ argentRegionRose += argentRegionOrange//2
        hide screen statsInteractionOrange
        hide screen negociationOrangeRose
        scene mapRegionGrise
        call screen vueTerritoire

label orangeAttaqueRose:
    $regionOrangeActionFaite=True
    if armeeRegionOrange>=armeeRegionRose :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionOrange
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationOrangeRose
    elif armeeRegionOrange<armeeRegionRose:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionOrange
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationOrangeRose


#------------------------------------------------------------------------------------------------------

label upgradeRegionOrange:
    hide screen infoRegionOrange
    call screen upgradeRegionOrange
screen upgradeRegionOrange:
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

label upgradeChoixOrange1:
    if argentRegionOrange >  50 and populationRegionOrange > 50 and nourritureRegionOrange > 25 :
        if niveauRegionOrange<6 :
            $regionOrangeActionFaite=True
            $ argentRegionOrange -= 50
            $ populationRegionOrange -=50
            $ nourritureRegionOrange-=25
            $ niveauRegionOrange+=1
            hide screen statsInteractionOrange
            scene mapRegionViolette
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"
    else :
        a "Il vous manque des ressources (il vous faut 50 d'argent, 50 de population et 25 de nourriture pour améliorer votre territoire(niv max : 6)) "
        hide screen statsInteractionOrange
        scene mapRegionViolette
        call screen vueTerritoire

label upgradeChoixOrange2:
            if argentRegionOrange > 130 and populationRegionOrange > 130 and nourritureRegionOrange > 65 :
                if niveauRegionOrange<6 :
                    $regionOrangeActionFaite=True
                    $ argentRegionOrange -= 130
                    $ populationRegionOrange -= 130
                    $ nourritureRegionOrange-=65
                    $ niveauRegionOrange+=3
                    hide screen statsInteractionOrange
                    scene mapRegionViolette
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"
            else :
                a "Il vous manque des ressources (il vous faut 130 d'argent, 130 de population et 65 de nourriture pour améliorer votre territoire de trois niveaux (niv max : 6))"
                hide screen statsInteractionOrange
                scene mapRegionViolette
                call screen vueTerritoire
