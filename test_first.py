from First_Task import process_number

def test_first_task():
    assert process_number('13133') == '33'

    assert process_number('99999') == 'Превышено'

    assert process_number('99') == '36'
