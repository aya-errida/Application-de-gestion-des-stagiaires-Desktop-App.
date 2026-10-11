from models import Formation

F1 = Formation()


LABELS = [
    "Nom",
    "Prenom",
    "Email",
    "Telephone",
    "Note",
    "Pays"
]

COLS = (
    "ID",
    "Nom",
    "Prenom",
    "Email",
    "Tel",
    "Note",
    "Pays",
    "Statut"
)

JSON_FILE = "stagiaires.json"
CSV_FILE = "stagiaires.csv"
TXT_FILE = "rapport.txt"

WINDOW_TITLE = "Gestion des stagiaires"
WINDOW_SIZE = "1300x650"