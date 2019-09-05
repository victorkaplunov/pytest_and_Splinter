import pytest
from splinter import Browser


@pytest.fixture(scope="module")
def browser():
    global browser
    browser = Browser('firefox', headless=True)
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
    """Paste word 'test' into origin field and get text from translation field"""
    swap_button = browser.find_by_css('div.button.button_icon.button_icon_swap')
    swap_button.click()
    browser.find_by_id('textarea').fill("test")
    translation = browser.is_text_present('испытание', wait_time=10)
    browser.quit()
    return translation

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """Настройка генератора отчетов pytest_html. Добавляет заголовок в отчет для колонок с
    описанием теста (docstring) и временем."""
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    """Настройка генератора отчетов pytest_html. Добавялет колонки с описанием теста (docstring)  и временем в отчет."""
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.now(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """Настройка генератора отчетов pytest_html. Добавялет описание теста (docstring)."""
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
