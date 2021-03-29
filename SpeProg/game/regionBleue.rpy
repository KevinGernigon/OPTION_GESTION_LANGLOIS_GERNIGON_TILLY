


transform carre_zoom:
    zoom 1.5
transform exit_zoom:
    zoom 0.05

screen infoRegionBleue :
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionBleue :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionBleue :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionBleue:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionBleue:
            xpos 910
            ypos 170
        if(regionBleueActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionBleue")
        if (regionJauneActive==False or regionRoseActive==False) and regionBleueActionFaite==False:        
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueBleue")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90  
            action  Hide("infoRegionBleue")










########################################################################################################################
########################################################################################################################







label interactionBleue :
    hide screen infoRegionBleue
    scene office
    show pythie at left
    show screen statsInteractionBleue
    call screen interactionBleue
screen statsInteractionBleue:
    image "../images/blackbox.png"
    text "Région Bleue" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionBleue :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionBleue :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionBleue:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionBleue:
        xpos 1150
        ypos 20

screen interactionBleue:
    imagebutton :
        idle "boxInteragir1"
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeBleue")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureBleue")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsBleue")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesBleue")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurBleue")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionBleue")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeBleue:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeBleue2
label ministreArmeeBleue2 :
    call screen ministreArmeeBleue2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeBleue2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeBleue2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeBleue")
    text " +%d" % variableJauge:  
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyBleue"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeBleue")
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
        idle "armyBleue"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeBleue")
    text " +%d" % variableJauge:  
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeBleue")
    text " -%d" % variableJauge:  
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeBleue:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionBleue < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionBleue -=  variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeBleue:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionBleue += variableJauge
                $ armeeGeneral -= variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire










#agriculture
label ministreAgricultureBleue:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureBleue2
label ministreAgricultureBleue2 :
    call screen ministreAgricultureBleue2


screen ministreAgricultureBleue2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureBleue2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureBleue")
    text " +%d" % variableJauge: 
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodBleue"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureBleue")
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
        idle "foodBleue"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureBleue")
    text " +%d" % variableJauge: 
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureBleue")
    text " -%d" % variableJauge: 
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureBleue:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionBleue < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionBleue -= variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureBleue:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionBleue += variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire


#civils


label ministreCivilsBleue:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsBleue2
label ministreCivilsBleue2 :
    call screen ministreCivilsBleue2

screen ministreCivilsBleue2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsBleue2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsBleue")
    text " +%d" % variableJauge: 
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBleue"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsBleue")
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
        idle "popBleue"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsBleue")
    text " +%d" % variableJauge: 
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsBleue")
    text " -%d" % variableJauge: 
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsBleue:
            p "Je souhaite requisitionner des civils"
            if populationRegionBleue < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionBleue -= variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsBleue:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionBleue += variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire



#finances
label ministreFinancesBleue:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesBleue2
label ministreFinancesBleue2 :
    call screen ministreFinancesBleue2

screen ministreFinancesBleue2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesBleue2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesBleue")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesBleue"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesBleue")
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
        idle "financesBleue"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesBleue")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesBleue")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesBleue:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionBleue < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionBleue -= variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesBleue:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionBleue += variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurBleue:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurBleue2

label ministreAmbassadeurBleue2 :
    call screen ministreAmbassadeurBleue2

screen ministreAmbassadeurBleue2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurBleue2"), Jump("variableJauge")]
    imagebutton :
        idle "armyBleue"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurBleue")
    text " +%d" % variableJauge: 
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBleue"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurBleue")
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
        idle "foodBleue"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurBleue")
    text " +%d" % variableJauge: 
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBleue"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurBleue")
    text " -%d" % variableJaugeDiv2: 
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesBleue"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurBleue")
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
        idle "financesBleue"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurBleue")
    text " +%d" % variableJauge: 
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodBleue"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurBleue")
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
        idle "popBleue"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurBleue")
    text " +%d" % variableJauge: 
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyBleue"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurBleue")
    text " -%d" % variableJauge: 
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurBleue:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionBleue < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionBleue -= variableJauge
                $ armeeRegionBleue += variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurBleue:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionBleue < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionBleue < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionBleue -= variableJaugeDiv2
                $ argentRegionBleue -= variableJaugeDiv2
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurBleue:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionBleue < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionBleue += variableJauge
                $ nourritureRegionBleue -= variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurBleue:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionBleue < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionBleue += variableJauge
                $ armeeRegionBleue -= variableJauge
                $ regionBleueActionFaite = True
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire



label attaqueBleue:
    hide screen infoRegionBleue
    call screen attaqueBleue
screen attaqueBleue:       
    if regionJauneActive==False:
        imagebutton:
            idle "regionJauneRouge.png"
            xpos 370
            ypos 90
            action Jump("bleueAttaqueJaune")
        image "logoAttaque":
            xpos 575
            ypos 200          
    if regionRoseActive==False:
        imagebutton:
            idle "regionRoseRouge.png"
            xpos 265
            ypos 45
            action Jump("bleueAttaqueRose")
        image "logoAttaque":
            xpos 450
            ypos 50 
    if regionOrangeActive==False:
        imagebutton:
            idle "regionOrangeRouge.png"
            xpos 265
            ypos 45
            action Jump("bleueAttaqueOrange")
        image "logoAttaque":
            xpos 450
            ypos 50 
    if regionRougeActive==False:
        imagebutton:
            idle "regionRougeRouge.png"
            xpos 265
            ypos 45
            action Jump("bleueAttaqueRouge")
        image "logoAttaque":
            xpos 450
            ypos 50 
    if regionRougeActive==False:
        imagebutton:
            idle "regionVerteRouge.png"
            xpos 265
            ypos 45
            action Jump("bleueAttaqueVerte")
        image "logoAttaque":
            xpos 450
            ypos 50 


#negociation guerre de bleue vers rouge
screen negociationBleueRouge:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBleueRouge")
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
        action  Jump("refusNegociationBleueRouge")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBleueRouge:
    if armeeRegionBleue>=armeeRegionRouge :
        $ armeeRegionBleue -=armeeRegionRouge
        $ armeeRegionRouge = 0
        $ regionRougeActive=True
        hide screen statsInteractionBleue
        hide screen negociationBleueRouge
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionRouge:
        $ armeeRegionRouge-=armeeRegionBleue
        $ armeeRegionBleue =0
        $ regionBleueActive = False
        hide screen statsInteractionBleue
        hide screen negociationBleueRouge
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBleueRouge:
    if armeeRegionBleue>=armeeRegionRouge :
        $ argentRegionBleue += argentRegionRouge//4
        $ argentRegionRouge -= argentRegionRouge//4
        hide screen statsInteractionBleue
        hide screen negociationBleueRouge
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionRouge:
        $ argentRegionBleue -= argentRegionBleue//2
        $ argentRegionRouge += argentRegionBleue//2
        hide screen statsInteractionBleue
        hide screen negociationBleueRouge
        scene mapRegionGrise
        call screen vueTerritoire

label bleueAttaqueRouge:
    $regionBleueActionFaite=True
    if armeeRegionBleue>=armeeRegionRouge :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBleueRouge
    elif armeeRegionBleue<armeeRegionRouge:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBleueRouge



#negociation guerre de bleue vers rouge
screen negociationBleueVerte:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBleueVerte")
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
        action  Jump("refusNegociationBleueVerte")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBleueVerte:
    if armeeRegionBleue>=armeeRegionVerte :
        $ armeeRegionBleue -=armeeRegionVerte
        $ armeeRegionVerte = 0
        $ regionVerteActive=True
        hide screen statsInteractionBleue
        hide screen negociationBleueVerte
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionVerte:
        $ armeeRegionVerte-=armeeRegionBleue
        $ armeeRegionBleue =0
        $ regionBleueActive = False
        hide screen statsInteractionBleue
        hide screen negociationBleueVerte
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBleueVerte:
    if armeeRegionBleue>=armeeRegionVerte :
        $ argentRegionBleue += argentRegionVerte//4
        $ argentRegionVerte -= argentRegionVerte//4
        hide screen statsInteractionBleue
        hide screen negociationBleueVerte
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionVerte:
        $ argentRegionBleue -= argentRegionBleue//2
        $ argentRegionVerte += argentRegionBleue//2
        hide screen statsInteractionBleue
        hide screen negociationBleueVerte
        scene mapRegionGrise
        call screen vueTerritoire

label bleueAttaqueVerte:
    $regionBleueActionFaite=True
    if armeeRegionBleue>=armeeRegionVerte :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBleueVerte
    elif armeeRegionBleue<armeeRegionVerte:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBleueVerte


#negociation guerre de bleue vers orange
screen negociationBleueOrange:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBleueOrange")
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
        action  Jump("refusNegociationBleueOrange")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBleueOrange:
    if armeeRegionBleue>=armeeRegionOrange :
        $ armeeRegionBleue -=armeeRegionOrange
        $ armeeRegionOrange = 0
        $ regionOrangeActive=True
        hide screen statsInteractionBleue
        hide screen negociationBleueOrange
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionOrange:
        $ armeeRegionOrange-=armeeRegionBleue
        $ armeeRegionBleue =0
        $ regionBleueActive = False
        hide screen statsInteractionBleue
        hide screen negociationBleueOrange
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBleueOrange:
    if armeeRegionBleue>=armeeRegionOrange :
        $ argentRegionBleue += argentRegionOrange//4
        $ argentRegionOrange -= argentRegionOrange//4
        hide screen statsInteractionBleue
        hide screen negociationBleueOrange
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionOrange:
        $ argentRegionBleue -= argentRegionBleue//2
        $ argentRegionOrange += argentRegionBleue//2
        hide screen statsInteractionBleue
        hide screen negociationBleueOrange
        scene mapRegionGrise
        call screen vueTerritoire

label bleueAttaqueOrange:
    $regionBleueActionFaite=True
    if armeeRegionBleue>=armeeRegionOrange :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBleueOrange
    elif armeeRegionBleue<armeeRegionOrange:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBleueOrange

#negociation guerre de bleue vers rose
screen negociationBleueRose:
    imagebutton :
        idle "accepter"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBleueRose")
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
        action  Jump("refusNegociationBleueRose")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBleueRose:
    if armeeRegionBleue>=armeeRegionRose :
        $ armeeRegionBleue -=armeeRegionRose
        $ armeeRegionRose = 0
        $ regionRoseActive=True
        hide screen statsInteractionBleue
        hide screen negociationBleueRose
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionRose:
        $ armeeRegionRose-=armeeRegionBleue
        $ armeeRegionBleue =0
        $ regionBleueActive = False
        hide screen statsInteractionBleue
        hide screen negociationBleueRose
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBleueRose:
    if armeeRegionBleue>=armeeRegionRose :
        $ argentRegionBleue += argentRegionRose//4
        $ argentRegionRose -= argentRegionRose//4
        hide screen statsInteractionBleue
        hide screen negociationBleueRose
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionRose:
        $ argentRegionBleue -= argentRegionBleue//2
        $ argentRegionRose += argentRegionBleue//2
        hide screen statsInteractionBleue
        hide screen negociationBleueRose
        scene mapRegionGrise
        call screen vueTerritoire

label bleueAttaqueRose:
    $regionBleueActionFaite=True
    if armeeRegionBleue>=armeeRegionRose :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBleueRose
    elif armeeRegionBleue<armeeRegionRose:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBleueRose

#negociation guerre de bleue vers jaune
screen negociationBleueJaune:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationBleueJaune")
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
        action  Jump("refusNegociationBleueJaune")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationBleueJaune:
    if armeeRegionBleue>=armeeRegionJaune :
        $ armeeRegionBleue -=armeeRegionJaune
        $ armeeRegionJaune = 0
        $ regionJauneActive=True
        hide screen statsInteractionBleue
        hide screen negociationBleueJaune
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionJaune:
        $ armeeRegionJaune-=armeeRegionBleue
        $ armeeRegionBleue =0
        hide screen statsInteractionBleue
        hide screen negociationBleueJaune
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationBleueJaune:
    if armeeRegionBleue>=armeeRegionJaune :
        $ argentRegionBleue += argentRegionJaune//4
        $ argentRegionJaune -= argentRegionJaune//4
        hide screen statsInteractionBleue
        hide screen negociationBleueJaune
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionBleue<armeeRegionJaune:
        $ argentRegionBleue -= argentRegionBleue//2
        $ argentRegionJaune += argentRegionBleue//2
        hide screen statsInteractionBleue
        hide screen negociationBleueJaune
        scene mapRegionGrise
        call screen vueTerritoire

label bleueAttaqueJaune:
    $regionBleueActionFaite=True
    if armeeRegionBleue>=armeeRegionJaune :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationBleueJaune
    elif armeeRegionBleue<armeeRegionJaune:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionBleue
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationBleueJaune





label upgradeRegionBleue:
    hide screen infoRegionBleue
    call screen upgradeRegionBleue
screen upgradeRegionBleue:       
    imagebutton :
        idle "upgrade1"
        xalign 0.3
        yalign 0.5
        action  Jump("upgradeChoix1Bleue")
    imagebutton :
        idle "upgrade2"
        xalign 0.7
        yalign 0.5
        action  Jump("upgradeChoix2Bleue")

label upgradeChoix1Bleue:
    if argentRegionBleue >  50 and populationRegionBleue > 50 and nourritureRegionBleue > 25 :
        if niveauRegionBleue<6 :
            $regionBleueActionFaite=True
            $ argentRegionBleue -= 50
            $ populationRegionBleue -=50
            $ nourritureRegionBleue-=25
            $ niveauRegionBleue+=1
            hide screen statsInteractionBleue
            scene mapRegionGrise
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"    
    else :
        a "Il vous manque des ressources "
        hide screen statsInteractionBleue
        scene mapRegionGrise
        call screen vueTerritoire

label upgradeChoix2Bleue:
            if argentRegionBleue > 130 and populationRegionBleue > 130 and nourritureRegionBleue > 65 :
                if niveauRegionBleue<6 :
                    $regionBleueActionFaite=True
                    $ argentRegionBleue -= 130
                    $ populationRegionBleue -= 130
                    $ nourritureRegionBleue-=35         
                    $ niveauRegionBleue+=3
                    hide screen statsInteractionBleue
                    scene mapRegionGrise
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"    
            else :
                a "Il vous manque des ressources "
                hide screen statsInteractionBleue
                scene mapRegionGrise
                call screen vueTerritoire