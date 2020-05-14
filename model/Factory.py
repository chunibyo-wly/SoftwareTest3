from model.Plan import PlanA, PlanB
from model.Baggage import Baggage


def get_plan(country, ship, price, baggage, area):
    if country == 1:
        return PlanA(ship, price, baggage)
    elif country == 2:
        return PlanB(ship, price, baggage, area)
