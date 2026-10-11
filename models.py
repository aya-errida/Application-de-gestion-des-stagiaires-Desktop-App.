class Stagiaire:
    def __init__(self,id,nom,prenom,email,telephone,note):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.note = note
        self.pays = "Maroc"


class StagiaireEtranger(Stagiaire):
    def __init__(self,id,nom, prenom,email,telephone,pays,note):
        super().__init__(id,nom,prenom,email,telephone,note)
        self.pays = pays


class Formation:
    def __init__(self):
        self.stagiaires = []
        self.corbeille = []

    def ajouter(self, stagiaire):
        self.stagiaires.append(stagiaire)

    def chercher(self, id_stagiaire):
        for stagiaire in self.stagiaires:
            if stagiaire.id == id_stagiaire:
                return stagiaire

        return None

    def supprimer(self, id_stagiaire):
        stagiaire = self.chercher(id_stagiaire)

        if stagiaire:
            self.corbeille.append(stagiaire)
            self.stagiaires.remove(stagiaire)

    def restaurer(self):
        if self.corbeille:
            self.stagiaires.append(
                self.corbeille.pop()
            )

    def moyenne(self):
        if not self.stagiaires:
            return 0

        return (
            sum(
                stagiaire.note
                for stagiaire in self.stagiaires
            )
            / len(self.stagiaires)
        )