import itertools as it
import time
from collections import namedtuple

from school_data import get_schools_data


class _SchoolSearch(namedtuple("SchoolSearch", ["school", "similitude_index"])):
    __slots__ = ()

    def __le__(self, other):
        return self.similitude_index <= other.similitude_index

    def __lt__(self, other):
        return self.similitude_index < other.similitude_index

    def __gt__(self, other):
        return self.similitude_index > other.similitude_index


def _search(schools, search_plain_text):
    def __sort_similitud_index_key(custom):
        return custom.similitude_index

    def __key_fun(x):
        return (x["SCHNAM05"], x["LCITY05"], x["LSTATE05"])

    grouped_data = it.groupby(
        sorted(schools, key=__key_fun),
        key=__key_fun,
    )

    grouped_data_school = tuple(
        _SchoolSearch(
            key,
            len(
                set(" ".join(key).lower().split(" ")).intersection(
                    set(search_plain_text.lower().split(" "))
                )
            ),
        )
        for key, rows in grouped_data
    )

    sorted_data_school = sorted(
        grouped_data_school, key=__sort_similitud_index_key, reverse=True
    )

    search_results = sorted_data_school[:3]

    return search_results


def search_schools(search_plain_text):
    start_time = time.time()
    schools = tuple(get_schools_data())
    search_results = _search(schools, search_plain_text.lower())
    print("--- %s seconds ---" % (time.time() - start_time))

    print("1.", search_results[0].school[0])
    print(search_results[0].school[1], ", ", search_results[0].school[2])

    print("2.", search_results[1].school[0])
    print(search_results[1].school[1], ", ", search_results[1].school[2])

    print("3.", search_results[2].school[0])
    print(search_results[2].school[1], ", ", search_results[2].school[2])
