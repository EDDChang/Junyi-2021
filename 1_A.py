import unittest
class StringReverser:
    def reverse(self, s):
        ret = ""
        for i, c in enumerate(s):
            ret = c + ret
        return ret
class StringReverserTest(unittest.TestCase):
    
    def test_example_testcase(self):
        SR = StringReverser()
        self.assertEqual(SR.reverse("junyiacademy"), "ymedacaiynuj")
    
    def test_my_testcase0(self):
        SR = StringReverser()
        self.assertEqual(SR.reverse("abc"), "cba")

    def test_my_testcase1(self):
        SR = StringReverser()
        self.assertEqual(SR.reverse(""), "")

    def test_my_testcase2(self):
        SR = StringReverser()
        self.assertEqual(SR.reverse("happy"), "yppah")

if __name__ == '__main__':
	unittest.main()
