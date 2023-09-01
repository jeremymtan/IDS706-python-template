# taken from https://pytest.org/en/7.4.x/getting-started.html#run-multiple-tests
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
