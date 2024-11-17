import pytest
from sigma.Bmi import calculate_bmi

def test_bmi_normal_weight():
    result= calculate_bmi(1.73,65)
    assert(result==0)

def test_bmi_under_weight():
    result = calculate_bmi(1.73,50)
    assert(result==-1)

def test_bmi_over_weight():
    result = calculate_bmi(1.73,80)
    assert(result==1)