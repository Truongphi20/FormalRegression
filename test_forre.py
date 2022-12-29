import unittest
import forre as fo

class TestForre(unittest.TestCase):
	def setUp (self):
		print("\nChecking...")
		self.hs1 = [2,1]	#7,8
		self.hs2 = [1,3,1]	#4,5,6
		self.val1 = 26
		self.val2 = 16
	
	def tearDown(self):
		print("Tear Down\n")

	def test_normal(self):
		print("normal()")
		self.assertEqual(fo.normal(self.hs1,self.hs2),[2, 2, 2, 2, 2, 1, 1, 1, 1, 1])

	def test_extenda(self):
		print("extenda()")
		print("#Solve")
		self.assertEqual(fo.extenda(self.hs1,self.hs2),([2, 2, 2, 2, 2, 1, 1, 1, 1, 1], [1, 1, 1, 3, 3, 3, 1, 1, 1]))
		print("#Invert")
		self.assertEqual(fo.extenda(self.hs2,self.hs1),([1, 1, 1, 3, 3, 3, 1, 1, 1], [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
	unittest.main()