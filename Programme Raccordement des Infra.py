import csv


class Batiment:

    def __init__(self, id_building, list_infras):
        self.id_building = id_building
        self.list_infras = list_infras

    def __str__(self):
        return f" ID du bâtiment: {self.id_building}\nListe des infrastructures: {self.list_infras} "


    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return sum(infra.length for infra in self.list_infras) + other
        return NotImplemented

    def get_building_difficulty(self):
        # Utiliser sum() pour calculer la somme des longueurs des infrastructures
        total_difficulty = sum(self.list_infras)  #return sum(infra.length for infra in self.list_infras) + other !!!!
        return total_difficulty

    def __lt__(self, other):
        return self.get_building_difficulty() < other.get_building_difficulty()




    # Fonction pour sélectionner le bâtiment le moins difficile à raccorder
    def get_least_difficult_building(buildings):

     least_difficult_building = None
     least_difficult_building = min(buildings)
     return least_difficult_building




class Infra:

    def __init__(self, infra_id, length, infra_type, nb_houses):
        self.infra_id = infra_id
        self.length = length
        self.infra_type = infra_type
        self.nb_houses = nb_houses

    def __str__(self):
        return f"ID de l'infrastructure: {self.infra_id}, Longueur: {self.length}, Type: {self.infra_type}, Nombre de maisons: {self.nb_houses}"

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.length + other
        return NotImplemented

    def get_infra_difficulty(self):
        return self.length / self.nb_houses

    def repair_infra(self):
        # réparation de l'infrastructure
        self.infra_type = "infra_intacte"






#la liste initiale dans laquelle on va stocker les batiments à réparer
buildings_impacted = []
chemin_fichier_csv = "./data/reseau_en_arbre.csv"

# Lecture du fichier CSV et remplissage de la liste donnees_a_remplacer
with open(chemin_fichier_csv, newline='') as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv)

    # un Dictionnaire temporaire pour regrouper les infrastructures par id_batiment
    infrastructures_par_batiment = {}

    # Parcourir chaque ligne du fichier CSV
    for ligne in lecteur_csv:
        id_building = ligne['id_batiment']
        infra_id = ligne['infra_id']
        longueur = float(ligne['longueur'])
        infra_type = ligne['infra_type']
        nb_houses = int(ligne['nb_maisons'])

        if infra_type == "a_remplacer": #seulement les batiments à réparer

         # Créeation d'une instance Infra
         infra = Infra(infra_id, longueur, infra_type, nb_houses)

         # Vérifier si le bâtiment existe déjà dans le dictionnaire
         if id_building in infrastructures_par_batiment:
             infrastructures_par_batiment[id_building].append(infra)
         else:
             infrastructures_par_batiment[id_building] = [infra]

         # Créeation des instances de Batiment à partir du dictionnaire et les stocker dans une liste(pour l'ordre) buildings_impacted
    for id_building, list_infras in infrastructures_par_batiment.items():
        batiment = Batiment(id_building, list_infras)
        buildings_impacted.append(batiment)



# Afficher la liste buildings_impacted pour voire chaque batiment avec ses infrastructures à remplacer
# for batiment in buildings_impacted:
#     print(f"Id du batiment: {batiment.id_building}")
#     for infra in batiment.list_infras:
#         print(f"Infra ID: {infra.infra_id}, Longueur: {infra.length}, Type: {infra.infra_type}")
#     print()





# Exemple d'utilisation de l'algorithme
if __name__ == "__main__":

    #les bâtiments qui n'ont pas besoin de réparation
    non_repairable_buildings = [building for building in buildings_impacted if all(infra.infra_type == "infra_intacte" for infra in building.list_infras)]

    # une Liste vide pour stocker les bâtiments réparés
    repaired_buildings = []

    # un Processus itératif jusqu'à ce que tous les bâtiments soient réparés
    while buildings_impacted:
        least_difficult_building = Batiment.get_least_difficult_building(buildings_impacted)

        # Réparer toutes les infrastructures du bâtiment
        for infra in least_difficult_building.list_infras:
            infra.repair_infra()
        # Stocker le bâtiment dans la nouvelle liste
        repaired_buildings.append(least_difficult_building)
        # Enlever le bâtiment de la liste initiale
        buildings_impacted.remove(least_difficult_building)

    # Une fois que tous les bâtiments sont réparés, la liste "repaired_buildings" contient tous les bâtiments réparés




# Afficher la liste repaired_buildings pour voire les batiments qui sont réparés en ordre bien sur

for batiment in repaired_buildings:
    print(f"Id du batiment: {batiment.id_building}")
    for infra in batiment.list_infras:
        print(f"Infra ID: {infra.infra_id}, Longueur: {infra.length}, Type: {infra.infra_type}")
    print()