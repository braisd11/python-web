import reflex as rx

from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor
from link_bio.styles.styles import Size as Size
import link_bio.constants as const 


def sponsors() -> rx.Component:
    return rx.chakra.vstack(
        title("Colaboran"),
        rx.chakra.responsive_grid(
            link_sponsor(
                "favicon.ico",
                const.REFLEX_URL,
                "Favicon"
            ),
            link_sponsor(
                "logo.png",
                const.GITHUB_URL,
                "LavaDogs"
            ),
            spacing=Size.BIG.value,
            columns=[1, 2]
        ),
        width="100%",
        align_items="start"
    )