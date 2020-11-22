# Source File Name: slotmachine0_4.py
# Author's Name: TCL
# Last Modified By: Aldrin Jerome Almacin
# Date Last Modified: November 22, 2020
"""
  Program Description:  This program is a Casino-style slot machine.
  The player is given cash to begin the game and he plays the slot machine to earn more cash. He is given a fair chance of winning the game.
  Winning an additional jackpot price is also possible when the user gets 3 pairs. The user can also reset or quit the game if desired.

  Version: 0.4: Kingdom's version
"""

# import statements
import random
import pygame
import time
from game_assets.colors import rgb

# Initialize pygame
pygame.init()

# Initialize game constants
FRAME_RATE = 30
GAME_TITLE = "Slot Machine"
BACKGROUND_IMAGE_NAME = "game_assets/slot/background.png"
pad_y = 14

"""
  Class: SlotMachineButton
  Description: A generic slot machine button. It only have an image positioned in the screen.
"""
class SlotMachineButton(pygame.sprite.Sprite):
  def __init__(self, image_file_name, pos):
    pygame.sprite.Sprite.__init__(self)
    # Load the png image with transparency
    self.image = pygame.image.load("game_assets/slot/" + image_file_name)
    self.image = self.image.convert_alpha()
    # Move the rect to make sure it follows the image
    self.rect = self.image.get_rect()
    self.rect = self.rect.move(pos)
    self.pos = pos

"""
  Class: SlotMachineBetButton
  Description: Sprite used as a button that has a bet value.
"""
class SlotMachineBetButton(SlotMachineButton):
  """
    Constructor:
      params:
        image_file_name: @override
        bet_value: The bet value.
        pos: @override
  """
  def __init__(self, image_file_name, bet_value, pos):
    SlotMachineButton.__init__(self, image_file_name, pos)
    self.bet_value = bet_value

"""
  Class: SlotMachineActionButton
  Description: Slot machine button that can call a function/method
"""
class SlotMachineActionButton(SlotMachineButton):
  """
    Constructor:
      params:
        image_file_name: @override
        function_callable: The method to be called when this button is clicked
        pos: @override
  """
  def __init__(self, image_file_name, function_callable, pos):
    SlotMachineButton.__init__(self, image_file_name, pos)
    self.function_callable = function_callable

  """
    Function: Execute Func
    Purpose: Executes the function callable
  """
  def execute_func(self):
    self.function_callable()

"""
  Class: SlotMachine
  Description: The slot machine which is the main game object. All the methods required when playing a slot machine is included in this class.
"""
class SlotMachine:
  MAIN_MSG = "Kingdom's Slot Machine"
  YOU_WIN = "You just won $"
  YOU_WIN_JACKPOT = "Jackpot won $"
  YOU_LOST = "You just lost $"
  YOU_BET = "You bet $"
  NO_CASH_LEFT = "Cannot bet to that amount. Cash not enough."
  CANNOT_SPIN = "Cannot spin. Change bet to a lower value."
  STARTING_BET = 10
  JACKPOT_INCREASE_RATE = .15

  """
    Constructor:
      params:
        starting_jackpot: The jackpot price to start the game with
        starting_cash: The Starting cash when the game starts
  """
  def __init__(self, starting_jackpot, starting_cash):
    # Set all the sounds
    pygame.mixer.init()
    self.bet_snd = pygame.mixer.Sound("game_assets/sounds/slot/bet_snd.wav")
    self.bet_no_cash_snd = pygame.mixer.Sound("game_assets/sounds/slot/bet_no_cash_snd.wav")
    self.spin_snd = pygame.mixer.Sound("game_assets/sounds/slot/spin_snd.ogg")
    self.spinning_snd = pygame.mixer.Sound("game_assets/sounds/slot/spinning_snd.ogg")
    self.reset_snd = pygame.mixer.Sound("game_assets/sounds/slot/reset_snd.ogg")
    self.jackpot_snd = pygame.mixer.Sound("game_assets/sounds/slot/jackpot.wav")

    # Set Starting values
    self.starting_jackpot = starting_jackpot
    self.starting_cash = starting_cash

    # Set the icons/images that would be in the reels
    self.icons = []
    self.__create_icons()

    # Call the method used to set the initial values
    self.set_resettable_values()

  """
    Method: Set resettable values
    Description: Set the values of the slot machine which are resettable
  """
  def set_resettable_values(self):
    self.current_message = SlotMachine.MAIN_MSG
    self.current_jackpot = self.starting_jackpot
    self.current_cash = self.starting_cash
    self.results = 3*["Ryo"]
    self.bet = SlotMachine.STARTING_BET

  """
    Method: __create_icons
    Purpose: Private method used to create and set icons in an array.
  """
  def __create_icons(self):
   # The bonus win rate is for when no sad face is on the reel
    self.icons.append(Icon("Riboku", 0, 0, "riboku_icon.png", bonus_win_rate = 1))
    self.icons.append(Icon("Ten", 10, 1, "ten_icon.png"))
    self.icons.append(Icon("Kyoukai", 20, 2, "kyoukai_icon.png"))
    self.icons.append(Icon("Ouhon", 30, 2, "ouhon_icon.png"))
    self.icons.append(Icon("Shin", 100, 2, "shin_icon.png"))
    self.icons.append(Icon("Kanki", 200, 2, "kanki_icon.png"))
    self.icons.append(Icon("Moubu", 300, 5, "moubu_icon.png"))
    self.icons.append(Icon("Ryo", 1000, 10, "ryo_icon.png", bonus_win_rate = 5))

  """
    Method: Set bet
    Purpose: Method used to set a bet. When valid, the user is allowed to bet. If not, then tell the user he's out of cash.
  """
  def set_bet(self, bet):
    if self.current_cash - bet >= 0:
      self.bet = bet
      self.current_message = SlotMachine.YOU_BET + str(self.bet)
      self.bet_snd.play()
    else:
      self.current_message = SlotMachine.NO_CASH_LEFT
      self.bet_no_cash_snd.play()

  """
    Group of Functions: Getters
    Purpose: These methods are used to get attributes as a method.
  """
  def get_bet(self):
    return self.bet

  def get_current_cash(self):
    return self.current_cash

  def get_current_jackpot(self):
    return self.current_jackpot

  def get_current_message(self):
    return self.current_message

  """
    Method: Spin
    Purpose: Method used to spin the reels in the slot machine. It generates spin values to be used as spin data. Spinning is only allowed when there is enough money to do so.
  """
  def spin(self):
    if self.current_cash - self.bet >= 0:
      self.spin_snd.play()
      # pay the bet and increase the jackpot
      self.__pay()
      self.__increase_jackpot()

      # For each reel
      for spin in range(3):
        # Save the wildcard number as spinned_result
        spinned_result = random.randint(0, 100)

        if spinned_result in range(0, 40):     # 40% Chance
            self.results[spin] = self.icons[0].name
        elif spinned_result in range(40, 56):  # 16% Chance
            self.results[spin] = self.icons[1].name
        elif spinned_result in range(56, 70):  # 14% Chance
            self.results[spin] = self.icons[2].name
        elif spinned_result in range(70, 82):  # 12% Chance
            self.results[spin] = self.icons[3].name
        elif spinned_result in range(82, 89):  # 7% Chance
            self.results[spin] = self.icons[4].name
        elif spinned_result in range(89, 95):  # 6% Chance
            self.results[spin] = self.icons[5].name
        elif spinned_result in range(95, 99):  # 4% Chance
            self.results[spin] = self.icons[6].name
        elif spinned_result in range(99, 100):  # 1% Chance
            self.results[spin] = self.icons[7].name

      # Check what does the result of the calculation rewards.
      self.__check_results()
    else:
      # Show the message why the slot machine cannot be spinned
      self.current_message = SlotMachine.CANNOT_SPIN

  """
    Method: Pay
    Purpose: Private method used to reduce the cash using the bet amount. Pays for one spin.
  """
  def __pay(self):
    self.current_cash -= self.bet

  """
    Method: Increase jackpot
    Purpose: Private method used to increase the jackpot prize to be winned.
  """
  def __increase_jackpot(self):
    self.current_jackpot += (int(self.bet * SlotMachine.JACKPOT_INCREASE_RATE))

  """
    Method: Check results
    Purpose: Check how much the player won or lost
  """
  def __check_results(self):
    winnings = 0
    jackpot_won = 0
    # Go through each icon and check how many of the said icon is present. Base on that, check how much the player have won.
    for icon in self.icons:
      # Check how many of this icon is on the reel. Multiply the win rate to the bet and add it to winnings.
      if self.results.count(icon.name) == 3:
        winnings += self.bet * icon.win_rate_full
        self.jackpot_snd.play()
        # Play jackpot when 3 of a kind and not sadface is the result
        if winnings > 0:
          jackpot_won = self.jackpot_win()
      if self.results.count(icon.name) == 2:
        winnings += self.bet * icon.win_rate_two
    # If there is 1 seven, it is considered a win
    if self.results.count(self.icons[7].name) == 1:
      winnings += self.bet * self.icons[7].bonus_win_rate
    # If there is no sad face, it is considered a bet return win
    if self.results.count(self.icons[0].name) == 0:
      winnings += self.bet * self.icons[0].bonus_win_rate

    # If the winner won the jackpot or the winner just won something or the winner lost
    # Set the appropriate message
    if jackpot_won > 0:
      self.current_message = SlotMachine.YOU_WIN_JACKPOT + str(jackpot_won) + " With Cash $" + str(winnings)
    elif winnings > 0:
      self.current_cash += winnings
      self.current_message = SlotMachine.YOU_WIN + str(winnings)
    elif winnings <= 0:
      self.current_message = SlotMachine.YOU_LOST + str(self.bet)
    else:
      self.current_message = "Somethings wrong"

  """
    Method: Jackpot win
    Purpose: Play the jackpot and return the value of the player's jackpot price.
    Returns: The jackpot winnings
  """
  def jackpot_win(self):
    # Set the wildcard jackpot number
    JACKPOT_WILDCARD = 7
    # Generate a random number from 1 to 100
    jackpot_try = random.randint(1, 100)
    jackpot_try = 7
    winnings = 0

    # Compare the wildcard to the random number
    if jackpot_try == JACKPOT_WILDCARD:
      # If they match, then the user wins
      self.current_cash += self.current_jackpot
      # Set the current jackpot as the winnings. This is done before resetting the jackpot price to the starting jackpot value.
      winnings = self.current_jackpot
      # Reset the jackpot
      self.current_jackpot = self.starting_jackpot
      self.jackpot_snd.play()
      print("jacki")
    return winnings

  """
    Method: Reset
    Purpose: Resets the slot machine to its default values when the slot machine started.
  """
  def reset(self):
    self.set_resettable_values()

"""
  Class: Icon
  Description: The icons shown inside the reels
"""
class Icon(pygame.sprite.Sprite):
  """
    Constructor:
      params:
        name: The name of the icon
        win_rate_full: The winning rate when 3 of these icons are selected
        win_rate_two: The winning rate when 2 of these icons are selected
        icon_image: The file name of the image of this sprite
        bonus_win_rate: Optional win rate for special icons
  """
  def __init__(self, name, win_rate_full, win_rate_two, icon_image, bonus_win_rate = 0):
    pygame.sprite.Sprite.__init__(self)
    self.name = name
    self.image = pygame.image.load("game_assets/slot/" + icon_image)
    self.image = self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.win_rate_full = win_rate_full
    self.win_rate_two = win_rate_two
    self.bonus_win_rate = bonus_win_rate

"""
  Class: DigitalFont
  Description: An object that shows a text label using the digital font ttf.
"""
class DigitalFont(pygame.sprite.Sprite):
  """
    Constructor:
      params:
        method: The method that is used to grab the right message
        pos: The text's position in the screen
        color: Optional parameter which is the color of the text
  """
  def __init__(self, method, pos, color = rgb(143,8,8)):
    pygame.sprite.Sprite.__init__(self)
    self.digital_font = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 22)
    self.font_color = color
    self.meth = method
    self.pos = pos

  """
    Method: Get rendered surface
    Purpose: Returns the rendered text
    Returns: The rendered text
  """
  def get_rendered_surface(self):
    return self.digital_font.render(str(self.meth()), 1, self.font_color)

  """
    Method: Update
    Purpose: Render the text
  """
  def update(self):
    self.digital_font.render(str(self.meth()), 1, self.font_color)

  """
    Function: Start game
    Purpose: Starts the slot machine game
  """
def start_game():
  # Assign the Display Variables
  background = pygame.image.load(BACKGROUND_IMAGE_NAME)
  screen = pygame.display.set_mode((1200,700))
  pygame.display.set_caption(GAME_TITLE)

  # Create the slot machine object and hashes to be used by the game
  slot_machine = SlotMachine(1000, 100)
  spin_results = slot_machine.results
  icon_images = [] # The current icon images or spin result icons

  # Create the text labels
  digital_fonts_hash = [
    {"method": slot_machine.get_bet, "pos": (265, 424 + pad_y)},
    {"method": slot_machine.get_current_cash, "pos": (83, 424 + pad_y)},
    {"method": slot_machine.get_current_jackpot, "pos": (438, 424 + pad_y)},
  ]
  digital_fonts = pygame.sprite.Group()

  current_message_digifont = DigitalFont(slot_machine.get_current_message, (100, 140 + pad_y), rgb(0, 0, 0))

  for digital_font in digital_fonts_hash:
    digital_fonts.add(DigitalFont(digital_font["method"], digital_font["pos"]))

  # Set the constants
  BUTTON_BOTTOM_POS = background.get_height() - 165 + pad_y

  # Create the bet buttons
  bet_buttons_hash = [
    {"image_file_name": "ten_button.png", "bet_value": 10, "pos": (70, BUTTON_BOTTOM_POS)},
    {"image_file_name": "twenty_button.png", "bet_value": 20, "pos": (140, BUTTON_BOTTOM_POS)},
    {"image_file_name": "fifty_button.png", "bet_value": 50, "pos": (490, BUTTON_BOTTOM_POS)},
    {"image_file_name": "hundred_button.png", "bet_value": 100, "pos": (560, BUTTON_BOTTOM_POS)}
  ]
  bet_buttons = pygame.sprite.Group()

  for bet_button in bet_buttons_hash:
    bet_buttons.add(SlotMachineBetButton(bet_button["image_file_name"], bet_button["bet_value"], bet_button["pos"]))

  # Create the action buttons
  spin_button = SlotMachineActionButton("spin_button.png" , slot_machine.spin, (270, BUTTON_BOTTOM_POS))
  reset_button = SlotMachineActionButton("reset_button.png" , slot_machine.reset, (210, BUTTON_BOTTOM_POS + 30))
  quit_button = SlotMachineActionButton("quit_button.png" , slot_machine.reset, (422, BUTTON_BOTTOM_POS + 30))
  action_buttons = pygame.sprite.Group(spin_button, reset_button, quit_button)

  # Create all the symbols/icons to be shown in the reels
  all_symbols = pygame.sprite.Group()
  icons = slot_machine.icons
  for icon in icons:
    all_symbols.add(icon)

  # Set the game clock
  clock = pygame.time.Clock()

  # The reel positions is saved as an array with tuples
  reel_positions = [(78, 258 + pad_y), (260, 258 + pad_y), (438, 258 + pad_y)]

  # Add the spin result symbols to icon images
  for symbol in all_symbols:
    for symbol_name in spin_results:
      if (symbol.name == symbol_name):
        icon_images.append(symbol)

  # Set the variables to be used by the game loop
  start_time = 0
  spinning = False

  # Set the previous spin results
  prev_results = slot_machine.results

  #Play the bg music
  pygame.mixer.music.load("game_assets/sounds/slot/background_msc.mp3")
  pygame.mixer.music.play(-1)

  # Set the current slot machine values as previous values
  prev_bet, prev_jackpot, prev_current_msg, prev_cash = slot_machine.bet, slot_machine.current_jackpot, slot_machine.current_message, slot_machine.current_cash

  # Create functions used to get the previous slot machine values
  def prev_get_bet():
    return prev_bet
  def prev_get_current_cash():
    return prev_cash
  def prev_get_current_jackpot():
    return prev_jackpot
  def prev_get_current_msg():
    return prev_current_msg

  # Set the text values as the previous values
  # The reason this is done is to not let the user see how much he won until the spin animation is done
  prev_bet_digifont = DigitalFont(prev_get_bet, (265, 424 + pad_y))
  prev_cash_digifont = DigitalFont(prev_get_current_cash, (83, 424 + pad_y))
  prev_jackpot_digifont = DigitalFont(prev_get_current_jackpot, (438, 424 + pad_y))
  prev_message_digifont = DigitalFont(prev_get_current_msg, (100, 140 + pad_y), rgb(0, 0, 0))

  # Create the sprite group digifonts
  # The prev digifonts are the ones to be shown to the user while the spin animation is still running.
  prev_digifonts = pygame.sprite.Group(prev_bet_digifont, prev_jackpot_digifont, prev_cash_digifont, prev_message_digifont)

  # Continue looping while the player hasn't ended the game
  continue_playing = True
  while (continue_playing):
    # Tick
    clock.tick(FRAME_RATE)

    # Check for events
    for event in pygame.event.get():
      # Stop the loop when the user chooses to quit the game
      if (event.type == pygame.QUIT):
        continue_playing = False
      # When the user pushes the mouse button down, Check which sprites are involved
      elif (event.type == pygame.MOUSEBUTTONDOWN):
        # Check if a bet button is clicked then set the bet value to the value of that button
        for bet_button in bet_buttons:
          if(bet_button.rect.collidepoint(event.pos)):
            slot_machine.set_bet(bet_button.bet_value)
        # Check if spin button is clicked
        if(spin_button.rect.collidepoint(event.pos)):
          # Make sure you cant click the spin button while the reels are spinning
          if not spinning:
            # Execute the function inside the spin button. It would be slot_machine.spin()
            spin_button.execute_func()
            # If the message in the slot machine says the user cannot spin the reels, nothing happens. But if it is not then do the spin and set the spin results in the icon images
            if slot_machine.current_message != SlotMachine.CANNOT_SPIN:
              spin_results = slot_machine.results

              # Set the result's icon into icon_images
              icon_images = []
              for symbol in all_symbols:
                for symbol_name in spin_results:
                  if (symbol.name == symbol_name):
                    icon_images.append(symbol)

              # Set the start time to current time. Making the spin animation run
              start_time = time.time()

              # Set spinning to true to make sure the user can't click spin again while spinning
              spinning = True
            else:
              slot_machine.bet_no_cash_snd.play()
        # If it is the reset button, call the function associated with the button and play the reset sound
        elif(reset_button.rect.collidepoint(event.pos)):
          slot_machine.reset_snd.play()
          reset_button.execute_func()
        # If the quit button is clicked, stop the loop
        elif(quit_button.rect.collidepoint(event.pos)):
          continue_playing = False


    # Display the sprites

    # Display the background image
    #screen.blit(background, background.get_rect())
    screen.blit(background, (0, 350-background.get_height()/2))

    # Update the action buttons and position them on the screen
    action_buttons.update()
    for action_button in action_buttons:
      screen.blit(action_button.image, action_button.pos)

    # Update the texts
    digital_fonts.update()

    # Update the bet buttons and position them on the screen
    bet_buttons.update()
    for bet_button in bet_buttons:
      screen.blit(bet_button.image, bet_button.pos)

    # This section is the one responsible for the reel animation
    # While the current time - the time the spin button is clicked is less than one
    # Change the images in the reel and show the previous/current texts
    if time.time() - start_time < 1 and spinning:
      # Display the current icons in the reel so it does not change until the pulling the lever sound is finished
      for i in range(3):
        screen.blit(prev_results[i].image, reel_positions[i])
      # Display the current texts
      for digital_font in prev_digifonts:
        screen.blit(digital_font.get_rendered_surface(), digital_font.pos)
    elif time.time() - start_time < 2 and spinning:
      # Display a random icon in each reel and play the spinning sound
      for i in range(3):
        screen.blit(icons[random.randint(0, len(icons) - 1)].image, reel_positions[i])
      slot_machine.spinning_snd.play()
      # Display the current texts
      for digital_font in prev_digifonts:
        screen.blit(digital_font.get_rendered_surface(), digital_font.pos)
    else:
      # The animation is done and display the resulted values
      for i in range(3):
        screen.blit(icon_images[i].image, reel_positions[i])
      screen.blit(current_message_digifont.get_rendered_surface(), current_message_digifont.pos)
      # Spinning is now false. The user can hit spin again
      spinning = False
      # Set the prev results to the current images to be used again on animation
      prev_results = icon_images
      # Stop the spinning sound if playing
      slot_machine.spinning_snd.stop()
      # Render the current texts in the screen
      for digital_font in digital_fonts:
        screen.blit(digital_font.get_rendered_surface(), digital_font.pos)

      # Reset the prev values
      prev_bet, prev_jackpot, prev_current_msg, prev_cash = slot_machine.bet, slot_machine.current_jackpot, slot_machine.current_message, slot_machine.current_cash

    # Refresh the display
    pygame.display.flip()

def play_sound(*args):
    if len(args) == 3:
        a,b,c = args[0],args[1],args[2]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)), maxtime=c)
    elif len(args) == 2:
        a,b = args[0],args[1]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)))

"""
  Function: Main
  Purpose: Calls the start game function
"""
def Casino():
  start_game()

#Calls the main function
if __name__ == "__main__": Casino()
