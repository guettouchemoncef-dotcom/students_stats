"""
Fichier principal du projet StudentStats.
Teste les fonctions du module utils.
"""

import utils


def main():
    """
    Fonction principale exécutant les tests.
    """
    notes = [12, 15, 9, 18, 14]

    print("Liste des notes :", notes)
    print("Moyenne :", utils.calcul_moyenne(notes))
    print("Maximum :", utils.trouver_max(notes))
    print("Minimum :", utils.trouver_min(notes))


if __name__ == "__main__":
    main()