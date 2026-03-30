import mysql.connector
from tabulate import tabulate
from src.common.config import DB_CONFIG
from src.common.helpers import print_menu

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# 1. AFFICHAGE AVEC JOINTURE ET TRI (Nouveauté)
def lister_factures_admin(date_debut=None, date_fin=None):
    """Affiche les factures avec jointures, triées par client et période."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    
    # Requête avec jointures demandée
    query = """
        SELECT c.nom, o.id AS num_cmd, o.date_commande, f.date_facture, f.montant_ttc
        FROM client c
        JOIN commande o ON c.id = o.id_client
        JOIN facture f ON o.id = f.id_commande
    """
    params = []
    if date_debut and date_fin:
        query += " WHERE o.date_commande BETWEEN %s AND %s"
        params = [date_debut, date_fin]
    
    # Tri administratif : Nom puis Date
    query += " ORDER BY c.nom ASC, o.date_commande DESC"
    
    cur.execute(query, params)
    data = cur.fetchall()
    
    headers = ["Client", "N° Commande", "Date Commande", "Date Facture", "Montant TTC"]
    rows = [[d['nom'], d['num_cmd'], d['date_commande'], d['date_facture'], f"{d['montant_ttc']} €"] for d in data]
    
    print("\n--- RAPPORT ADMINISTRATIF DES FACTURES ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    
    cur.close()
    conn.close()

# 2. MODIFICATION CLIENT (CRUD UPDATE)
def modifier_email_client(id_client, nouvel_email):
    """Modifie l'email d'un client par son ID."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE client SET email = %s WHERE id = %s", (nouvel_email, id_client))
    conn.commit()
    success = cur.rowcount > 0
    cur.close()
    conn.close()
    return success

# --- MENU PRINCIPAL ---
if __name__ == "__main__":
    while True:
        print_menu("Mode DB-API - Gestion BoutikPro")
        print("1. Liste des factures (Tri administratif)")
        print("2. Filtrer par période")
        print("3. Modifier l'email d'un client (CRUD)")
        print("Q. Quitter")
        
        choix = input("\nVotre choix : ").upper()
        
        if choix == '1':
            lister_factures_admin()
        elif choix == '2':
            d1 = input("Date début (AAAA-MM-DD) : ")
            d2 = input("Date fin (AAAA-MM-DD) : ")
            lister_factures_admin(d1, d2)
        elif choix == '3':
            id_c = input("ID du client : ")
            mail = input("Nouvel email : ")
            if modifier_email_client(id_c, mail):
                print("✅ Email mis à jour !")
            else:
                print("❌ Client introuvable.")
        elif choix == 'Q':
            print("Fermeture...")
            break