from selene import browser, have, be
import allure


class VacancyPage:
    # @allure.step('Open page with vacancy')
    def open(self):
        with allure.step('Open page with vacancy'):
            browser.open(
                '/global-careers-en/jobs/gr/209045/Software-Engineer-for-Automation-_-TDI/Athens.html'
            )
            browser.element('#consentAcceptAll').click()

    @allure.step('Check job title ')
    def job_title_should_have_text(self, job_title):
        browser.element('#ja-job-title').should(have.text(job_title))

    @allure.step('Check work reqiurements facts')
    def work_requirements_should_have_facts(self, skill, work_mode, location):
        browser.element('.ja-facts').all('.btn-light').should(
            have.exact_texts(f'{skill}', f'{work_mode}', f'{location}')
        )

    @allure.step('Check more work requirements facts')
    def work_requirements_should_have_more_facts(
        self, experience, travel, language, service, less_btn
    ):
        browser.element('.ja-section-more-facts').all('.btn-light').should(
            have.exact_texts(
                f'{experience}',
                f'{travel}',
                f'{language}',
                f'{service}',
                f'{less_btn}',
            )
        )

    @allure.step("Click on 'More' button")
    def click_more_button(self):
        browser.element('#facts-show-more').click()

    @allure.step('Check task block name')
    def asser_name_tasks_block(self, block_name):
        browser.element('#headline-our-offer').should(have.exact_text(block_name))

    @allure.step("Click on 'Show more' button")
    def click_show_more_button(self):
        browser.element('.show-more').click()

    @allure.step("Check that 'Show more' button works correct")
    def asser_new_line(self, new_line):
        browser.element('#info-our-offer > ul > li:nth-child(8)').should(
            have.exact_text(new_line)
        )

    @allure.step('Check visibility panel image')
    def panel_img_is_visivle(self):
        browser.element('.ja-panel-image').should(be.visible)
