import unittest

from metta import run_metta

class MeTTaTest(unittest.TestCase):

    def test_run_metta(self):
        # REM: this is the initial implementation, which can be
        #      moved to MeTTa class later or changed
        program = '''
            (isa red color)
            (isa green color)
            (isa blue color)
            ;(isa comment color)
            !(match &self (isa $color color) $color)

            (= (f) (+ 2 3))
            !(f)
        '''

        result = run_metta(program)
        self.assertEqual('[[red, green, blue], [5]]', repr(result))

    def test_run_complex_query(self):
        program = '''
            (A B)
            (C B)

            !(match &self (, (A $x) (C $x)) $x)
        '''

        result = run_metta(program)
        self.assertEqual('[[B]]', repr(result))

