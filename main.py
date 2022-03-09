import copy
import csv
import subprocess
import datetime
import random
import adminSection
import clientSection
#import clientSection
#fonction pour gerer les exceptions entrees par l'utilisateur

nomGagnant=""
#Sprint 1: qui consiste a developper les fonctions d'ajout des produits,modification, retrait des prdouits d'un catalogue
#Reservé à l'administrateur

#Dictionnaire du produit

productDictionnary= {

    "Reference" : "",
    "Nom du Produit" :"",
    "Prix":0.0,
    "Quantité":0

}

#customerDictionary


custumerDictionnary={
    "Nom" : "",
    "Id" : "",
    "Montant Total Achat" : 0.0,
    "Nombre de points Hebdommadaires" : 0,
    "Nombre de points Total" : 0,
    "Point convertis en argent" : 0.0
}

#Catalogue des produits

productCatalogue=[]
custumerList=[]
productCatalogueB=[]
listeDesMontants = []
Sortedliste = []



#Ajout d'un ou des produits 

#Fonction de verification de l'existence d'un produit
def productVerification(refProduct,productCatalogue):
    for product in productCatalogue:
        if product['Reference']==refProduct :
            return True

#Ajout Manuel

#Fonction de confirmation avant la création d'un produit
def productConfirmCreation(refProduct,nameProduct,priceProduct,qtyProduct):
    print("Vous allez créer le produit \"{}\", de reference \"{}\" dont la quantité est \"{}\" et qui coute \"{}\" FCFA l'unité".format(nameProduct,refProduct,qtyProduct,priceProduct))
    userInputConfirmation=input("Confirmez-vous la création de ce produit ?(Entrez \"y\" pour confirmer__")
    if userInputConfirmation.lower()=="y":
        return True

#Fonction de creation d'un produit
def productCreation(refProduct,nameProduct,priceProduct,qtyProduct):

    if productConfirmCreation(refProduct,nameProduct,priceProduct,qtyProduct):
        currentProductDictionnary=copy.deepcopy(productDictionnary)
        currentProductDictionnary['Reference']=refProduct
        currentProductDictionnary['Nom du Produit']=nameProduct
        currentProductDictionnary['Prix']=priceProduct
        currentProductDictionnary['Quantité']=qtyProduct

        productCatalogue.append(currentProductDictionnary)
        print("")
        print("Votre produit \"{}\" a été ajouté avec succès".format(nameProduct))
        print("")
        return productCatalogue

    else:
        print("")
        print("Votre produit \"{}\" n'a pas pu être ajouté".format(nameProduct))
        print("")
        return productCatalogue

#Ajout dynamique

#NomdufichierCSV = input("Entrez le nom de votre fichier : ") + ".csv"

def productCreationD(userInputFile):
    #NomdufichierCSV=""
    NomdufichierCSV=userInputFile+".csv"

    with open(NomdufichierCSV) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')  
        lineCount = 0  
        status = 0

        for row in csvReader:
            if lineCount == 0:
                pass
                lineCount += 1  
            else:  
            #print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}')
                while productVerification(row[0],productCatalogue) and status == 0:
                        print("Votre produit {}, de reference {} existe déjà".format(row[0],row[1]))
                        status = 1
                if not productVerification(row[0],productCatalogue) and status != 1:

                    currentProductDictionnary =copy.deepcopy(productDictionnary)  
                    currentProductDictionnary['Reference']=row[0]
                    currentProductDictionnary['Nom du Produit']=str(row[1])
                    currentProductDictionnary['Prix']=float(row[2])
                    currentProductDictionnary['Quantité']=int(row[3])
                    productCatalogue.append(currentProductDictionnary) 

                    print("")
                    print("Votre produit \"{}\" a été ajouté avec succès".format(row[1]))
                    print("") 
                    lineCount += 1  
                status=0
        #print(f'Processed {lineCount} lines.')
        return productCatalogue

#Test pour les fonctions d'ajout dynamique et manuel. Etat-Okay 
#test1=productCreationD('productInventory')
#test2=productCreation("POOO6","Nido 1 Sachet",100,300)
#print(test1)
#print(test2)

#Modification d'un produit

#fonction de confirmation de modification du stock
def productConfirmStockModification(refProduct,newQtyProduct):
    print("")
    print("Vous allez modifier le stock du produit de reference \"{}\".La nouvelle quantité sera \"{}\" ".format(refProduct,newQtyProduct))
    print("")
    userInputConfirmation=input("Confirmez-vous la modification du stock de ce produit ?(Entrez \"y\" pour confirmer__")
    if userInputConfirmation.lower()=="y":
        return True

#fonction de modification du stock d'un produit
def productStockModification(refProduct,productCatalogue,newQtyProduct):
        if productVerification(refProduct,productCatalogue):
           for product in productCatalogue:
                if productConfirmStockModification(refProduct,newQtyProduct):
                    product['Quantité']=newQtyProduct  
                    print("")
                    print("Votre produit \"{}\" a été modifié avec succès. Son nouveau stock est -- \"{}\"" .format(product['Nom du Produit'],product['Quantité']))
                    print("") 
                return productCatalogue
        else:
            print("Le produit de reference \"{}\" n'existe pas".format(refProduct))

#fonction de confirmation de modification du prix
def productConfirmPriceModification(refProduct,newPriceProduct):
    print("Vous allez modifier le prix du produit de reference \"{}\".Le nouveau prix sera \"{}\" F CFA ".format(refProduct,newPriceProduct))
    print("")
    userInputConfirmation=input("Confirmez-vous la modification du prix de ce produit ?(Entrez \"y\" pour confirmer__")
    print("")
    if userInputConfirmation.lower()=="y":
        return True

#fonction de modification du prix d'un produit
def productPriceModification(refProduct,productCatalogue,newPriceProduct):
        if productVerification(refProduct,productCatalogue):
           for product in productCatalogue:
                if productConfirmPriceModification(refProduct,newPriceProduct):
                    product['Prix']=newPriceProduct  
                    print("")
                    print("Votre produit \"{}\" de reference \"{}\" a été modifié avec succès. Son nouveau prix est -- \"{}\" F CFA" .format(product['Nom du Produit'],product['Reference'],product['Prix']))
                    print("")
                return productCatalogue
        else:
            print("Le produit de reference \"{}\" n'existe pas".format(refProduct))

#Suppression d'un produit

#fonction de confirmation de suppression d'un produit
def productConfirmDelete(refProduct):
    print("Vous allez supprimer le produit de reference {}".format(refProduct))
    print("")

    userInputConfirmation=input("Confirmez-vous la suppression de ce produit ?(Entrez \"y\" pour confirmer__")
    if userInputConfirmation.lower()=="y":
        return True


#fonction de retrait d'un produit du catalogue
def productRemove(refProduct,productCatalogue):
    if productVerification(refProduct,productCatalogue):
         for product in productCatalogue:
                    if product["Reference"]==refProduct:
                     if productConfirmDelete(refProduct):

                        productCatalogue.remove(product)  
                        print("")
                        print("Votre produit \"{}\" a été supprimé avec succès.".format(product['Nom du Produit']))
                        print("") 
    else:
            print("Le produit de reference \"{}\" n'existe pas".format(refProduct))
    return productCatalogue 

#Sprint 2

#Fonction pour la creation des clients avec un fichier .csv
def customerCreation():
    with open('customerInventory1.csv') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')  
            lineCount = 0  
            for row in csvReader:
                if lineCount == 0:
                    pass
                    lineCount += 1  
                else:  
                #print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}')  
                    currentCustomerDictionnary =copy.deepcopy(custumerDictionnary)  
                    currentCustomerDictionnary['Nom']=row[0]
                    currentCustomerDictionnary['Id']=row[1]
                    currentCustomerDictionnary['Montant Total Achat']=float(row[2])
                    currentCustomerDictionnary['Nombre de points Hebdommadaires']=int(row[3])
                    currentCustomerDictionnary['Nombre de points Total']=int(row[4])
                    currentCustomerDictionnary['Point convertis en argent']=int(row[5])
                    custumerList.append(currentCustomerDictionnary) 
                    #print(row[3])

                    print("")
                   # print("Votre client \"{}\" a été ajouté avec succès".format(row[1]))
                    print("") 
                    lineCount += 1  
            #print(f'Processed {lineCount} lines.')
            return custumerList
test1=customerCreation()


#Fonction de verification de l'existence d'un client
def custumerVerification(Identifiant,custumerList):
    for client in custumerList:
        if client['Id']==Identifiant :
            return True

#Fonction d'identification d'un client
def custumerIdentify(Nom,Id):
    if custumerVerification(Id,custumerList):
        currentCustumer=copy.copy(custumerDictionnary)
        currentCustumer["Nom"] = Nom
        currentCustumer["Id"] = Id
        custumerList.append(currentCustumer)
        return currentCustumer

#Fonction de confirmation avant achat
def productBuyingConfirmation(qtyProduct,nameProduct,priceProduct):
    print("Vous allez acheter {} exemplaires du produit {} coutant {} F l'unité".format(qtyProduct,nameProduct,priceProduct))
    userInputConfirmation=input("Confirmez-vous l'achat ? (Entrez \"y\" pour confirmer, \"n\" pour annuler__)")
    if userInputConfirmation.lower()=="y":
        return True
# Fonction d'achat d'un produit avec ses points
def productBying(Nom, nameProduct, Quantité):
    total=0.0
    status="0"
    for product in productCatalogue:
        if product["Nom du Produit"] == nameProduct:
            if product["Quantité"] >= Quantité:
                refProduct=product["Reference"]
                priceProduct=product["Prix"]
                if productVerification(refProduct,productCatalogue):
                    status=0
                    if productBuyingConfirmation(Quantité,nameProduct,priceProduct):
                        for product in productCatalogue:
                            if product["Reference"] == refProduct:
                                product["Quantité"] -= Quantité 
                                for client in custumerList:
                                    if client["Nom"] == Nom:
                                        client["Montant Total Achat"] =client["Montant Total Achat"]+product["Prix"]*Quantité
                                        print("Votre achat de {} {} vous a couté {} Francs CFA".format(Quantité,nameProduct,product['Prix']*Quantité))
                                        priceInPointConversion(Nom)
                                        total=product["Prix"]*Quantité
                                        status= total
                                    
            elif product["Quantité"] < Quantité :
                print("Vous ne pouvez pas acheter \"{}\" \"{}\" ! Veuillez revoir votre quantité ".format(Quantité, nameProduct))
                status= 0
        
    return status           
    #return total

#Fonction d'affichage du catalogue
def viewCatalogue():
    numeroArticle=1
    print('         Liste des produits')
    for product in productCatalogue:
        print("{}. {} -> Prix: {} ; Quantité: {}".format(numeroArticle, product['Nom du Produit'],product['Prix'], product['Quantité'])) 
        numeroArticle+=1
    if productCatalogue==[]:
        return True
#Fonction d'affichage de la liste des clients
def viewCustumerList():
    numeroClient=1
    print('           Liste des clients')
    for client in custumerList:
        print("{}. {} -> Identifiant : {} ; Montant Total Achat: {} F ; NB de points Hebdo : {}  ; NB de points Total: {} ; Gain totaux : {}".format(numeroClient, client['Nom'],client['Id'], client['Montant Total Achat'],client['Nombre de points Hebdommadaires'],client["Nombre de points Total"], client["Point convertis en argent"])) 
        numeroClient+=1

def viewClientTotal():

    numeroClient=1
    print(" ")
    print("\t\t\t\t\t\t------------  ------------- ")
    print('\n\t\t\t\t\t\t    LISTE DES CLIENTS    ')
    print(" ")
    print("\t\t\t\t\t\t------------  ------------- ")


    print('\n')
    for client in custumerList:
        print("-----------------------------------------------------------------------------------------------------------------------")
        print()
        print("\t\t\tNom {}\n\t\t\tIdentifiant :{}\n\t\t\tMontant Total Achat : {}F\n\t\t\tNB de Points Hebdo :{} \n\t\t\tNB de Points Total :{}\n\t\t\tGain Totaux:{}\n\t\t\t".format(client['Nom'],client['Id'], client['Montant Total Achat'],client['Nombre de points Hebdommadaires'],client["Nombre de points Total"], client["Point convertis en argent"]))
        print()
        print("-----------------------------------------------------------------------------------------------------------------------")
        print()
        numeroClient+=1


#Fonction de conversion du prix en nombre() et etre notifié si j’ai gagné des points
def priceInPointConversion(nameClient):
    for price in custumerList:
        if price["Nom"]==nameClient:
            price["Nombre de points Hebdommadaires"]+=price["Montant Total Achat"]//10000
            if price["Nombre de points Hebdommadaires"] >= 1:
                temporarHebdo=price["Nombre de points Hebdommadaires"]
                price["Nombre de points Total"]+=temporarHebdo
                print("Vous avez gagné {} Points.".format(temporarHebdo))
                temporarHebdo=0
                price["Montant Total Achat"]=0

#Fonction de conversion des points en argent
def pointInMoneyConversion(name):
    for client in custumerList:
        if client["Nom"] == name:
            montant=client["Nombre de points Hebdommadaires"]*1000
            client["Point convertis en argent"] += montant
            client["Nombre de points Hebdommadaires"] = 0
          
            return montant

def pointInMoneyConversionView(name):
    for client in custumerList:
        if client["Nom"] == name:
            montant=client["Nombre de points Hebdommadaires"]*1000
            client["Point convertis en argent"] += montant
            return montant
        

#Afficher le catalogue des produits qu'il peut acheter avec ses points cumulés
def viewProductPointBuyingCatalogue(name):
    montantUtilisable=pointInMoneyConversion(name)
    numeroArticle=1
    print('     ---------    LISTE DES PRODUITS DISPONIBLES A PARTIR DE VOS POINTS  ---------    ')
    status=False
    for product in productCatalogue:
        for customer in custumerList:
            if name==customer["Nom"]:
                cust=customer["Point convertis en argent"]
        if product["Prix"] <= montantUtilisable:  
            productCatalogueB.append(productCatalogue)
            print("")
            print("{}. {}   ->   Prix: {} :   Quantité:   {}".format(numeroArticle, product['Nom du Produit'],product['Prix'], product['Quantité'])) 
            numeroArticle+=1
            status=True

        elif product['Prix']<=cust:
            productCatalogueB.append(productCatalogue)
            print("")
            print("{}. {}   ->   Prix: {} :   Quantité:   {}".format(numeroArticle, product['Nom du Produit'],product['Prix'], product['Quantité'])) 
            numeroArticle+=1
            status=True

    return status

#Fonction d'achat d'un produit en utilisant les points cumules
def productByingWithPoint(Nom, nameProduct, Quantité):
    status=0
    for product in productCatalogue:
        if product["Nom du Produit"] == nameProduct:
            if product["Quantité"] >= Quantité:
                refProduct=product["Reference"]
                priceProduct=product["Prix"]
                if productVerification(refProduct,productCatalogue):
                    if productBuyingConfirmation(Quantité,nameProduct,priceProduct):
                        for product in productCatalogue:
                            if product["Reference"] == refProduct:
                                product["Quantité"] -= Quantité 
                                for client in custumerList:
                                    if client["Nom"] == Nom:
                                        pointInMoneyConversion(Nom)
                                        if client["Point convertis en argent"] >= product["Prix"]*Quantité:
                                            client["Point convertis en argent"] -= product["Prix"]*Quantité
                                            print("Votre achat de {} {} vous a couté {} Francs. CFA déduis de vos points.Il vous reste {}  Francs CFA Bonus".format(Quantité,nameProduct,product["Prix"]*Quantité,client["Point convertis en argent"]))
                                            status=True
                                       
                                        else :
                                            print("Vous n'avez pas assez de points pour acheter cet article")
                                            status=True

            else:
                print("Vous ne pouvez pas acheter {} {} ! Veuillez revoir votre quantité ".format(Quantité, nameProduct))
                status=True
    return status

       

#Fonction pour Consulter mon solde : mes points cumulés
def viewPoints(name):
    for client in custumerList:
        if client["Nom"] == name:
            print("Nom : {}   ->   Nombre de points : {}".format(name, client["Nombre de points Hebdommadaires"]))
            return True
      



#fonction pour désigner le gagnant du tirage au sort
def gagnantTirageAuSort():
    global nomGagnant
    for user in custumerList:
        listeDesMontants.append(user["Montant Total Achat"])
    listeDesMontants2 = [int(val) for val in listeDesMontants]
    listeDesMontants2.sort(reverse=True)
    
    for montant in listeDesMontants2:
        for user in custumerList:
            if montant == user["Montant Total Achat"]:
                Sortedliste.append(user)
   
    listeSelectionnes = []
    #Ne pas oublier de changer le range à 10
    for i in range (10):

        listeSelectionnes.append(Sortedliste[i])
    vainqueur = random.choice(listeSelectionnes)
    print(vainqueur["Nom"] + " est le gagnant du tirage au sort et beneficie d'un bon d'achat d'une valeur de 10000F valide une semaine ")
    nomGagnant=vainqueur["Nom"]
    return vainqueur["Nom"]

#Fonction pour afficher l'alarme
def alarmStock():
    listeProduitInf=[]
    for product in productCatalogue:
        if product["Quantité"] < 20:
            listeProduitInf.append(product)
    if listeProduitInf != []:
         for product in listeProduitInf:
             print("                     Attention ! Le stock de {} est inférieur à 20                            ".format(product["Nom du Produit"]))

      
#Fonction pour consulter mon solde : mes bons d'achat
def viewBonAchat(name):
        if nomGagnant == name:
            print("Felicitations {} !".format(name))
            return True
#Fonction pour générer les Logs du système
LogFile = 'ecoShop.log' 
def addToLogFile(actionnerName,description):
    #on ouvre le fichier en mode d'ajout 
    date = datetime.datetime.now()
    logContent = ''
    logContent += date.strftime('%A')+' le '+ str(date.day) +'-'+str(date.month)+'-'+str(date.year) +' a '+str(date.hour)+':'+str(date.minute) +' '+ actionnerName +' '+description
    logFile = open(LogFile,'a')
    logFile.write(logContent +'\n')
    logFile.close()

#Fonction d'affichage du catalogue
def viewCatalogueTotal():

    numeroArticle=1
    print(" ")
    print("\t\t\t\t\t\t------------  ------------- ")
    print('\n\t\t\t\t\t\t    LISTE DES PRODUITS    ')
    print(" ")
    print("\t\t\t\t\t\t------------  ------------- ")


    print('\n')
    for product in productCatalogue:
        print("-----------------------------------------------------------------------------------------------------------------------")
        print()
        print("\t\t\tProduct {}\n\t\t\tReference :{}\n\t\t\tNom du Produit : {}\n\t\t\tPrix du Produit :{} FCFA\n\t\t\tQuantité en Stock :{}\n\t\t\t".format(numeroArticle,product['Reference'],product['Nom du Produit'],product['Prix'],product['Quantité']))
        print()
        print("-----------------------------------------------------------------------------------------------------------------------")
        print()
        numeroArticle=numeroArticle+1

listeDesPoints = []
Sortlist = []
#fonction pour connaitre les 3 meilleurs clients
def topthreeclients():

    
    for user in custumerList:
        listeDesPoints.append(user["Nombre de points Total"])
    listeDesPoints.sort(reverse=True)
    for point in listeDesPoints:
        for user in custumerList:
            if point == user["Nombre de points Total"]:
                Sortlist.append(user)
        listeTopTrois = []
    for i in range(3):
        listeTopTrois.append(Sortlist[i])

    for top in listeTopTrois:
        print("-----------------------------------------------------------------------------------------------------------------------")
        print()
        print("\t\t\tIdentifiant :{}\n\t\t\tNom: {}\n\t\t\tMontant Total Achat : {}F\n\t\t\tNB de Points Hebdo :{} \n\t\t\tNB de Points Total :{}\n\t\t\tGain Totaux:{}\n\t\t\t".format(top['Id'],top['Nom'], top['Montant Total Achat'],top['Nombre de points Hebdommadaires'],top["Nombre de points Total"], top["Point convertis en argent"]))
        print()
        print("-----------------------------------------------------------------------------------------------------------------------")
        print()
       
                                
def clientverif(nom):
    for customer in custumerList:
        if customer["Nom"] == nom:
            return True 
      
def productNameVerif(nom):
    for product in productCatalogue:
        if product["Nom du Produit"]==nom:
            return True
#productCreation("P001","Pain",1500,200)
#productBying("Maeva Fru","Pain",10)
#productBying("Audrey Ngue","Pain",100)
#productBying("Max Keller", "Pain",5)

#productBying("Lucie Batonga","Pain",10)
#productByingWithPoint("Audrey Ngue","Pain",2)
#print(custumerList)

#topthreeclients()