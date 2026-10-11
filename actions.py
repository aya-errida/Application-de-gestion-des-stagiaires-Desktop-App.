import re
from tkinter import messagebox, simpledialog, END

from config import F1
from models import Stagiaire, StagiaireEtranger
from data_manager import sauvegarder_tout

table = None
entries = None


def initialiser(treeview, entries_dict):
    global table, entries
    table, entries = treeview, entries_dict


def supprimer():
    sel = table.selection()

    if not sel:
        messagebox.showerror("Erreur", "Sélectionner un stagiaire")
        return

    values = table.item(sel[0], "values")
    id_val = int(values[0])

    F1.supprimer(id_val)

    sauvegarder_tout()
    refresh()

    messagebox.showinfo("Succès", "Stagiaire supprimé") 


def restaurer():
    F1.restaurer()

    sauvegarder_tout()
    refresh()

    messagebox.showinfo("Succès", "Stagiaire restauré")


def rechercher():
    try:
        id_val = simpledialog.askinteger(
            "Recherche",
            "Entrer l'ID du stagiaire :"
        )

        if id_val is None:
            return

        resultats = []

        for s in F1.stagiaires:
            if s.id == id_val:
                resultats.append(s)
                break

        if resultats:
            refresh(resultats)
        else:
            messagebox.showerror("Erreur", "Stagiaire introuvable")

    except Exception as e:
        messagebox.showerror("Erreur", str(e))


def refresh(data=None):
    for item in table.get_children():
        table.delete(item)

    data = data or F1.stagiaires

    for s in data:
        statut = "Admis" if s.note >= 10 else "Non admis"
        table.insert("", "end", values=(
            s.id, s.nom, s.prenom, s.email,
            s.telephone, s.note, getattr(s, "pays", ""), statut
        ))


def vider_entries():
    for e in entries.values():
        e.delete(0, END)


def remplir_entries(event):
    sel = table.selection()
    if not sel:
        return

    values = table.item(sel[0], "values")

    for e in entries.values():
        e.delete(0, END)

    keys = ["Nom", "Prenom", "Email", "Telephone", "Note", "Pays"]
    for i, k in enumerate(keys, start=1):
        entries[k].insert(0, values[i])


def demander_id(titre):
    return simpledialog.askinteger(titre, "Veuillez saisir l'ID :")

def valider(email, tel, note):
    if not (0 <= note <= 20):
        return "Note invalide"

    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return "Email invalide"

    if not re.match(r'^0[5-7][0-9]{8}$', tel):
        return "Téléphone invalide"

    return None

def ajouter():
    try:
        nom = entries["Nom"].get()
        prenom = entries["Prenom"].get()
        email = entries["Email"].get()
        tel = entries["Telephone"].get()
        note = float(entries["Note"].get())
        pays = entries["Pays"].get()

        err = valider(email, tel, note)
        if err:
            messagebox.showerror("Erreur", err)
            return

        new_id = len(F1.stagiaires) + 1

        if pays:
            s = StagiaireEtranger(new_id, nom, prenom, email, tel, pays, note)
        else:
            s = Stagiaire(new_id, nom, prenom, email, tel, note)

        F1.ajouter(s)
        sauvegarder_tout()
        refresh()
        vider_entries()

        messagebox.showinfo("Succès", "Ajout réussi")

    except Exception as e:
        messagebox.showerror("Erreur", str(e))


def afficher(liste, titre):
    tri = messagebox.askyesno("Tri", "Ordre décroissant ?")
    liste.sort(key=lambda x: x.note, reverse=tri)
    refresh(liste)

def modifier():
    sel = table.selection()
    if not sel:
        messagebox.showerror("Erreur", "Sélectionner un stagiaire")
        return

    values = table.item(sel[0], "values")
    s = F1.chercher(int(values[0]))

    if not s:
        return

    try:
        email = entries["Email"].get()
        tel = entries["Telephone"].get()
        note = float(entries["Note"].get())

        err = valider(email, tel, note)
        if err:
            messagebox.showerror("Erreur", err)
            return

        s.nom = entries["Nom"].get()
        s.prenom = entries["Prenom"].get()
        s.email = email
        s.telephone = tel
        s.note = note

        pays = entries["Pays"].get()
        if pays:
            s.pays = pays

        sauvegarder_tout()
        refresh()
        vider_entries()

        messagebox.showinfo("Succès", "Modification réussie")

    except Exception as e:
        messagebox.showerror("Erreur", str(e))