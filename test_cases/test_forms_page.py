from base_pages.forms_page import FormsPage

def test_form_page(setup):
    driver= setup
    page=FormsPage(driver)
    page.open_form()
    page.fill_form("USHA","NAZARE","ushanazare2@gmail.com","8390767975")