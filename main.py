import tkinter as tk
from tkinter import ttk

from config import (
    LABELS,
    COLS,
    WINDOW_TITLE,
    WINDOW_SIZE
)

from data_manager import initialiser_donnees

from actions import (
    initialiser,refresh,ajouter,modifier, remplir_entries,
    supprimer, restaurer, rechercher
)

root = tk.Tk()
root.title(WINDOW_TITLE)
root.geometry(WINDOW_SIZE)


frame_form = tk.Frame(root)
frame_form.pack(pady=10)

entries = {}

for i, label in enumerate(LABELS):
    tk.Label(
        frame_form,
        text=label
    ).grid(row=i, column=0, padx=5, pady=5)

    e = tk.Entry(frame_form, width=40)

    e.grid(
        row=i,column=1,padx=5, pady=5
    )

    entries[label] = e


frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(
    frame_btn,
    text="Ajouter",
    command=ajouter
).grid(row=0, column=0, padx=5)

tk.Button(
    frame_btn,
    text="Modifier",
    command=modifier
).grid(row=0, column=1, padx=5)

tk.Button(
    frame_btn,
    text="Supprimer",
    command=supprimer
).grid(row=0, column=2, padx=5)

tk.Button(
    frame_btn,
    text="Restaurer",
    command=restaurer
).grid(row=0, column=3, padx=5)

tk.Button(
    frame_btn,
    text="Rechercher ID",
    command=rechercher
).grid(row=0, column=4, padx=5)


table = ttk.Treeview(
    root,
    columns=COLS,
    show="headings",
    height=15
)

for col in COLS:
    table.heading(col, text=col)
    table.column(col, width=140)

table.pack(fill="both", expand=True)

table.bind(
    "<<TreeviewSelect>>",
    remplir_entries
)


initialiser(table, entries)
initialiser_donnees()
refresh()
root.mainloop()