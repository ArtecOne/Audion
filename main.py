import flet as ft
import asyncio
from components import effectObj

class App:
    def __init__(self , page : ft.Page):
        print("updated!")
        
        self.page = page
        
        self.page.adaptive = True
        
        self.page.title = "Hello, World!"
    
        self.page.auto_scroll = True
        
        self.init()
        
    def init(self):

        effectObj.effect.constructor()
        self.page.add(
        )


async def main(page : ft.Page):
    App(page)


asyncio.run(ft.app_async(main))