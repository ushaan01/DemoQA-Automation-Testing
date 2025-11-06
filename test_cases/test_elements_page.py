import pytest
from base_pages.elements_page import ElementsPage
from utilities.read_excel import get_data


@pytest.mark.parametrize("name,email,current,permanent",get_data("Elements"))
def test_text_box(setup,name,email,current,permanent):
    driver=setup
    page=ElementsPage(driver)
    page.open_text_box()
    page.fill_text_box(name, email, current, permanent)
    output =page.get_output()
    assert name in output
    assert email in output
