import pygame

# colors
YELLOW = (255, 255, 0)
ULTRAMARIN = (18, 10, 143)

# characteristics of each segment
segment_width = 30
segment_height = 30
# distance between each segment
segment_margin = 0
 
# our speed
x_change = segment_width + segment_margin
y_change = 0

class Segment(pygame.sprite.Sprite):
    # constructor function
    def __init__(self, x, y):
        # cll the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(ULTRAMARIN)
 

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# pygame library can init. itself
pygame.init()
 
# create an our screen size
screen = pygame.display.set_mode([1280, 800])

pygame.display.set_caption('TURBO ULTRAMARIN SNAKE')

allspriteslist = pygame.sprite.Group()
 
# create our snake
snake_segments = []
for n in range(15):
    x = 20 - (segment_width + segment_margin) * n
    y = 3
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 
 
clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # speed based on the key pressed
        # segment plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) *- 1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) *- 1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
 
    # gt rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)
 
    # fgure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)
 
    # insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)
 

    # colour our screen
    screen.fill(YELLOW)
 
    allspriteslist.draw(screen)
 
    pygame.display.flip()
 
    # Pause
    clock.tick(5)
 
pygame.quit()