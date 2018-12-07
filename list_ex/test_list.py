from unittest import TestCase, main
from list_ex import convert_to_int_list, flatten_2d_lst, \
    reverse_and_double_string, GuineaPig, fav_pigs

class ListTest(TestCase):
    def test_ex1(self):
        lst1 = [1, 5.0, "str"] 
        self.assertEqual(convert_to_int_list(lst1), [1, 5, 0])
        lst2 = ["s", 42, True]
        self.assertEqual(convert_to_int_list(lst2), [0, 42, 0])
    
    def test_ex2(self):
        nested_lst = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        expected = [i for i in range(1, 10)]
        self.assertEqual(flatten_2d_lst(nested_lst), expected)
    
    def test_ex3(self):
        string = "abcd"
        rev = "dcbaa"
        self.assertEqual(reverse_and_double_string(string, "a"), rev)

        string = "abcd"
        rev = "dcbba"
        self.assertEqual(reverse_and_double_string(string, "b"), rev)

    def test_ex4(self):
        pigs_data = [("belly", 5), ("button", 5), ("brownie", 4), 
            ("grey", 2), ("fluffy", 1), ("walter", 3)]
        pigs = [GuineaPig(name, fav_level) for name, fav_level in pigs_data]
        expected_fav_pigs = [pigs[0], pigs[1], pigs[2], pigs[5]]
        self.assertEqual(fav_pigs(pigs), expected_fav_pigs)





main(verbosity=3)