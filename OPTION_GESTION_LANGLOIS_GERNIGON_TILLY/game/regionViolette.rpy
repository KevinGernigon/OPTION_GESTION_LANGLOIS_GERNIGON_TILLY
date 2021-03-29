
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
        $ popUpInfoRegionOn=True
        image "../images/carre_gris.png":
            at carre_zoom
            xpos 750
            ypos 80
        text "Armee :" :
            xpos 760
            ypos 80
        text "%d" % armeeRegionViolette :
            xpos 910
            ypos 80
        text "Argent :" :
            xpos 760
            ypos 110
        text "%d" % argentRegionViolette :
            xpos 910
            ypos 110
        text "Population :":
            xpos 760
            ypos 140
        text "%d" % populationRegionViolette:
            xpos 910
            ypos 140
        text "Nourriture :":
            xpos 760
            ypos 170
        text "%d" % nourritureRegionViolette:
            xpos 910
            ypos 170
        if(regionVioletteActionFaite==False):
            imagebutton :
                idle "../images/interagir.png"
                xpos 800
                ypos 220
                action Jump("interactionViolette")
        if (regionOrangeActive==False or regionBleueActive==False) and regionVioletteActionFaite==False:        
            imagebutton :
                idle "../images/attaquer.png"
                xpos 800
                ypos 280
                action  Jump("attaqueViolette")
        imagebutton :
            idle "../images/exit.png"
            at exit_zoom
            xpos 1000
            ypos 90  
            action  Hide("infoRegionViolette")










########################################################################################################################
########################################################################################################################







label interactionViolette :
    hide screen infoRegionViolette
    scene office
    show pythie at left
    show screen statsInteractionViolette
    call screen interactionViolette
screen statsInteractionViolette:
    image "../images/blackbox.png"
    text "Région Violette" :
        xpos 580
        ypos 70
    text "Armee :" :
        xpos 100
        ypos 20
    text "%d" % armeeRegionViolette :
        xpos 200
        ypos 20
    text "Argent :" :
        xpos 400
        ypos 20
    text "%d" % argentRegionViolette :
        xpos 500
        ypos 20
    text "Population :":
        xpos 700
        ypos 20
    text "%d" % populationRegionViolette:
        xpos 850
        ypos 20
    text "Nourriture :":
        xpos 1000
        ypos 20
    text "%d" % nourritureRegionViolette:
        xpos 1150
        ypos 20

screen interactionViolette:
    imagebutton :
        idle "boxInteragir1"
        xalign 0.2
        ypos 100
        action  Jump("ministreArmeeViolette")
    text "Armée":
        xalign 0.18
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xalign 0.8
        ypos 100
        action  Jump("ministreAgricultureViolette")
    text "Nourriture":
        xalign 0.87
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xalign 0.22
        ypos 400
        action  Jump("ministreCivilsViolette")
    text "Civils":
        xalign 0.18
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xalign 0.8
        ypos 400
        action  Jump("ministreFinancesViolette")
    text "Finances":
        xalign 0.87
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xalign 0.5
        ypos 400
        action  Jump("ministreAmbassadeurViolette")
    text "Ambassade":
        xalign 0.47
        ypos 580
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "upgrade1"
        xalign 0.5
        ypos 100
        action  Jump("upgradeRegionViolette")
    text "Améliorer":
        xalign 0.47
        ypos 200
        outlines [ (3, "#000", 0, 0) ]








#armees
label ministreArmeeViolette:
    p "Assistante convoquez moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeViolette2
label ministreArmeeViolette2 :
    call screen ministreArmeeViolette2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5
transform variableJaugeText :
    zoom 2


screen ministreArmeeViolette2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreArmeeViolette2"), Jump("variableJauge")]
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeViolette")
    text " +%d" % variableJauge:  
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyViolette"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeViolette")
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
        idle "armyViolette"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donTroupesArmeeViolette")
    text " +%d" % variableJauge:  
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeViolette")
    text " -%d" % variableJauge:  
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionTroupesArmeeViolette:
            p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
            if armeeRegionViolette < variableJauge :
                a "Nous n'avons pas assez de soldats à vous léguer mon commandant."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ armeeGeneral += variableJauge
                $ armeeRegionViolette -=  variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire

label donTroupesArmeeViolette:
            if armeeGeneral < variableJauge :
                p "Vous ne pouvez pas faire ça, vous ne possédez pas assez de soldats"
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je souhaite renforcer la zone je vous ais donc envoyé des soldats"
                a "Merci commandant"
                $ armeeRegionViolette += variableJauge
                $ armeeGeneral -= variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire










#agriculture
label ministreAgricultureViolette:
    p "Assistante convoquez moi le ministre de l'agriculture svp"
    show agriculture at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAgricultureViolette2
label ministreAgricultureViolette2 :
    call screen ministreAgricultureViolette2


screen ministreAgricultureViolette2:
#choix gauche
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAgricultureViolette2"), Jump("variableJauge")]
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureViolette")
    text " +%d" % variableJauge: 
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodViolette"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureViolette")
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
        idle "foodViolette"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donNourritureAgricultureViolette")
    text " +%d" % variableJauge: 
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureViolette")
    text " -%d" % variableJauge: 
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



label requisitionNourritureAgricultureViolette:
            p "Je souhaite requisitionner de la nourriture"
            if nourritureRegionViolette < variableJauge :
                a "Nous ne pouvons pas vous donner de nourriture, nous subvenons tout juste à nos besoins."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ nourritureRegionViolette -= variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire

label donNourritureAgricultureViolette:
            if nourritureGeneral < variableJauge :
                p "Je ne peux pas vous donner de nourriture, je n'en possède pas assez."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de la nourriture"
                a "Merci commandant"
                $ nourritureGeneral -= variableJauge
                $ nourritureRegionViolette += variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire


#civils


label ministreCivilsViolette:
    p "Assistante convoquer moi le ministre des civils svp"
    show civil at right
    c "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreCivilsViolette2
label ministreCivilsViolette2 :
    call screen ministreCivilsViolette2

screen ministreCivilsViolette2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreCivilsViolette2"), Jump("variableJauge")]
    imagebutton :
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsViolette")
    text " +%d" % variableJauge: 
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popViolette"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsViolette")
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
        idle "popViolette"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donCivilsViolette")
    text " +%d" % variableJauge: 
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsViolette")
    text " -%d" % variableJauge: 
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionCivilsViolette:
            p "Je souhaite requisitionner des civils"
            if populationRegionViolette < variableJauge :
                a "Veuillez m'excuser mon commandant, nous n'avons pas assez de civils à vous confier."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationGeneral += variableJauge
                $ populationRegionViolette -= variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire

label donCivilsViolette:
            if populationGeneral < variableJauge :
                "Vous n'avez pas assez de civils dans votre armée générale."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie des civils"
                a "Merci commandant"
                $ populationGeneral -= variableJauge
                $ populationRegionViolette += variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire



#finances
label ministreFinancesViolette:
    p "Assistante convoquez moi le ministre des finances svp"
    show religion at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreFinancesViolette2
label ministreFinancesViolette2 :
    call screen ministreFinancesViolette2

screen ministreFinancesViolette2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreFinancesViolette2"), Jump("variableJauge")]
    imagebutton :
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesViolette")
    text " +%d" % variableJauge:
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesViolette"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesViolette")
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
        idle "financesViolette"
        xpos 950
        yalign 0.5
        at choix_icons
        action  Jump("donFinancesViolette")
    text " +%d" % variableJauge:
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesViolette")
    text " -%d" % variableJauge:
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

label requisitionFinancesViolette:
            p "Je souhaite requisitionner de l'argent"
            if argentRegionViolette < variableJauge :
                a "Veuillez m'excuser mon commandant mais nous ne pouvons pas nous permettre ce sacrifice."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentGeneral += variableJauge
                $ argentRegionViolette -= variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire

label donFinancesViolette:
            if argentGeneral < variableJauge :
                p "Je n'ai pas assez d'argent."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                p "Je vous envoie de l'argent"
                a "Merci commandant"
                $ argentGeneral -= variableJauge
                $ argentRegionViolette += variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire



#ambassadeur
label ministreAmbassadeurViolette:
    p "Assistante convoquer moi l'ambassadeur de cette région svp"
    show ambassadeur at right
    h "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreAmbassadeurViolette2

label ministreAmbassadeurViolette2 :
    call screen ministreAmbassadeurViolette2

screen ministreAmbassadeurViolette2:
    imagebutton :
        idle "modifyJauge"
        xalign 0.5
        yalign 0.25
        action  [SetVariable("lastScreen", "ministreAmbassadeurViolette2"), Jump("variableJauge")]
    imagebutton :
        idle "armyViolette"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurViolette")
    text " +%d" % variableJauge: 
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popViolette"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurViolette")
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
        idle "foodViolette"
        xalign 0.6
        yalign 0.3
        at choix_icons
        action  Jump("augmenterNourritureAmbassadeurViolette")
    text " +%d" % variableJauge: 
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popViolette"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurViolette")
    text " -%d" % variableJaugeDiv2: 
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesViolette"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurViolette")
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
        idle "financesViolette"
        xalign 0.295
        yalign 0.7
        at choix_icons
        action  Jump("vendreNourritureAmbassadeurViolette")
    text " +%d" % variableJauge: 
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodViolette"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurViolette")
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
        idle "popViolette"
        xalign 0.695
        yalign 0.7
        at choix_icons
        action  Jump("reintegrerSoldatsAmbassadeurViolette")
    text " +%d" % variableJauge: 
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyViolette"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurViolette")
    text " -%d" % variableJauge: 
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



label augmenterArmeeEmbassadeurViolette:
            p "Je souhaite que vous entrainez des civils en soldats"
            if populationRegionViolette < variableJauge :
                a "Nous ne pouvons pas nous permettre d'entraîner autant de civils, notre population est déjà faible..."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionViolette -= variableJauge
                $ armeeRegionViolette += variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire

label augmenterNourritureAmbassadeurViolette:
            p "Je souhaite que vous produisiez plus de nourriture"
            if argentRegionViolette < variableJaugeDiv2 :
                a "Nous n'avons pas les moyens de produire plus de nourriture actuellement."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            if populationRegionViolette < variableJaugeDiv2 :
                a "Nous ne pouvons pas nous permettre de risquer le peu de paysans qu'il nous reste avec du travail forcé."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ nourritureGeneral += variableJauge
                $ populationRegionViolette -= variableJaugeDiv2
                $ argentRegionViolette -= variableJaugeDiv2
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire

label vendreNourritureAmbassadeurViolette:
            p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
            if nourritureRegionViolette < variableJauge :
                a "Nous n'avons pas assez de nourriture à vous vendre."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ argentRegionViolette += variableJauge
                $ nourritureRegionViolette -= variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire



label reintegrerSoldatsAmbassadeurViolette:
            p "Je souhaite que des soldats retournent au statut de civil"
            if armeeRegionViolette < variableJauge :
                a "Nous ne pouvons pas nous passer du si peu de soldats qu'il nous reste."
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire
            else :
                a "Très bien commandant "
                $ populationRegionViolette += variableJauge
                $ armeeRegionViolette -= variableJauge
                $ regionVioletteActionFaite = True
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire



label attaqueViolette:
    hide screen infoRegionViolette
    call screen attaqueViolette
screen attaqueViolette:       
    if regionOrangeActive==False:
        imagebutton:
            idle "regionOrangeRouge.png"
            xpos 370
            ypos 90
            action Jump("violetteAttaqueOrange")
        image "logoAttaque":
            xpos 575
            ypos 200          


#negociation guerre de violette vers jaune
screen negociationVioletteOrange:
    imagebutton :
        idle "accepter"
        xpos 300
        yalign 0.5
        at choix_icons
        action  Jump("acceptationNegociationVioletteOrange")
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
        action  Jump("refusNegociationVioletteOrange")
    text "Refuser" :
        xpos 960
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]

label refusNegociationVioletteOrange:
    if armeeRegionViolette>=armeeRegionOrange :
        $ armeeRegionViolette -=armeeRegionOrange
        $ armeeRegionOrange = 0
        $ regionOrangeActive=True
        hide screen statsInteractionViolette
        hide screen negociationVioletteOrange
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionViolette<armeeRegionOrange:
        $ armeeRegionOrange-=armeeRegionViolette
        $ armeeRegionViolette =0
        hide screen statsInteractionViolette
        hide screen negociationVioletteOrange
        scene mapRegionGrise
        call screen vueTerritoire

label acceptationNegociationVioletteOrange:
    if armeeRegionViolette>=armeeRegionOrange :
        $ argentRegionViolette += argentRegionOrange//4
        $ argentRegionOrange -= argentRegionOrange//4
        hide screen statsInteractionViolette
        hide screen negociationVioletteOrange
        scene mapRegionGrise
        call screen vueTerritoire
    elif armeeRegionViolette<armeeRegionOrange:
        $ argentRegionViolette -= argentRegionViolette//2
        $ argentRegionOrange += argentRegionViolette//2
        hide screen statsInteractionViolette
        hide screen negociationVioletteOrange
        scene mapRegionGrise
        call screen vueTerritoire

label violetteAttaqueOrange:
    $regionVioletteActionFaite=True
    if armeeRegionViolette>=armeeRegionOrange :
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionViolette
        p "Je vous déclare la guerre !"
        a "S'il vous plait prenez cet Argent et épargnez nos vies !"
        call screen negociationVioletteOrange
    elif armeeRegionViolette<armeeRegionOrange:
        hide screen vueTerritoire
        scene office
        show pythie at left
        show armees at right
        show screen statsInteractionViolette
        p "Je vous déclare la guerre !"
        a "Vous n'avez aucune chance mécréant !"
        a "Mais je veux bien vous laisser partir en échange de la moitié de votre Argent."
        call screen negociationVioletteOrange





label upgradeRegionViolette:
    hide screen infoRegionViolette
    call screen upgradeRegionViolette
screen upgradeRegionViolette:       
    imagebutton :
        idle "upgrade1"
        xalign 0.3
        yalign 0.5
        action  Jump("upgradeChoix1Violette")
    imagebutton :
        idle "upgrade2"
        xalign 0.7
        yalign 0.5
        action  Jump("upgradeChoix2Violette")

label upgradeChoix1Violette:
    if argentRegionViolette >  50 and populationRegionViolette > 50 and nourritureRegionViolette > 25 :
        if niveauRegionViolette<6 :
            $regionVioletteActionFaite=True
            $ argentRegionViolette -= 50
            $ populationRegionViolette -=50
            $ nourritureRegionViolette-=25
            $ niveauRegionViolette+=1
            hide screen statsInteractionViolette
            scene mapRegionGrise
            call screen vueTerritoire
        else :
            a "Vous êtes déjà au niveau maximum"    
    else :
        a "Il vous manque des ressources "
        hide screen statsInteractionViolette
        scene mapRegionGrise
        call screen vueTerritoire

label upgradeChoix2Violette:
            if argentRegionViolette > 130 and populationRegionViolette > 130 and nourritureRegionViolette > 65 :
                if niveauRegionViolette<6 :
                    $regionVioletteActionFaite=True
                    $ argentRegionViolette -= 130
                    $ populationRegionViolette -= 130
                    $ nourritureRegionViolette-=35         
                    $ niveauRegionViolette+=3
                    hide screen statsInteractionViolette
                    scene mapRegionGrise
                    call screen vueTerritoire
                else :
                    a "Vous êtes déjà au niveau maximum"    
            else :
                a "Il vous manque des ressources "
                hide screen statsInteractionViolette
                scene mapRegionGrise
                call screen vueTerritoire