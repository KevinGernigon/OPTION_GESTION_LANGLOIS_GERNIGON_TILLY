
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
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionVerte :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionVerte :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionVerte:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionVerte:
            xpos 910
            ypos 170
        if(regionVerteActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionVerte")
        if (regionRougeActive==False or regionBleueActive==False) and regionVerteActionFaite==False:
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueVerte")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90
            action  Hide("infoRegionVerte")










########################################################################################################################
########################################################################################################################







label interactionVerte :
    hide screen infoRegionVerte
    scene office
    show pythie at left
    show screen statsInteractionVerte
    call screen interactionVerte
screen statsInteractionVerte:
    image "../images/blackbox.png"
    text "Région Verte" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionVerte :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionVerte :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionVerte:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionVerte:
        xpos 1150
        ypos 20

screen interactionVerte:
    imagebutton :
        idle "boxInteragir1"
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeVerte")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureVerte")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsVerte")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesVerte")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurVerte")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionVerte")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeVerte:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeVerte2
label ministreArmeeVerte2 :
    call screen ministreArmeeVerte2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeVerte2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeVerte2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeVerte")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyVerte"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeVerte")
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
        idle "armyVerte"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeVerte")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeVerte")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeVerte:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionVerte < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionVerte -=  variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeVerte:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionVerte += variableJauge
                $ armeeGeneral -= variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire










#agriculture
label ministreAgricultureVerte:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureVerte2
label ministreAgricultureVerte2 :
    call screen ministreAgricultureVerte2


screen ministreAgricultureVerte2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureVerte2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureVerte")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodVerte"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureVerte")
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
        idle "foodVerte"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureVerte")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureVerte")
    text " -%d" % variableJauge:
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureVerte:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionVerte < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionVerte -= variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureVerte:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionVerte += variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire


#civils


label ministreCivilsVerte:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsVerte2
label ministreCivilsVerte2 :
    call screen ministreCivilsVerte2

screen ministreCivilsVerte2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsVerte2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsVerte")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popVerte"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsVerte")
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
        idle "popVerte"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsVerte")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsVerte")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsVerte:
            p "Je souhaite requisitionner des civils"
            if populationRegionVerte < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionVerte -= variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsVerte:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionVerte += variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire



#finances
label ministreFinancesVerte:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesVerte2
label ministreFinancesVerte2 :
    call screen ministreFinancesVerte2

screen ministreFinancesVerte2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesVerte2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesVerte")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesVerte"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesVerte")
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
        idle "financesVerte"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesVerte")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesVerte")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesVerte:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionVerte < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionVerte -= variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesVerte:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionVerte += variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurVerte:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurVerte2

label ministreAmbassadeurVerte2 :
    call screen ministreAmbassadeurVerte2

screen ministreAmbassadeurVerte2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurVerte2"), Jump("variableJauge")]
    imagebutton :
        idle "armyVerte"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurVerte")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popVerte"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurVerte")
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
        idle "foodVerte"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurVerte")
    text " +%d" % variableJauge:
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popVerte"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurVerte")
    text " -%d" % variableJaugeDiv2:
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesVerte"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurVerte")
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
        idle "financesVerte"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurVerte")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodVerte"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurVerte")
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
        idle "popVerte"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurVerte")
    text " +%d" % variableJauge:
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyVerte"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurVerte")
    text " -%d" % variableJauge:
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurVerte:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionVerte < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionVerte -= variableJauge
                $ armeeRegionVerte += variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurVerte:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionVerte < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionVerte < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionVerte -= variableJaugeDiv2
                $ argentRegionVerte -= variableJaugeDiv2
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurVerte:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionVerte < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionVerte += variableJauge
                $ nourritureRegionVerte -= variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurVerte:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionVerte < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionVerte += variableJauge
                $ armeeRegionVerte -= variableJauge
                $ regionVerteActionFaite = True
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire



label attaqueVerte:
    hide screen infoRegionVerte
    call screen attaqueVerte
screen attaqueVerte:
    if regionRougeActive==False:
        imagebutton:
            idle "regionRougeRouge.png"
            xpos 720
            ypos 290
            action Jump("verteAttaqueRouge")
        image "logoAttaque":
            xpos 912
            ypos 320
    if regionBleueActive==False:
        imagebutton:
            idle "regionBleueRouge.png"
            xpos 420
            ypos 280
            action Jump("verteAttaqueBleue")
        image "logoAttaque":
            xpos 550
            ypos 350

#negociation guerre de verte vers grise
screen negociationVerteBleue:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationVerteBleue")
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
        action  Jump("refusNegociationVerteBleue")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationVerteBleue:
    if armeeRegionVerte>=armeeRegionBleue :
        $ armeeRegionVerte -=armeeRegionBleue
        $ armeeRegionBleue = 0
        $ regionBleueActive=True
        hide screen statsInteractionVerte
        hide screen negociationVerteBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionVerte<armeeRegionBleue:
        $ armeeRegionBleue-=armeeRegionVerte
        $ armeeRegionVerte =0
        $ regionVerteActive = False
        hide screen statsInteractionVerte
        hide screen negociationVerteBleue
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationVerteBleue:
    if armeeRegionVerte>=armeeRegionBleue :
        $ argentRegionVerte += argentRegionBleue//4
        $ argentRegionBleue -= argentRegionBleue//4
        hide screen statsInteractionVerte
        hide screen negociationVerteBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionVerte<armeeRegionBleue:
        $ argentRegionVerte -= argentRegionVerte//2
        $ argentRegionBleue += argentRegionVerte//2
        hide screen statsInteractionVerte
        hide screen negociationVerteBleue
        scene mapRegionGrise
        call screen vueTerritoire

label verteAttaqueBleue:
    $regionVerteActionFaite=True
    if armeeRegionVerte>=armeeRegionBleue :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionVerte
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationVerteBleue
    elif armeeRegionVerte<armeeRegionBleue:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionVerte
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationVerteBleue

#negociation guerre de verte vers jaune
screen negociationVerteRouge:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationVerteRouge")
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
        action  Jump("refusNegociationVerteRouge")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationVerteRouge:
    if armeeRegionVerte>=armeeRegionRouge :
        $ armeeRegionVerte -=armeeRegionRouge
        $ armeeRegionRouge = 0
        $ regionRougeActive=True
        hide screen statsInteractionVerte
        hide screen negociationVerteRouge
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionVerte<armeeRegionRouge:
        $ armeeRegionRouge-=armeeRegionVerte
        $ armeeRegionVerte =0
        hide screen statsInteractionVerte
        hide screen negociationVerteRouge
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationVerteRouge:
    if armeeRegionVerte>=armeeRegionRouge :
        $ argentRegionVerte += argentRegionRouge//4
        $ argentRegionRouge -= argentRegionRouge//4
        hide screen statsInteractionVerte
        hide screen negociationVerteRouge
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionVerte<armeeRegionRouge:
        $ argentRegionVerte -= argentRegionVerte//2
        $ argentRegionRouge += argentRegionVerte//2
        hide screen statsInteractionVerte
        hide screen negociationVerteRouge
        scene mapRegionGrise
        call screen vueTerritoire

label verteAttaqueRouge:
    $regionVerteActionFaite=True
    if armeeRegionVerte>=armeeRegionRouge :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionVerte
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationVerteRouge
    elif armeeRegionVerte<armeeRegionRouge:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionVerte
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationVerteRouge





label upgradeRegionVerte:
    hide screen infoRegionVerte
    call screen upgradeRegionVerte
screen upgradeRegionVerte:
    imagebutton :
        idle "upgrade1"
        xalign 0.3
        yalign 0.5
        action  Jump("upgradeChoix1Verte")
    imagebutton :
        idle "upgrade2"
        xalign 0.7
        yalign 0.5
        action  Jump("upgradeChoix2Verte")

label upgradeChoix1Verte:
    if argentRegionVerte >  50 and populationRegionVerte > 50 and nourritureRegionVerte > 25 :
        if niveauRegionVerte<6 :
            $regionVerteActionFaite=True
            $ argentRegionVerte -= 50
            $ populationRegionVerte -=50
            $ nourritureRegionVerte-=25
            $ niveauRegionVerte+=1
            hide screen statsInteractionVerte
            scene mapRegionGrise
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"
    else :
        a "Il vous manque des ressources (il vous faut 50 d'argent, 50 de population et 25 de nourriture pour améliorer votre territoire(niv max : 6))"
        hide screen statsInteractionVerte
        scene mapRegionGrise
        call screen vueTerritoire

label upgradeChoix2Verte:
            if argentRegionVerte > 130 and populationRegionVerte > 130 and nourritureRegionVerte > 65 :
                if niveauRegionVerte<6 :
                    $regionVerteActionFaite=True
                    $ argentRegionVerte -= 130
                    $ populationRegionVerte -= 130
                    $ nourritureRegionVerte-=65
                    $ niveauRegionVerte+=3
                    hide screen statsInteractionVerte
                    scene mapRegionGrise
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"
            else :
                a "Il vous manque des ressources (il vous faut 130 d'argent, 130 de population et 65 de nourriture pour améliorer votre territoire de trois niveaux (niv max : 6))"
                hide screen statsInteractionVerte
                scene mapRegionGrise
                call screen vueTerritoire
