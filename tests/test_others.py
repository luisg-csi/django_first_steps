def test_always_passes():
    assert True

def test_always_fails():
    assert False

#nuevas funciones a testear
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }

# content of test_sample
def inc(x):
    return x + 1


def test__fail_answer():
    assert inc(3) == 5

def test__true_answer():
    assert inc(inc(3)) == 5    