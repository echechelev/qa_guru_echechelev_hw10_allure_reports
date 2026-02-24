import allure
from selene import browser, by, have


@allure.tag("ui")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Homework")
@allure.story("Незарегистрированный пользователь может открыть репозиторий")
@allure.label("owner", "Evgeniy Chechelev")
@allure.title("Проверка названия Issue #1 в репозитории")
@allure.description("Ищем репозиторий, переходим в Issues и проверяем заголовок Issue")
def test_lambda():
	with allure.step('Открываем GitHub'):
		browser.open('https://github.com/')

	with allure.step('Нажимаем на поле поиска'):
		browser.element('.header-search-button').click()

	with allure.step('Вводим название репозитория и отправляем запрос'):
		browser.element('#query-builder-test').type(
			'echechelev/qa_guru_echechelev_hw10_allure_reports').submit()

	with allure.step('Переходим в найденный репозиторий'):
		browser.element(
			by.link_text('echechelev/qa_guru_echechelev_hw10_allure_reports')
		).click()

	with allure.step("Открываем вкладку Issues"):
		browser.element(
			'[href="/echechelev/qa_guru_echechelev_hw10_allure_reports/issues"]'
		).click()

	with allure.step("Проверяем, что Issue #1 имеет ожидаемое название"):
		browser.element('a[href*="/issues/1"]').should(
			have.text("# 1 Test issue for automation")
		)
