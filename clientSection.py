import main
import os
import subprocess
import adminSection

#Premiere Banniere pour Client
def clientBanner():
    subprocess. call("cls", shell = True)
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
    print("|                    Bienvenue M./Mme sur cet espace reservé pour vous.                            |")
    print("|                OPA2M vous permettra de faciliter l'achat de vos produits.                        |")
    print("|      OPA2M vous permettra egalement de profiter des avantages de votre supermarché preféré.      |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                 Vous souhaitez__ :                                               |")
    print("|                                                                                                  |")
    print("|                                     1.  Effectuer un Achat                                       |")
    print("|                                     2.  Consulter votre Solde                                    |")
    print("|                                     3.  Consulter le Catalogue des Produits                      |")
    print("|                                                                                                  |")
    print("|                    Pour retourner au menu principal : Tapez 4                                    |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("|                          Developpé par : Audrey N., Maeva M., Manuella K., Oliver M., Philippe H.|")
    print("|--------------------------------------------------------------------------------------------------|")
    clientBannerChoice()

def clientBannerChoice():
    while True:    
        choice=adminSection.choiceException()
        if choice==1:
            subprocess. call("cls", shell = True)
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
            print("|                           Bienvenue M./Mme sur cet espace reservé pour vous.                     |")
            print("|                                     ----------   ------------                                    |")
            print("|                                        ACHAT D'UN PRODUIT                                        |")
            print("|                                     ----------   ------------                                    |")
            print("|                                                                                                  |")
            print("|                                 Vous souhaitez __ :                                              |")
            print("|                                                                                                  |")
            print("|                                     1.  Acheter avec vos points cumulés                          |")
            print("|                                     2.  Effectuer un paiement normal                             |")
            print("|                                                                                                  |")
            print("|                    Pour retourner au menu precedent : Tapez 3                                    |")
            print("|                    Pour retouner au menu principale : Tapez 4                                    |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                          Developpé par : Audrey N., Maeva M., Manuella K., Oliver M., Philippe H.|")
            print("|--------------------------------------------------------------------------------------------------|") 
            while True:    

                userchoice=adminSection.choiceException()
                if userchoice==1:
                        responseUser="y"
                        nameClient=input("Entrez votre nom s'il-vous plaît:__")
                        print("")
                        if main.viewProductPointBuyingCatalogue(nameClient):
                            while responseUser.lower()=="y":
                
                                nameProduct=input("Quel produit souhaitez-vous acheter ?__")
                                print("")
                                while True:
                                    try:
                                        qtyProduct=int(input("Combien d'exemplaire prendrez-vous pour ce produit ?__"))
                                        print("")
                                    except:
                                        print("Veuillez entrer une quantité valide ")
                                        print("")
                                    else:
                                                break
                                
                                if not main.productByingWithPoint(nameClient,nameProduct,qtyProduct):
                                        print("Le produit {} n'existe pas! ".format(nameProduct))
                                    
                                    
                                
                                responseUser=input("Voulez-vous acheter un autre produit ?(Tapez \"y\")__")
                                print("")
                                if responseUser != "y":
                                 print("")
                   
                                 print("Que souhaitez-vous faire maintenant ? Si vous voulez refaire un achat avec les points cumulés, tapez \"1\". Tapez \"2\" pour effectuer un paiement normal, \"3\" pour retourner au menu precedent et enfin \"4\" pour repartir au menu principal ")
                               
                        else:
                            print("Desole, vous ne pouvez effectuer aucun achat ")

                        
    
                        #if responseUser=="y":

                         #          print ("Que souhaitez-vous faire maintenant ? Si vous voulez refaire un achat à partir de vos points cumulés, tapez \"1\". Tapez \"2\" pour effectuer un achat normal, \"3\" pour retourner au menu precedent et enfin \"4\" pour repartir au menu principal ")  
           



                elif userchoice==2:
                    responseUser="y"
                    nameClient=input("Entrez votre nom s'il-vous plaît:__")
                    print("")
                    newBuying=0.0
                    while responseUser.lower()=="y":
                        main.viewCatalogue()
                        nameProduct=input("Quel produit souhaitez-vous acheter ?__")
                        print("")
                        
                        while True:
                            try:
                                qtyProduct=int(input("Combien d'exemplaire prendrez-vous pour ce produit ?__"))
                                print("")
                            except:
                                print("Veuillez entrer une quantité valide ")
                                print("")
                            else:
                                        break
                        r=main.productBying(nameClient,nameProduct,qtyProduct)
                        if r == "0":
                            print("Votre produit n'existe pas")
                                             
                        newBuying+=float(r)
                        print("")
                        responseUser=input("Voulez-vous acheter un autre produit ?(Tapez \"y\")__")

                        print("")
                        if responseUser != "y":
                            print("")
                            print("Le montant à payer s'élève à :__{} F CFA".format(newBuying))

                            print("Que souhaitez-vous faire maintenant ? Si vous voulez effectuer un achat par paiement normal, tapez \"2\". Tapez \"1\" pour acheter vos produits a partir de vos points cumulés, \"3\" pour retourner au menu precedent et enfin \"4\" pour repartir au menu principal ")
                            
                            main.addToLogFile(nameClient,"A ACHETER PRODUIT DE "+''+ str(newBuying))
                                



                    
                elif userchoice==3:
                    clientBanner()
                elif userchoice==4:
                    adminSection.firstBanner()
        elif choice==2:
            nameClient=input("Entrez votre nom s'il-vous plaît:__")
            print("")
            if main.viewPoints(nameClient):
             print("-----------------------------------------------------------------------------------------------------------------------")
             print("-----------------------------------------------------------------------------------------------------------------------")
            else :
                 print("Désolé, vous n'avez obtenu aucun point jusqu'ici. Veuillez effectuer des achats afin d'en obtenir")
            print("")
            if not main.viewBonAchat(nameClient):
                     print("     Vous n'avez aucun bon d'achat     ")

        elif choice==3:
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
            print("|                           Bienvenue M./Mme sur cet espace reservé pour vous.                     |")
            print("|                                     ----------   ------------                                    |")
            print("|                                       LISTE DE NOS PRODUITS                                      |")
            print("|                                     ----------   ------------                                    |")
            print("|                                                                                                  |")
            print("|                                 Vous souhaitez __ :                                              |")
            print("|                                                                                                  |")
            print("|                                     1. Consulter la liste de tous nos produits                   |")
            print("|                                     2. Consulter la liste des produits en fonction de            |")
            print("|                                        vos points cumulés                                        |")
            print("|                                                                                                  |")
            print("|                    Pour retourner au menu precedent : Tapez 3                                    |")
            print("|                    Pour retourner au menu principal: Tapez 4                                     |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                                                                                                  |")
            print("|                          Developpé par : Audrey N., Maeva M., Manuella K., Oliver M., Philippe H.|")
            print("|--------------------------------------------------------------------------------------------------|") 
    
            while True:    
                userchoice=adminSection.choiceException()
                if userchoice==1:
                    main.viewCatalogueTotal()
                    while True :
                        try:
                            responseUser=int(input("Que souhaitez-vous faire maintenant ? Tapez \"3\" pour retourner au menu precedent et \"3\", au menu principal__ "))

                        except:
                            print("Entrez une reponse valide")
                    
                elif userchoice==2:
                    name=input("Entrez votre nom__")
                   
                    if not main.clientverif(name):
                        print("Désolé, votre nom ne figure pas dans la liste des clients ayant des points")

                    else:
                                
                        main.viewProductPointBuyingCatalogue(name)
                    while True :
                        try:
                            responseUser=int(input("Que souhaitez-vous faire maintenant ? Tapez \"3\" pour retourner au menu precedent et \"3\", au menu principal__ "))

                        except:
                            print("Entrez une reponse valide")


                        
                         
                    
                
                elif userchoice==3:
                    clientBanner()
                elif userchoice==4:
                    adminSection.firstBanner()
        elif choice==4:
            adminSection.firstBanner()
     

        
                    
                
        
        
        
        
       # elif choice==2:
            #print("Consultation du Solde")
            #forAdmin.priceInPointConversion()
            #break
        #elif choice==3:
            #consultListBanner()