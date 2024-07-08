def inc(x):
    return x + 1


def test_answer_wrong():
    assert inc(3) == 5

def test_answer_wright():
    assert inc(3) == 4
    
@pytest.mark.regression
def test_in_regression()
    assert true