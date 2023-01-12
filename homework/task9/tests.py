import unittest
from random import randint
from test_scripts import *

class TestUserCode(unittest.TestCase):
    def setUp(self):
        self.user_lst = [5, 3, 6, 3, 8]
        self.user_lst2 = [1, 2, 3, 4, 5]
        self.user_lst3 = [5, 4, 3, 2, 1]
        self.moreprev = [6, 8]
        self.a = '213'
        self.b = get_copy(self.a)

    def test_my_sum_maxvalue(self):
        self.assertEqual(my_sum_maxvalue(1,2,3), 5)
    
    def test_my_func_exponent(self):
        self.assertEqual(my_func_exponent(2,3), 8)

    def test_my_func_moreprev(self):
        self.assertListEqual(my_func_moreprev(self.user_lst), self.moreprev)

    def test_my_func_moreprev2(self):
        self.assertTrue(my_func_moreprev(self.user_lst2))
    
    def test_my_func_moreprev3(self):
        self.assertFalse(my_func_moreprev(self.user_lst3))

    def test_get_copy(self):
        self.assertIs(self.a, self.b)

    def test_calculation_mass(self):
        self.assertEqual(Road(40, 5000).calculation_mass(), 25000)
    
    def test_road_class(self):
        self.assertIsInstance(Road(10, 2000), Road)

    def test_get_full_name(self):
        self.assertEqual(Position('Ivan', 'Losev', 2 , 4 , 6).get_full_name(), 'Ivan Losev')
    
    def test_get_total_income(self):
        self.assertEqual(Position('Ivan', 'Losev', 2 , 4 , 6).get_total_income(), 10)
    
    """ def test_raises(self):
        self.assertRaises(Div_Null,div_null, 1, 0 )      """
    
if __name__ == '__main__':
    unittest.main()


