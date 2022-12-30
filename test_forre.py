import unittest
import forre as fo

class TestForre(unittest.TestCase):
	def setUp (self):
		print("\n\nChecking...")
		self.hs1 = [2,1]	#7,8
		self.hs2 = [1,3,1]	#4,5,6
		self.val1 = 26
		self.val2 = 16
	
	def tearDown(self):
		print("Tear Down")


	def test_quydong(self):
		print("quydong")
		self.assertEqual(fo.quydong(self.hs1,self.hs2),([10,5],[3,9,3]))

	def test_dienso(self):
		print("dienso")
		print("#1")
		self.assertEqual(fo.dienso(1,5,3,[0,0,0,0,0,0,0,0]),[0,0,3,3,3,3,0,0])
		print("#2")
		self.assertEqual(fo.dienso(2,4,3,[0,0,0,0,0]),[0,0,0,3,3])

	def test_dausi(self):
		print("dausi")
		print('#1')
		self.assertEqual(fo.dausis(self.hs2,self.hs1),[3,12,15,5])
		print('#2')
		self.assertEqual(fo.dausis(self.hs1,self.hs2),[10,15,12,3])

if __name__ == '__main__':
	unittest.main()