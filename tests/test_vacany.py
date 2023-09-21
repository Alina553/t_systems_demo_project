import pytest
from selene import browser, have, be


def test_page():
    browser.open(
        'https://t-systems.jobs/global-careers-en/jobs/gr/209045/Software-Engineer-for-Automation-_-TDI/Athens.html'
    )
    browser.element('#consentAcceptAll').click()

    # check job-title
    browser.element('#ja-job-title').should(
        have.text('SOFTWARE ENGINEER FOR AUTOMATION - TDI')
    )

    # check header
    browser.element('.ja-facts').all('.btn-light').should(
        have.exact_texts('Professionals', 'Regular (Part Time possible)', 'Athens')
    )

    # check 'more' btn
    browser.element('#facts-show-more').click()
    browser.element('.ja-section-more-facts').all('.btn-light').should(
        have.exact_texts(
            '3-5 years Experience Required',
            '0-25% Amount of Travel',
            'English',
            'Deutsche Telekom Cloud Services s.r.o.',
            'less',
        )
    )

    # check 'your task' block
    browser.element('#headline-our-offer').should(have.exact_text('Your tasks'))

    # ckeck 'Show more' btn
    browser.element('.show-more').click()
    browser.element('#info-our-offer > ul > li:nth-child(8)').should(
        have.exact_text('    Working in international teams across Europe.')
    )

    # check image
    browser.element('.ja-panel-image').should(be.visible)
