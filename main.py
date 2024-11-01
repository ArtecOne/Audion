import flet as ft
import os as os
import asyncio

class App:
    def __init__(self , page : ft.Page):
        print("updated!")

        self.page = page

        self.page.adaptive = True

        self.page.title = "Hello, World!"

        self.page.autoscroll = True

        self.init()

    def init(self):
        text = ft.Text("Hello, World", bgcolor=ft.colors.GREEN)

        self.page.add(
            text
            )

from components.utils.findFile import find_file
url = find_file("music/How_You_Remind_Me.mp3")



async def main(page : ft.Page):

    def volume_down():
        audio1.volume -= 0.1
        audio1.update()

    def volumeup():
        audio1.volume += 0.1
        audio1.update()

    audio1 = ft.Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,
        #onloaded=lambda : print("Loaded"),
        #onduration_changed=lambda e: print("Duration changed:", e.data),
        #on_position_changed=lambda e: print("Position changed:", e.data),
        #on_state_changed=lambda e: print("State changed:", e.data),
        #on_seek_complete=lambda : print("Seek complete"),
    )

    page.overlay.append(audio1)
    page.add(
        ft.ElevatedButton("Play", on_click=lambda *x: audio1.play()),
        ft.ElevatedButton("Pause", on_click=lambda *x: audio1.pause()),
        ft.ElevatedButton("Resume", on_click=lambda *x: audio1.resume()),
        ft.Row(
            [
                ft.ElevatedButton("Volume down", on_click=volume_down),
                ft.ElevatedButton("Volume up", on_click=volumeup),
            ]
        ),
        ft.ElevatedButton(
            "Get duration", on_click=lambda : print("Duration:", audio1.getduration())
        ),
        ft.ElevatedButton(
            "Get current position",
            on_click=lambda : print("Current position:", audio1.get_current_position()),
        ),
    )

    App(page)


asyncio.run(ft.app_async(main))