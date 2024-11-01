import flet as ft
import os as os
import asyncio
from components.utils.findFile import find_file

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


class musicPlayer(ft.Audio):
    def __init__(self, balance, volumen):

        super().__init__(volume = volumen, balance = balance, src='.')
        
        self.audio = None

    def setAudio(self, url):
        self.src=url

    def volume_down(self, _):
        self.volume -= 0.1
        self.update()

    def volume_up(self, _):
        self.volume += 0.1
        self.update()

    def avanzar(self, _):
        self.seek(self.get_current_position() + 5000)
    
    def retroceder(self, _):
        self.seek(self.get_current_position() - 5000)
        

async def main(page : ft.Page):

    audio1 = musicPlayer(volumen=1, balance=1)
    audio2 = musicPlayer(volumen=1, balance=-1)

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = find_file(f"music/{e.files[0].name}")
        
        audio1.setAudio(selected_files.value)
        audio1.update()
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    

    # Open directory dialog
    def get_directory_result(e: ft.FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()

    get_directory_dialog = ft.FilePicker(on_result=get_directory_result)
    directory_path = ft.Text()

    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, get_directory_dialog])

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False
                    ),
                ),
                selected_files,
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "Open directory",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path,
            ]
        ),
    )


    page.overlay.append(audio1)
    page.overlay.append(audio2)
    page.add(
        ft.ElevatedButton("Play", on_click=lambda *x: audio1.play()),
        ft.ElevatedButton("Play", on_click=lambda *x: audio2.play()),
        ft.ElevatedButton("Pause", on_click=lambda *x: audio1.pause()),
        ft.ElevatedButton("Resume", on_click=lambda *x: audio1.resume()),
        ft.ElevatedButton("Retroceder 5s", on_click= audio1.retroceder),
        ft.ElevatedButton("Avanzar 5s", on_click= audio1.avanzar),
        ft.ElevatedButton("prueba", on_click=lambda *x: print(url)),
        ft.Row(
            [
                ft.ElevatedButton("Volume down", on_click=audio1.volume_down),
                ft.ElevatedButton("Volume up", on_click=audio1.volume_up),
            ]
        ),
        ft.ElevatedButton(
            "Get duration", on_click=lambda *x: print("Duration:", audio1.get_duration())
        ),
        ft.ElevatedButton(
            "Get current position",
            on_click=lambda *x: print("Current position:", audio1.get_current_position()),
        ),
    )

    App(page)


asyncio.run(ft.app_async(main))