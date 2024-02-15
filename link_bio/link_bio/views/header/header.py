import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
import link_bio.constants as const



def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Brais Díaz", size="xl"),
            rx.vstack(
                rx.heading(
                    "Brais Díaz",
                    size="lg",
                    color=TextColor.HEADER.value
                ),
                rx.text(
                    "@braisdr11",
                    padding_top = Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(const.X_URL),
                    link_icon(const.X_URL),
                    link_icon(const.X_URL),
                    link_icon(const.X_URL),
                    link_icon(const.X_URL)
                ),
                align_items="start"
            ),
            spacing=Size.BIG.value
        ),

        rx.flex(
            info_text("+1", "años de experiencia"),
            rx.spacer(),
            info_text("+1", "años de experiencia"),
            rx.spacer(),
            info_text("+1", "años de experiencia"),
            width="100%"
        ),

        rx.text(
            """Soy ingeniero de software backend.
            Estudié el ciclo superior de DAM en el IES de Teis en Vigo.
            En el ciclo aprendí Java, Python con respecto a lenguajes de programación.
            Sobre Bases de Datos aprendí MySql.
            También aprendí HTML, CSS y Android Studio entre otras cosas.""",
            color = TextColor.BODY.value
        ),
        spacing= Size.BIG.value,
        align_items= "start"
    )