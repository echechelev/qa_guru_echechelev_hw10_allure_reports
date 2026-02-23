import allure
from selene import browser, by, have


@allure.tag("smoke")
@allure.severity(allure.severity_level.MINOR)
@allure.feature("Homework")
@allure.story("Незарегистрированный пользователь может открыть репозиторий")
@allure.label("owner", "Evgeniy Chechelev")
@allure.title("Проверка названия Issue #1 в репозитории")
@allure.description("Ищем репозиторий, переходим в Issues и проверяем заголовок Issue")
@allure.step("Открыть GitHub")
def open_github():
	browser.open('https://github.com')


@allure.step("Выполнить поиск репозитория: {repo}")
def search_repo(repo: str):
	browser.element('.header-search-button').click()
	browser.element('#query-builder-test').type(repo).submit()


@allure.step("Перейти в репозиторий: {repo}")
def go_to_repo(repo: str):
	browser.element(by.link_text(repo)).click()


@allure.step("Открыть вкладку Issues")
def open_issues():
	browser.element(
		'[href="/echechelev/qa_guru_echechelev_hw10_allure_reports/issues"]'
	).click()


@allure.step("Проверить название Issue #1")
def check_issue_1_title():
	browser.element('a[href*="/issues/1"]').should(
		have.text("# 1 Test issue for automation")
	)


def test_github_issue_with_decorator_steps():
	open_github()
	search_repo("echechelev/qa_guru_echechelev_hw10_allure_reports")
	go_to_repo("echechelev/qa_guru_echechelev_hw10_allure_reports")
	open_issues()
	check_issue_1_title()
