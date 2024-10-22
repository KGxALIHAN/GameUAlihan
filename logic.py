import random

class GuessingGame:
    def __init__(self, min_value, max_value, attempts, initial_capital):
        self.min_value = min_value
        self.max_value = max_value
        self.attempts = attempts
        self.initial_capital = initial_capital
        self.target_number = random.randint(self.min_value, self.max_value)

    def play_round(self, guess, bet):
        if bet > self.initial_capital:
            raise ValueError("Ставка больше доступного капитала!")

        if guess == self.target_number:
            self.initial_capital += bet
            print(f"Вы угадали! Ваш выигрыш: {bet * 2}. Капитал: {self.initial_capital}")
            return True
        else:
            self.initial_capital -= bet
            print(f"Неверно! Вы потеряли {bet}. Остаток капитала: {self.initial_capital}")
            return False

    def is_game_over(self):
        return self.attempts <= 0 or self.initial_capital <= 0

    def reduce_attempts(self):
        self.attempts -= 1
