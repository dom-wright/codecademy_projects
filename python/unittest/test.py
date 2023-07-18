import surfshop
import unittest


class TestSurfing(unittest.TestCase):

    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_one_surfboard(self):
        self.assertEqual(self.cart.add_surfboards(
            1), "Successfully added 1 surfboard to cart!")

    def test_add_multiple_surfboards(self):
        for num in range(2, 5):
            with self.subTest(num):
                self.assertEqual(self.cart.add_surfboards(
                    num), f"Successfully added {num} surfboards to cart!")
                self.cart.num_surfboards = 0

    @unittest.skip
    def test_add_five_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError,
                          self.cart.add_surfboards, 5)
        # with self.assertRaises(surfshop.TooManyBoardsError):
        #     self.cart.add_surfboards(5)

    @unittest.expectedFailure
    def test_apply_discount(self):
        self.cart.apply_locals_discount()
        self.assertEqual(self.cart.locals_discount, True)


unittest.main()
