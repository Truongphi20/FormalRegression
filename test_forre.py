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

	


if __name__ == '__main__':
	unittest.main()