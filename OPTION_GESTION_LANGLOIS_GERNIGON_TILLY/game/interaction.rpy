label interaction:
    define p = Character(_('Pythie'), color="#c8ffc8")
    define a = Character(_('Ministre des armées'), color="#c8ffc8")
    define h = Character(_('Ministre de l"agriculture'), color="#c8ffc8")
    define c = Character(_('Ministre des civils'), color="#c8ffc8")
    define r = Character(_('Ministre des religions'), color="#c8ffc8")
    define a = Character(_('Ambassadeur'), color="#c8ffc8")

    default var_armee_totale = 150
    default var_argent_totale = 150
    default var_population_totale = 150
    default var_nourriture_totale = 150

    default var_armee_region_1 = 50
    default var_argent_region_1 = 50
    default var_population_region_1 = 50
    default var_nourriture_region_1 = 50


    image office = im.Scale ("office.png", 1280, 720)

    scene bg office

    show pythie at left
#armees
    menu:
        "Convoquer le ministre des armées":
            p "Assistante convoquer moi le ministre des armées svp"
            show armees at right
            a "Vous m'avez demandé commandant ?"
            p "Oui je voulais vous demander..."
            menu:
                "Augmenter la taille de mon armée(30)":
                    p "Je souhaite requisitionner des soldats pour augmenter la taille de mes armées"
                    a "Très bien commandant "
                    $ var_armee_totale += 30
                    $ var_armee_region_1 -=  30
                "Donner des soldats(30)":
                    p "Je souhaite renforcer la zone je vous ait donc envoyer des soldats"
                    a "Merci commandant"
                    $ var_armee_region_1 += 30
                    $ var_armee_totale -= 30
#agriculture
        "Convoquer le ministre de l'agriculture":
            p "Assistante convoquer moi le ministre de l'agriculture svp"
            show agriculture at right
            h "Vous m'avez demandé commandant ?"
            p "Oui je voulais vous demander..."
            menu:
                "Requistionner de la nourriture(30)":
                    p "Je souhaite requisitionner de la nourriture"
                    a "Très bien commandant "
                    $ var_nourriture_totale += 30
                    $ var_nourriture_region_1 -= 30
                "Donner de la nourriture(30)":
                    p "Je vous envoie de la nourriture"
                    a "Merci commandant"
                    $ var_nourriture_totale -= 30
                    $ var_nourriture_region_1 += 30
#civils
        "Convoquer le ministre des civils":
            p "Assistante convoquer moi le ministre des civils svp"
            show civil at right
            c "Vous m'avez demandé commandant ?"
            p "Oui je voulais vous demander..."
            menu:
                "Requistionner des civils(30)":
                    p "Je souhaite requisitionner des civils"
                    a "Très bien commandant "
                    $ var_population_totale += 30
                    $ var_population_region_1 -= 30
                "Donner des civils(30)":
                    p "Je vous envoie des civils"
                    a "Merci commandant"
                    $ var_population_totale -= 30
                    $ var_population_region_1 += 30
#finances
        "Convoquer le ministre des finances":
            p "Assistante convoquer moi le ministre des finances svp"
            show religion at right
            h "Vous m'avez demandé commandant ?"
            p "Oui je voulais vous demander..."
            menu:
                "Requistionner de l'argent(30)":
                    p "Je souhaite requisitionner de l'argent"
                    a "Très bien commandant "
                    $ var_argent_totale += 30
                    $ var_argent_region_1 -= 30
                "Donner de l'argent(30)":
                    p "Je vous envoie de l'argent"
                    a "Merci commandant"
                    $ var_argent_totale -= 30
                    $ var_argent_region_1 += 30
#ambassadeur
        "Convoquer l'ambassadeur de cette région":
            p "Assistante convoquer moi l'ambassadeur de cette région svp"
            show ambassadeur at right
            h "Vous m'avez demandé commandant ?"
            p "Oui je voulais vous demander..."
            "Augmenter la taille de l'armée de cette région(+30 armee / -30 population)":
                p "Je souhaite que vous entrainez des civils en soldats"
                a "Très bien commandant "
                $ var_population_region_1 -= 30
                $ var_armee_region_1 += 30
            "Augmenter la nourriture de cette région(+30 nourriture / -15 argent -15 population)":
                p "Je souhaite que vous produisiez plus de nourriture"
                a "Très bien commandant "
                $ var_nourriture_totale += 30
                $ var_population_region_1 -= 15
                $ var_argent_region_1 -= 15
            "Augmenter l'argent de cette région(+30 argent / -30 nourriture)":
                p "Je souhaite que vous vendiez de la nourriture contre de l'argent"
                a "Très bien commandant "
                $ var_argent_region_1 += 30
                $ var_nourriture_region_1 -= 30
            "Augmenter la taille de la population de cette région(+30 population / -30 armee)":
                p "Je souhaite des soldats retournent au statut de civil"
                a "Très bien commandant "
                $ var_population_region_1 += 30
                $ var_armee_region_1 -= 30
