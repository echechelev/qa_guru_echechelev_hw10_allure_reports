from selene import browser, have, by


def test_selene():
	browser.open('https://github.com/')
	browser.element('.header-search-button').click()
	browser.element('#query-builder-test').type(
		'echechelev/qa_guru_echechelev_hw10_allure_reports').submit()
	browser.element(
		by.link_text('echechelev/qa_guru_echechelev_hw10_allure_reports')).click()
	browser.element(
		'[href="/echechelev/qa_guru_echechelev_hw10_allure_reports/issues"]').click()

	browser.element('a[href*="/issues/1"]').should(
		have.text("# 1 Test issue for automation")
	)
