import main
import os
import adminSection

#Premiere Banniere pour Client
def clientBanner():
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
            print("|                    Pour retouner au menu principale : Tapez 4                                         |")
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
                                
                                if main.productByingWithPoint(nameClient,nameProduct,qtyProduct):
                                    responseUser=input("Souhaitez-vous sortir ?(Tapez \"y\")__")
                                    clientBanner()
                                    
                                else:
                                        print("Le produit {} n'existe pas! ".format(nameProduct))
                               
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
                        
                        
                        newBuying+=r
                        print("")
                        responseUser=input("Voulez-vous acheter un autre produit ?(Tapez \"y\")__")
                        print("")
                    print("Le montant à payer s'élève à :__{} F CFA".format(newBuying))

                            



                    
                elif userchoice==3:
                    clientBanner()
                elif userchoice==4:
                    adminSection.firstBanner()
        elif choice==2:
            nameClient=input("Entrez votre nom s'il-vous plaît:__")
            print("")
            main.viewPoints(nameClient)
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            main.viewBonAchat(nameClient)
        elif choice==3:
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
            print("|                    Pour retourner au menu principal: Tapez 4                                         |")
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
                
                elif userchoice==2:
                    name=input("Entrez votre nom__")
                   
                    if not main.clientverif(name):
                        print("Désolé, votre nom ne figure pas dans la liste des clients ayant des points")

                    else:
                                
                        main.viewProductPointBuyingCatalogue(name)


                        
                         
                    
                
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