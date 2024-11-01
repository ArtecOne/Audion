import flet as ft
import asyncio

class effect:

    def __init__(self, parent: ft.Container, effectType : str):
        
        self.effectType = effectType
        self.parent = parent
        self.width = 276
        self.height = 45
        
        self.init()

    def init(self):
        
        data = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Text(self.effectType , size= 14),
                    ft.Slider(min=0, max=100, divisions=10, label="{value}%")
                ]
            ),
            width=self.width,
            height=self.height
        )

        self.content = ft.Row(
            controls=[
                data
            ]
        )

if __name__ == "__main__":

    async def main(page: ft.Page):
        
        effectsFrame = ft.Container()
        effect_instance = effect(effectsFrame, "Chorus")
        effectsFrame.content = effect_instance.content
        
        page.add(
            effectsFrame
        )

ft.app(target=main)

    