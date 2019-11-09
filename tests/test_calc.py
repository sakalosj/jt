import pytest

from calc import Calc


@pytest.mark.parametrize('a, b, expected', [pytest.param(1, 2, 3, id='two_int'),
                             pytest.param(1.14, 2, 3.14, id='float, int')])
def test_calc_add(a, b, expected):
    calc = Calc()
    assert expected == calc.add(a,b)
