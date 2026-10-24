
import flet as ft
import flet_lottie as ftl


def main(page: ft.Page):
    page.title = "Mohammad Baidossi"
    page.bgcolor = ft.Colors.RED_100

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    PASSWORD = "1234"
    BIRTHDAY_PASSWORD = "04072003"

    def create_confetti():
        return ftl.Lottie(
            src="Confetti.json",
            width=500,
            height=500,
            animate=True,
            repeat=True
        )

    def show_special_birthday():
        page.clean()

        birthday_text = ft.Text(
            "CONGRATS YOU FOUND THE SECRET BIRTHDAY MESSAGE!",
            size=30,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )

        page.add(
            birthday_text,
            create_confetti(),
            ft.Button("Log out", on_click=lambda e: show_login())
        )

    def show_home():
        page.clean()

        welcome_text = ft.Text(
            "Welcome to my app!",
            size=30,
            weight=ft.FontWeight.BOLD
        )

        logout_button = ft.Button(
            "Log out",
            on_click=lambda e: show_login()
        )

        page.add(welcome_text, create_confetti(), logout_button)

    # Normal click
    def submit_clicked(e):
        if user_input.value == PASSWORD:
            show_home()
        else:
            user_input.error_text = "Incorrect password!"
            page.update()

    # Long press
    def submit_long_pressed(e):
        if user_input.value == BIRTHDAY_PASSWORD:
            show_special_birthday()
        else:
            user_input.error_text = "Incorrect password!"
            page.update()

    def show_login():
        page.clean()

        user_input.value = ""
        user_input.error_text = None

        submit_button = ft.Button(
            "Submit",
            on_click=submit_clicked,
            on_long_press=submit_long_pressed
        )

        container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Hello, World!", size=30),
                    ft.Text("Enter your password"),
                    user_input,
                    submit_button
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                tight=True
            ),
            padding=50,
            bgcolor=ft.Colors.WHITE,
            border_radius=30
        )

        page.add(container)

    user_input = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        width=300
    )

    show_login()


ft.run(main, assets_dir="../src/assets")
