# menu function
def menu(): 
    print("->1<- Chiffrer / déchiffrer des messages")
    print("->2<- Créer un couple d clés publique / privée (générer un grand nombre premie")
    print("->3<- Signer / générer un certificat")
    print("->4<- Vérifier un certificat")
    print("->5<- Enregistrer un document dans le coffre-fort")
    print("->6<- Envoyer un message (asynchrone)")
    print("->7<- Demander une preuve de connaissance.")
    print("->0<- I WANT IT ALL !! I WANT IT NOW !! SecCom from scratch")

    try:
        choice = input("\n>>> Enter le nombre de votre choix :")
        choice = int(choice)
        assert choice in list(range(8))
    except:
        print("---> Saisie erronée. Ressaisir\n")
        return menu()
    else:
        return choice



# function call
menu()