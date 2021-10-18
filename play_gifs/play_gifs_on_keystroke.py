import pyglet

class Assassin(pyglet.sprite.Sprite):
    def __init__(self, batch, img):
        pyglet.sprite.Sprite.__init__(self, img, x = 50, y = 30)

    def stand(self):
        self.img = pyglet.image.load("assassin1.png")
        return self

    def move(self):
        self.img = pyglet.image.load('assassin2.png')    
        return self

class Game(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, width = 315, height = 220)
        self.batch_draw = pyglet.graphics.Batch()
        self.player = Assassin(batch = self.batch_draw, img = pyglet.image.load("assassin1.png"))
        self.keys_held = []      
        self.schedule = pyglet.clock.schedule_interval(func = self.update, interval = 1/60.) 

    def on_draw(self): 
        self.clear()         
        self.batch_draw.draw()
        self.player.draw()  

    def on_key_press(self, symbol, modifiers):
        self.keys_held.append(symbol)
        if symbol == pyglet.window.key.RIGHT:
            self.player = self.player.move()
            print "The 'RIGHT' key was pressed"

    def on_key_release(self, symbol, modifiers):
        self.keys_held.pop(self.keys_held.index(symbol))
        self.player = self.player.stand()
        print "The 'RIGHT' key was released"

    def update(self, interval):
        if pyglet.window.key.RIGHT in self.keys_held:
            self.player.x += 50 * interval

if __name__ == "__main__":
    window = Game()
    pyglet.app.run()