from pages.main_menu_page import MainMenuPage

def test_item_can_be_bought_with_credits(driver):
    main = MainMenuPage(driver)

    main.open()
    main.get_secret_credits()
    main.buy_item_from_shop(1)

    assert main.is_item_bought(1)