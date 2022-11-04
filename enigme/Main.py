###IMPORTATIONS###
import random
import sys
import pickle
import os.path
import Commande
import fich_sauv

class Main():
    ###VARIABLES ET DICOS###
    var_sauv = None
    argent = 0
    points = 0
    e_resol = 0
    e_ab = 0
    ct = 0
    espace = ' ' * 35
    e = 0
    nb_e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    indice_fournis = 0
    max_indices = 2
    améliorations = 0
    niv_ = 0
    essais_ = 0
    pt = 0
    ar_ = 0

    en = ["Si cela cache, ce n'est que pour mieux révéler.\nCela bloque autant que cela permet de passer.\nLa réponse est dans la question.\nQue suis-je ?",
          "Je suis le commencement de l’effroi,\nLa fin de la durée et de l’espace,\nLe commencement de toutes extrémités,\nEt la fin de chaque contrée.\nQui suis-je ?",
          "Celui qui le fabrique le vend,\nCelui qui l'achète ne s'en sert pas,\nCelui qui s'en sert ne le sais pas.\nQu'est-ce ?",
          "Je serai hier, j'étais demain.",
          "Je suis si fragile que lorsque l'on prononce mon nom, je meurs.",
          "Je suis tout au bout de ta main,\nJe commence la nuit et je finis demain.",
          "Je me vide en me remplissant,\nEt je me remplis en me vidant,\nQue suis-je?",
          "Les feignant me vénèrent, mais je suis leur pire énemie.\nLes travailleurs me craignent mais je pourrais les soulager.\nQue suis-je ?",
          "Plus j'ai de gardien, moins je suis en sécurité\nMoins j'ai de gardien, plus je suis en sécurité.\nQue suis-je ?",
          "Une boite sans charnière, sans clé, sans couvercle.\nPourtant à l'intérieur est caché un trésor doré.",
          "Lors d'une guerre, un chevalier fut transpercé, il en mourrut,\nun deuxiéme guerrier fut décapité et les deux écuiers eurent la tête tranchée.\nCombien y a-t-il eu de morts ?",
          "Lumières qui fuient la lumière.",
          "Vivant sans souffle,\nFroid comme la mort,\nJamais assoiffé, toujours buvant,\nEn cotte de mailles, jamais cliquetant.",
          "Sans pieds, Sans mains, Sans ailes,\nje monte au ciel.",
          "Tellement magique qu'il vient à vous tous les soirs,\nIl vous emmène partout sans vous déplacer.\nPour le voir, vous devez d'abord fermer les yeux."]
    repn = [("une enigme", "une énigme"),
            ("le e", " la lettre e", " le E"),
            "un cercueil",
            "aujourd'hui",
            "le silence",
            ("le n", "la lettre n", "le N"),
            "un sablier",
            "l'ennui",
            "un secret",
            "un oeuf",
            ("2", "deux"),
            ("les etoiles", "les étoiles"),
            "un poisson",
            ('une âme', 'une ame', 'la fumée', 'de la fumée'),
            ('le rêve', 'un rêve')]
    indices = ["Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
               "la réponse comporte 4 caractère, déterminant et espace compris",
               "c'est matériel",
               "c'est un moment",
               "c'est immatériel",
               "la réponse comporte 4 caractère, déterminant et espace compris",
               "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
               "long de 5 caractère (déterminant et espace(s) eventuel(s) non compris), ça commence par un 'e'",
               "c'est immatériel",
               "ne pas prendre les mots au pied de la lettre",
               "faire attention aux sens de 'eurent'",
               "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
               "le poid du son",
               "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice",
               ""]

    tresbien = "Très bien..."
    revenez = "Revenez vite !"
    pasdargent = "Vous n'avez pas assez d'argent :("
    enigme = "/enigme"
    stat = "/stat"
    partir = "/leave"
    reset = "/reset"
    boutique = "/shop"
    abandon = "/abandon"
    correct = "Bonne réponse !!!!"

    enigmeI = -1
    enigmes = {
    }
    while(enigmeI != 12):
        enigmeI += 1
        if(enigmeI < 11):
            a = (",")
        else:
            a = ("")
        enigmes['rep e'+str(enigmeI+1)] = str(en[enigmeI]) + str(a)

    repnI = -1
    rep_enigme = {
    }
    while(repnI != 12):
        repnI += 1
        if(repnI < 11):
            a = (",")
        else:
            a = ("")
        rep_enigme['rep e'+str(repnI+1)] = str(repn[repnI]) + str(a)

    indiceI = -1
    idi = {
    }
    while(indiceI != 12):
        indiceI += 1
        if(indiceI < 11):
            a = (",")
        else:
            a = ("")
        idi['e'+str(indiceI+1)] = str(indices[indiceI]) + str(a)
        
    def mauvaisecmd():
        print("\nMAUVAISE COMMANDE")

    def sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_):
        global var_sauv
        var_sauv = [argent, points, e_resol, e_ab, ct, espace, e, nb_e,
                    indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_]
        fich_sauv = open("d:/python/enigme/fich_sauv", "wb")
        pickle.dump(var_sauv, fich_sauv)
        fich_sauv.close()

    def charger():
        global var_sauv, argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_
        fichier = "fich_sauv"
        if os.path.isfile(fichier):
            fich_sauv = open(fichier, 'rb')
            var_sauv = pickle.load(fich_sauv)
            fich_sauv.close()
            argent = var_sauv[0]
            points = var_sauv[1]
            e_resol = var_sauv[2]
            e_ab = var_sauv[3]
            ct = var_sauv[4]
            espace = var_sauv[5]
            e = var_sauv[6]
            nb_e = var_sauv[7]
            indice_fournis = var_sauv[8]
            max_indices = var_sauv[9]
            améliorations = var_sauv[10]
            niv_ = var_sauv[11]
            essais_ = var_sauv[12]
            pt = var_sauv[13]
            ar_ = var_sauv[14]
        else:
            print("Le fichier de sauvegarde '%s' n'existe pas" % fichier)

    def repondre(niv, essais, pt, ar):
        global points
        global e_resol
        global ct
        global e_ab
        global indice_fournis
        global argent
        rep = input()
        if rep in Main.rep_enigme['rep e%s' % e] or rep == 'triche':
            print("\n", Main.correct)
            ct = 0
            points = points + pt
            argent += ar
            e_resol = e_resol + 1
            print("+ %s point !!" % pt)
            print("+ %s$ !!" % ar)
            Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e,
                indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
            Commande.help()
        elif rep == Main.abandon:
            e_ab = e_ab + 1
            print("\n", Main.tresbien)
            print("\npoints : %s" % points)
            nb_e.append(e)
            Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e,
                indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
            Commande.help()
        elif rep == '/indice':
            if indice_fournis in (0, 1):
                print(Main.idi['i %s' % e])
                if Main.idi['i %s' % e] == "\nCette énigme est une énigme de niveau %s, par conséquent il n'y a pas d'indice disponible" % niv:
                    pass
                else:
                    indice_fournis += 1
            elif indice_fournis == max_indices:
                print("\nVous avez déjà eu tous vos indices !!")
            Main.repondre(niv_, essais_, pt_, ar_)
        elif rep == '/niveau':
            print("\nenigme de niveau %s" % niv)
            Main.repondre(niv_, essais_, pt_, ar_)
        elif '/' in rep:
            Main.mauvaisecmd()
            Main.repondre(niv_, essais_, pt_, ar_)
        else:
            while rep != Main.rep_enigme['rep e%s' % e]:
                ct = ct + 1
                Main.mauvaisecmd()
                rep = input()
                if rep in Main.rep_enigme['rep e%s' % e]:
                    print(Main.correct)
                    if ct > essais:
                        print(
                            "\n%s réponses ou plus ont été écrites donc vous ne gagnez pas de points à cette énigme-ci..." % essais)
                        Commande.help()
                    else:
                        points = points + pt
                        argent += ar
                    e_resol = e_resol + 1
                    ct = 0
                    print("+ %s point !!" % pt)
                    print("+ %s$ !!" % ar)
                    Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e,
                        indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                    Commande.help()
                elif rep == Main.abandon:
                    e_ab = e_ab + 1
                    ct = 0
                    print("\n", Main.tresbien)
                    print("\npoints : %s" % points)
                    Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e,
                        indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                    Commande.help()
                elif rep == '/indice':
                    if indice_fournis in (0, 1):
                        print(Main.idi['i %s' % e])
                        if Main.idi['i %s' % e] == "\nCette énigme est une énigme de niveau %s, par conséquent il n'y a pas d'indice disponible" % niv:
                            pass
                        else:
                            indice_fournis += 1
                    elif indice_fournis == max_indices:
                        print("\nVous avez déjà eu tous vos indices !!")
                    Main.repondre(niv_, essais_, pt_, ar_)
                elif rep == '/niveau':
                    print("\nenigme de niveau %s" % niv)
                    Main.repondre(niv_, essais_, pt_, ar_)
                elif '/' in rep:
                    Main.mauvaisecmd()
                    Main.repondre(niv_, essais_, pt_, ar_)

    def tirer_enigme():
        global e
        global niv_
        global essais_
        global pt_
        global ar_

    if len(nb_e) == 0:
        print("BRAVO A VOUS !!!! VOUS AVEZ RESOLU TOUTES LES ENIGMES, VOUS AVEZ FINI LE JEU !!!!")
        print("\n", reset, "pour recommencer une partie en réinitialisant toutes les données. Sinon ", partir)
        print("\n pour quitter définitivement")
        choice = input()
        if choice == partir:
            sys.exit()
        elif choice == reset:
            Commande.reset()
        else:
            mauvaisecmd()
            tirer_enigme()
    else:
        e = random.choice(nb_e)
        print("...\n")
        print("Tirage de l'enigme en cours...\n")
        print("...\n")
        print(['e%s' % e])
        nb_e.remove(e)
        # sus here \/
        if e in (2, 4, 6, 9, 11):
            niv_ = 1
            essais_ = 3
            pt_ = 1
            ar_ = random.randint(6, 18)
            sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e,
                   indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
            repondre(niv_, essais_, pt_, ar_)
        elif e in (3, 5, 8, 10, 13):
            niv_ = 2
            essais_ = 2
            pt_ = 2
            ar_ = random.randint(18, 30)
            sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e,
                   indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
            repondre(niv_, essais_, pt_, ar_)
        elif e in (1, 7, 12, 14):
            niv_ = 3
            essais_ = 2
            pt_ = 3
            ar_ = random.randint(30, 42)
            sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e,
                   indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
            repondre(niv_, essais_, pt_, ar_)

    ###BOUCLE PRINIPALE###
    s = "\n\nBIENVENUE DANS UN JEU D'ENIGMES !!!"
    xx = s.center(153, '=')
    print(xx, "\n")
    charger()
    print("\n")
    Commande.help()
