import unittest
import random
from search import nfind, kmpfind, karp_rabin_search, Rabin_Karp_Matcher, KR_find


class TestStringSearchAlgorithms(unittest.TestCase):

    def test_naive_search(self):
        self.assertEqual(nfind("", ""), [0])
        self.assertEqual(nfind("pattern", ""), [])
        self.assertEqual(nfind("", "text"), [])
        self.assertEqual(nfind("pattern", "pattern"), [0])
        self.assertEqual(nfind("pattern", "text"), [])
        self.assertEqual(nfind("a", "aaa"), [0, 1, 2])

    def test_kmp_search(self):
        self.assertEqual(kmpfind("", ""), [0])
        self.assertEqual(kmpfind("pattern", ""), [])
        self.assertEqual(kmpfind("", "text"), [])
        self.assertEqual(kmpfind("pattern", "pattern"), [0])
        self.assertEqual(kmpfind("pattern", "text"), [])
        self.assertEqual(kmpfind("a", "aaa"), [0, 1, 2])

    def test_karp_rabin_search(self):
        self.assertEqual(karp_rabin_search("", ""), [0])
        self.assertEqual(karp_rabin_search("pattern", ""), [])
        self.assertEqual(karp_rabin_search("", "text"), [])
        self.assertEqual(karp_rabin_search("pattern", "pattern"), [0])
        self.assertEqual(karp_rabin_search("pattern", "text"), [])
        self.assertEqual(karp_rabin_search("a", "aaa"), [0, 1, 2])

    def test_2_karp_rabin_2(self):
        self.assertEqual(Rabin_Karp_Matcher("", ""), [0])
        self.assertEqual(Rabin_Karp_Matcher("pattern", ""), [])
        self.assertEqual(Rabin_Karp_Matcher("", "text"), [])
        self.assertEqual(Rabin_Karp_Matcher("pattern", "pattern"), [0])
        self.assertEqual(Rabin_Karp_Matcher("pattern", "text"), [])
        self.assertEqual(Rabin_Karp_Matcher("a", "aaa"), [0, 1, 2])

    def test_2_karp_rabin_3(self):
        self.assertEqual(KR_find("", ""), [0])
        self.assertEqual(KR_find("pattern", ""), [])
        self.assertEqual(KR_find("", "text"), [])
        self.assertEqual(KR_find("pattern", "pattern"), [0])
        self.assertEqual(KR_find("pattern", "text"), [])
        self.assertEqual(KR_find("a", "aaa"), [0, 1, 2])

    def test_random_search(self):
        alphabet = "ab"
        random.seed(42)  # Setting seed for reproducibility
        for _ in range(10):
            pattern = ''.join(random.choice(alphabet) for _ in range(random.randint(1, 10)))
            text = ''.join(random.choice(alphabet) for _ in range(random.randint(1, 20)))
            self.assertEqual(nfind(pattern, text), kmpfind(pattern, text))
            self.assertEqual(nfind(pattern, text), karp_rabin_search(pattern, text))
            self.assertEqual(nfind(pattern, text), Rabin_Karp_Matcher(pattern, text))
            self.assertEqual(nfind(pattern, text), KR_find(pattern, text))


if __name__ == '__main__':
    unittest.main()
