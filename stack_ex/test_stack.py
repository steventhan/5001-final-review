from unittest import TestCase, main
from stack import Stack
from stack_ex import find_stack_length

class StackTest(TestCase):
    def test_find_stack_length(self):
        stack_obj = Stack([1, 2, 3])
        self.assertEqual(find_stack_length(stack_obj), 3)
        self.assertEqual(stack_obj.top(), 3)


main(verbosity=3)