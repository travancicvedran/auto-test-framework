from pages.main_menu_page import MainMenuPage

def test_item_cannot_be_bought_without_credits(driver):
    main = MainMenuPage(driver)

    main.open()
    main.buy_item_from_shop(2)

    assert not main.is_item_bought(2)
