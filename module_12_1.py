import unittest
import runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = runner.Runner('Ivanov')
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runtester = runner.Runner('Petrov')
        for _ in range(10):
            runtester.run()
        self.assertEqual(runtester.distance, 100)

    def test_challenge(self):
        walker = runner.Runner('Ivanov')
        runtester = runner.Runner('Petrov')
        for _ in range(10):
            walker.walk()
            runtester.run()
        self.assertNotEqual(walker.distance, runtester.distance)


if __name__ == "__main__":
    unittest.main()
