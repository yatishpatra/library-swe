import unittest
from src.library import Library
class TestLibrarySprint1(unittest.TestCase):
    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        self.assertIn("B1", lib.books)
    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book("B1", "Python", "Guido")
    def test_borrow_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        self.assertEqual(lib.books["B1"]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        with self.assertRaises(ValueError):
            lib.borrow_book("B1")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        lib.return_book("B1")
        self.assertEqual(lib.books["B1"]["status"], "Available")
if __name__ == "__main__":
    unittest.main()