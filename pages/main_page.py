import re

from playwright.sync_api import Page


from pages.base_page import BasePage

class MainPage(BasePage):
    """Клас Главной страницы"""
    def __init__(self, page: Page):
        super().__init__(page)
