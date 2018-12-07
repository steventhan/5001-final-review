from unittest import TestCase, main
from guinea_pig import GuineaPig

class GuineaPigTest(TestCase):
    def setUp(self):
        self.button = GuineaPig("button", "black/white", 5, 3, 5)
        self.grey = GuineaPig("grey", "grey/white", 5, 3, 3)
        self.walter = GuineaPig("walter", "white/orange", 1, 2, 3)
        self.brownie = GuineaPig("brownie", "brown", 1, 3, 4)

    def test_init(self):
        self.assertEqual(self.button.name, "button")
        self.assertEqual(self.button.color, "black/white")
        self.assertEqual(self.button.age, 5)
        self.assertEqual(self.button.weight, 3)
    
    def test_jump(self):
        self.assertFalse(self.button.jump())
        self.assertTrue(self.walter.jump())

    def test_eq(self):
        self.assertTrue(self.grey == self.button)
        self.assertTrue(self.button == self.grey)

    def test_gt(self):
        self.assertTrue(self.button > self.walter)
        self.assertTrue(self.brownie > self.walter)
        self.assertFalse(self.button > self.grey)

    def test_ge(self):
        self.assertTrue(self.grey >= self.button)
        self.assertTrue(self.button >= self.walter)
        self.assertTrue(self.brownie >= self.walter)
        self.assertTrue(self.button >= self.grey)

    def test_lt(self):
        self.assertTrue(self.grey <= self.button)
        self.assertTrue(self.walter <= self.button)
        self.assertTrue(self.walter <= self.brownie)
        self.assertTrue(self.grey <= self.button)
    
    def test_add(self):
        super_pig = self.brownie + self.walter
        self.assertEqual(super_pig.name, "brownie walter")
        self.assertEqual(super_pig.age, 2)
        self.assertEqual(super_pig.weight, 5)
        self.assertEqual(super_pig.fav_level, 3)
        self.assertEqual(super_pig.color, "brown/white/orange")


main(verbosity=3)