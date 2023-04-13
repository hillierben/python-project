from project import name_split, check_email, check_number
import pytest

def test_name():
    assert name_split("Ben Hillier") == ['Ben', 'Hillier']
    with pytest.raises(SystemExit):
        name_split("Ben")


def test_email():
    assert check_email("hillierben@gmail.com") == "hillierben@gmail.com"
    with pytest.raises(SystemExit):
        check_email("hillier@")


def test_number():
    assert check_number("07982638828") == "07982638828"
    with pytest.raises(SystemExit):
        check_number("0123321")
    with pytest.raises(SystemExit):
        check_number("12345678912")





