#coding-utf8
import pandas as pd
class sac_Dos_approche_gloutonne:
    """
    La classe sac_Dos prend en parametre
    parametre 1 === le fichier excel contenant les donnees du sac a dos
        Assurez-vous que dans le fichier excel
        colonne1 == poids
        colonne2 == valeurs 
        colonne3 == max_Weight
    parametre 2 === le nom de la feuille dans le fichier excel
    Sheet1 est le nom par defaut de la feuille

    """
    def __init__(self,typeDeFichier,fichier,max_Weight) -> None:
        if typeDeFichier == 'excel':
            data = pd.read_excel(fichier)
        elif typeDeFichier == 'csv':
            data = pd.read_csv(fichier)
        else:
            raise ValueError("Type de fichier non supporté. Utilisez 'excel' ou 'csv'.")
        previous_columns = data.columns
        Columns = {previous_columns[0]:'poids',
                    previous_columns[1]:'valeurs',
                    previous_columns[2]:'max_Weight'}
        # Renommer les colonnes pour une utilisation plus simple
        data.rename(columns=Columns, inplace=True)
        self.poids = data['poids']
        self.values = data['valeurs']
        self.max_Weight = max_Weight
        self.values_Per_weight = [v/p for v, p in zip(self.values, self.poids) if p != 0]
        

    def solutionApprocheParPoids(self):
        choisi = {}
        # Tri par poids croissant, puis valeur décroissante si égalité
        indices = sorted(range(len(self.poids)), key=lambda i: (self.poids[i], -self.values[i]))
        Poid = 0
        Valeur = 0
        for idx in indices:
            if self.poids[idx] + Poid <= self.max_Weight:
                Poid += self.poids[idx]
                Valeur += self.values[idx]
                choisi[idx] = 1
            else:
                choisi[idx] = 0
        #self.meilleurSolutionApproche.append([Poid, Valeur])
        return choisi

    def solutionApprocheParValeur(self):
        choisi = {}
        # Tri par valeur décroissante, puis poids croissant si égalité
        indices = sorted(range(len(self.values)), key=lambda i: (-self.values[i], self.poids[i]))
        Poid = 0
        Valeur = 0
        for idx in indices:
            if self.poids[idx] + Poid <= self.max_Weight:
                Poid += self.poids[idx]
                Valeur += self.values[idx]
                choisi[idx] = 1
            else:
                choisi[idx] = 0
        #self.meilleurSolutionApproche.append([Poid, Valeur])
        return choisi

    def solutionApprocheParValeurParPoid(self):
        choisi = {}
        # Tri par ratio décroissant, puis poids croissant si égalité
        indices = sorted(range(len(self.values_Per_weight)), key=lambda i: (-self.values_Per_weight[i],self.poids[i],-self.values[i]))
        Poid = 0
        Valeur = 0
        for idx in indices:
            if self.poids[idx] + Poid <= self.max_Weight:
                Poid += self.poids[idx]
                Valeur += self.values[idx]
                choisi[idx] = 1
            else:
                choisi[idx] = 0
        #self.meilleurSolutionApproche.append([Poid, Valeur])
        return choisi

    def SolutionOptimal(self):
        Sols = [self.solutionApprocheParValeur(),
                self.solutionApprocheParPoids(),
                self.solutionApprocheParValeurParPoid()]
        Sol1, Sol2, Sol3 = Sols[0], Sols[1], Sols[2]
    
        
        def indices_selectionnes(sol):
            return [i+1 for i in range(len(self.values)) if sol.get(i, 0) == 1]

        print("\n--- Approche par valeurs ---")
        print("Objets sélectionnés :", indices_selectionnes(Sol1))
        print("Valeur totale :", sum(self.values[i-1] for i in indices_selectionnes(Sol1)))
        print("Poids total   :", sum(self.poids[i-1] for i in indices_selectionnes(Sol1)))

        print("\n--- Approche par poids ---")
        print("Objets sélectionnés :", indices_selectionnes(Sol2))
        print("Valeur totale :", sum(self.values[i-1] for i in indices_selectionnes(Sol2)))
        print("Poids total   :", sum(self.poids[i-1] for i in indices_selectionnes(Sol2)))

        print("\n--- Approche par ratio (val/poids) ---")
        print("Objets sélectionnés :", indices_selectionnes(Sol3))
        print("Valeur totale :", sum(self.values[i-1] for i in indices_selectionnes(Sol3)))
        print("Poids total   :", sum(self.poids[i-1] for i in indices_selectionnes(Sol3)))

        valeur1 = sum(self.values[i-1] for i in indices_selectionnes(Sol1))
        valeur2 = sum(self.values[i-1] for i in indices_selectionnes(Sol2))
        valeur3 = sum(self.values[i-1] for i in indices_selectionnes(Sol3))
        Vals = [valeur1, valeur2, valeur3]
        optimal_index = Vals.index(max(Vals))
        print("\n--- Meilleure solution avec les appproches gloutonnes ---")
        if optimal_index == 0:
            print("Approche par valeurs")
            print("Valeur totale :", valeur1)
        elif optimal_index == 1:
            print("Approche par poids")
            print("Valeur totale :", valeur2)
        else:
            print("Approche par ratio (val/poids)")
            print("Valeur totale :", valeur3)
        return Sols[optimal_index]
    
    def __main__(self):
        sol = self.SolutionOptimal()



# Exemple d'utilisation de la classe sac_Dos

print("Bienvenue dans le sac à dos glouton !")
print("\v====  BAG 1 ====\v")
if __name__ == "__main__":
    sac1 = sac_Dos_approche_gloutonne(typeDeFichier='excel',fichier='donnees_sac_a_dos1.xlsx', max_Weight=15)
    sac1.__main__()
print("\v====  BAG 2 ====\v")
if __name__ == "__main__":
    sac2 = sac_Dos_approche_gloutonne(typeDeFichier='excel',fichier='donnees_sac_a_dos2.xlsx', max_Weight=1000)
    sac2.__main__()
print("\v====  BAG 3 ====\v")
if __name__ == "__main__":
    sac3 = sac_Dos_approche_gloutonne(typeDeFichier='csv',fichier='donnees_sac_a_dos3.csv', max_Weight=900)
    sac3.__main__()