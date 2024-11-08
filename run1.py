# Домашнее задание по теме "Простые Юнит-Тесты"

import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def skip_it(func):
        def wrapper(self, *args, **kwargs):
            if getattr(self, 'is_frozen', False):
                self.skipTest("Тесты в этом кейсе заморожены")
            return func(self, *args, **kwargs)
        return wrapper

    @skip_it
    def test_walk(self):
        run_1 = Runner('Usein')
        for _ in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    @skip_it
    def test_run(self):
        run_2 = Runner('Nick')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    @skip_it
    def test_challenge(self):
        run_1 = Runner('Usein')
        run_2 = Runner('Nick')
        for _ in range(10):
            run_1.walk()
            run_2.run()
        self.assertNotEqual(run_1.distance, run_2.distance)


if __name__ == '__main__':
    unittest.main()