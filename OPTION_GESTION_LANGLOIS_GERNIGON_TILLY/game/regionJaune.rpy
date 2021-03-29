
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
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionJaune :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionJaune :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionJaune:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionJaune:
            xpos 910
            ypos 170
        if(regionJauneActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionJaune")
        if (regionBeigeActive==False or regionGriseActive==False or regionRoseActive==False or regionBleueActive==False) and regionJauneActionFaite==False:
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueJaune")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90
            action  Hide("infoRegionJaune")










########################################################################################################################
########################################################################################################################







label interactionJaune :
    hide screen infoRegionJaune
    scene office
    show pythie at left
    show screen statsInteractionJaune
    call screen interactionJaune
screen statsInteractionJaune:
    image "../images/blackbox.png"
    text "Région Jaune" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionJaune :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionJaune :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionJaune:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionJaune:
        xpos 1150
        ypos 20

screen interactionJaune:
    imagebutton :
        idle "boxInteragir1"
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeJaune")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureJaune")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsJaune")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesJaune")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurJaune")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionJaune")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeJaune:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeJaune2
label ministreArmeeJaune2 :
    call screen ministreArmeeJaune2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeJaune2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeJaune2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeJaune")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyJaune"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeJaune")
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
        idle "armyJaune"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeJaune")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeJaune")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeJaune:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionJaune < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionJaune -=  variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeJaune:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionJaune += variableJauge
                $ armeeGeneral -= variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire










#agriculture
label ministreAgricultureJaune:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureJaune2
label ministreAgricultureJaune2 :
    call screen ministreAgricultureJaune2


screen ministreAgricultureJaune2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureJaune2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureJaune")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodJaune"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureJaune")
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
        idle "foodJaune"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureJaune")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureJaune")
    text " -%d" % variableJauge:
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureJaune:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionJaune < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionJaune -= variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureJaune:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionJaune += variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire


#civils


label ministreCivilsJaune:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsJaune2
label ministreCivilsJaune2 :
    call screen ministreCivilsJaune2

screen ministreCivilsJaune2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsJaune2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsJaune")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popJaune"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsJaune")
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
        idle "popJaune"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsJaune")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsJaune")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsJaune:
            p "Je souhaite requisitionner des civils"
            if populationRegionJaune < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionJaune -= variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsJaune:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionJaune += variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire



#finances
label ministreFinancesJaune:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesJaune2
label ministreFinancesJaune2 :
    call screen ministreFinancesJaune2

screen ministreFinancesJaune2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesJaune2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesJaune")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesJaune"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesJaune")
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
        idle "financesJaune"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesJaune")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesJaune")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesJaune:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionJaune < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionJaune -= variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesJaune:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionJaune += variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurJaune:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurJaune2

label ministreAmbassadeurJaune2 :
    call screen ministreAmbassadeurJaune2

screen ministreAmbassadeurJaune2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurJaune2"), Jump("variableJauge")]
    imagebutton :
        idle "armyJaune"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurJaune")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popJaune"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurJaune")
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
        idle "foodJaune"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurJaune")
    text " +%d" % variableJauge:
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popJaune"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurJaune")
    text " -%d" % variableJaugeDiv2:
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesJaune"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurJaune")
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
        idle "financesJaune"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurJaune")
    text " +%d" % variableJauge:
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodJaune"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurJaune")
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
        idle "popJaune"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurJaune")
    text " +%d" % variableJauge:
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyJaune"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurJaune")
    text " -%d" % variableJauge:
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurJaune:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionJaune < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionJaune -= variableJauge
                $ armeeRegionJaune += variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurJaune:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionJaune < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionJaune < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionJaune -= variableJaugeDiv2
                $ argentRegionJaune -= variableJaugeDiv2
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurJaune:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionJaune < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionJaune += variableJauge
                $ nourritureRegionJaune -= variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurJaune:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionJaune < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionJaune += variableJauge
                $ armeeRegionJaune -= variableJauge
                $ regionJauneActionFaite = True
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire



label attaqueJaune:
    hide screen infoRegionJaune
    call screen attaqueJaune
screen attaqueJaune:
    if regionBeigeActive==False:
        imagebutton:
            idle "regionBeigeRouge.png"
            xpos 370
            ypos 90
            action Jump("jauneAttaqueBeige")
        image "logoAttaque":
            xpos 575
            ypos 200
    if regionGriseActive==False:
        imagebutton:
            idle "regionGriseRouge.png"
            xpos 265
            ypos 45
            action Jump("jauneAttaqueGrise")
        image "logoAttaque":
            xpos 450
            ypos 50

#negociation guerre de jaune vers grise
screen negociationJauneGrise:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationJauneGrise")
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
        action  Jump("refusNegociationJauneGrise")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationJauneGrise:
    if armeeRegionJaune>=armeeRegionGrise :
        $ armeeRegionJaune -=armeeRegionGrise
        $ armeeRegionGrise = 0
        $ regionGriseActive=True
        hide screen statsInteractionJaune
        hide screen negociationJauneGrise
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionJaune<armeeRegionGrise:
        $ armeeRegionGrise-=armeeRegionJaune
        $ armeeRegionJaune =0
        $ regionJauneActive = False
        hide screen statsInteractionJaune
        hide screen negociationJauneGrise
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationJauneGrise:
    if armeeRegionJaune>=armeeRegionGrise :
        $ argentRegionJaune += argentRegionGrise//4
        $ argentRegionGrise -= argentRegionGrise//4
        hide screen statsInteractionJaune
        hide screen negociationJauneGrise
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionJaune<armeeRegionGrise:
        $ argentRegionJaune -= argentRegionJaune//2
        $ argentRegionGrise += argentRegionJaune//2
        hide screen statsInteractionJaune
        hide screen negociationJauneGrise
        scene mapRegionGrise
        call screen vueTerritoire

label jauneAttaqueGrise:
    $regionJauneActionFaite=True
    if armeeRegionJaune>=armeeRegionGrise :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionJaune
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationJauneGrise
    elif armeeRegionJaune<armeeRegionGrise:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionJaune
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationJauneGrise

#negociation guerre de jaune vers beige
screen negociationJauneBeige:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationJauneBeige")
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
        action  Jump("refusNegociationJauneBeige")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationJauneBeige:
    if armeeRegionJaune>=armeeRegionBeige :
        $ armeeRegionJaune -=armeeRegionBeige
        $ armeeRegionBeige = 0
        $ regionBeigeActive=True
        hide screen statsInteractionJaune
        hide screen negociationJauneBeige
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionJaune<armeeRegionBeige:
        $ armeeRegionBeige-=armeeRegionJaune
        $ armeeRegionJaune =0
        hide screen statsInteractionJaune
        hide screen negociationJauneBeige
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationJauneBeige:
    if armeeRegionJaune>=armeeRegionBeige :
        $ argentRegionJaune += argentRegionBeige//4
        $ argentRegionBeige -= argentRegionBeige//4
        hide screen statsInteractionJaune
        hide screen negociationJauneBeige
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionJaune<armeeRegionBeige:
        $ argentRegionJaune -= argentRegionJaune//2
        $ argentRegionBeige += argentRegionJaune//2
        hide screen statsInteractionJaune
        hide screen negociationJauneBeige
        scene mapRegionGrise
        call screen vueTerritoire

label jauneAttaqueBeige:
    $regionJauneActionFaite=True
    if armeeRegionJaune>=armeeRegionBeige :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionJaune
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationJauneBeige
    elif armeeRegionJaune<armeeRegionBeige:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionJaune
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationJauneBeige

#negociation guerre de jaune vers rose
screen negociationJauneRose:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationJauneRose")
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
        action  Jump("refusNegociationJauneRose")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationJauneRose:
    if armeeRegionJaune>=armeeRegionRose :
        $ armeeRegionJaune -=armeeRegionRose
        $ armeeRegionRose = 0
        $ regionRoseActive=True
        hide screen statsInteractionJaune
        hide screen negociationJauneRose
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionJaune<armeeRegionRose:
        $ armeeRegionRose-=armeeRegionJaune
        $ armeeRegionJaune =0
        hide screen statsInteractionJaune
        hide screen negociationJauneRose
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationJauneRose:
    if armeeRegionJaune>=armeeRegionRose :
        $ argentRegionJaune += argentRegionRose//4
        $ argentRegionRose -= argentRegionRose//4
        hide screen statsInteractionJaune
        hide screen negociationJauneRose
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionJaune<armeeRegionRose:
        $ argentRegionJaune -= argentRegionJaune//2
        $ argentRegionRose += argentRegionJaune//2
        hide screen statsInteractionJaune
        hide screen negociationJauneRose
        scene mapRegionGrise
        call screen vueTerritoire

label jauneAttaqueRose:
    $regionJauneActionFaite=True
    if armeeRegionJaune>=armeeRegionRose :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionJaune
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationJauneRose
    elif armeeRegionJaune<armeeRegionRose:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionJaune
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationJauneRose

#negociation guerre de jaune vers Bleue --------------------------------------------------------------

screen negociationJauneBleue:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationJauneBleue")
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
        action  Jump("refusNegociationJauneBleue")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationJauneBleue:
    if armeeRegionJaune>=armeeRegionBleue :
        $ armeeRegionJaune -=armeeRegionBleue
        $ armeeRegionBleue = 0
        $ regionBleueActive=True
        hide screen statsInteractionJaune
        hide screen negociationJauneBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionJaune<armeeRegionBleue:
        $ armeeRegionBleue-=armeeRegionJaune
        $ armeeRegionJaune =0
        hide screen statsInteractionJaune
        hide screen negociationJauneBleue
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationJauneBleue:
    if armeeRegionJaune>=armeeRegionBleue :
        $ argentRegionJaune += argentRegionBleue//4
        $ argentRegionBleue -= argentRegionBleue//4
        hide screen statsInteractionJaune
        hide screen negociationJauneBleue
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionJaune<armeeRegionBleue:
        $ argentRegionJaune -= argentRegionJaune//2
        $ argentRegionBleue += argentRegionJaune//2
        hide screen statsInteractionJaune
        hide screen negociationJauneBleue
        scene mapRegionGrise
        call screen vueTerritoire

label jauneAttaqueBleue:
    $regionJauneActionFaite=True
    if armeeRegionJaune>=armeeRegionBleue :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionJaune
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationJauneBleue
    elif armeeRegionJaune<armeeRegionBleue:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionJaune
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationJauneBleue
#------------------------------------------------------------------------------------------------------

label upgradeRegionJaune:
    hide screen infoRegionJaune
    call screen upgradeRegionJaune
screen upgradeRegionJaune:
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
    if argentRegionJaune >  50 and populationRegionJaune > 50 and nourritureRegionJaune > 25 :
        if niveauRegionJaune<6 :
            $regionJauneActionFaite=True
            $ argentRegionJaune -= 50
            $ populationRegionJaune -=50
            $ nourritureRegionJaune-=25
            $ niveauRegionJaune+=1
            hide screen statsInteractionJaune
            scene mapRegionGrise
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"
    else :
        a "Il vous manque des ressources "
        hide screen statsInteractionJaune
        scene mapRegionGrise
        call screen vueTerritoire

label upgradeChoix2:
            if argentRegionJaune > 130 and populationRegionJaune > 130 and nourritureRegionJaune > 65 :
                if niveauRegionJaune<6 :
                    $regionJauneActionFaite=True
                    $ argentRegionJaune -= 130
                    $ populationRegionJaune -= 130
                    $ nourritureRegionJaune-=35
                    $ niveauRegionJaune+=3
                    hide screen statsInteractionJaune
                    scene mapRegionGrise
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"
            else :
                a "Il vous manque des ressources "
                hide screen statsInteractionJaune
                scene mapRegionGrise
                call screen vueTerritoire
