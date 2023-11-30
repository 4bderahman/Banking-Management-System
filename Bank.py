import random
import csv

# Classe Banque pour la gestion des clients et de leurs comptes bancaires
class Banque:
    def __init__(self):
        # Dictionnaires pour stocker les informations des clients, des comptes, et la relation entre eux
        self._clients = {}
        self._comptes = {}
        self._clients_comptes = {}

    # Méthode pour ajouter un nouveau client et son compte
    def ajouter_client(self, num_cl, mpc, num_c, solde_c):
        self._clients[num_cl] = mpc
        self._comptes[num_c] = solde_c
        self._clients_comptes[num_cl] = num_c

    # Méthode pour supprimer un client et son compte associé
    def supprimer_client(self, num_c):
        num_cl = [key for key, value in self._clients_comptes.items() if value == num_c]
        if num_cl:
            del self._clients[num_cl[0]]
            del self._comptes[num_c]
            del self._clients_comptes[num_cl[0]]

    # Méthode pour modifier le mot de passe (code secret) d'un client
    def modifier_mp_client(self, num_cl, nouveau_mp):
        if num_cl in self._clients:
            self._clients[num_cl] = nouveau_mp

    # Méthode pour déposer de l'argent dans un compte
    def deposer(self, num_c, montant):
        if num_c in self._comptes:
            self._comptes[num_c] += montant

    # Méthode pour retirer de l'argent d'un compte
    def retirer(self, num_c, montant):
        if num_c in self._comptes and self._comptes[num_c] >= montant:
            self._comptes[num_c] -= montant

    # Méthode pour générer un numéro de compte unique basé sur le numéro du client
    def generer_num_compte(self, num_cl):
        return int(str(num_cl) + str(random.randint(0, 100)))

    # Méthode pour écrire les informations des clients dans un fichier CSV
    def ecrire_fichier_csv(self):
        with open('clients.csv', 'w', newline='') as csvfile:
            fieldnames = ['Numéro Client', 'Code Secret']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for num_cl, code_secret in self._clients.items():
                writer.writerow({'Numéro Client': num_cl, 'Code Secret': code_secret})

    # Méthode pour manipuler les structures de données
    def manipuler_sts(self):
        liste_num_comptes = list(self._clients_comptes.values())
        tuple_num_comptes = tuple(self._clients_comptes.values())
        set_num_comptes = set(self._clients_comptes.values())

        return liste_num_comptes, tuple_num_comptes, set_num_comptes

    # Getters pour accéder aux données privées
    def get_clients(self):
        return self._clients

    def get_comptes(self):
        return self._comptes

    def get_clients_comptes(self):
        return self._clients_comptes

# Instance de la classe Banque
banque = Banque()

# Boucle principale du programme pour l'interaction avec l'utilisateur
while True:
    print("Menu principal:")
    print("1. Ajouter un Compte")
    print("2. Supprimer un Compte")
    print("3. Accéder au compte client")
    print("4. Quitter")

    choix = int(input("Choisissez une option: "))

    if choix == 1:
        # Ajout d'un nouveau client et compte
        numCl = int(input("Numéro du client: "))
        MPC = input("Code secret: ")
        numC = banque.generer_num_compte(numCl)
        SoldeC = float(input("Solde initial du compte: "))
        banque.ajouter_client(numCl, MPC, numC, SoldeC)
        print("Compte ajouté avec succès!")

    elif choix == 2:
        # Suppression d'un compte client
        numC = int(input("Numéro du compte à supprimer: "))
        banque.supprimer_client(numC)
        print("Compte supprimé avec succès!")

    elif choix == 3:
        # Accès au menu du compte client
        numCl = int(input("Numéro du client: "))
        mdp = input("Code secret: ")

        # Vérification des informations du client
        if numCl in banque.get_clients() and mdp == banque.get_clients()[numCl]:
            while True:
                print("Menu client:")
                print("1. Modifier son mot de passe")
                print("2. Afficher son solde")
                print("3. Déposer une somme d'argent")
                print("4. Retirer une somme d'argent")
                print("5. Quitter")

                choix_client = int(input("Choisissez une option: "))

                if choix_client == 1:
                    # Modification du mot de passe du client
                    nouveau_mdp = input("Nouveau mot de passe: ")
                    banque.modifierMPClient(numCl, nouveau_mdp)
                    print("Mot de passe modifié avec succès!")

                elif choix_client == 2:
                    # Affichage du solde du client
                    print(f"Solde actuel: {banque.get_comptes()[banque.get_clients_comptes()[numCl]]} Dh")

                elif choix_client == 3:
                    # Dépôt d'une somme d'argent dans le compte du client
                    montant = float(input("Montant à déposer: "))
                    banque.deposer(banque.get_clients_comptes()[numCl], montant)
                    print("Dépôt effectué avec succès!")

                elif choix_client == 4:
                    # Retrait d'une somme d'argent du compte du client
                    montant = float(input("Montant à retirer: "))
                    banque.retirer(banque.get_clients_comptes()[numCl], montant)
                    print("Retrait effectué avec succès!")

                elif choix_client == 5:
                    # Retour au menu principal
                    print("Retour au menu principal client.")
                    break

                else:
                    print("Option invalide. Veuillez choisir une option valide.")

        else:
            print("Numéro de client ou mot de passe incorrect.")

    elif choix == 4:
        # Écriture des informations dans un fichier CSV avant de quitter
        banque.ecrire_fichier_csv()
        print("Au revoir!")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")
