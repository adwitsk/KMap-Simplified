import unittest
from HW2_2018276 import *

class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(3,"(0,2,6) d-"),"w'y'+xy'")
		self.assertEqual(minFunc(3,"(2,5,7) d-"),"w'xy'+wy")
		self.assertEqual(minFunc(2,"(0) d(2)"),"x'")
		self.assertEqual(minFunc(3,"(0,4,5) d-"),"x'y'+wx'")
		self.assertEqual(minFunc(4,"(0,1,2,4,5,6,8,9,12,13,14) d-"),"y'+w'z'+xz'")
		self.assertEqual(minFunc(4,"(1,3,7,11,15) d(0,2,5)"),"yz+w'x' OR yz+w'z")
		self.assertEqual(minFunc(4,"(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) d-"),"1")
		self.assertEqual(minFunc(3,"(1,2,3,6) d(0)"),"w'+xy'")
		self.assertEqual(minFunc(4,"(0,3,4,7,8,11,12,13,15) d-"),"y'z'+yz+wxy' OR y'z'+yz+wxz")
		self.assertEqual(minFunc(3,"(0,1,4,6,7) d-"),"w'x'+wx+x'y' OR w'x'+wx+wy'")
		
                
if __name__=='__main__':
	unittest.main()
