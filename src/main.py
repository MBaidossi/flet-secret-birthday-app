import flet as ft
import flet_lottie as ftl

def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    confetti = ftl.Lottie(
        src="confetti.json",
        width=300,
        height=300,
        animate=True,
        repeat=False,
        visible=False
    )

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=counter,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
