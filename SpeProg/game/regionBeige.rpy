
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
        xpos 300
        ypos 100
        action  Jump("ministreArmeeBeige")
    text "Armée":
        xpos 300
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 100
        action  Jump("ministreAgricultureBeige")
    text "Nourriture":
        xpos 820
        ypos 200
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir3"
        xpos 300
        ypos 400
        action  Jump("ministreCivilsBeige")
    text "Civils":
        xpos 300
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir4"
        xpos 680
        ypos 400
        action  Jump("ministreFinancesBeige")
    text "Finances":
        xpos 820
        ypos 500
        outlines [ (3, "#000", 0, 0) ]
    imagebutton :
        idle "boxInteragir5"
        xpos 490
        ypos 250
        action  Jump("ministreAmbassadeurBeige")
    text "Ambassade":
        xalign 0.43
        yalign 0.58
        outlines [ (3, "#000", 0, 0) ]









#armees
label ministreArmeeBeige:
    p "Assistante convoquer moi le ministre des armées svp"
    show armees at right
    a "Vous m'avez demandé commandant ?"
    p "Oui je voulais vous demander..."
    jump ministreArmeeBeige2
label ministreArmeeBeige2 :
    call screen ministreArmeeBeige2

# dezoom pour les icons de choix
transform choix_icons :
    zoom 0.5

screen ministreArmeeBeige2:

#choix gauche
    imagebutton :
        idle "armyGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionTroupesArmeeBeige")
    text "+30" :
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyBeige"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionTroupesArmeeBeige")
    text "-30" :
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
    text "+30" :
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donTroupesArmeeBeige")
    text "-30" :
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de soldats":
        xpos 870
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

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
                $ regionBeigeActionFaite = True
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
#choix gauche
    imagebutton :
        idle "foodGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionNourritureAgricultureBeige")
    text "+30" :
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodBeige"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionNourritureAgricultureBeige")
    text "-30" :
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
    text "+30" :
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donNourritureAgricultureBeige")
    text "-30" :
        xpos 870
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de nourriture":
        xpos 860
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]



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
        idle "popGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionCivilsBeige")
    text "+30" :
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBeige"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionCivilsBeige")
    text "-30" :
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
    text "+30" :
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donCivilsBeige")
    text "-30" :
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don de civils":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

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
        idle "financesGeneral"
        xpos 280
        yalign 0.5
        at choix_icons
        action  Jump("requisitionFinancesBeige")
    text "+30" :
        xpos 300
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesBeige"
        xpos 370
        yalign 0.5
        at choix_icons
        action Jump("requisitionFinancesBeige")
    text "-30" :
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
    text "+30" :
        xpos 980
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesGeneral"
        xpos 850
        yalign 0.5
        at choix_icons
        action Jump("donFinancesBeige")
    text "-30" :
        xpos 880
        yalign 0.6
        outlines [ (2, "#000", 0, 0) ]
    text "Don d'argent":
        xpos 880
        yalign 0.65
        outlines [ (3, "#000", 0, 0) ]

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
        idle "armyBeige"
        xalign 0.295
        yalign 0.3
        at choix_icons
        action  Jump("augmenterArmeeEmbassadeurBeige")
    text "+30" :
        xalign 0.3
        yalign 0.4
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBeige"
        xalign 0.38
        yalign 0.3
        at choix_icons
        action Jump("augmenterArmeeEmbassadeurBeige")
    text "-30" :
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
    text "+30" :
        xalign 0.6
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "popBeige"
        xalign 0.70
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurBeige")
    text "-15" :
        xalign 0.69
        yalign 0.41
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "financesBeige"
        xalign 0.8
        yalign 0.3
        at choix_icons
        action Jump("augmenterNourritureAmbassadeurBeige")
    text "-15" :
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
    text "+30" :
        xalign 0.3
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "foodBeige"
        xalign 0.38
        yalign 0.7
        at choix_icons
        action Jump("vendreNourritureAmbassadeurBeige")
    text "-30" :
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
    text "+30" :
        xalign 0.69
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    imagebutton :
        idle "armyBeige"
        xalign 0.635
        yalign 0.7
        at choix_icons
        action Jump("reintegrerSoldatsAmbassadeurBeige")
    text "-30" :
        xalign 0.628
        yalign 0.77
        outlines [ (2, "#000", 0, 0) ]
    text "Retour à la vie civile":
        xpos 740
        yalign 0.82
        outlines [ (3, "#000", 0, 0) ]



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





label upgradeRegionBeige:
    hide screen infoRegionBeige
    call screen upgradeRegionBeige
screen upgradeRegionBeige:       
    imagebutton :
        idle "boxInteragir1"
        xpos 300
        ypos 100
        action  Jump("upgradeChoix1")
    imagebutton :
        idle "boxInteragir2"
        xpos 680
        ypos 100
        action  Jump("upgradeChoix2")

label upgradeChoix1:

            if argentRegionBeige > 50 and populationRegionBeige > 50 and nourritureRegionBeige > 25 :
                return
            else :
                a "Il vous manque des ressources "
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire

label upgradeChoix2:
            if argentRegionBeige > 130 and populationRegionBeige > 130 and nourritureRegionBeige > 65 :
               return
            else :
                a "Il vous manque des ressources "
                hide screen statsInteractionBeige
                scene mapRegionGrise
                call screen vueTerritoire