from unittest import TestCase
from model.Baggage import Baggage
from model.Factory import get_plan
from model.Plan import PlanA, PlanB
import yaml


class TestData:
    _data = None

    def __new__(cls, *args, **kwargs):
        if not cls._data:
            with open('test/test_data.yaml', 'r') as f:
                cls._data = yaml.load(f, Loader=yaml.FullLoader)
        return cls._data['test_data']


class TestPlan(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.bl = [
            Baggage(1, 1, 1, 1),
            Baggage(1, 1, 1, 10),
            Baggage(1, 1, 1, 20),
            Baggage(1, 1, 1, 30),
            Baggage(1, 1, 1, 40)
        ]
        self.test_data = TestData()

    def tearDown(self) -> None:
        super().tearDown()

    def test_get_plan(self):
        self.assertIsInstance(get_plan(1, 1, 1000, [
            self.bl[2],
            self.bl[2]
        ], 1), PlanA)

        for i in range(len(self.test_data)):
            baggage = []
            for j in self.test_data[i]['baggage']:
                baggage.append(Baggage(
                    j['length'], j['width'], j['height'], j['weight']
                ))
            self.assertEqual(
                get_plan(
                    self.test_data[i]['country'],
                    self.test_data[i]['ship'],
                    self.test_data[i]['price'],
                    baggage,
                    self.test_data[i]['area']
                ).get_all_price()[2],
                self.test_data[i]['answer']
            )
