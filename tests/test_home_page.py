import allure
import pytest
from locators.home_page_locators import TestHomePageLocators
from data_tests import expected_texts, DZEN_URL, BASE_URL


class TestHomePageSamokat:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления соответствующего текста ответа при нажатии на каждый вопрос')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_1, TestHomePageLocators.ANSWER_FAQ_1, expected_texts['faq1']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_2, TestHomePageLocators.ANSWER_FAQ_2, expected_texts['faq2']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_3, TestHomePageLocators.ANSWER_FAQ_3, expected_texts['faq3']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_4, TestHomePageLocators.ANSWER_FAQ_4, expected_texts['faq4']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_5, TestHomePageLocators.ANSWER_FAQ_5, expected_texts['faq5']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_6, TestHomePageLocators.ANSWER_FAQ_6, expected_texts['faq6']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_7, TestHomePageLocators.ANSWER_FAQ_7, expected_texts['faq7']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_8, TestHomePageLocators.ANSWER_FAQ_8, expected_texts['faq8'])

    ])
    def test_click_question_shows_answer_faq(self, driver, home_page, question_locator, answer_locator, expected_text):
        home_page.scroll_to_faq()
        home_page.click_the_question(question_locator)
        answer = home_page.get_the_answer_text(answer_locator)
        assert answer == expected_text

    @allure.title('Проверка нажатия на логотип "Яндекс"')
    @allure.description('Проверка открытия страницы Яндекс.Дзен в соседней вкладке при нажатии на логотип "Яндекс"')
    def test_clicking_yandex_logo_opens_dzen_page(self, driver, home_page):
        home_page.click_logo_yandex_open_dzen_page()
        assert driver.current_url == DZEN_URL

    @allure.title('Проверка нажатия на логотип "Самокат"')
    @allure.description('Проверка перехода на главную страницу при нажатии на логотип "Самокат"')
    def test_click_logo_samokat_open_home_page(self, driver, home_page):
        home_page.click_order_button_header()
        home_page.click_logo_open_home_page()
        assert driver.current_url == BASE_URL
