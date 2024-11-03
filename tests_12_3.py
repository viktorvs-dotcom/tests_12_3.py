import unittest
import tests_12_1, tests_12_2


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        walk1 = tests_12_1.runner.Runner('First')
        for i in range(10):
            walk1.walk()
        self.assertEqual(walk1.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        walk2 = tests_12_1.runner.Runner('Second')
        for j in range(10):
            walk2.run()
        self.assertEqual(walk2.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        walk3 = tests_12_1.runner.Runner('Third')
        walk4 = tests_12_1.runner.Runner('Fourth')
        for k in range(10):
            walk3.run()
            walk4.walk()
        self.assertNotEqual(walk3.distance, walk4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = tests_12_2.runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = tests_12_2.runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = tests_12_2.runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        first_rase = tests_12_2.runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        res = first_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        second_rase = tests_12_2.runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        res = second_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        third_rase = tests_12_2.runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        res = third_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res
