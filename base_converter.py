import flet as ft

def create_base_converter(page: ft.Page):
    def convert_and_update(e):
        input_value = input_field.value.strip().lower()
        selected_base = int(base_selector.value)

        if not input_value:
            dec_output.value = ""
            bin_output.value = ""
            oct_output.value = ""
            hex_output.value = ""
            error_text.value = ""
            page.update()
            return

        try:
            decimal_value = int(input_value, selected_base)

            dec_output.value = str(decimal_value)
            bin_output.value = bin(decimal_value)[2:]
            oct_output.value = oct(decimal_value)[2:]
            hex_output.value = hex(decimal_value)[2:].upper()

            error_text.value = ""

        except ValueError:
            error_text.value = f"エラー: 無効な値です。"
            dec_output.value = ""
            bin_output.value = ""
            oct_output.value = ""
            hex_output.value = ""

        page.update()


    input_field = ft.TextField(
        label="値を入力してください",
        on_change=convert_and_update,
        autofocus=True,
    )

    base_selector = ft.Dropdown(
        label="入力値の基数",
        value="10",
        options=[
            ft.dropdown.Option("2", "2進数 (Binary)"),
            ft.dropdown.Option("8", "8進数 (Octal)"),
            ft.dropdown.Option("10", "10進数 (Decimal)"),
            ft.dropdown.Option("16", "16進数 (Hexadecimal)"),
        ],
        on_change=convert_and_update,
    )

    dec_output = ft.TextField(label="10進数 (Decimal)", read_only=True)
    bin_output = ft.TextField(label="2進数 (Binary)", read_only=True)
    oct_output = ft.TextField(label="8進数 (Octal)", read_only=True)
    hex_output = ft.TextField(label="16進数 (Hexadecimal)", read_only=True)

    error_text = ft.Text(color=ft.Colors.RED, weight=ft.FontWeight.BOLD)

    # --- Layout ---
    return ft.Column(
        controls=[
            ft.Text("基数変換", size=20, weight=ft.FontWeight.BOLD),
            ft.Row(
                controls=[
                    ft.Container(content=input_field, expand=True),
                    ft.Container(content=base_selector, width=150),
                ]
            ),
            error_text,
            ft.Divider(),
            dec_output,
            bin_output,
            oct_output,
            hex_output,
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
