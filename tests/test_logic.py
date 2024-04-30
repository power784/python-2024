import unittest
from unittest.mock import patch, MagicMock
import Logic
import Objects

class TestLogicFunctions(unittest.TestCase):

    def setUp(self):
        self.balls = [
            Objects.Obstacle(100, 200, 10, 0, 5, 0),
           	Objects.Obstacle(300, 400, 20, 1, 10, 1),
            Objects.Obstacle(500, 600, 15, 2, 8, 3),
            Objects.Obstacle(700, 800, 25, 3, 12, 1)
        ]
        self.player = Objects.Player(50, 50, 10)

    def test_move(self):
        # Проверяем, что функция move корректно обновляет положение шаров
        expected_positions = [
            (200, 95), (400, 310), (608, 500), (800, 712)
        ]
        Logic.move(self.balls)
        for i, ball in enumerate(self.balls):
            self.assertEqual((ball.x, ball.y), expected_positions[i])

    @patch('random.randint')
    def test_generate_obstacles(self, mock_randint):
        # Моки для функции random.randint
        mock_randint.side_effect = [1, 10, 20, 1, 30, 40, 0, 50, 60, 1, 70, 80]
        balls = []
        Logic.generate_obstacles(self.player, balls)
        self.assertEqual(len(balls), 2)  # Проверяем, что создано 2 препятствия

    def test_check_collisions(self):
        # Проверяем, что функция check_collisions корректно обнаруживает столкновения
        self.assertTrue(Logic.check_collisions(self.player, self.balls))
        self.balls.append(Objects.Obstacle(40, 40, 30, 30, 5, 0))
        self.assertFalse(Logic.check_collisions(self.player, self.balls))

if __name__ == '__main__':
    unittest.main()
