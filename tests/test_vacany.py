from pages.vacancy_page import VacancyPage


vacancy_page = VacancyPage()


def test_job_title():
    vacancy_page.open()

    vacancy_page.job_title_should_have_text('SOFTWARE ENGINEER FOR AUTOMATION - TDI')


def test_check_header():
    # check header
    vacancy_page.open()

    vacancy_page.work_requirements_should_have_facts(
        'Professionals', 'Regular (Part Time possible)', 'Athen'
    )


def test_more_btn():
    # check 'more' btn
    vacancy_page.open()
    vacancy_page.click_more_button()

    vacancy_page.work_requirements_should_have_more_facts(
        '3-5 years Experience Required',
        '0-25% Amount of Travel',
        'English',
        'Deutsche Telekom Cloud Services s.r.o.',
        'less',
    )


def test_tasks_block():
    # check 'your task' block
    vacancy_page.open()

    vacancy_page.asser_name_tasks_block('Your tasks')


def test_show_more_btn():
    # check 'Show more' btn
    vacancy_page.open()
    vacancy_page.click_show_more_button()

    vacancy_page.asser_new_line('    Working in international teams across Europe.')


def test_check_img():
    # check image
    vacancy_page.panel_img_is_visivle()
