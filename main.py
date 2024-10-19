from decouple import Config, config
from group_47.logic import GuessingGame

def load_settings():
    min_value = config('MIN_VALUE', cast=int)
    max_value = config('MAX_VALUE', cast=int)
    attempts = config('ATTEMPTS', cast=int)
    initial_capital = config('INITIAL_CAPITAL', cast=int)
    return min_value, max_value, attempts, initial_capital

def main():
    # Загрузка настроек
    min_value, max_value, attempts, initial_capital = load_settings()
    
    # Инициализация игры
    game = GuessingGame(min_value, max_value, attempts, initial_capital)

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Ваш начальный капитал: {initial_capital}")
    
    while not game.is_game_over():
        try:
            guess = int(input(f"Введите ваше число ({min_value}-{max_value}): "))
            bet = int(input(f"Введите вашу ставку: "))
            game.play_round(guess, bet)
            game.reduce_attempts()
        except ValueError as e:
            print(e)
        
    if game.initial_capital > 0:
        print("Игра окончена. Поздравляем, вы выиграли!")
    else:
        print("Игра окончена. Вы потеряли весь капитал.")

if __name__ == "__main__":
    main()
