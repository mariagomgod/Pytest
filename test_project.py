import pytest

results_add = [
(2,2,4),
(2,0,2),
(2,-1,1)
]

results_subtract = [
(2,2,0),
(2,0,2),
(2,-1,3)
]

@pytest.mark.parametrize("a,b,expected", results_add)
def test_add(a,b,expected):
    import project

    # probar suma básica
    assert project.add(a,b) == expected


@pytest.mark.parametrize("a,b,expected", results_subtract)
def test_subtract(a,b,expected):
    import project

    # probar resta básica
    assert project.subtract(a,b) == expected


