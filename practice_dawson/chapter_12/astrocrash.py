import math, random
from tkinter import N
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images ={SMALL: games.load_image("chapter_12/asteroid_small.bmp"),
            MEDIUM: games.load_image("chapter_12/asteroid_med.bmp"),
            LARGE: games.load_image("chapter_12/asteroid_big.bmp")}
    SPEED = 2
    SPAWN = 2

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(
            image=Asteroid.images[size], x=x, y=y,
                dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                dy=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size
            )
        self.size = size

    def update(self):
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
    
    def die(self):
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(x=self.x,
                                        y=self.y,
                                        size=self.size - 1)
                games.screen.add(new_asteroid)
            self.destroy()

class Ship(games.Sprite):

    image = games.load_image("chapter_12/ship.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    MISSILE_DELAY = 25
    sound = games.load_sound("chapter_12/thrust.wav")

    def __init__(self, x, y):
        super(Ship, self).__init__(image=Ship.image, x=x, y=y)
        self.missile_wait = 0

    def update(self):
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0        
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180        
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/ 180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.missile_wait > 0:
            self.missile_wait -= 1
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY
        
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
    
    def die(self):
        self.destroy()



class Missile(games.Sprite):
    image = games.load_image("chapter_12/missile.bmp")
    sound = games.load_sound("chapter_12/missile.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        Missile.sound.play()
        angle = ship_angle * math.pi/180
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super(Missile, self).__init__(image=Missile.image, x=x, y=y,
                                    dx=dx, dy=dy)
        self.lifetime = Missile.LIFETIME
    
    def update(self):
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        self.destroy()

def main():
    nebula_image = games.load_image("chapter_12/nebula.jpg")
    games.screen.background = nebula_image
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid =Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)
    ship = Ship(x=games.screen.width/2,
                y=games.screen.height/2)
    games.screen.add(ship)
    games.screen.mainloop()


if __name__ == "__main__":
    main()
