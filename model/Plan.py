import yaml

import sys
from os.path import abspath, join, dirname


class Rule:
    _rule = None

    def __new__(cls, *args, **kwargs):
        if not cls._rule:
            with open('model/rule.yaml', 'r') as f:
                cls._rule = yaml.load(f, Loader=yaml.FullLoader)
        return cls._rule['area_rule']


class Plan:
    def __init__(self, ship_class, price, baggage, area=None):
        self._ship_class = ship_class
        self._price = price
        self._baggage = baggage
        self._area = area


class PlanA(Plan):
    def __init__(self, ship_class, price, baggage):
        super().__init__(ship_class, price, baggage)

    def get_all_price(self):
        sum_weight = 0
        max_weight = 0

        for i in self._baggage:
            sum_weight += i.weight

        if self._ship_class == 1:
            max_weight = 40
        elif self._ship_class == 2:
            max_weight = 30
        elif self._ship_class == 3:
            max_weight = 20
        baggage_price = max(0, (sum_weight - max_weight) * 0.015 * self._price)

        return self._price, baggage_price, self._price + baggage_price


def _sort_key(data):
    return data.sum


class PlanB(Plan):
    def __init__(self, ship_class, price, baggage, area):
        super().__init__(ship_class, price, baggage, area)
        self._baggage.sort(key=_sort_key)

    def _get_extra_number(self, max_number=None):
        if not max_number:
            max_number = Rule()[self._area - 1]['max_number']

        number_a = len([i.weight < 23 for i in self._baggage])
        number_b = len(self._baggage) - len([i.weight < 23 for i in self._baggage])
        extra_number = number_a + number_b - max_number

        if extra_number <= 0:
            return 0
        elif extra_number == 1:
            return Rule()[self._area - 1]['extra'][0]
        elif extra_number == 2:
            return Rule()[self._area - 1]['extra'][0] + \
                   Rule()[self._area - 1]['extra'][1]
        else:
            return Rule()[self._area - 1]['extra'][0] + \
                   Rule()[self._area - 1]['extra'][1] + \
                   Rule()[self._area - 1]['extra'][2] * (extra_number - 2)

    def _get_extra_weight_size(self):

        def check_weight(b):
            if b.weight > Rule()[self._area - 1]['weight'][1]:
                return 2
            elif b.weight > Rule()[self._area - 1]['weight'][0]:
                return 1
            else:
                return 0

        def check_size(b):
            return b.sum > Rule()[self._area - 1]['size'][0]

        tmp = 0
        for i in self._baggage:
            if check_weight(i) and check_size(i):
                tmp += Rule()[self._area - 1]['level'][3]
            elif check_weight(i) == 2:
                tmp += Rule()[self._area - 1]['level'][1]
            elif check_weight(i) == 1:
                tmp += Rule()[self._area - 1]['level'][0]
            elif check_size(i):
                tmp += Rule()[self._area - 1]['level'][2]
        return tmp

    def get_all_price(self):
        if self._ship_class == 1:
            baggage_price = self._get_extra_number(2) + self._get_extra_weight_size()
        else:
            baggage_price = self._get_extra_number() + self._get_extra_weight_size()
        # print(self._get_extra_number(2), self._get_extra_weight_size())
        return self._price, baggage_price, self._price + baggage_price
