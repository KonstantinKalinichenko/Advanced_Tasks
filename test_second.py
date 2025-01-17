from Second_Task import Item, generate_product_report


def test_second_task():
    assert (generate_product_report(
        '2023-01-15:Книга:10;2023-01-20:Флешка:5;2023-02-05:Книга:8')
            == ['Книга: - 2023-01-15: 10 - 2023-02-05: 8', 'Флешка: - 2023-01-20: 5'])

    assert (generate_product_report(
        '2023-03-10:Карандаш:7;2023-04-01:Ручка:6;2023-04-15:Тетрадь:8;2023-04-15:Тетрадь:10')
            == ['Карандаш: - 2023-03-10: 7', 'Ручка: - 2023-04-01: 6', 'Тетрадь: - 2023-04-15: 18'])