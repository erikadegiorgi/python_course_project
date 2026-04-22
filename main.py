print("hello world")

#esercizio 
#creo la classe Studenti con i relativi attributi
class Studente():
  def __init__(self, nome, cognome, eta, matricola):
    self.nome = nome
    self.cognome = cognome
    self.eta = eta
    self.matricola = matricola
    self.voti = []

#creo i metodi della classe
  def presentati(self):
    print(f"Salve sono {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è {self.matricola}")

  def aggiungi_voto(self, voto):
    if 18 <= voto <= 30:
      self.voti.append(voto)
      print(f"Voto {voto} registrato correttamente per {self.nome}.")
    elif voto < 18:
      print(f"Esame non superato: il voto {voto} è insufficiente e non verrà aggiunto.")
    else:
      print("Errore: un voto non può essere superiore a 30.")

  def calcola_media(self):
    if not self.voti:
      return 0
    return sum(self.voti) / len(self.voti)

  def studia(self, ore):
    print(f"Lo studente/ssa {self.nome} {self.cognome} ha studiato {ore} ore")
    
#definisco 2 oggetti per la classe
Studente1 = Studente("Anna","Lucrezi",24,"1357a")
Studente2 = Studente("Bruna","Carry",27,"2468b")

#testiamo il codice 
Studente1.presentati()
Studente2.presentati()

Studente1.aggiungi_voto(25)
Studente1.aggiungi_voto(21)
Studente1.aggiungi_voto(29)
Studente1.aggiungi_voto(19)

Studente2.aggiungi_voto(27)
Studente2.aggiungi_voto(23)
Studente2.aggiungi_voto(27)
Studente2.aggiungi_voto(18)

Studente1.calcola_media()
Studente2.calcola_media()
print(f"la media di {Studente1.nome} {Studente1.cognome} è {Studente1.calcola_media()}")
print(f"la media di {Studente2.nome} {Studente2.cognome} è {Studente2.calcola_media()}")

Studente1.studia(7)
Studente2.studia(9)