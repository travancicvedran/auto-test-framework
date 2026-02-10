from pages.main_menu_page import MainMenuPage

def test_credits_reset_after_progress_reset(driver):
    main = MainMenuPage(driver)

    main.open()
    main.reset_progress()

    assert main.get_credits() == 0