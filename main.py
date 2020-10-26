from sprites import *
from word_generation import *


class Game:
    def __init__(self):
        # init game window, etc
        pg.init()
        pg.mixer.init()
        self.font = pg.font.SysFont('Arial', 25)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # reset game/start new
        self.all_sprites = pg.sprite.Group()
        self.boxes = pg.sprite.Group()
        self.texts = []
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.gen_words()
            self.move_words()
            self.draw()

    def update(self):
        # loop update
        self.boxes.update()

    def events(self):
        # events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def gen_words(self):
        # generate word
        self.word = choose_word(wordlist)
        self.text_h, self.text_w = self.font.size(self.word)
        self.block = textblock(WIDTH/2, HEIGHT-500, self.text_h, self.text_w)
        self.blockxy = self.block.rect
        print(self.word)

        self.texts += self.word
        self.boxes.add(self.block)

    def draw(self):
        # game loop draw
        self.screen.fill((0, 0, 0))
        randword = self.font.render(self.word, False, (255, 255, 255))

        self.boxes.draw(self.screen)

        # blit word on textblock
        for block in self.boxes:
            self.screen.blit(randword, (self.blockxy[0] + 2, self.blockxy[1]))

        # update display after drawing
        screenCopy = self.screen.copy()
        waitTime = 5500
        waitCount = 0
        while waitCount < waitTime:
            waitCount += 60
            pg.event.pump()  # Tells pygame to handle it's event, instead of pygame.event.get()
            self.screen.blit(screenCopy, (0, 0))
            pg.display.flip()

    def move_words(self):
        # for word in
        pass

    def delete_word(self):
        pass

    def start_screen(self):
        pass

    def game_over(self):
        pass


g = Game()
g.start_screen()
while g.running:
    g.new()
    g.game_over()

pg.quit()
