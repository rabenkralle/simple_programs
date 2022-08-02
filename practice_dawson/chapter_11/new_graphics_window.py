from turtle import color
from superwires import games, color # вместо livewires как в книге, надо грузить superwires. только так работает.

games.init(screen_width=640, screen_height=480, fps=50)
wall_image = games.load_image("chapter_11/wall.jpg", transparent=False)
games.screen.background = wall_image
won_message = games.Text(value="Victory!",
                    size=100,
                    color=color.red,
                    x=games.screen.width/2,
                    y=games.screen.height/2)
games.screen.add(won_message)
games.screen.mainloop()