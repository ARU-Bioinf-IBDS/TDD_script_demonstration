from complement import complement


def test_a():
    assert complement('A') == 'T'


def test_t():
    assert complement('T') == 'A'


def test_g():
    assert complement('G') == 'C'


def test_c():
    assert complement('C') == 'G'


def test_atgc():
    assert complement('ATGC') == 'TACG'


def test_given_example():
    assert complement('CAATTTGGGG') == 'GTTAAACCCC'
