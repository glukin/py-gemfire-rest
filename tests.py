import unittest  
from GemfireClient import *
import os


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        hostname = "mclaren.gemstone.com"
        port = 8080
        debug_mode = False
        self.client = GemfireClient(hostname, port, debug_mode)
        self.myRepo = self.client.create_repository("orders")
        self.myRegion = self.myRepo.get_region()
        
        #conn = self.client.connection()
          
    def test_list_all_regions(self):
        allregions = self.client.list_all_regions()
        self.assertIsInstance(allregions, list)
        
        
    def test_get_repo(self):
        productRepo = self.client.create_repository("products")
        self.assertNotEqual(False, productRepo)
        
    
        
    def test_new_query(self):
        random_string = os.urandom(4)
        newquery = self.client.new_query(random_string,"SELECT * FROM /orders")
        self.assertEqual(newquery, True)
    
    def test_adhoc_query(self):
        name1 = "abc"
        id1 = 13
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        result = self.myRegion.create(13,c1)
        self.assertEqual(result, True)
        newquery = self.client.adhoc_query("SELECT * FROM /orders")
        result = self.myRegion.delete(13)
        self.assertEqual(result, True)
        
        
    def test_list_all_queries(self):
        allqueries = self.client.list_all_queries()
   
        
    def test_list_all_functions(self):
        data = self.client.list_all_functions()
  
    def test_run_function(self):
        value = {"args": [2]}
        data = self.client.execute_function("functionTest","MostValuedCustomer", value)
    
        
        
        
    def test_repo(self):
        repo = self.myRepo.get_region()
      
        
   
        
    def test_save_singleobject(self):
        name = "abc"
        id = 002
        surname = "def"  
        result = self.myRepo.save(Customer(name,id,surname))
        self.assertEqual(result, True)
        self.myRepo.delete(002)
        
    def test_save_listofobject(self):
        name = "abc"
        id = 002
        surname = "def" 
        name1 = "abc"
        id1 = 107
        surname1 = "def"
        c1 = Customer(name1, id1, surname1)
        c2 = Customer(name, id, surname)
        c3 = [c1,c2]
        result = self.myRepo.save(c3)
        self.assertEqual(result, True)
        self.myRepo.delete(c3)
    
    def test_find(self):
        name = "abc"
        id = 02
        surname = "def"  
        self.myRepo.save(Customer(name,id,surname))
        name1 = "abc"
        id1 = 03
        surname1 = "def"  
        c1 = Customer(name1, id1, surname1)
        c2 = Customer(name, id, surname)
        self.myRepo.save([c1,c2])
        self.myRepo.find([03,02])
        
        
        
    def test_findall(self):
        self.myRepo.find_all()
        
    
    def test_exists(self):
        name = "abc"
        id = 10
        surname = "def"  
        self.myRepo.save(Customer(name,id,surname))
        result = self.myRepo.exists(10)
        self.assertEqual(result, True)
        self.myRepo.delete(10)
        
    def test_repo_get_region(self):
        find = self.myRepo.get_region()
        return find
    
    def test_repo_delete_id(self):
        name = "abc"
        id = 001
        surname = "def"  
        self.myRepo.save(Customer(name,id,surname))
        result = self.myRepo.delete(001)
        self.assertEqual(result, True)
    
    def test_delete_listobject(self):
        name = "abc"
        id = 207
        surname = "def"  
        name1 = "abc"
        id1 = 107
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        c2 = Customer(name, id, surname)
        c3 = [c1,c2]
        self.myRepo.save(c3)
        result = self.myRepo.delete(c3)
        self.assertEqual(result, True)
        
        
    def test_delete_singleject(self):
        name = "abc"
        id = 207
        surname = "def"  
        c2 = Customer(name, id, surname)
        self.myRepo.save(c2)
        saved = self.myRepo.delete(c2)
        
    
       

    def testrun_query(self):
        qu = ["1 : 2"]
        runquery = self.client.run_query("try", qu)
        #self.assertIsInstance(runquery, object)
         
        
    def test_create(self):
        name1 = "abc"
        id1 = 13
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        result = self.myRegion.create(13,c1)
        self.assertEqual(result, True)
        self.myRegion.delete(13)
        #result = self.myRegion.create(95, value)
        
            
    def test_keys(self):
        name1 = "abc"
        id1 = 78
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        result = self.myRegion.create(78, c1)
        self.assertEqual(result, True)
        self.myRegion.keys()
        self.myRegion.delete(78)
        
        
       
     
    def test_put(self):
        name1 = "abc"
        id1 = 14
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        self.assertEqual(self.myRegion.put(14, c1), True)
        self.myRegion.delete(14)
        
        
        
    def test_get(self): 
        name1 = "abc"
        id1 = 15
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        self.assertEqual(self.myRegion.put(15, c1), True)
        result = self.myRegion.get(15)
        #self.assertEqual(result, object)
        self.myRegion.delete(15)
        #self.assertEqual(data,json)
        
    def test_dirget(self):
        name1 = "abc"
        id1 = 15
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        self.assertEqual(self.myRegion.put(15, c1), True)
        result = self.myRegion[15]
        #self.assertEqual(result, object)
        self.assertEqual(self.myRegion.delete(15), True)
         
        
        
    def test_putAll(self):  
        name1 = "abc"
        id1 = 93
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        name = "abc"
        id = 94
        surname = "def" 
        c2 = Customer(name, id, surname)
        item = {93:c1, 94:c2}
        self.assertEqual(self.myRegion.put_all(item), True)
        self.assertEqual(self.myRegion.delete(93,94), True)
       
        
        
    def test_update(self):
        name1 = "abc"
        id1 = 93
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        name = "abc"
        id = 94
        surname = "def" 
        c2 = Customer(name, id, surname)
        item = {93:c1, 94:c2}
        
        self.assertEqual(self.myRegion.put_all(item), True)
        name3 = "abc"
        id3 = 95
        surname3 = "def" 
        c3 = Customer(name3, id3, surname3)
        updt = self.myRegion.update(94, c3)
        self.assertEqual(updt, True)
        self.assertEqual(self.myRegion.delete(93,94), True)
        
        
    def test_compare_And_Set(self): 
        name1 = "abc"
        id1 = 94
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        name = "abc"
        id = 96
        surname = "def" 
        c2 = Customer(name, id, surname)
        self.assertEqual(self.myRegion.put(94, c1), True)
        self.assertEqual(self.myRegion.compare_and_set(94,c1,c2), True)
        self.assertEqual(self.myRegion.delete(94), True)
        
        
    def test_get_All(self):
        self.assertIsInstance(self.myRegion.get_all(), object)
    
      
    def test_iterator(self):
        for key in self.myRegion.keys():
            print key
          
    def test_delete(self):
        name1 = "abc"
        id1 = 94
        surname1 = "def" 
        c1 = Customer(name1, id1, surname1)
        self.assertEqual(self.myRegion.put(94,c1), True)
        self.assertEqual(self.myRegion.delete(94), True)
        
        
    def testclear(self):
        clearall = self.myRegion.clear()    
        self.assertEqual(clearall, True)
        
    

            
    
