from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input_selector = ("input[placeholder='Search your Address, City or Zip Code']")

    def load_and_consent(self):
        self.page.goto("https://www.accuweather.com/", wait_until="domcontentloaded")
        if self.page.is_visible(".fc-consent-root", timeout=3000):
            self.page.locator("button.fc-cta-consent.fc-primary-button").click()

    def search_city(self, city_name: str):
        self.page.locator(self.search_input_selector).press_sequentially(city_name)
        self.page.wait_for_selector(".results-container")

    def click_search_bar(self):
        self.page.click(self.search_input_selector)

    def click_first_result(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(".search-bar-result__name")

    def click_first_recent_result(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(".featured-locations__locations")

    def click_hamburger_button(self):
        self.page.click(".hamburger-button > use")

    def click_settings_button(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.get_by_role("link", name="settings").click()

    def click_back_button(self):
        self.page.go_back()

    def change_c_to_f(self):
        self.page.select_option("#unit.settings-card__setting__select", value="F")

    def check_if_weather_unit_is_f(self):
        if self.page.locator("recent-location-temp-unit") == "F":
            return True

    def results_list_is_visible(self):
        self.page.is_visible(".featured-locations")

    def location_label_is_visible(self):
        self.page.is_visible(".search-bar-result current-location-result")

    def settings_page_is_visible(self):
        self.page.is_visible("header-menu")

    def get_page_header(self):
        return self.page.inner_text(".header-loc")
