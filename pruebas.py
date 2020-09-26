import os
import time
import unittest
import app
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UnitTest(unittest.TestCase):
        
    def test_rf01(self):
        
        self.driver = webdriver.Firefox(executable_path="driver/geckodriver-v0.27.0-linux64/geckodriver")
        
        driver = self.driver
        driver.get("http://localhost:5000/")
        self.assertIn("Coffe Clasification", driver.title)
        
        time.sleep(2)
        
        
        boton_subir = driver.find_element_by_class_name('upload-label')
        self.assertIn("True", str(boton_subir.is_displayed()))

        time.sleep(2)
        self.driver.close()
        
    def test_rf02(self):
        
        self.driver = webdriver.Firefox(executable_path="driver/geckodriver-v0.27.0-linux64/geckodriver")
        
        driver = self.driver
        driver.get("http://localhost:5000/")
        
        imagen = driver.find_element_by_id("imageUpload")
        imagen.send_keys(os.getcwd()+"/uploads/grano_1.jpeg")
        
        time.sleep(3)
        self.driver.close()
    
    def test_rf03(self):
        
        prediccion = app.class_pred("uploads/grano_1.jpeg")
        
        if prediccion == "AplastadoR":
            self.assertIn("AplastadoR", prediccion)
        elif prediccion == "ArrugadoR":
            self.assertIn("ArrugadoR", prediccion)
        elif prediccion == "BrocaR":
            self.assertIn("BrocaR", prediccion)
        elif prediccion == "NegroR":
            self.assertIn("NegroR", prediccion)
        elif prediccion == "Sobre SecadoR":
            self.assertIn("Sobre SecadoR", prediccion)
        elif prediccion == "CardenilloR":
            self.assertIn("CardenilloR", prediccion)
        elif prediccion == "CristalizadoR":
            self.assertIn("CristalizadoR", prediccion)
        elif prediccion == "Mordido o cortadoR":
            self.assertIn("Mordido o cortadoR", prediccion)
        elif prediccion == "ReposadoR":
            self.assertIn("ReposadoR", prediccion)
        elif prediccion == "VeteadoR":
            self.assertIn("VeteadoR", prediccion)
        elif prediccion == "InmaduroR":
            self.assertIn("InmaduroR", prediccion)
        elif prediccion == "SanoR":
            self.assertIn("SanoR", prediccion)
        elif prediccion == "VinagreR":
            self.assertIn("VinagreR", prediccion)
        elif prediccion == "FlojoR":
            self.assertIn("FlojoR", prediccion)
        elif prediccion == "MantequilloR":
            self.assertIn("MantequilloR", prediccion)
            
    def test_rf04(self):
        
        self.driver = webdriver.Firefox(executable_path="driver/geckodriver-v0.27.0-linux64/geckodriver")
        
        driver = self.driver
        driver.get("http://localhost:5000/")
          
        imagen = driver.find_element_by_id("imageUpload")
        imagen.send_keys(os.getcwd()+"/uploads/grano_1.jpeg")
        time.sleep(2)
        
        boton = driver.find_element_by_id("btn-predict")
        boton.send_keys(Keys.ENTER)
        time.sleep(2)
        
        resultado = driver.find_element_by_id('result')
        self.assertIn("True", str(resultado.is_displayed()))

        time.sleep(2)
        self.driver.close()
        
    def test_rnf05(self):
        
        self.driver = webdriver.Firefox(executable_path="driver/geckodriver-v0.27.0-linux64/geckodriver")
        
        driver = self.driver
        driver.get("http://localhost:5000/")
        
        imagen = driver.find_element_by_id("imageUpload")
        imagen.send_keys(os.getcwd()+"/uploads/grano_1.jpeg")
        time.sleep(2)
        
        boton_predecir = driver.find_element_by_id('btn-predict')
        self.assertIn("True", str(boton_predecir.is_displayed()))

        time.sleep(2)
        self.driver.close()
         
if __name__ == '__main__':
    unittest.main()
    