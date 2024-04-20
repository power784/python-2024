import unittest
import Objects

class TestObjects(unittest.TestCase):

    def test_player_init(self):
        # Проверяем правильность инициализации объекта Player
        player = Objects.Player(100, 200, 5)
        self.assertEqual(player.y, 100)
        self.assertEqual(player.x, 200)
        self.assertEqual(player.speed, 5)

    def test_obstacle_init(self):
        # Проверяем правильность инициализации объекта Obstacle
        obstacle = Objects.Obstacle(50, 75, 20, 30, 8, 2)
        self.assertEqual(obstacle.y, 50)
        self.assertEqual(obstacle.x, 75)
        self.assertEqual(obstacle.w, 20)
        self.assertEqual(obstacle.h, 30)
        self.assertEqual(obstacle.speed, 8)
        self.assertEqual(obstacle.dr, 2)

if __name__ == '__main__':
    unittest.main()
