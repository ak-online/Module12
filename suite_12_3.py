# Д/З "Систематизация и пропуск тестов".

import run1
import unittest
import module_12_2 as md


mysuite = unittest.TestSuite()
mysuite.addTest(unittest.TestLoader().loadTestsFromTestCase(run1.RunnerTest))
mysuite.addTest(unittest.TestLoader().loadTestsFromTestCase(md.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(mysuite)