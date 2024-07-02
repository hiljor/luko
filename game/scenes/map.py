import pygame

from maps.maps import MapFactory


class MapScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)
        self.text = "woo"
        self.mapFactory = MapFactory()
        self.current_map = self.mapFactory.new_map(20, 8, 5)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.current_map.swap_selected_location(-1)
            elif event.key == pygame.K_RIGHT:
                self.current_map.swap_selected_location(1)
            elif event.key == pygame.K_RETURN:
                self.current_map.choose_location()

    def update(self):
        pass

    def render(self, screen):
        width = screen.get_width() - 100  # Subtracting buffer from total width
        height = screen.get_height() - 100  # Subtracting buffer from total height

        buffer = 50  # Buffer offset for initial point

        # Calculate grid dimensions with buffer
        grid_width = width + buffer
        grid_height = height + buffer

        # Draw all paths between points
        for edge in self.current_map.edges:
            pygame.draw.line(screen, (255, 255, 255),
                    (buffer + edge[0][1] * grid_height / self.current_map.rows, buffer + edge[0][0] * grid_width / self.current_map.cols),
                    (buffer + edge[1][1] * grid_height / self.current_map.rows, buffer + edge[1][0] * grid_width / self.current_map.cols))

        # Draw the current path
        for i in range(len(self.current_map.path) - 1):
            pygame.draw.line(screen, (255, 0, 0),
                    (buffer + self.current_map.path[i][1] * grid_height / self.current_map.rows, buffer + self.current_map.path[i][0] * grid_width / self.current_map.cols),
                    (buffer + self.current_map.path[i + 1][1] * grid_height / self.current_map.rows, buffer + self.current_map.path[i + 1][0] * grid_width / self.current_map.cols))

        # Draw all points
        for point in self.current_map.points:
            pygame.draw.circle(screen, (255, 255, 255),
                    (buffer + int(point[1] * grid_height / self.current_map.rows), buffer + int(point[0] * grid_width / self.current_map.cols)), 5)

        # Highlight current location
        if self.current_map.current is not None:
            pygame.draw.circle(screen, (255, 0, 0),
                    (buffer + int(self.current_map.current[1] * grid_height / self.current_map.rows), buffer + int(self.current_map.current[0] * grid_width / self.current_map.cols)), 10, 3)

        # Highlight neighbors
        if self.current_map.current is not None:
            for neighbour in self.current_map.neighbours[self.current_map.current]:
                color = (255, 255, 0) if neighbour == self.current_map.selected else (255, 255, 255)
                pygame.draw.circle(screen, color,
                        (buffer + int(neighbour[1] * grid_height / self.current_map.rows), buffer + int(neighbour[0] * grid_width / self.current_map.cols)), 10, 3)
        else:
            for start in self.current_map.starts:
                color = (255, 255, 0) if start == self.current_map.selected else (255, 255, 255)
                pygame.draw.circle(screen, color,
                        (buffer + int(start[1] * grid_height / self.current_map.rows), buffer + int(start[0] * grid_width / self.current_map.cols)), 10, 3)
                    
