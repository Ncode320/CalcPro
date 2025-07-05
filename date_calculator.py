import flet as ft
import datetime
import time
import threading

def create_date_calculator(page: ft.Page):
    today = datetime.date.today()
    reiwa_year = today.year - 2018
    date_str = f"令和{reiwa_year}年 (西暦{today.year}年) {today.month}月{today.day}日"

    date_display = ft.Text(date_str, size=18, weight=ft.FontWeight.BOLD)
    time_display = ft.Text(size=24, weight=ft.FontWeight.BOLD)

    def update_time():
        while True:
            now = datetime.datetime.now()
            time_display.value = now.strftime("%H:%M:%S")
            try:
                page.update()
            except Exception as e:
                break
            time.sleep(1)

    time_thread = threading.Thread(target=update_time, daemon=True)
    time_thread.start()


    # --- 1. 日付差計算 ---

    def on_start_date_change(e):
        start_date_field.value = e.control.value.strftime('%Y-%m-%d')
        start_date_picker.open = False
        page.update()

    def on_end_date_change(e):
        end_date_field.value = e.control.value.strftime('%Y-%m-%d')
        end_date_picker.open = False
        page.update()

    start_date_picker = ft.DatePicker(
        on_change=on_start_date_change,
        first_date=datetime.datetime(year=2000, month=1, day=1),
        last_date=datetime.datetime.now() + datetime.timedelta(days=365*5),
    )
    end_date_picker = ft.DatePicker(
        on_change=on_end_date_change,
        first_date=datetime.datetime(year=2000, month=1, day=1),
        last_date=datetime.datetime.now() + datetime.timedelta(days=365*5),
    )

    page.overlay.extend([start_date_picker, end_date_picker])

    def open_start_datepicker(e):
        start_date_picker.open = True
        page.update()

    def open_end_datepicker(e):
        end_date_picker.open = True
        page.update()

    start_date_field = ft.TextField(label="開始日 (YYYY-MM-DD)", value="2000-01-01", expand=True)
    end_date_field = ft.TextField(label="終了日 (YYYY-MM-DD)", value=datetime.date.today().strftime("%Y-%m-%d"), expand=True)

    start_date_picker_button = ft.IconButton(
        icon=ft.Icons.CALENDAR_MONTH,
        tooltip="カレンダーから開始日を選択",
        on_click=open_start_datepicker,
    )
    end_date_picker_button = ft.IconButton(
        icon=ft.Icons.CALENDAR_MONTH,
        tooltip="カレンダーから終了日を選択",
        on_click=open_end_datepicker,
    )

    date_diff_result_text = ft.Text("ここに結果が表示されます", size=16)

    def calculate_date_diff(e):
        try:
            start_date = datetime.datetime.strptime(start_date_field.value, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date_field.value, "%Y-%m-%d").date()
            delta = end_date - start_date
            date_diff_result_text.value = f"差は {delta.days} 日です。"
        except ValueError:
            date_diff_result_text.value = "エラー: 日付の形式が正しくありません (YYYY-MM-DD)。"
        page.update()

    # --- 2. 日数変換 ---

    days_input_field = ft.TextField(label="変換したい日数を入力", keyboard_type=ft.KeyboardType.NUMBER, value="1000")
    conversion_result_text1 = ft.Text(size=16)
    conversion_result_text2 = ft.Text(size=16)

    def convert_days(e):
        try:
            days = int(days_input_field.value)
            if days < 0:
                conversion_result_text1.value = "エラー: 正の整数を入力してください。"
                conversion_result_text2.value = ""
                page.update()
                return

            years = days // 365
            remaining_days_after_years = days % 365
            weeks_in_remaining = remaining_days_after_years // 7
            days_in_remaining = remaining_days_after_years % 7

            conversion_result_text1.value = f"→ {years} 年 {weeks_in_remaining} 週間 {days_in_remaining} 日"

            total_weeks = days // 7
            days_in_total_weeks = days % 7
            conversion_result_text2.value = f"→ または {total_weeks} 週間 {days_in_total_weeks} 日"

        except (ValueError, TypeError):
            conversion_result_text1.value = "エラー: 有効な数値を入力してください。"
            conversion_result_text2.value = ""
        page.update()

    convert_days(None)

    # --- Layout ---
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        date_display,
                        time_display,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=10,
                border_radius=10,
                bgcolor=ft.Colors.BLUE_50,
                margin=ft.margin.only(bottom=10)
            ),
            ft.Divider(),
            ft.Text("日付差計算", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([start_date_field, start_date_picker_button]),
            ft.Row([end_date_field, end_date_picker_button]),
            ft.ElevatedButton("差を計算", on_click=calculate_date_diff, expand=True),
            date_diff_result_text,

            ft.Divider(height=10, color="transparent"),
            ft.Divider(),
            ft.Divider(height=10, color="transparent"),

            ft.Text("日数変換", size=20, weight=ft.FontWeight.BOLD),
            days_input_field,
            ft.ElevatedButton("変換", on_click=convert_days, expand=True),
            conversion_result_text1,
            conversion_result_text2,
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.ADAPTIVE
    )
