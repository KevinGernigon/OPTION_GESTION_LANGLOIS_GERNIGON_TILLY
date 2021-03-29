
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
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionRouge :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionRouge :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionRouge:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionRouge:
            xpos 910
            ypos 170
        if(regionRougeActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionRouge")
        if (regionVerteActive==False or regionBleueActive==False) and regionRougeActionFaite==False:
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueRouge")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90
            action  Hide("infoRegionRouge")










########################################################################################################################
########################################################################################################################







label interactionRouge :
    hide screen infoRegionRouge
    scene office
    show pythie at left
    show screen statsInteractionRouge
    call screen interactionRouge
screen statsInteractionRouge:
    image "../images/blackbox.png"
    text "Région Rouge" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionRouge :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionRouge :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionRouge:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionRouge:
        xpos 1150
        ypos 20

screen interactionRouge:
    imagebutton :
        idle "boxInteragir1"
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeRouge")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureRouge")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsRouge")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesRouge")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurRouge")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionRouge")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeRouge:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeRouge2
label ministreArmeeRouge2 :
    call screen ministreArmeeRouge2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeRouge2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeRouge2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeRouge")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyRouge"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeRouge")
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
        idle "armyRouge"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeRouge")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeRouge")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeRouge:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionRouge < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionRouge -=  variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeRouge:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionRouge += variableJauge
                $ armeeGeneral -= variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire










#agriculture
label ministreAgricultureRouge:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureRouge2
label ministreAgricultureRouge2 :
    call screen ministreAgricultureRouge2


screen ministreAgricultureRouge2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureRouge2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureRouge")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodRouge"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureRouge")
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
        idle "foodRouge"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureRouge")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureRouge")
    text " -%d" % variableJauge:
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureRouge:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionRouge < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionRouge -= variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureRouge:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionRouge += variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire


#civils


label ministreCivilsRouge:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsRouge2
label ministreCivilsRouge2 :
    call screen ministreCivilsRouge2

screen ministreCivilsRouge2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsRouge2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsRouge")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popRouge"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsRouge")
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
        idle "popRouge"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsRouge")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsRouge")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsRouge:
            p "Je souhaite requisitionner des civils"
            if populationRegionRouge < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionRouge -= variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsRouge:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionRouge += variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire



#finances
label ministreFinancesRouge:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesRouge2
label ministreFinancesRouge2 :
    call screen ministreFinancesRouge2

screen ministreFinancesRouge2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesRouge2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesRouge")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesRouge"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesRouge")
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
        idle "financesRouge"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesRouge")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesRouge")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesRouge:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionRouge < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionRouge -= variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesRouge:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionRouge += variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurRouge:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurRouge2

label ministreAmbassadeurRouge2 :
    call screen ministreAmbassadeurRouge2

screen ministreAmbassadeurRouge2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurRouge2"), Jump("variableJauge")]
    imagebutton :
        idle "armyRouge"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurRouge")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popRouge"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurRouge")
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
        idle "foodRouge"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurRouge")
    text " +%d" % variableJauge:
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popRouge"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurRouge")
    text " -%d" % variableJaugeDiv2:
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesRouge"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurRouge")
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
        idle "financesRouge"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurRouge")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodRouge"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurRouge")
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
        idle "popRouge"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurRouge")
    text " +%d" % variableJauge:
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyRouge"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurRouge")
    text " -%d" % variableJauge:
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurRouge:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionRouge < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionRouge -= variableJauge
                $ armeeRegionRouge += variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurRouge:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionRouge < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionRouge < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionRouge -= variableJaugeDiv2
                $ argentRegionRouge -= variableJaugeDiv2
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurRouge:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionRouge < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionRouge += variableJauge
                $ nourritureRegionRouge -= variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurRouge:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionRouge < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionRouge += variableJauge
                $ armeeRegionRouge -= variableJauge
                $ regionRougeActionFaite = True
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire



label attaqueRouge:
    hide screen infoRegionRouge
    call screen attaqueRouge
screen attaqueRouge:
    if regionVerteActive==False:
        imagebutton:
            idle "regionVerteRouge.png"
            xpos 712
            ypos 425
            action Jump("rougeAttaqueVerte")
        image "logoAttaque":
            xpos 912
            ypos 520
    if regionBleueActive==False:
        imagebutton:
            idle "regionBleueRouge.png"
            xpos 420
            ypos 280
            action Jump("rougeAttaqueBleue")
        image "logoAttaque":
            xpos 550
            ypos 350

#negociation guerre de rouge vers grise
screen negociationRougeBleue:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationRougeBleue")
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
        action  Jump("refusNegociationRougeBleue")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationRougeBleue:
    if armeeRegionRouge>=armeeRegionBleue :
        $ armeeRegionRouge -=armeeRegionBleue
        $ armeeRegionBleue = 0
        $ regionBleueActive=True
        hide screen statsInteractionRouge
        hide screen negociationRougeBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionRouge<armeeRegionBleue:
        $ armeeRegionBleue-=armeeRegionRouge
        $ armeeRegionRouge =0
        $ regionRougeActive = False
        hide screen statsInteractionRouge
        hide screen negociationRougeBleue
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationRougeBleue:
    if armeeRegionRouge>=armeeRegionBleue :
        $ argentRegionRouge += argentRegionBleue//4
        $ argentRegionBleue -= argentRegionBleue//4
        hide screen statsInteractionRouge
        hide screen negociationRougeBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionRouge<armeeRegionBleue:
        $ argentRegionRouge -= argentRegionRouge//2
        $ argentRegionBleue += argentRegionRouge//2
        hide screen statsInteractionRouge
        hide screen negociationRougeBleue
        scene mapRegionGrise
        call screen vueTerritoire

label rougeAttaqueBleue:
    $regionRougeActionFaite=True
    if armeeRegionRouge>=armeeRegionBleue :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionRouge
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationRougeBleue
    elif armeeRegionRouge<armeeRegionBleue:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionRouge
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationRougeBleue

#negociation guerre de rouge vers jaune
screen negociationRougeVerte:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationRougeVerte")
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
        action  Jump("refusNegociationRougeVerte")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationRougeVerte:
    if armeeRegionRouge>=armeeRegionVerte :
        $ armeeRegionRouge -=armeeRegionVerte
        $ armeeRegionVerte = 0
        $ regionVerteActive=True
        hide screen statsInteractionRouge
        hide screen negociationRougeVerte
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionRouge<armeeRegionVerte:
        $ armeeRegionVerte-=armeeRegionRouge
        $ armeeRegionRouge =0
        hide screen statsInteractionRouge
        hide screen negociationRougeVerte
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationRougeVerte:
    if armeeRegionRouge>=armeeRegionVerte :
        $ argentRegionRouge += argentRegionVerte//4
        $ argentRegionVerte -= argentRegionVerte//4
        hide screen statsInteractionRouge
        hide screen negociationRougeVerte
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionRouge<armeeRegionVerte:
        $ argentRegionRouge -= argentRegionRouge//2
        $ argentRegionVerte += argentRegionRouge//2
        hide screen statsInteractionRouge
        hide screen negociationRougeVerte
        scene mapRegionGrise
        call screen vueTerritoire

label rougeAttaqueVerte:
    $regionRougeActionFaite=True
    if armeeRegionRouge>=armeeRegionVerte :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionRouge
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationRougeVerte
    elif armeeRegionRouge<armeeRegionVerte:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionRouge
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationRougeVerte





label upgradeRegionRouge:
    hide screen infoRegionRouge
    call screen upgradeRegionRouge
screen upgradeRegionRouge:
    imagebutton :
        idle "upgrade1"
        xalign 0.3
        yalign 0.5
        action  Jump("upgradeChoix1Rouge")
    imagebutton :
        idle "upgrade2"
        xalign 0.7
        yalign 0.5
        action  Jump("upgradeChoix2Rouge")

label upgradeChoix1Rouge:
    if argentRegionRouge >  50 and populationRegionRouge > 50 and nourritureRegionRouge > 25 :
        if niveauRegionRouge<6 :
            $regionRougeActionFaite=True
            $ argentRegionRouge -= 50
            $ populationRegionRouge -=50
            $ nourritureRegionRouge-=25
            $ niveauRegionRouge+=1
            hide screen statsInteractionRouge
            scene mapRegionGrise
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"
    else :
        a "Il vous manque des ressources (il vous faut 50 d'argent, 50 de population et 25 de nourriture pour améliorer votre territoire(niv max : 6))"
        hide screen statsInteractionRouge
        scene mapRegionGrise
        call screen vueTerritoire

label upgradeChoix2Rouge:
            if argentRegionRouge > 130 and populationRegionRouge > 130 and nourritureRegionRouge > 65 :
                if niveauRegionRouge<6 :
                    $regionRougeActionFaite=True
                    $ argentRegionRouge -= 130
                    $ populationRegionRouge -= 130
                    $ nourritureRegionRouge-=65
                    $ niveauRegionRouge+=3
                    hide screen statsInteractionRouge
                    scene mapRegionGrise
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"
            else :
                a "Il vous manque des ressources (il vous faut 130 d'argent, 130 de population et 65 de nourriture pour améliorer votre territoire de trois niveaux (niv max : 6))"
                hide screen statsInteractionRouge
                scene mapRegionGrise
                call screen vueTerritoire
