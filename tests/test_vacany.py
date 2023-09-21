import allure
from pages.vacancy_page import VacancyPage


def test_description():
    allure.dynamic.tag("web")
    allure.dynamic.feature("Check vacancy page")


def test_vacancy_page():
    vacancy_page = VacancyPage()

    vacancy_page.open()

    # check job-title
    vacancy_page.job_title_should_have_text('SOFTWARE ENGINEER FOR AUTOMATION - TDI')

    # check header
    vacancy_page.work_requirements_should_have_facts(
        'Professionals', 'Regular (Part Time possible)', 'Athens'
    )

    # check 'more' btn
    vacancy_page.click_more_button()
    vacancy_page.work_requirements_should_have_more_facts(
        '3-5 years Experience Required',
        '0-25% Amount of Travel',
        'English',
        'Deutsche Telekom Cloud Services s.r.o.',
        'less',
    )

    # check 'your task' block
    vacancy_page.asser_name_tasks_block('Your tasks')

    # check 'Show more' btn
    vacancy_page.click_show_more_button()
    vacancy_page.asser_new_line('    Working in international teams across Europe.')

    # check image
    vacancy_page.panel_img_is_visivle()
