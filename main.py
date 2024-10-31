import flet as ft
import asyncio

class App:
    def __init__(self , page : ft.Page):
        print("updated!")
        
        self.page = page
        
        self.page.adaptive = True
        
        self.page.title = "Hello, World!"
    
        self.page.auto_scroll = True
        
        self.init()
        
    def init(self):
        text = ft.Text("Hello, World", bgcolor=ft.colors.GREEN)

        self.page.add(
            text
            )


async def main(page : ft.Page):
    
    App(page)


asyncio.run(ft.app_async(main))