import main
import os
import clientSection

#fonction pour gerer les exceptions entrees par l'utilisateur
def choiceException():
    userChoice=0
   
    while True:
            try:   
              userChoice=int(input("             Saississez le chiffre correspondant à votre choix:__"))      
            except:
                print("                             Entrez une saisi valide")
            else:

             return userChoice    



#fonction de banniere 1
def firstBanner():
    os.system('cls||clear')

    print("|--------------------------------------------------------------------------------------------------|")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                       -- OPA2M v0.1 --                                           |")
    print("|                                                                                                  |")
    print("|           OPA2M est une application concu pour une experience optimale de votre supermarché.     |")
    print("|                                 Vous êtes__ :                                                    |")
    print("|                                     1.  Administrateur                                           |")
    print("|                                     2.  Client                                                   |")
    print("|                 Souhaitez-vous sortir de ce programme ? Tapez 3                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                     Orange Digital Center - AWS re/Start: Programmation en Python|")
    print("|                          Developpé par : Audrey N., Maeva M., Manuella K., Oliver M., Philippe H.|")
    print("|                                                                                                  |")
    print("|--------------------------------------------------------------------------------------------------|")
    
    firstChoice()
    

#fonction pour diriger l'utilisateur en fonction de son choix admin ou client
def firstChoice():   
    while True:    

        choice=choiceException()
        if choice==1:
            adminBanner()
        elif choice==2:
            clientSection.clientBanner()
        elif choice==3:
            break
        
    

#banniere admin principale           
def adminBanner():
    os.system('cls||clear')
    print("|--------------------------------------------------------------------------------------------------|")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    main.alarmStock()
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                       -- OPA2M v0.1 --                                           |")
    print("|                                                                                                  |")
    print("|              Bienvenue M. l'Administrateur sur cet espace reservé pour vous.                     |")
    print("|       OPA2M vous permettra de faciliter la gestion de votre catalogue de produits.               |")
    print("| OPA2M vous accompagne egalement dans l'amelioration de l'experience client de votre supermarché. |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                 Vous souhaitez__ :                                               |")
    print("|                                                                                                  |")
    print("|                                     1.  Ajouter un Produit dans le Catalogue                     |")
    print("|                                     2.  Modifier un Produit du Catalogue                         |")
    print("|                                     3.  Retirer un Produit du Catalogue                          |")
    print("|                                     4.  Consulter le Catalogue des Produits                      |")
    print("|                                     5.  Consulter la Liste des Clients                           |")
    print("|                                     6.  Identifier le Gagnant de la Semaine                      |")
    print("|                                     7.  Identifier le \"top 3\" de vos Clients                     |")
    print("|                                                                                                  |")
    print("|                    Pour retourner au menu principal : Tapez 8                                    |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                          Developpé par : Audrey N., Maeva M., Manuella K., Oliver M., Philippe H.|")
    print("|--------------------------------------------------------------------------------------------------|")
    adminChoice()

    #fonction pour les choix du menu administrateur
def adminChoice():  
    

    while True:    
        choice=choiceException()
        if choice==1:
            os.system('cls||clear')
    

            print("|--------------------------------------------------------------------------------------------------|")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                         - - OPA2M v0.1 --                                        |")
            print("|                                     ----------   ------------                                    |")
            print("|                                         AJOUT D'UN PRODUIT                                       |")
            print("|                                     ----------   ------------                                    |")
            print("|                                                                                                  |")
            print("|                  Bienvenue M. l'Administrateur sur cet espace reservé pour vous.                 |")
            print("|                                 Vous souhaitez__ :                                               |")
            print("|                                                                                                  |")
            print("|                                     1.  Ajout manuel                                             |")
            print("|                                     2.  Ajout par fichier .csv                                   |")
            print("|                                                                                                  |")
            print("|                       Pour retourner au menu precedent :  Tapez 3                                |")
            print("|                       Pour retourner au menu principal : Tapez 4                                 |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                          Developpé par : Audrey N., Maeva M., Manuella K., Oliver M., Philippe H.|")
            print("|                                                                                                  |")
            print("|--------------------------------------------------------------------------------------------------|")

            while True:    

                choice=choiceException()
                if choice==1:
                    i=0
                    status = 0
                    responseUser="y"
                    # numberUser=int(input("Combien de produits souhaitez-vous ajouter ?__"))
                    # for i in range(0,numberUser):
                    while responseUser.lower()=="y":
                        refProduct=input("La Reference du Produit que vous souhaitez créer__ :")
                        print("")
                        while main.productVerification(refProduct,main.productCatalogue) and status == 0:
                            print("Votre produit existe déjà")
                            status = 1
                        if not main.productVerification(refProduct,main.productCatalogue) and status != 1:

                        #refProduct=input("La Reference du Produit :")
                            nameProduct=input("Le Nom du Produit__:")
                            print("")

                            while True: 
                                priceProduct=0.0          
                                try:
                                    priceProduct=float(input("Son Prix Unitaire__:"))
                                    print("")

                                except:
                                    print("Veuillez entrer un prix valide ")
                                    print("")

                                else:
                                    break
                            while True:
                                try:
                                    qtyProduct=int(input("Sa Quantite__:"))
                                    print("")

                                except:
                                    print("Veuillez entrer une quantite valide ")
                                    print("")

                                else:
                                    break


                            main.productCreation(refProduct,nameProduct,priceProduct,qtyProduct)

                        responseUser=input("Voulez-vous creer un autre produit ?(Tapez \"y\")__")
                        

                        
                        if responseUser != "y":
                            print("")
                   
                            print("Que souhaitez-vous faire maintenant ? Si vous voulez refaire un ajout manuel, tapez \"1\". Tapez \"2\" pour un ajout à partir d'un fichier .csv, \"3\" pour retourner au menu precedent et enfin \"4\" pour repartir au menu principal ")
                        print("")
                        status=0
                elif choice==2:

                    try:
                        userInputFile = input("Entrez le nom de votre fichier :__ ") 
                        main.productCreationD(userInputFile)
                    except:
                        print("Veuillez entrer un nom de fichier valide.")

                    responseUser=input("Voulez-vous creer un autre produit ?(Tapez \"y\")__") 
                    if responseUser != "y":
                            print("")
                   
                            print("Que souhaitez-vous faire maintenant ? Si vous voulez refaire un ajout dynamique, tapez \"2\". Tapez \"1\" pour un ajout manuel, \"3\" pour retourner au menu precedent et enfin \"4\" pour repartir au menu principal ")

                elif choice==3:
                    adminBanner()
                elif choice==4:
                    firstBanner()
                


        elif choice==2:
            os.system('cls||clear')
            print("|--------------------------------------------------------------------------------------------------|")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                       -- OPA2M v0.1 --                                           |")
            print("|                                                                                                  |")
            print("|              Bienvenue M. l'Administrateur sur cet espace reservé pour vous.                     |")
            print("|                                     ----------   ------------                                    |")
            print("|                                     MODIFICATION D'UN PRODUIT                                    |")
            print("|                                     ----------   ------------                                    |")
            print("|                                                                                                  |")
            print("|                                 Vous souhaitez __ :                                              |")
            print("|                                                                                                  |")
            print("|                                     1.  Modifier la quantité du produit                          |")
            print("|                                     2.  Modifier le prix du produit                              |")
            print("|                                                                                                  |")
            print("|                    Pour retourner au menu precedent : Tapez 3                                    |")
            print("|                    Pour retourner au menu principal : Tapez 4                                    |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                          Developpé par : Audrey N., Maeva M., Manuella K., Oliver M., Philippe H.|")
            print("|--------------------------------------------------------------------------------------------------|")
            print("")
            refProduct=input("La Reference du Produit que vous souhaitez modifier:__")

            while True:
            
                choice=choiceException()
                if choice==1:
                    responseUser="y"
                    while responseUser.lower()=="y":
                    # print("")
                        #refProduct=input("La Reference du Produit dont vous souhaitez modifier le stock:__")
                        print("")
                        while True: 
                            try:
                                newQtyProduct=int(input("Le Nouveau Stock du Produit:__"))
                                print("")

                            except:
                                        print("Veuillez entrer une quantité valide ")
                                        print("")

                            else:
                                        break
                        main.productStockModification(refProduct,main.productCatalogue,newQtyProduct)
                        print("")

                        responseUser=input("Voulez-vous modifier un autre produit ?(Tapez \"y\")__")
                        if responseUser =="y":
                            refProduct=input("La Reference du Produit dont vous souhaitez modifier le stock:__")
                        else:
                            print("")
                   
                            print ("Que souhaitez-vous faire maintenant ? Si vous voulez refaire une modification de stock, tapez \"1\". Tapez \"2\" pour modifier le prix du produit, \"3\" pour retourner au menu precedent et enfin \"4\" pour repartir au menu principal ")
                        print("")     
                            
                elif choice==2:
                    responseUser="y"
                    while responseUser.lower()=="y":
                        print("")
                        while True: 
                                try:
                                    newPriceProduct=float(input("Le Nouveau Prix du Produit:__"))
                                    print("")


                                except:
                                        print("Veuillez entrer un prix valide ")
                                        print("")

                                else:
                                        break
                        main.productPriceModification(refProduct,main.productCatalogue,newPriceProduct)
                        responseUser=input("Voulez-vous modifier un autre produit ?(Tapez \"y\")__")
                        if responseUser =="y":
                            refProduct=input("La Reference du Produit dont vous souhaitez modifier le prix:__")
                        else:
                            print("")
                   
                            print ("Que souhaitez-vous faire maintenant ? Si vous voulez refaire une modification du prix, tapez \"2\". Tapez \"1\" pour modifier le stock du produit, \"3\" pour retourner au menu precedent et enfin \"4\" pour repartir au menu principal ")

                        print("")
                
                elif choice==3:
                        adminBanner()
                elif choice==4:
                    firstBanner()                       
 
        elif choice==3:
            responseUser="y"

            while responseUser.lower()=="y":
                print("")
                refProduct=input("La Reference du Produit que vous souhaitez supprimer:__")
                print("")
                main.productRemove(refProduct,main.productCatalogue)
                print("")
                responseUser=input("Voulez-vous supprimer un autre produit ?(Tapez \"y\")__")
           
        elif choice==4:
            main.viewCatalogueTotal()

        elif choice==5:
            main.viewClientTotal()

        elif choice==6:
            main.gagnantTirageAuSort()
        elif choice==7:
            print("                                    ------ LE TOP 3 DES CLIENTS ------                            ")
            main.topthreeclients()
        elif choice==8:
            firstBanner()
    
    
           
firstBanner()