class Domino:
    def __init__(self , Cote1 , Cote2):
        self.Cote1 = Cote1
        self.Cote2 = Cote2
        
    def Affiche_Points(self):
        print(f"le cote 1 :{self.Cote1}")
        print(f"le cote 2  : {self.Cote2}")
        
    def somme_poits(self ):
        return(self.Cote1 + self.Cote2) 
    
D1 = Domino(4 , 5)
D2= Domino(5 , 2)
D1.Affiche_Points()
D2.Affiche_Points()
print("La somme de deux domino est" ,(D1.somme_poits() + D2.somme_poits()) )
        
        