import flet as ft

def create_ratio_calculator(page: ft.Page):
    a = ft.TextField(label="A", width=70)
    b = ft.TextField(label="B", width=70)
    c = ft.TextField(label="C", width=70)
    d = ft.TextField(label="D", width=70)
    result_text = ft.Text("ここに結果が表示されます", size=16)

    def calculate_ratio(e):
        try:
            vals = {
                'a': a.value,
                'b': b.value,
                'c': c.value,
                'd': d.value
            }

            # 空のフィールドを探す
            empty_fields = [k for k, v in vals.items() if not v]
            if len(empty_fields) != 1:
                result_text.value = "エラー: 未知数は1つにしてください。"
                page.update()
                return

            unknown = empty_fields[0]

            val_a = float(a.value) if a.value else None
            val_b = float(b.value) if b.value else None
            val_c = float(c.value) if c.value else None
            val_d = float(d.value) if d.value else None

            # A:B = C:D -> A*D = B*C
            result = ""
            if unknown == 'd':
                if val_a == 0:
                    result = "不定" if val_b * val_c == 0 else "不能"
                else:
                    value = (val_b * val_c) / val_a
                    d.value = f"{value}"
                    result = f"D = {value:.4f}"
            elif unknown == 'c':
                if val_b == 0:
                    result = "不定" if val_a * val_d == 0 else "不能"
                else:
                    value = (val_a * val_d) / val_b
                    b.value = f"{value}"
                    result = f"C = {value:.4f}"
            elif unknown == 'b':
                if val_c == 0:
                    result = "不定" if val_a * val_d == 0 else "不能"
                else:
                    value = (val_a * val_d) / val_c
                    c.value = f"{value}"
                    result = f"B = {value:.4f}"
            elif unknown == 'a':
                if val_d == 0:
                    result = "不定" if val_b * val_c == 0 else "不能"
                else:
                    value = (val_b * val_c) / val_d
                    a.value = f"{value}"
                    result = f"A = {value:.4f}"

            result_text.value = result

        except (ValueError, TypeError):
            result_text.value = "エラー: 数値を入力してください。"
        except ZeroDivisionError:
            result_text.value = "Error: Devided by zero."

        page.update()

    # --- Layout ---
    return ft.Column(
        controls=[
            ft.Text("比率計算 (A : B = C : D)", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("未知数としたい項目を1つだけ空にして計算してください。", text_align=ft.TextAlign.CENTER),
            ft.Row([a, ft.Text(":", size=20), b], alignment=ft.MainAxisAlignment.CENTER),
            ft.Text("=", size=20),
            ft.Row([c, ft.Text(":", size=20), d], alignment=ft.MainAxisAlignment.CENTER),
            ft.ElevatedButton("計算", on_click=calculate_ratio),
            result_text,
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
