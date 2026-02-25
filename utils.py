def calcul_moyenne(liste_notes):
    """
    Calcule la moyenne des notes.

    Args:
        liste_notes (list): liste des notes.

    Returns:
        float: moyenne des notes.
    """
    if not liste_notes:
        return 0

    somme = sum(liste_notes)
    moyenne = somme / len(liste_notes)

    return moyenne