import pygame

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((1200, 700))
    from main_menu.main_menu import MainMenu
    mainMenu = MainMenu(win)
    mainMenu.run()