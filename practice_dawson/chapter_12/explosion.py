from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)
nebula_image = games.load_image("chapter_12/nebula.jpg", transparent=0)
games.screen.background = nebula_image
explosion_files = ["chapter_12/explosion1.bmp",
                "chapter_12/explosion2.bmp",
                "chapter_12/explosion3.bmp",
                "chapter_12/explosion4.bmp",
                "chapter_12/explosion5.bmp",
                "chapter_12/explosion6.bmp",
                "chapter_12/explosion7.bmp",
                "chapter_12/explosion8.bmp",
                "chapter_12/explosion9.bmp"]

explosion = games.Animation(images=explosion_files,
                            x=games.screen.width/2,
                            y=games.screen.height/2,
                            n_repeats=0,
                            repeat_interval=5)
games.screen.add(explosion)
games.screen.mainloop()