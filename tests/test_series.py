from math_series.series import fibonacci ,locus ,sum_series


def test_one():
    actual = fibonacci(4)
    exepcted=3
    assert actual==exepcted


def test_five():
    actual = fibonacci(5)
    exepcted=5
    assert actual==exepcted

    
def test_eight():
    actual = fibonacci(8)
    exepcted=21
    assert actual==exepcted

def test_seven():
    actual = fibonacci(7)
    exepcted=13
    assert actual==exepcted

def test_zero():
    actual = fibonacci(0)
    exepcted=0
    assert actual==exepcted

def test_one():
    actual = fibonacci(1)
    exepcted=1
    assert actual==exepcted

def  test_zerolocus():
    actual = locus(0)
    exepcted=2
    assert actual==exepcted

def test_onelocus():
    actual = locus(1)
    exepcted=1
    assert actual==exepcted

def test_fivelocus():
    actual = locus(5)
    exepcted=11
    assert actual==exepcted

def test_eightlocus():
    actual = locus(7)
    exepcted=29
    assert actual==exepcted

def test_Sum7():
    actual = sum_series(7,2,3)
    exepcted=55
    assert actual==exepcted

def test_sum5():
    actual = sum_series(5,2,3)
    exepcted=21
    assert actual==exepcted

def test_sum3():
    actual = sum_series(3,2,3)
    exepcted=8
    assert actual==exepcted
 






