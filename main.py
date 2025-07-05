import flet as ft

from standard_calculator import create_standard_calculator
from date_calculator import create_date_calculator
from matrix_calculator import create_matrix_calculator
from ratio_calculator import create_ratio_calculator
from base_converter import create_base_converter

def main(page: ft.Page):
    page.title = "多機能電卓アプリ"
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="標準電卓",
                icon=ft.Icons.CALCULATE,
                content=create_standard_calculator(page),
            ),
            ft.Tab(
                text="日付計算",
                icon=ft.Icons.CALENDAR_MONTH,
                content=create_date_calculator(page),
            ),
            ft.Tab(
                text="基数変換",
                icon=ft.Icons.TRANSFORM,
                content=create_base_converter(page),
            ),
            ft.Tab(
                text="行列計算",
                icon=ft.Icons.GRID_ON,
                content=create_matrix_calculator(page),
            ),
            ft.Tab(
                text="比率計算",
                icon=ft.Icons.PERCENT,
                content=create_ratio_calculator(page),
            ),
        ],
        expand=1,
    )

    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)
