import unittest
import runner2 as runner

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def tearDown(self):
        for key in self.all_results:
            print(key, self.all_results[key])


    def setUp(self):
        self.run1 = runner.Runner("Усейн", 10)
        self.run2 = runner.Runner("Андрей", 9)
        self.run3 = runner.Runner("Ник", 3)

    def test1_us_nick(self):
        tur1 = runner.Tournament(90, self.run1, self.run3)
        self.all_results = tur1.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Ник")


    def test2_and_nick(self):
        self.tur2 = runner.Tournament(90, self.run2, self.run3)
        self.all_results = self.tur2.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Ник")


    def test3_us_and_nick(self):
        self.tur3 = runner.Tournament(90, self.run1, self.run2, self.run3)
        self.all_results = self.tur3.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Ник")


if __name__ == "__main__":
    unittest.main()
