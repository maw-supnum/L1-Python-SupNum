ls = ["1", "2", "3"], ["a", "b"], ["x", "y"], ["alpha", "beta"]
produit_cartesien_ls = [
    ("3", "b", "y", "beta"),
    ("1", "a", "x", "alpha"),
    ("1", "a", "x", "beta"),
    ("1", "a", "y", "alpha"),
    ("1", "a", "y", "beta"),
    ("1", "b", "x", "alpha"),
    ("1", "b", "x", "beta"),
    ("1", "b", "y", "alpha"),
    ("1", "b", "y", "beta"),
    ("2", "a", "x", "alpha"),
    ("2", "a", "x", "beta"),
    ("2", "a", "y", "alpha"),
    ("2", "a", "y", "beta"),
    ("2", "b", "x", "alpha"),
    ("2", "b", "x", "beta"),
    ("2", "b", "y", "alpha"),
    ("2", "b", "y", "beta"),
    ("3", "a", "x", "alpha"),
    ("3", "a", "x", "beta"),
    ("3", "a", "y", "alpha"),
    ("3", "a", "y", "beta"),
    ("3", "b", "x", "alpha"),
    ("3", "b", "x", "beta"),
    ("3", "b", "y", "alpha"),
    ]
print(len(produit_cartesien_ls))


from itertools import product

def produit_cartesien(*listes):
    return list(product(*listes))

# test
print(set(produit_cartesien(*ls)) == set(produit_cartesien_ls))


