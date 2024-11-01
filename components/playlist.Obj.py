import flet as ft
import asyncio
from utils.findFile import find_file
from base64 import b64encode

class PlaylistUI(ft.Container):
    def __init__(self, parent: ft.Container , photoURL: str = None , title: str = None , creator: str = None):
        super().__init__()
        self.isolated = True
        self.is_isolated = lambda: self.isolated
        self.parent = parent
        self.photoURL = photoURL
        self.title = title
        self.creator = creator
        self.width = 276
        self.height = 45
        self.bgcolor = ft.colors.BLACK
        #self.border = ft.border.all(2 , ft.colors.RED)
        self.shape = ft.BoxShape.RECTANGLE
        self.border_radius = 16
        self.padding = ft.Padding(right= 0 , left= 17 , top= 0 , bottom= 0)
        self.expand_loose = True
        self.isPlaying = False
        self.gradient =  ft.LinearGradient([ft.colors.BLACK , ft.colors.BLACK], begin= ft.alignment.center)
        self.gradientKeys = {
            "True" : [ft.colors.BLACK , "#095B5C"],
            "False" : [ft.colors.BLACK , ft.colors.BLACK]
        }
        
        print(f"is this obj isolated? {self.is_isolated()}")
        
        self.init()
    
    def switchPlaying(self):
        print("playing")
        self.isPlaying = not self.isPlaying
        self.gradient.colors = self.gradientKeys[str(self.isPlaying)]
        self.update()
        
    def init(self):
        
        data = ft.Container(
            content= ft.Column(
                                controls=[
                                        ft.Text(self.title,
                                                size= 16,
                                                text_align= ft.alignment.center_right,
                                                font_family= "IBM Plex Mono Bold",
                                                ),
                                        ft.Text(self.creator,
                                                size= 14,
                                                text_align= ft.alignment.center_right,
                                                font_family= "IBM Plex Mono Light",
                                                )
                                        ],
                                spacing= 0,
            ),
            #border= ft.border.all(2 , ft.colors.RED),
            alignment= ft.alignment.center_right,
            expand= True,
            shape = ft.BoxShape.RECTANGLE,
            padding= ft.Padding(right= 17 , left= 0 , top= 0 , bottom= 0),
        )
        
        
        self.content = ft.Row(
            controls=[
                ft.Image(self.photoURL , width= 32 , height= 32),
                data
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            spacing= 17,
        )
        
        

if __name__ == "__main__":
    
    async def main(page: ft.Page):
        
        page.fonts = {
            "IBM Plex Mono": find_file("assets/fonts/IBMPlexMono-Regular.ttf"),
            "IBM Plex Mono Bold": find_file("assets/fonts/IBMPlexMono-Bold.ttf"),
            "IBM Plex Mono Light": find_file("assets/fonts/IBMPlexMono-Light.ttf"),
        }
        
        playlistFrame = ft.Column(height= 300,
                                  width= float("inf"),
                                  scroll= ft.ScrollMode.ALWAYS,)
        
        playlists = {
            "Mamaguevo": PlaylistUI(playlistFrame , find_file("assets/img/1384060.png"), "Mamaguevo" , "Creator"),
        }
        
        controls = [
            playlists["Mamaguevo"]
        ]
        
        for i in range(10):
            controls.append(
                PlaylistUI(playlistFrame,
                           find_file("assets/img/1384060.png"),
                           f"Playlist {i}",
                           "Creator")
            )
        
        playlistFrame.controls = controls
        
        page.add(
            playlistFrame
        )
        
        await asyncio.sleep(3)
        
        playlists["Mamaguevo"].switchPlaying()
        
        
        
        
        await asyncio.sleep(3)
        
        playlists["Mamaguevo"].switchPlaying()
    
    asyncio.run(ft.app_async(main))