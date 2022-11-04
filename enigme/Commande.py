import random
import time
import sys
import Main

def felicitation(point, indice):
    print("BRAVO !! Vous avez atteint les ",point ," points ou plus !\nVous débloquez " ,indice , " indice suplémentaire !!")

def mauvaisecmd():
    print("\nMAUVAISE COMMANDE")

class Commande(): 
    
    def help():
        global nb_e
        cmd = input("\nTapez /help pour connaitre toutes les commandes de jeu.\n(Vous pouvez taper directement la Commande voulue au lieu\nde passer par /help si vous connaissez la commande souhaitée) : ")
        if cmd == '/help':
            print("\n")
            print(Main.enigme,": tirer une énigme au hasard\n/stat : voir ses statistiques\n/leave : quitter la partie(attention, si vous quitter, rien ne sera enregistré !)\n/rules : voir les règles du jeu\n/shop : acéder au magasin")
            print(Main.reset, " : réinitialiser le jeu")
            Commande.help()
        elif cmd == Main.stat:
            Commande.info()
        elif cmd == Main.partir:
            Commande.leave()
        elif cmd == Main.enigme:
            Main.tirer_enigme()
        elif cmd == '/rules':
            Commande.rules()
        elif cmd == '/config':
            Commande.config_niveau()
        elif cmd == Main.boutique:
            Commande.shop()
        elif cmd == Main.reset:
            Commande.reset()
        else:
            cm = False
            while cm == False:
                Main.mauvaisecmd()
                cmd = input()
          
                if cmd == '/help':
                    print(Main.enigme, "\n: tirer une énigme au hasard\n/stat : voir ses statistiques\n/leave : quitter la partie(attention, si vous quitter, rien ne sera enregistré !)\n/rules : voir les règles du jeu")
                    cm = True
                    Commande.help()
                if cmd == Main.stat:
                    cm = True
                    Commande.info()
                elif cmd == Main.partir:
                    cm = True
                    Commande.leave()
                elif cmd == Main.enigme:
                    cm = True
                    Main.tirer_enigme()
                elif cmd == '/rules':
                    cm = True
                    Commande.rules()
                elif cmd == '/config':
                    cm = True
                    Commande.config_niveau()
                elif cmd == Main.boutique:
                    cm = True
                    Commande.shop()
                elif cmd == Main.reset:
                    cm = True
                    Commande.reset()
                        
    def info():
        global max_indices
        global améliorations
        print("\n")
        if points >= 10 and points < 20:
            améliorations += 1
            if améliorations == 1:
                print(Main.felicitation(10, 1))
                max_indices += 1
        elif points >= 20:
            améliorations += 1

            if améliorations == 2:
                print(Main.felicitation(20, 2))
                max_indices += 2
            elif améliorations == 1:
                print(Main.felicitation(10, 1))
                max_indices += 1
                améliorations += 1
                print("\n", Main.felicitation(20, 2))
                max_indices += 2
        print("Vos statistiques :\n\npoints : %s\nnb d'énigme résolues : %s\nMain abandonnées : %s\nvotre argent : %s$\nindices disponibles : %s\nindices utilisés : %s" % (points, e_resol, e_ab, argent, (max_indices - indice_fournis), indice_fournis))
        Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
        Commande.help()

    def leave():
        sur = input("\nÊtes-vous sur (oui/non) ? ")
        if sur == 'oui':
            print("\n", Main.tresbien)
            sys.exit()
        elif sur == 'non':
            print("\nOk")
            Commande.help()
        else:
            mauvaisecmd()
            Commande.leave()

    def rules():
        rules = open("D:/python/enigme/rules.txt", encoding="utf8")
        R = rules.read()
        print("\n", R)
        p = input("\nVous pouvez faire /config ou 'pass' pour retrouner à l'accueil : ")
        if p == '/config':
            Commande.config_niveau()
        elif p == 'pass' or "'pass'":
            print("\n", Main.tresbien)
            Commande.help()
        else:
            while p != '/config' or 'pass' or "'pass'":
                mauvaisecmd()
                p = input("Vous pouvez faire /config ou 'pass' pour retourner à l'accueil : ")
                if p == '/config':
                    Commande.config_niveau()
                elif p == 'pass' or "'pass'":
                    Commande.help()

    def config_niveau():
        print("\nCaractérisiques des niveaux : \n\nniveau 1 : 1 indice possible\n           3 essais avant l'anulation du comptage des points de l'enigme\n           rapporte 1 point\n           rapporte entre 6 et 18$\nniveau 2 : 1 indice possible\n           2 essais possibles avant l'anunulation du comptage des points\n           rapporte 2 points\n           rapporte entre 18 et 30$\nniveau 3 : aucun indices possibles\n           2 essais avant l'anulation du comptage des points\n           rapporte 3 points\n           rapporte entre 30 et 42$.")
        Commande.help()

    # transformer les if / elif en une seul méthode ??????
    def shop(): 
        global max_indices
        global argent
        SHOP = open("d:/python/enigme/shop.txt", encoding="utf8")
        shop = SHOP.read()
        print("\n", shop)
        print("\nargent : %s" % argent)
        print("\nTapez ici le numéro de l'article que vous voulez acheter, sinon 'pass' pour fermer le shop :")
        choix = input()
        if choix in ('pass', "'pass'"):
            print("\n", Main.tresbien)
            print("\n", Main.revenez)
            Commande.help()
        elif choix in ("1", "1)"):
            if argent >= 70:
                max_indices += 1
                argent -= 70
                print("\nSuper !")
                print("\nMerci,", Main.revenez)
                print("\nargent : %s" % argent)
                Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                Commande.help()
            else:
                print("\n", Main.pasdargent)
                Commande.help()
        elif choix in ("2", "2)"):
            if argent >= 135:
                max_indices += 2
                argent -= 135
                print("\nSuper !")
                print("\nMerci,")
                print("\nargent : %s" % argent)
                Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                Commande.help()
            else:
                print("\n", Main.pasdargent)
                Commande.help()
        elif choix in ('3', '3)'):
            if argent >= 195:
                max_indices += 3
                argent -= 195
                print("\nSuper !")
                print("\nMerci,",Main.revenez)
                print("\nargent : %s" % argent)
                Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                Commande.help()
            else:
                print("\n", Main.pasdargent)
                Commande.help()
        elif choix in ('4', '4)'):
            if argent >= 50:
                print("\nAlors...")
                print("\n...")
                print("\nVous n'avez pas le droit à un indice et vous n'avez qu'un essai !!")
                print("\nQuelle est la couleur du cheval blanc d'henri IV ??")
                rep = input()
                if rep == 'blanc':
                    print("\nBRAVO !!! C'était difficile non ?")
                    argent_argent = random.randint(10, 20) * 3
                    print("\n+ %s$ !" % argent_argent)
                    print("+ 6 points !")
                    argent += argent_argent
                    points += 6
                    Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                    Commande.help()
                else:
                    print("\nraté ! c'était facile pourtant !")
                    Commande.help()
            else:
                print("\n", Main.pasdargent)
                Commande.help()
        elif choix in ('5', '5)'):
            if argent >= 30:
                print("\nVoulez-vous vraiment savoir l'information ultra-confidentielle?")
                print("\nEn fait comme vous avez deja payé je vais la dire... :)")
                print("\n\nLES CHAUSSETTES DE L'ARCHIDUCHESSE SONT SECHES !! PAS ARCHISECHES !!!!")
                Commande.help()
            else:
                print("\n", Main.pasdargent)
                Commande.help()
        else:
            mauvaisecmd()
            Commande.shop()
            
    def reset():
        global var_sauv, argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_
        argent = 0
        points = 0
        e_resol = 0
        e_ab = 0
        ct = 0
        e = 0
        indice_fournis = 0
        améliorations = 0
        niv_ = 0
        essais_ = 0
        #pt_ = 0
        ar_ = 0
        nb_e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        max_indices = 2
        time.sleep(1)
        str = "Réinitialisation terminée !!"
        x = str.center(153, "-")
        print("\n\n", x, "\n\n")
        Main.sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
        Commande.help()