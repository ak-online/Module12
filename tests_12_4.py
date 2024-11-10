import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def test_walk(self):
        try:
            walker = Runner('Ivanov', -10)
            for _ in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError as err:
            logging.error('Ошибка', exc_info=True)
            logging.warning(f"Неверная скорость для Runner - {err}")


    def test_run(self):
        try:
            runtester = Runner(25)
            for _ in range(10):
                runtester.run()
            self.assertEqual(runtester.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except TypeError as err:
            logging.error('Ошибка', exc_info=True)
            logging.warning(f"Неверный тип данных для объекта Runner - {err}")


    def test_challenge(self):
        walker = Runner('Ivanov')
        runtester = Runner('Petrov')
        for _ in range(10):
            walker.walk()
            runtester.run()
        self.assertNotEqual(walker.distance, runtester.distance)
        logging.info('"test_challenge" выполнен успешно!')


# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
# t = Tournament(101, first, second)
# print(t.start())

if __name__ == "__main__":
    unittest.main()