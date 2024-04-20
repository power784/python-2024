import unittest
from unittest.mock import patch, MagicMock
import pygame
import Graphics
import Objects

class TestButtonClass(unittest.TestCase):

    def setUp(self):
        self.button = Graphics.Button(100, 200, 50, 100, (255, 0, 0))

    @patch('pygame.mouse.get_pos')
    def test_is_pressed(self, mock_get_pos):
        # Проверяем, что is_pressed возвращает True, когда курсор находится внутри кнопки
        mock_get_pos.return_value = (125, 225)
        self.assertTrue(self.button.is_pressed())

        # Проверяем, что is_pressed возвращает False, когда курсор находится за пределами кнопки
        mock_get_pos.return_value = (50, 50)
        self.assertFalse(self.button.is_pressed())

    @patch('pygame.draw.rect')
    @patch('pygame.font.Font')
    def test_draw(self, mock_font, mock_draw_rect):
        # Создаем мок для объекта Font
        mock_font_obj = MagicMock()
        mock_font.return_value = mock_font_obj

        # Создаем мок для метода render объекта Font
        mock_render = MagicMock()
        mock_font_obj.render.return_value = mock_render

        # Создаем мок для объекта Surface
        mock_surface = MagicMock()

        # Вызываем метод draw
        self.button.draw(mock_surface)

        # Проверяем, что метод draw был вызван с правильными аргументами
        mock_draw_rect.assert_called_with(mock_surface, (255, 0, 0), (100, 200, 50, 100))
        mock_font.assert_called_with(None, 36)
        mock_font_obj.render.assert_called_with("Играть", True, [255, 255, 255])
        mock_surface.blit.assert_called_with(mock_render, (132, 208))

class TestFunctions(unittest.TestCase):

    @patch('pygame.font.Font')
    @patch('pygame.draw.rect')
    def test_draw_main_screen(self, mock_draw_rect, mock_font):
        # Создаем моки для объектов Font и Surface
        mock_font_obj = MagicMock()
        mock_font.return_value = mock_font_obj
        mock_render1 = MagicMock()
        mock_render2 = MagicMock()
        mock_font_obj.render.side_effect = [mock_render1, mock_render2]
        mock_surface = MagicMock()

        # Создаем мок для объекта Button
        mock_button = MagicMock()

        # Вызываем функцию draw_main_screen
        Graphics.draw_main_screen(mock_surface, 100, 50, mock_button)

        # Проверяем, что функция была вызвана с правильными аргументами
        mock_surface.fill.assert_called_with([255, 255, 255])
        mock_button.draw.assert_called_with(mock_surface)
        mock_font.assert_called_with(None, 36)
        mock_font_obj.render.assert_any_call("Лучший счёт : 100", True, [0, 0, 255])
        mock_font_obj.render.assert_any_call("Прошлый раз : 50", True, [0, 0, 255])
        mock_surface.blit.assert_any_call(mock_render1, (10, 40))
        mock_surface.blit.assert_any_call(mock_render2, (300, 40))

    # Добавьте другие тесты для остальных функций по аналогии

class TestGraphicsFunctions(unittest.TestCase):

    @patch('pygame.display.flip')
    @patch('pygame.draw.rect')
    @patch('pygame.font.Font')
    def test_draw_game_screen(self, mock_font, mock_draw_rect, mock_flip):
        # Создаем мок для объекта Surface
        mock_surface = MagicMock()

        # Создаем мок для объекта Player
        mock_player = MagicMock(spec=Objects.Player)
        mock_player.y = 100
        mock_player.x = 200

        # Создаем список моков для объектов Obstacle
        mock_obstacles = [
            MagicMock(spec=Objects.Obstacle, y=50, x=60, w=20, h=30),
            MagicMock(spec=Objects.Obstacle, y=150, x=250, w=40, h=10)
        ]

        # Создаем мок для объекта Font
        mock_font_obj = MagicMock()
        mock_font.return_value = mock_font_obj

        # Создаем мок для метода render объекта Font
        mock_render = MagicMock()
        mock_font_obj.render.return_value = mock_render

        # Вызываем функцию draw_game_screen
        Graphics.draw_game_screen(mock_surface, mock_player, mock_obstacles, 1000)

        # Проверяем, что функция была вызвана с правильными аргументами
        mock_surface.fill.assert_called_with([255, 255, 255])
        mock_draw_rect.assert_any_call(mock_surface, [0, 255, 0], (100, 200, 30, 30))
        mock_draw_rect.assert_any_call(mock_surface, [255, 0, 0], (50, 60, 20, 30))
        mock_draw_rect.assert_any_call(mock_surface, [255, 0, 0], (150, 250, 40, 10))
        mock_font.assert_called_with(None, 36)
        mock_font_obj.render.assert_called_with("Cчёт : 1000", True, [0, 0, 255])
        mock_surface.blit.assert_called_with(mock_render, (10, 40))
        mock_flip.assert_called_once()
if __name__ == '__main__':
    unittest.main()
