from pages.main_menu_page import MainMenuPage
from pages.level_selection_page import LevelSelectionPage

def test_can_not_enter_locked_level(driver):
    main = MainMenuPage(driver)
    level = LevelSelectionPage(driver)

    main.open()
    main.select_category("Pronouns")
    main.go_to_level_selection()

    assert level.is_level_locked()
