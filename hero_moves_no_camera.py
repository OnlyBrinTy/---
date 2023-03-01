import os
import sys
import pygame


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))
    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Hero(pygame.sprite.Sprite):
    def __init__(self, app, pos):
        super().__init__(app.hero_group, app.all_sprites)
        
        self.image = load_image("mario.png")
        self.rect = self.image.get_rect(center=(Tile.width * pos[0], Tile.height * pos[1]))


class Tile(pygame.sprite.Sprite):
    width = height = 50
    
    def __init__(self, app, tile_type, pos_x, pos_y):
        super().__init__(app.tiles_group, app.all_sprites)
        
        self.image = {'wall': load_image('box.png'), 'empty': load_image('grass.png')}[tile_type]
        self.rect = self.image.get_rect(topleft=(self.width * pos_x, self.height * pos_y))


class App:
    width, height = 500, 500
    
    def __init__(self):
        pygame.init()

        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption('Mario')
        pygame.key.set_repeat(500, 140)
                
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.GroupSingle()

        self.hero = None

    def generate_level(self, level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile(self, 'empty', x, y)
                elif level[y][x] == '#':
                    Tile(self, 'wall', x, y)
                elif level[y][x] == '@':
                    Tile(self, 'empty', x, y)

                    self.hero = Hero(self, (x + 1, y + 1))

    def start_screen(self):
        intro_text = ["ЗАСТАВКА", "",
                      "Правила игры",
                      "Если в правилах несколько строк,",
                      "приходится выводить их построчно"]
        
        background = pygame.transform.scale(load_image('background.png'), (self.width, self.height))
        self.screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 30)
        text_coord = 50

        for line in intro_text:
            string_rendered = font.render(line, True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return

            pygame.display.update()
            self.clock.tick(self.fps)

    def run(self):
        self.generate_level(load_level('map1.txt'))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                else:
                    keys = pygame.key.get_pressed()
                    
                    if any(keys):
                        if keys[pygame.K_DOWN]:
                            self.hero.rect.y += Tile.height
                        elif keys[pygame.K_UP]:
                            self.hero.rect.y -= Tile.height
                        elif keys[pygame.K_RIGHT]:
                            self.hero.rect.x += Tile.width
                        elif keys[pygame.K_LEFT]:
                            self.hero.rect.x -= Tile.width

            self.draw(self.tiles_group, self.hero_group)
            self.clock.tick(self.fps)

    def draw(self, tiles, player):
        self.screen.fill('black')

        for tile in tiles.sprites():
            self.screen.blit(tile.image, tile.rect.center)

        self.screen.blit(player.sprite.image, player.sprite.rect.topleft)
        pygame.display.update()


if __name__ == '__main__':
    app = App()
    app.start_screen()
    app.run()
