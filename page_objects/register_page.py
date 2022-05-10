from page_objects import support_functions

register_button = 'mlb2-3239800'
url = 'https://fabrykatestow.pl/ciekawostki/'


def submit_register_to_newsletter_button_visible(driver_instance):
    support_functions.wait_for_visibility_of_element(driver_instance, register_button)
    elem = driver_instance.find_element_by_id(register_button)
    return elem.is_displayed()