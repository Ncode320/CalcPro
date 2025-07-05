import flet as ft
import numpy as np
from functools import reduce

class InputMatrix(ft.Column):
    def __init__(self, matrix_name: str, on_update_needed):
        super().__init__()
        self.matrix_name = matrix_name
        self.on_update_needed = on_update_needed
        self.spacing = 5
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.rows_dd = ft.Dropdown(
            label="行", value="2", width=75,
            options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
            on_change=self.rebuild_grid,
        )
        self.cols_dd = ft.Dropdown(
            label="列", value="2", width=75,
            options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
            on_change=self.rebuild_grid,
        )

        self.grid_container = ft.Column(spacing=5)

        self.controls = [
            ft.Text(f"行列 {self.matrix_name}", weight=ft.FontWeight.BOLD),
            ft.Row([self.rows_dd, self.cols_dd], alignment=ft.MainAxisAlignment.CENTER),
            self.grid_container,
        ]

        self.field_grid = []
        self.rebuild_grid()

    def rebuild_grid(self, e=None):
        self.grid_container.controls.clear()
        self.field_grid.clear()

        rows = int(self.rows_dd.value)
        cols = int(self.cols_dd.value)

        for i in range(rows):
            row_fields = []
            for j in range(cols):
                field = ft.TextField(
                    value="0", width=55, height=45,
                    text_align=ft.TextAlign.CENTER,
                    border_width=1, border_radius=5,
                    label=f"{self.matrix_name}{i+1}{j+1}",
                )
                row_fields.append(field)
            self.field_grid.append(row_fields)
            self.grid_container.controls.append(ft.Row(controls=row_fields, spacing=5))

        self.on_update_needed()

    def get_value(self) -> np.ndarray:
        rows = int(self.rows_dd.value)
        cols = int(self.cols_dd.value)
        matrix_data = []
        for i in range(rows):
            row_data = [float(self.field_grid[i][j].value or 0) for j in range(cols)]
            matrix_data.append(row_data)
        return np.array(matrix_data)

def create_matrix_calculator(page: ft.Page):
    matrix_count_dropdown = ft.Dropdown(
        label="行列の数", value="2",
        options=[ft.dropdown.Option(str(i)) for i in range(2, 11)],
        width=150,
    )

    matrix_input_area = ft.Row(
        wrap=True, spacing=20, run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    result_area = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    error_text = ft.Text(color=ft.Colors.RED, weight=ft.FontWeight.BOLD)

    def update_matrix_inputs(e=None):
        matrix_count = int(matrix_count_dropdown.value)
        matrix_input_area.controls.clear()
        matrix_names = [chr(ord('A') + i) for i in range(matrix_count)]

        for name in matrix_names:
            matrix_input_area.controls.append(InputMatrix(name, page.update))

        update_result_display(clear=True)
        page.update()

    def update_result_display(result_mat: np.ndarray = None, clear: bool = False):
        result_area.controls.clear()
        result_area.controls.append(ft.Text("=", size=24, weight=ft.FontWeight.BOLD))

        if clear:
            page.update()
            return

        if result_mat is not None:
            rows, cols = result_mat.shape
            grid = []
            for i in range(rows):
                row_texts = []
                for j in range(cols):
                    text_val = f"{result_mat[i, j]:.2f}"
                    row_texts.append(
                        ft.Container(
                            content=ft.Text(text_val, text_align=ft.TextAlign.CENTER),
                            width=55, height=45,
                            border=ft.border.all(1, ft.Colors.BLACK26),
                            border_radius=5, alignment=ft.alignment.center,
                        )
                    )
                grid.append(ft.Row(controls=row_texts, spacing=5))
            result_area.controls.extend(grid)
        page.update()

    def calculate_matrix_product(e):
        error_text.value = ""
        try:
            matrices = [control.get_value() for control in matrix_input_area.controls]
            result = reduce(np.dot, matrices)
            update_result_display(result_mat=result)

        except ValueError as ve:
            error_text.value = f"計算エラー: 行列の次元が一致しません。"
        except Exception as err:
            error_text.value = f"予期せぬエラー: {err}"
        page.update()

    matrix_count_dropdown.on_change = update_matrix_inputs
    update_matrix_inputs()

    # --- Layout ---
    return ft.Column(
        controls=[
            ft.Text("行列の積", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([matrix_count_dropdown], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            matrix_input_area,
            ft.Divider(),
            ft.ElevatedButton("計算", on_click=calculate_matrix_product, icon=ft.Icons.CALCULATE),
            error_text,
            result_area,
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.ADAPTIVE,
    )
