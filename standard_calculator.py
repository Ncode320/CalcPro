import flet as ft

def create_standard_calculator(page: ft.Page):
    result_display = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        expand=True,
        border_color="transparent",
        text_size=40
    )

    def button_clicked(e):
        data = e.control.data
        current_value = result_display.value

        if data == "=":
            try:
                expression = current_value.replace("×", "*").replace("÷", "/")
                result = eval(expression)
                result_display.value = str(result)
            except Exception:
                result_display.value = "エラー"
        elif data == "C":
            result_display.value = "0"
        else:
            if current_value == "0" and data not in ["+", "-", "×", "÷"]:
                result_display.value = data
            else:
                result_display.value += data

        page.update()

    buttons = [
        ("7", "8", "9", "÷"),
        ("4", "5", "6", "×"),
        ("1", "2", "3", "-"),
        ("C", "0", "=", "+"),
    ]

    button_controls = []
    for row in buttons:
        row_controls = []
        for text in row:
            btn = ft.ElevatedButton(
                text=text,
                data=text,
                on_click=button_clicked,
                expand=True,
                height=60,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    bgcolor=ft.Colors.WHITE24 if text in "C=÷×-+" else ft.Colors.WHITE10
                )
            )
            row_controls.append(btn)
        button_controls.append(ft.Row(controls=row_controls, expand=True))

    # --- Layout ---
    return ft.Column(
        controls=[
            ft.Row(controls=[result_display]),
            *button_controls
        ],
        expand=True
    )
