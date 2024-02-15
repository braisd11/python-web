import reflex as rx
import datetime

from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),

        rx.link(
            f"2014-{datetime.date.today().year} MOUREDEV BY BRAIS MOURE V3.",
            href="https://reflex.dev/docs/library/",
            is_external=True,
            font_size= Size.MEDIUM.value
        ),

        rx.text(
            "BUILDING SOFTWARE WITH ® FROM GALICIA TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            padding_top=Size.ZERO.value

        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )