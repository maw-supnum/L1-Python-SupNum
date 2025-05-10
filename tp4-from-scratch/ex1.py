import pandas as pd

# lire le fichier Notes_DEV110.xlsx
df = pd.read_excel("../assets/Notes_DEV110.xlsx")

# d = df.to_dict(orient="list")

student_number_grades_mapping = {}
for matricule, note_ds, note_exam in zip(df["Matricule"], df["DS"], df["Exam"]):
    student_number_grades_mapping[matricule] = {"ds": note_ds, "exam": note_exam}

# test_matricule = int(input("veuillez saisir un matricule : "))
# notes = student_number_grades_mapping.get(test_matricule)
# if notes is None:
#     print("Erreur: Matricule n'existe pas")
# else:
#     print(notes)

# lambda x: f(x) -> def f(x) anonyme
# print(max(student_number_grades_mapping, key= lambda x: student_number_grades_mapping[x]["exam"]))

matricules = []
notes_finales = []
for matricule, notes in student_number_grades_mapping.items():
    note_ds = notes["ds"]
    note_ds = note_ds if note_ds == note_ds else 0
    note_exam = notes["exam"]
    note_exam = note_exam if note_exam == note_exam else 0
    note_finale = int(0.4 * note_ds + 0.6 * note_exam * 100) / 100
    matricules.append(matricule)
    notes_finales.append(note_finale)

final_grades_df = pd.DataFrame({"Matricule": matricules, "Note": notes_finales})
final_grades_df.to_excel("../assets/notes_finales.xlsx", index=False)