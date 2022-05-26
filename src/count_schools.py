import itertools as it
from collections import namedtuple
from typing import Tuple

from school_data import get_schools_data


def _get_group_by_data(schools, column_name):
    def __key_fun(x):
        return x[column_name]

    grouped_data = it.groupby(sorted(schools, key=__key_fun), key=__key_fun)
    return grouped_data


def _total_schools(schools: Tuple[str, str]) -> None:
    print(f"Total Schools: {len(schools)}")


def _schools_by_state(schools: Tuple) -> None:
    grouped_data = _get_group_by_data(schools, "LSTATE05")
    print("Schools by State:")
    for key, rows in grouped_data:
        print(key, ": ", sum(1 for r in rows))


def _schools_by_metro_centric_locale(schools: Tuple) -> None:
    grouped_data = _get_group_by_data(schools, "MLOCALE")
    print("Schools by Metro-centric locale:")
    for key, rows in grouped_data:
        print(key, ": ", sum(1 for r in rows))


def _schools_by_city(schools: Tuple) -> None:
    class __School(namedtuple("School", ["city", "total"])):
        __slots__ = ()

        def __le__(self, other):
            return self.total <= other.total

        def __lt__(self, other):
            return self.total < other.total

        def __gt__(self, other):
            return self.total > other.total

    def __get_city_with_most_schools(data_school):
        city_most_school = __School(None, 0)
        for school in data_school:
            city_most_school = max(school, city_most_school)
        return city_most_school

    def __get_cities_with_at_least_one_school(data_school):
        city_with_at_least_one_school = __School(None, 1)
        cities = tuple(
            it.filterfalse(lambda p: p <= city_with_at_least_one_school, data_school)
        )
        return cities

    grouped_data = _get_group_by_data(schools, "LCITY05")

    grouped_data_school = tuple(
        __School(key, sum(1 for r in rows)) for key, rows in grouped_data
    )

    city_with_most_schools = __get_city_with_most_schools(grouped_data_school)

    cities_with_at_least_one_school = __get_cities_with_at_least_one_school(
        grouped_data_school
    )

    print(
        f"City with most schools: {city_with_most_schools.city} ({city_with_most_schools.total} schools)"
    )
    print(
        f"Unique cities with at least one school: {len(cities_with_at_least_one_school)}"
    )


def print_counts():
    schools = tuple(get_schools_data())
    _total_schools(schools)
    _schools_by_state(schools)
    _schools_by_metro_centric_locale(schools)
    _schools_by_city(schools)
