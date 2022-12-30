import unittest
import forre as fo

class TestForre(unittest.TestCase):
	def setUp (self):
		print("\n\nChecking...")
		self.hs1 = [2,1]	#7,8
		self.hs2 = [1,3,1]	#4,5,6
		self.val1 = 26
		self.val2 = 16
		self.l_vals = [(0,0),(2,4),(3,18),(6,180),(8,448)] # list toa do cua cac diem (x,y)
	
	def tearDown(self):
		print("Tear Down")


	def test_quydong(self):
		print("quydong")
		self.assertEqual(fo.quydong(self.hs1,self.hs2),([10,5],[3,9,3]))

	def test_dienso(self):
		print("dienso")
		self.assertEqual(fo.dienso(1,5,3,[0,0,0,0,0,0,0,0]),[0,0,3,3,3,3,0,0])
		self.assertEqual(fo.dienso(2,4,3,[0,0,0,0,0]),[0,0,0,3,3])

	def test_dausi(self):
		print("dausi")
		self.assertEqual(fo.dausis(self.hs2,self.hs1),[3,12,15,5])
		self.assertEqual(fo.dausis(self.hs1,self.hs2),[10,15,12,3])
		self.assertEqual(fo.dausis([1],[1]),[1])

	def test_leng(self):
		print("leng")
		self.assertEqual(fo.leng(self.l_vals),[2,1,3,2])

	def test_Reparelib(self):
		print("Reparelib")
		self.assertEqual(fo.Reparelib(self.l_vals),{2:(2,[1,1]),3:(14,[1]),6:(54,[1,1,1]),8:(134,[1,1])})

if __name__ == '__main__':
	unittest.main()