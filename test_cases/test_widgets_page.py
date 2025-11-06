from base_pages.widgets_page import WidgetsPage
from conftest import driver


def test_slider(setup):
    driver=setup
    page=WidgetsPage(driver)
    page.open_slider()
    page.move_slider(20)
    value=page.get_value()
    assert value.isdigit()
