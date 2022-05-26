from school_search import search_schools


def test_search_schools(capsys):
    search_schools("elementary school highland park")
    captured = capsys.readouterr()

    assert (
        captured.out
        == """'1. HIGHLAND PARK ELEMENTARY SCHOOL\n'\n 'MUSCLE SHOALS ,  AL\n'\n '2. HIGHLAND PARK ELEMENTARY SCHOOL\n'\n 'PUEBLO ,  CO\n'\n '3. ABESS PARK ELEMENTARY SCHOOL\n'\n 'JACKSONVILLE ,  FL\n') == ('1. HIGHLAND PARK ELEMENTARY SCHOOL\n'\n 'MUSCLE SHOALS ,  AL\n'\n '2. HIGHLAND PARK ELEMENTARY SCHOOL\n'\n 'PUEBLO ,  CO\n'\n '3. ABESS PARK ELEMENTARY SCHOOL\n'\n 'JACKSONVILLE ,  FL'"""
    )
