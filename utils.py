def trouver_max(liste_notes):
    """
    Trouve la note maximale dans la liste.

    Args:
        liste_notes (list): liste des notes.

    Returns:
        float: valeur maximale.
    """
    if not liste_notes:
        return None

    maximum = max(liste_notes)

    return maximum