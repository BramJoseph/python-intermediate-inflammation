"""Tests for the Patient model."""


from inflammation.models import Patient

import numpy.testing as npt

def test_create_patient():

    name = 'Alice'
    weight = 50
    height = 1.8
    
    p = Patient(name = name, weight = weight, height = height)

    assert p.name == name
    assert p.weight == weight
    assert p.height == height


def test_compute_patient_bmi():
    
    name = 'Maria'
    weight = 60
    height = 1.6

    Maria = Patient(name = name, weight = weight, height = height)
    expected_bmi = 23.4375
    bmi = Maria.get_body_mass_index() 
    
    npt.assert_almost_equal(bmi, expected_bmi)





