# we should define a function that opens
# a file given an argument `mode` and `file_name`
# return a descriptor for the file

def ouvrir_fichier(nom_fichier, mode):
    return open(nom_fichier, mode)