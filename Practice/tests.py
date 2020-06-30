import unittest
import work
import answers

class PracticeTests(unittest.TestCase):
	def test_ex_1(self):
		self.assertEqual(True, True)

	def test_ex_2(self):
		answer = 6
		try: 
			self.assertEqual(work.ex_2(4,5,6), answer)
			self.assertEqual(work.ex_2(6,2,4), answer)
			self.assertEqual(work.ex_2(2,4,6), answer)
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")
		
	def test_ex_3(self):
		answer = [1,2,3]
		try:
			self.assertEqual(work.ex_3(1,2,3), answer)
			self.assertEqual(work.ex_3(1,3,2), answer)
			self.assertEqual(work.ex_3(2,1,3), answer)
			self.assertEqual(work.ex_3(2,3,1), answer)
			self.assertEqual(work.ex_3(3,1,2), answer)
			self.assertEqual(work.ex_3(3,2,1), answer)
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_4(self):
		try:
			self.assertTrue(work.ex_4(18,2,3,4,1))
			self.assertTrue(work.ex_4(1,24,3,4,15))
			self.assertTrue(work.ex_4(1,2,33,4,17))
			self.assertTrue(work.ex_4(1,2,3,41,17))
			self.assertTrue(work.ex_4(1,2,33,4,172))
			self.assertFalse(work.ex_4(1,2,3,4,17))
			self.assertFalse(work.ex_4(1,2,3,4,1))
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_5(self):
		try:
			self.assertEqual(work.ex_5(2,4,22,55,3), 2)
			self.assertEqual(work.ex_5(2,44,22,55,3), 3)
			self.assertEqual(work.ex_5(2,4,2,5,3), 0)
			self.assertEqual(work.ex_5(223,411,22,55,23), 5)
			self.assertEqual(work.ex_5(11,11,21,55,3), 2)
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_6(self):
		try:
			self.assertEqual(work.ex_6([1,2,3,4,5]), 3)
			self.assertEqual(work.ex_6([20,22,24,56]), 30.5)
			self.assertEqual(work.ex_6([1,2]), 1.5)
			self.assertEqual(work.ex_6([1]), 1)
			self.assertEqual(work.ex_6([1,1,1,1,1,1,1,1,1,1]), 1)
			self.assertEqual(work.ex_6([1000, 1000, 1002, 1002]), 1001)
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")
			