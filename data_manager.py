import json
import csv

from models import Stagiaire, StagiaireEtranger
from config import F1, JSON_FILE, CSV_FILE, TXT_FILE


def sauvegarder_json():
    data = []
    for s in F1.stagiaires:
        data.append({
            "id": s.id,
            "nom": s.nom,
            "prenom": s.prenom,
            "email": s.email,
            "telephone": s.telephone,
            "note": s.note,
            "pays": s.pays
        })

    with open(
        JSON_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def sauvegarder_csv():
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "ID", "Nom", "Prenom", "Email",
            "Telephone", "Note", "Pays"
        ])

        for s in F1.stagiaires:
            writer.writerow([
                s.id, s.nom, s.prenom,
                s.email, s.telephone,
                s.note, s.pays
            ])


def generer_rapport_txt():
    with open(TXT_FILE, "w", encoding="utf-8") as f:

        f.write("===== RAPPORT DES STAGIAIRES =====\n\n")

        for s in F1.stagiaires:
            statut = "Admis" if s.note >= 10 else "Non admis"

            f.write(f"ID : {s.id}\n")
            f.write(f"Nom : {s.nom} {s.prenom}\n")
            f.write(f"Email : {s.email}\n")
            f.write(f"Telephone : {s.telephone}\n")
            f.write(f"Pays : {s.pays}\n")
            f.write(f"Note : {s.note}\n")
            f.write(f"Statut : {statut}\n")
            f.write("-" * 40 + "\n")

        f.write(f"\nTotal : {len(F1.stagiaires)}")


def charger_json():
    try:
        with open(
            JSON_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        F1.stagiaires.clear()
        for s in data:
            if s["pays"] == "Maroc":
                stagiaire = Stagiaire(
                    s["id"],
                    s["nom"],
                    s["prenom"],
                    s["email"],
                    s["telephone"],
                    s["note"]

                )

            else:

                stagiaire = StagiaireEtranger(
                    s["id"],
                    s["nom"],
                    s["prenom"],
                    s["email"],
                    s["telephone"],
                    s["pays"],
                    s["note"]

                )

            F1.ajouter(stagiaire)

    except FileNotFoundError:

        pass

def initialiser_donnees():

    charger_json()

    if len(F1.stagiaires) == 0:

        F1.ajouter(
            Stagiaire(
                1,
                "Ali",
                "Ahmed",
                "ali@gmail.com",
                "0611111111",
                14
            )
        )

        F1.ajouter(
            Stagiaire(
                2,
                "Sara",
                "Youssef",
                "sara@gmail.com",
                "0622222222",
                9
            )
        )

        F1.ajouter(
            StagiaireEtranger(
                3,
                "John",
                "Smith",
                "john@gmail.com",
                "0633333333",
                "USA",
                16
            )
        )

        F1.ajouter(
            StagiaireEtranger(
                4,
                "Emma",
                "Brown",
                "emma@gmail.com",
                "0644444444",
                "UK",
                7
            )
        )

        F1.ajouter(
            Stagiaire(
                5,
                "Omar",
                "Karim",
                "omar@gmail.com",
                "0655555555",
                18
            )
        )

def sauvegarder_tout():
    sauvegarder_json()
    sauvegarder_csv()
    generer_rapport_txt()