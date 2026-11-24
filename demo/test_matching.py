import unittest
from matching import Opportunity, screen

class MatchingTests(unittest.TestCase):
    def test_match(self):
        self.assertEqual(screen("Masters","Engineering",Opportunity("A","masters","engineering")), "potential match")
    def test_unknown(self):
        self.assertEqual(screen("masters","engineering",Opportunity("A",None,"engineering")), "needs review")
    def test_mismatch_over_unknown(self):
        self.assertEqual(screen("masters","engineering",Opportunity("A",None,"history")), "criteria mismatch")
    def test_missing_profile(self):
        with self.assertRaises(ValueError):
            screen("","engineering",Opportunity("A",None,None))

if __name__ == "__main__":
    unittest.main()
