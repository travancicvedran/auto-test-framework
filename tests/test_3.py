from pages.main_menu_page import MainMenuPage
from pages.level_selection_page import LevelSelectionPage
from pages.game_over_page import GameOverPage

def test_gameOver_after_time_runs_out(driver):
    main = MainMenuPage(driver)
    level = LevelSelectionPage(driver)

    main.open()
    main.select_category("Pronouns")
    main.go_to_level_selection()
    level.select_level(1)

    over = GameOverPage(driver)

    assert over.is_loaded()
