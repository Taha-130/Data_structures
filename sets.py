# Les sets sont des collections non ordonnées qui ne contiennent pas de doublons.
# Un set garantit que chaque élément est unique et les éléments ne sont pas indexés.

mon_set = {1, 2, 3, 4, 5}

# Ajouter un élément au set
# Vous pouvez ajouter un élément avec la méthode add().
mon_set.add(6)  # Le set devient {1, 2, 3, 4, 5, 6}

# Essayer d'ajouter un doublon
# Les sets ne permettent pas d'ajouter un doublon, l'élément sera ignoré
mon_set.add(3)  # Le set reste {1, 2, 3, 4, 5, 6}

# Supprimer un élément avec remove()
# Vous pouvez supprimer un élément spécifique avec la méthode remove().
mon_set.remove(4)  # Le set devient {1, 2, 3, 5, 6}

# Vérifier si un élément est dans le set
# Vous pouvez tester la présence d'un élément avec l'opérateur 'in'
print(3 in mon_set)  # Affiche True car l'élément 3 est bien dans le set

# Afficher le set modifié
print(mon_set)  # Affiche {1, 2, 3, 5, 6}
