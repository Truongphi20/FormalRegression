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
		self.assertEqual(fo.dausis(self.hs2,self.hs1,0),[3,12,15,5])
		self.assertEqual(fo.dausis(self.hs1,self.hs2,0),[10,15,12,3])
		self.assertEqual(fo.dausis([1],[1],0),[1])
		self.assertEqual(fo.dausis([3,2,1],[1,2,3],2),[18,24,18])
		self.assertEqual(fo.dausis([1,2],[3,2,1],0),[6,18,9,3])

	def test_leng(self):
		print("leng")
		self.assertEqual(fo.leng(self.l_vals,1),[2,1,3,2])

	def test_Reparelib(self):
		print("Reparelib")
		self.assertEqual(fo.Reparelib(self.l_vals),({2:(2.0,[1,1]),3:(14.0,[1]),6:(54.0,[1,1,1]),8:(134.0,[1,1])}, 1.0))

	def test_HisThuc(self):
		print("HisThuc")
		self.assertEqual(fo.HitThuc([(1,0),(3,24),(4,60),(7,336),(8,504),(10,990)]).last_vals,{7:(6.0,[6,18,9,3]),8:(6.0,[18,24,18]), 10: (6.0, [3, 9, 18, 6])})
		self.assertEqual(fo.HitThuc(self.l_vals).last_vals,{6:(6.0,[6,18,9,3]),8:(6.0,[45,63,54,18])})
		self.assertEqual(fo.HitThuc([(-5,-125),(-1,-1),(0,0),(3,27),(7,343)]).last_vals,{3:(6.0,[6,18,36,60,30,10]),7:(6.0,[126,186,180,108,54,18])})
		self.assertEqual(fo.HitThuc([(-1.5,-7.875),(-1,-3),(0.5,-0.375),(3,9),(4,32),(6,144)]).last_vals,{3:(0.75,[180,270,270,180,108,54,18]),4:(0.75,[175,525,1050,1350,1425,1275,900,300]),6:(0.75,[48,144,288,480,720,700,420,210,70])}) #x^3-2x^2
		self.assertEqual(fo.HitThuc([(-5,30),(-1,2),(0.5,-0.25),(3,6),(4,12),(6,30)]).last_vals,{0.5:(0.5,[3,6,9,12,15,18,21,24,16,8]),3:(0.5,[5,10,15,12,9,6,3]),4:(0.5,[2,4,6,8,10,5]),6:(0.5,[4,8,6,4,2])})
if __name__ == '__main__':
	unittest.main()