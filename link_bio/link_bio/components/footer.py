import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.hstack(
            rx.link(
            f"2014-{datetime.date.today().year} MOUREDEV BY BRAIS MOURE V3.",
            href="https://reflex.dev/docs/library/",
            is_external=True
            ),
            rx.text("BUILDING SOFTWARE WITH ® FROM GALICIA TO THE WORLD.")
        )
    )