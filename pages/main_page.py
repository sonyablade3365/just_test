import re

from playwright.sync_api import Page
from pages.base_page import BasePage
from components.sidebar_component import SideComponent

class MainPage(BasePage):
    """Клас Главной страницы"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.sidebar = SideComponent(page)