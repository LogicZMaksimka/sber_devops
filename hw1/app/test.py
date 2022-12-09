from app import home

def test_main_page():
    assert home() == "Cacti with spike length >= 3: [('rebutia', 'senilis', 3), ('rebutia', 'albiflora', 3), ('echinopsis', 'amblayensis', 3), ('echinopsis', 'albispinosa', 4), ('mammillaria', 'bocasana', 4)]"

def test_nothing():
    assert True
