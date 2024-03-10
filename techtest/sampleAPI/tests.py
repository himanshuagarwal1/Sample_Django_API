from django.test import TestCase

import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):

    def setUp(self):
       
        self.client = Client()

    def test1(self):
        
        response = self.client.get("/client/")
        self.assertEqual(response.status_code, 200)
    
    def test2(self):

        response = self.client.get("/client/1")
        self.assertEqual(response.status_code, 200)

    def test3(self):

        response = self.client.get("/client/")
        
        dat = {  "name": "himanshu",
        "contact_number" : 5054,
        "contact_email" : "himand4shu4@gmail.com",
        "status": True
        }


        response = self.client.post("/client/", data = dat)
        self.assertEqual(response.status_code, 201)

        

   