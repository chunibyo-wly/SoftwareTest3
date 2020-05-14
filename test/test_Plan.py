from unittest import TestCase
from model.Plan import PlanA, PlanB
from model.Baggage import Baggage


class TestPlanA(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.bl = [
            Baggage(1, 1, 1, 1),
            Baggage(1, 1, 1, 10),
            Baggage(1, 1, 1, 20),
            Baggage(1, 1, 1, 30),
            Baggage(1, 1, 1, 40)
        ]

    def tearDown(self) -> None:
        super().tearDown()

    def test_get_all_price(self):
        self.assertEqual(PlanA(1, 1000, [
            self.bl[2],
            self.bl[2]
        ]).get_all_price(), (1000, 0, 1000))

        self.assertEqual(PlanA(1, 1000, [
            self.bl[3],
            self.bl[3]
        ]).get_all_price(), (1000, 300, 1300))


class TestPlanB(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.bl = [
            Baggage(1, 1, 1, 1),
            Baggage(1, 1, 1, 10),
            Baggage(1, 1, 1, 20),
            Baggage(1, 1, 1, 30),
            Baggage(1, 1, 1, 40)
        ]

    def tearDown(self) -> None:
        super().tearDown()

    def test_get_all_price(self):
        self.assertEqual(PlanB(1, 1000, [
            self.bl[2],
            self.bl[2]
        ], 1).get_all_price(), (1000, 0, 1000))

        self.assertEqual(PlanB(1, 1000, [
            self.bl[3],
            self.bl[3]
        ], 2).get_all_price(), (1000, 1380, 2380))
