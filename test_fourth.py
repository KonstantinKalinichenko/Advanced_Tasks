from Fourth_Task import encode_string

def test_fourth_task():
    assert encode_string('абвгде 1') == 'бвгдеё'

    assert encode_string('это яблоко красное 7') == 'дщх ёзтхсх счжшфхл'