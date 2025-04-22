from utils import *
import unittest

if __name__ == "__main__":

  

  print("Voici quelques tests:")

  liste1 = [1, 2, 3, 4, 5]
  liste2= [0,0,1]
  liste3= []
  liste4= [0,0,0]
  liste5= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
  liste6= [1,-1]
  
  #moyenne1 = calculer_moyenne(liste1)
  #print(f"La moyenne de {liste1} est : {moyenne1}")

  self.assertEqual(calculer_moyenne(liste1), 3)
  self.assertEqual(calculer_moyenne(liste2), 1/3)
  self.assertEqual(calculer_moyenne(liste3), None)
  self.assertEqual(calculer_moyenne(liste4), 0)
  self.assertEqual(calculer_moyenne(liste5), 1)
  self.assertEqual(calculer_moyenne(liste6), 0)
  

