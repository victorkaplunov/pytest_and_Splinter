import pytest
from splinter import Browser


@pytest.fixture(scope="module")
def browser():
    global browser
    browser = Browser('firefox')
    return browser


@pytest.fixture(scope="module")
def base_url():
    """Base URL"""
    base_url = "https://yandex.ru/"
    return base_url


@pytest.fixture(scope="module")
def open_start_page(browser, base_url):
    """Open yandex.ru"""
    browser.visit(base_url)
    return browser


@pytest.fixture(scope="module")
def open_translate_page(open_start_page):
    """Open translate.yandex.ru"""
    link = browser.find_link_by_partial_href('translate').first
    link.click()
    return browser


@pytest.fixture(scope="module")
def get_translation(open_translate_page):
    """Get text from translation field"""
    swap_button = browser.find_by_css('div.button.button_icon.button_icon_swap')
    swap_button.click()
    browser.find_by_id('textarea').fill("test")
    translation = browser.is_text_present('испытание', wait_time=10)
    browser.quit()
    return translation

