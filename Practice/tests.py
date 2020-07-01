import unittest
import work
# import answers

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
			
	def test_ex_7(self):
		a = [9,9,9,94]
		b = [1,4,5,6]
		c = [666,666,668]
		d = [666,666,665]
		try:
			self.assertTrue(work.ex_7(a,b))
			self.assertFalse(work.ex_7(b,a))
			self.assertTrue(work.ex_7(c,d))
			self.assertFalse(work.ex_7(d,c))
			self.assertFalse(work.ex_7(a,a))
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_8(self):
		s = ["asdfasdf",
			"helloworld",
			"a",
			""]
		try:
			for i in range(4):
				self.assertEqual(list(s[i]), work.ex_8(s[i]))
			
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_9(self):
		s = ["the quick brown fox jumps over the lazy dog",
				"mary had a little lamb",
				"ahsan is a master programmer",
				"the rain in spain stays mainly in the plains"]
		a = [[1, 1, 1, 1, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1],
		 		[4, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0],
				[5, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 0, 3, 1, 1, 1, 0, 4, 3, 1, 0, 0, 0, 0, 0, 0],
				[5, 0, 0, 0, 2, 0, 0, 2, 6, 0, 0, 2, 1, 6, 0, 2, 0, 1, 4, 3, 0, 0, 0, 0, 2, 0]]
		try:
			for i in range(4):
				self.assertEqual(work.ex_9(s[i], a[i]))

		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_10(self):
		s = ["the quick brown fox jumps over the lazy dog",
				"mary had a little lamb",
				"ahsan is a master programmer",
				"the rain in spain stays mainly in the plains"]
		try:
			self.assertTrue(work.ex_10(s[1], s[0]))
			self.assertTrue(work.ex_10(s[2], s[1]))
			self.assertFalse(work.ex_10(s[2], s[3]))
			self.assertFalse(work.ex_10(s[0], s[2]))
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_11(self):
		s = ["the quick brown fox jumps over the lazy dog",
				"mary had a little lamb",
				"ahsan is a master programmer",
				"the rain in spain stays mainly in the plains"]
		a = [3,4,5,3]
		try:
			for i in range(4):
				self.assertEqual(work.ex_11(s[i]), a[i])
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_12(self):
		s = ["the quick brown fox jumps over the lazy dog",
				"mary had a little lamb",
				"ahsan is a master programmer",
				"the rain in spain stays mainly in the plains"]
		try:
			for i in range(4):
				self.assertEqual(work.ex_12(s[i]), s[i][::-1])
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_13(self):
		s = ["the quick brown fox jumps over the lazy dog",
				"mary had a little lamb",
				"ahsan is a master programmer",
				"the rain in spain stays mainly in the plains"]
		a = [s[0][:int(len(s[0])/2)] + s[1][int(len(s[1])):],
			 s[1][:int(len(s[1])/2)] + s[2][int(len(s[2])):],
			 s[2][:int(len(s[2])/2)] + s[3][int(len(s[3])):]
		]
		try:
			for i in range(3):
				self.assertEqual(work.ex_12(s[i], s[i+1]), a[i])


		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")
		
	def test_ex_14(self):
		s = ["asdfasdfasdfasdfasdfasdf",
				"bgbgbgbgbgbgbgbgbgbgbg",
				"rtrtrtrtrttrtrtrtrtrtrt",
				"popospospospos"]
		a = [s[0][::2] + s[1][::2] + s[2][::2],
			 s[1][::2] + s[2][::2] + s[3][::2],
			 s[2][::2] + s[3][::2] + s[0][::2]]
		try:
			for i in range(3):
				self.assertEqual(work.ex_12(s[i], s[i+1]), a[i])


		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")
		

	def test_ex_15(self):
		try:
			self.assertTrue(19, 3, 37, 4)
			self.assertFalse(19, 3, 24, 6)
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_16(self):
		a = [i for i in range(1,100,2)]
		try:
			self.assertEqual(a, work.ex_16())
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")

	def test_ex_17(self):
		a = [i for i in range(3, 60,3)]
		try:
			self.assertEqual(a, work.ex_17())
		except NotImplementedError:
			raise NotImplementedError("Not answered yet.")