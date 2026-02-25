"""
Module utils.py

Ce module contient les fonctions de calcul statistiques
pour une liste de notes étudiantes.
"""


def calcul_moyenne(liste_notes):
    """
    Calcule la moyenne des notes.

    Args:
        liste_notes (list): liste de nombres représentant les notes.

    Returns:
        float: moyenne des notes.
    """
    if not liste_notes:
        return 0

    somme = sum(liste_notes)
    moyenne = somme / len(liste_notes)

    return moyenne


def trouver_max(liste_notes):
    """
    Trouve la note maximale dans la liste.

    Args:
        liste_notes (list): liste de nombres représentant les notes.

    Returns:
        float: valeur maximale.
    """
    if not liste_notes:
        return None

    maximum = max(liste_notes)

    return maximum


def trouver_min(liste_notes):
    """
    Trouve la note minimale dans la liste.

    Args:
        liste_notes (list): liste de nombres représentant les notes.

    Returns:
        float: valeur minimale.
    """
    if not liste_notes:
        return None

    minimum = min(liste_notes)

    return minimum