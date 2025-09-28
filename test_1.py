import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
import allure

# with sync_playwright() as p:
#     browser = p.chromium.launch_persistent_context(user_data_dir= r"C:\Users\User\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb", headless=False)
#     page = browser.new_page()


class TestRegistration:
    @allure.title("Main page")
    def test_has_title(self, page: MainPage):
        page.goto("https://news.sportbox.ru/")
        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Новости спорта, Спортивная аналитика, Видео"))
    
    def test_has_sidebar_on_main_page(self, main_page: MainPage):
        """Проверяет наличие бокового меню на главной"""
        main_page.visit("https://news.sportbox.ru/")
        main_page.sidebar.check_visible_by_id(main_page.sidebar.locator_id)

    def test_get_sing_button(self, page: Page):
        page.goto("https://news.sportbox.ru/")
        # Click the get started link.
        page.locator("#enter_link").click()
        expect(page).to_have_title(re.compile("Авторизация"))

    def test_get_open_result(self, page: Page):
        page.goto("https://news.sportbox.ru/")
        # Click the get started link.
        page.get_by_role("link", name="Все", exact=True).click()
        expect(page).to_have_url(re.compile("https://news.sportbox.ru/stats"))

    def test_open_main_page(self, main_page : MainPage):
        main_page.visit("https://news.sportbox.ru/")
        main_page.check_current_url(re.compile("https://news.sportbox.ru/"))