"""
    Игра 2048
    Д/з № 3
"""
import random
import numpy as np


class Game:
    """
        Класс описывающий логику и реализацию игры 2048
    """
    def __init__(self):
        """
            Инициализация игры
            Создание пустого поля
        """
        self.score = 0
        # self.field = np.zeros((4, 4), dtype=np.int)
        self.field = np.array([[0 for col in range(4)]
                               for row in range(4)])

    def swap(self, row, col, route):
        """
            Поменять местами значения в поле в зависимости от type [col, row]
        """
        tmp_value = self.field[row][col]
        self.field[row + route][col] = tmp_value
        self.field[row][col] = 0

    def move_left(self):
        """
            Сдвинуть ячейки влево
        """
        self.field = self.field.transpose()
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(1, 4):
                    if self.field[row][col] != 0:
                        if self.field[row - 1][col] == 0:
                            self.swap(row, col, -1)
                            done += 1
                        elif self.field[row - 1][col] == self.field[row][col]:
                            self.field[row - 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row - 1][col]
                            done += 1
                if done == 0:
                    break
        self.field = self.field.transpose()
        return True

    def move_right(self):
        """
            Сдвинуть вправо
        """
        self.field = self.field.transpose()
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(4, 1, -1):
                    row *= -1
                    if self.field[row][col] != 0:
                        if self.field[row + 1][col] == 0:
                            self.swap(row, col, 1)
                            done += 1
                        elif self.field[row + 1][col] == self.field[row][col]:
                            self.field[row + 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row + 1][col]
                            done += 1
                if done == 0:
                    break
        self.field = self.field.transpose()
        return True

    def move_up(self):
        """
            Сдвинуть ввевх
        """
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(1, 4):
                    if self.field[row][col] != 0:
                        if self.field[row - 1][col] == 0:
                            self.swap(row, col, -1)
                            done += 1
                        elif self.field[row - 1][col] == self.field[row][col]:
                            self.field[row - 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row - 1][col]
                            done += 1
                if done == 0:
                    break
        return True

    def move_down(self):
        """
        Сдвинуть вниз
        """
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(4, 1, -1):
                    row *= -1
                    if self.field[row][col] != 0:
                        if self.field[row + 1][col] == 0:
                            self.swap(row, col, 1)
                            done += 1
                        elif self.field[row + 1][col] == self.field[row][col]:
                            self.field[row + 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row + 1][col]
                            done += 1
                if done == 0:
                    break
        return True

    def has_moves(self):
        """
            Выяснить есть ли еще куда ходить
        """
        count = 0
        for row in self.field:
            for cell in row:
                if cell == 0:
                    count += 1
        if count > 0:
            return True
        return False

    def get_score(self):
        """
            Вернуть очки в игре
        """
        return self.score

    def get_field(self):
        """
            Заполнить на поле две случайные ячейки и вернуть поле
        """
        if self.has_moves():
            k = 0
            while k < 2:
                row = random.randint(0, 3)
                cell = random.randint(0, 3)
                if self.field[row][cell] == 0:
                    if random.randrange(0, 100) <= 10:
                        self.field[row][cell] = 4
                    else:
                        self.field[row][cell] = 2
                    k = k + 1
        return self.field


def main():
    """
        Функция запуска игры в консоли
    """
    game = Game()

    while True:
        field = game.get_field()
        cell_width = len(str(max(
            cell
            for row in field
            for cell in row
        )))
        print("\033[H\033[J", end="")
        print("Score: ", game.get_score())
        print('\n'.join(
            ' '.join(
                str(cell).rjust(cell_width)
                for cell in row
            )
            for row in field
        ))

        if not game.has_moves():
            print("No available moves left, game over.")
            break

        print("L, R, U, D - move")
        print("Q - exit")

        try:
            input_letter = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        if input_letter in ('l', 'L'):
            game.move_left()
        elif input_letter in ('r', 'R'):
            game.move_right()
        elif input_letter in ('u', 'U'):
            game.move_up()
        elif input_letter in ('d', 'D'):
            game.move_down()
        elif input_letter in ('q', 'Q'):
            break

    print("Bye!")


if __name__ == '__main__':
    main()
