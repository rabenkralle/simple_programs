from superwires import games
import random

games.init(screen_width=640, screen_height=480, fps=50)

class Pan(games.Sprite):
    
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
    
    def check_collide(self):
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()

class Pizza(games.Sprite):
    
    def handle_collide(self):
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)


def main():
    wall_image = games.load_image("chapter_11/wall.jpg", transparent=False)
    games.screen.background = wall_image
    pizza_image = games.load_image("chapter_11/pizza.bmp")
    pizza_x = random.randrange(games.screen.width)
    pizza_y = random.randrange(games.screen.height)
    pizza = Pizza(image=pizza_image, 
                    x=pizza_x,
                    y=pizza_y
                    )
    games.screen.add(pizza)
    pan_image = games.load_image("chapter_11/pan.bmp")
    pan = Pan(image=pan_image, 
                    x=games.mouse.x,
                    y=games.mouse.y,
                    )
    games.screen.add(pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

if __name__== '__main__':
    main()