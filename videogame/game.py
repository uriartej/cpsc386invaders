#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# uriartej

"""Game objects to create PyGame based games."""

import os
import warnings
import pygame
import rgbcolors
from scene import PolygonTitleScene


def display_info():
    """Print out information about the display driver and video information."""
    print(f'The display is using the "{pygame.display.get_driver()}" driver.')
    print("Video Info:")
    print(pygame.display.Info())


# If you're interested in using abstract base classes, feel free to rewrite
# these classes.
# For more information about Python Abstract Base classes, see
# https://docs.python.org/3.8/library/abc.html


class VideoGame:
    """Base class for creating PyGame games."""

    def __init__(
        self,
        window_width=800,
        window_height=800,
        window_title="My Game",
    ):
        """Initialize a new game with the given window size and window title."""
        pygame.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            warnings.warn("Fonts disabled.", RuntimeWarning)
        if not pygame.mixer:
            warnings.warn("Sound disabled.", RuntimeWarning)
        self._scene_graph = None

    @property
    def scene_graph(self):
        """Return the scene graph representing all the scenes in the game."""
        return self._scene_graph

    def build_scene_graph(self):
        """Build the scene graph for the game."""
        raise NotImplementedError

    def run(self):
        """Run the game; the main game loop."""
        raise NotImplementedError


class MyVideoGame(VideoGame):
    """Show a colored window with a colored message and a polygon."""

    def __init__(self):
        """Init the Pygame demo."""
        super().__init__(window_title="Hello")
        self._main_dir = os.path.abspath(os.path.dirname(__file__))
        self._data_dir = os.path.join(self._main_dir, "data")
        self.build_scene_graph()

    def build_scene_graph(self):
        """Build scene graph for the game demo."""
        self._scene_graph = [
            PolygonTitleScene(
                self._screen,
                "Welcome to Space Invaders",
                title_color = rgbcolors.ghost_white,
                title_size = 72,
                background_color = rgbcolors.green,
                soundtrack = os.path.join(self._data_dir, "03+Dawn+Metropolis.mp3")
            )
        ]

    def run(self):
        """Run the game; the main game loop."""
        scene_iterator = iter(self.scene_graph)
        while True:
            current_scene = next(scene_iterator)
            current_scene.start_scene()
            while current_scene.is_valid():
                self._clock.tick(current_scene.frame_rate())
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            break
                    current_scene.process_event(event)
                
                current_scene.update_scene()
                current_scene.render_updates()
                current_scene.draw()

                pygame.display.flip()

                if not current_scene.is_valid():
                    break

            current_scene.end_scene()

            if not current_scene.is_last_scene():
                continue
                
            break
        
        pygame.quit()
        