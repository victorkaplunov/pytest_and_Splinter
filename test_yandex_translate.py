class TestClass(object):

    def test_start_page(self, open_start_page):
        """Start page is open"""
        assert open_start_page.title == 'Яндекс'

    def test_translate(self, open_translate_page):
        """Translate page is open"""
        assert open_translate_page.title.find("Яндекс.Переводчик") == 0

    def test_translation(self, get_translation):
        """Translate is correct"""
        assert get_translation
