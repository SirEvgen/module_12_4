import logging
import unittest
from runner_and_tournament import Runner
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        format="%(asctime)s | %(levelname)s | %(message)s", encoding='utf-8')
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('2222', -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.error(exc)
            logging.exception("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            self.runner = Runner(333, 5)
            self.runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc:
            logging.error(exc)
            logging.error("Неверный тип данных для объекта Runner", exc_info=True)





if __name__ == "__main__":
    unittest.main()