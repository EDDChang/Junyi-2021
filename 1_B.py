import unittest
class SentenceReverser:
    def reverse(self, s):
        ret = ""
        for i, c in enumerate(s):
            ret = c + ret
        return ret
    def reverse_sentence(self, s):
        ret = ''
        s = s.split(' ')
        for i, word in enumerate(s):
            ret += self.reverse(word)
            if i < len(s)-1:
                ret += ' '
        return ret
class StringReverserTest(unittest.TestCase):
    
    def test_example_testcase(self):
        SR = SentenceReverser()
        self.assertEqual(SR.reverse_sentence("flipped class room is important"), "deppilf ssalc moor si tnatropmi")
    
    def test_my_testcase0(self):
        SR = SentenceReverser()
        self.assertEqual(SR.reverse_sentence(""), "")

    def test_my_testcase1(self):
        SR = SentenceReverser()
        self.assertEqual(SR.reverse_sentence("hi i am edward"), "ih i ma drawde")

    def test_my_testcase2(self):
        SR = SentenceReverser()
        self.assertEqual(SR.reverse_sentence("dogecoin so crazy"), "niocegod os yzarc")

if __name__ == '__main__':
	unittest.main()

