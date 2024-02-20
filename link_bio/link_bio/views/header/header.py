import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.fonts import Font as Font
import link_bio.constants as const



def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(
                name="Brais Díaz",
                size="xl", 
                src="foto.jpg",
                bg=Color.CONTENT.value,
                color= TextColor.BODY.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.chakra.vstack(
                rx.chakra.heading(
                    "Brais Díaz",
                    size="lg"
                ),
                rx.text(
                    "@braisdr11",
                    padding_top = Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.chakra.hstack(
                    link_icon(
                        const.LINKEDIN_ICO,
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    link_icon(
                        const.GITHUB_ICO,
                        const.GITHUB_URL,
                        "Github"
                    ),
                    link_icon(
                        const.EMAIL_ICO,
                        f"mailto: {const.EMAIL_URL}",
                        "Mail"
                    ),
                    link_icon(
                        const.SPOTIFY_ICO,
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        const.R_ICO,
                        const.REFLEX_URL,
                        "Reflex"
                    ),
                    spacing=Size.DEFAULT.value
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),

        rx.chakra.flex(
            info_text("+1", "años de experiencia"),
            rx.chakra.spacer(),
            info_text("+1", "años de experiencia"),
            rx.chakra.spacer(),
            info_text("+1", "años de experiencia"),
            width="100%"
        ),

        rx.chakra.text(
            """Soy ingeniero de software backend.
            Estudié el ciclo superior de DAM en el IES de Teis en Vigo.
            En el ciclo aprendí Java y Python con respecto a lenguajes de programación.
            Sobre Bases de Datos aprendí MySql.
            También aprendí HTML, CSS y Android Studio entre otras cosas.""",
            color = TextColor.BODY.value,
            font_size=Size.MEDIUM.value
        ),
        spacing= Size.BIG.value,
        align_items= "start"
    )