inventaire = []

# Fonction pour ajouter un article à l'inventaire
def ajouter_article():
    nom = input("Entrez le nom de l'article: ")
    quantite = int(input("Entrez la quantité de l'article: "))
    prix = float(input("Entrez le prix de l'article: "))
    article = {
        'nom': nom,
        'quantite': quantite,
        'prix': prix
    }
    
    inventaire.append(article)
    print(f"Article '{nom}' ajouté avec succès!")
    
def supprimer_article():
    nom = input("Entrez le nom de l'article à supprimer: ")
    for article in inventaire:
        if article['nom'].lower() == nom.lower():
            inventaire.remove(article)
            print(f"Article '{nom}' supprimé avec succès!")
            return
    print(f"Article '{nom}' non trouvé.")
    
def afficher_resume():
    if inventaire:
        print("\n=== Résumé de l'inventaire ===")
        total_quantite = 0
        total_valeur = 0.0
        for article in inventaire:
            total_quantite += article['quantite']
            total_valeur += article['quantite'] * article['prix']
            print(f"Nom: {article['nom']}, Quantité: {article['quantite']}, Prix: {article['prix']}€")
        
        print(f"\nTotal articles : {total_quantite}")
        print(f"Valeur totale de l'inventaire : {total_valeur:.2f}€")
    else:
        print("L'inventaire est vide.")
        
def trier_inventaire():
    print("\nComment voulez-vous trier l'inventaire ?")
    print("1. Trier par prix")
    print("2. Trier par nom")
    
    choix = input("Choisissez une option (1/2): ")
    
    if choix == '1':
        inventaire.sort(key=lambda x: x['prix'])
        print("L'inventaire a été trié par prix.")
    elif choix == '2':
        inventaire.sort(key=lambda x: x['nom'].lower())
        print("L'inventaire a été trié par nom.")
    else:
        print("Choix invalide. Aucune modification apportée.")
        
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Ajouter un article")
        print("2. Supprimer un article")
        print("3. Afficher le résumé de l'inventaire")
        print("4. Trier l'inventaire")
        print("5. Quitter")
        
        choix = input("Choisissez une option (1/2/3/4/5): ")
        
        if choix == '1':
            ajouter_article()
        elif choix == '2':
            supprimer_article()
        elif choix == '3':
            afficher_resume()
        elif choix == '4':
            trier_inventaire()
        elif choix == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Exécution du programme
menu()
