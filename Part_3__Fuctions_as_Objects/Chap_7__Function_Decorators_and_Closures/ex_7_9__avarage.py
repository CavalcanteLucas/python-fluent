from ex_7_8__avarage_oo import Avarage


def make_avarager():
    series = []

    def avarager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return avarager
