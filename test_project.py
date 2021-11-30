def test_add():
    import project

    # probar suma básica
    assert project.add(2, 2) == 4

    # probar suma con cero
    assert project.add(2, 0) == 2

def test_subtract():
    import project

    # probar resta básica
    assert project.subtract(2, 2) == 0

    # probar resta con cero
    assert project.subtract(2, 0) == 2
