import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(
            src="logobrais2.png",
            heigth=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo con un nombre"
        ),

        rx.chakra.link(
            f"2014-{datetime.date.today().year} MOUREDEV BY BRAIS MOURE V3.",
            href=const.REFLEX_URL,
            is_external=True,
            font_size= Size.MEDIUM.value
        ),

        rx.chakra.text(
            "BUILDING SOFTWARE WITH ® FROM GALICIA TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            padding_top=Size.ZERO.value,
            white_space="normal"
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value
    )