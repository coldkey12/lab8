import pygame

# Function to draw circle
def drawCircle(screen, position, radius, color):
    pygame.draw.circle(screen, color, position, radius)

# Function to draw rectangle
def drawRectangle(screen, position, radius, color):
    top_left = (position[0] - radius, position[1] - radius)
    pygame.draw.rect(screen, color, pygame.Rect(top_left, (radius * 2, radius * 2)))

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'  # Default color
    points = []
    drawing_mode = 'circle'  # Start by drawing circles
    eraser_mode = False

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # Exit conditions
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Color change via keys
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                # Change drawing mode
                if event.key == pygame.K_o:
                    drawing_mode = 'circle'  # Switch to circle
                elif event.key == pygame.K_m:
                    drawing_mode = 'rectangle'  # Switch to rectangle
                elif event.key == pygame.K_e:
                    eraser_mode = not eraser_mode  # Toggle eraser mode

            # Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                if event.button == 1:  # Left click to draw
                    if eraser_mode:  # Erase
                        points = [point for point in points if not point_near(position, point, radius)]
                    else:
                        points.append((position, drawing_mode))

                elif event.button == 3:  # Right click shrinks radius
                    radius = max(1, radius - 1)

            # Mouse motion
            if event.type == pygame.MOUSEMOTION:
                pass  # Nothing to do here for now

        screen.fill((0, 0, 0))  # Fill screen with black

        # Draw all points (based on the drawing mode)
        for point, shape in points:
            if shape == 'circle':
                drawCircle(screen, point, radius, getColor(mode))
            elif shape == 'rectangle':
                drawRectangle(screen, point, radius, getColor(mode))

        # Draw eraser outline if in eraser mode
        if eraser_mode:
            pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), radius, 1)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # 60 FPS

# Function to get the color based on mode
def getColor(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    else:
        return (255, 255, 255)  # Default color is white

# Helper function to check if a point is near another point (for erasing)
def point_near(position, point, radius):
    x, y = position
    px, py = point[0]  # Extract position part from the tuple (position, mode)
    return (x - px) ** 2 + (y - py) ** 2 <= radius ** 2

if __name__ == "__main__":
    main()
