#   Objectif :
#   Implémenter une fonction récursive qui calcule la somme des chiffres d'un nombre donne
#   Conditions :
#   Utiliser une fonction récursive pour résoudre le problème.
#   Le code doit être propre, bien documenté et respecter les bonnes pratiques de programmation.
#   Le test doit être réalisé en PHP, Python et JavaScript.
#   Exemple :
#   Input : 12345
#   Output : 15 (1 + 2 + 3 + 4 + =
#   Instructions :
#   Écrire une fonction nommée sommeChiffres qui prend un seul argument, un entier positif.
#   La fonction doit retourner la somme des chiffres de l'entier donné.

def sommeChiffres(n):
    if isinstance(n, int) and n >= 0:
        if n < 10:
            return n
        else:
            return n % 10 + sommeChiffres(n // 10)
    else:
        raise ValueError("L'argument doit être un entier positif.")

try:
    result = sommeChiffres(12345)
    print(result) # Output : 15
except ValueError as e:
    print(e)
