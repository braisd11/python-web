import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.box(
            rx.chakra.span("brais", color=Color.PRIMARY.value),
            rx.chakra.span("diro", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x= Size.BIG.value,
        padding_y= Size.DEFAULT.value,
        z_index="999",
        top="0"
    )