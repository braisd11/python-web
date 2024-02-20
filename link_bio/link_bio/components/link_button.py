import reflex as rx
from link_bio.styles.styles import Size as Size
import link_bio.styles.styles as styles

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.chakra.image(
                    src=image,
                    height= Size.LARGE.value,
                    margin=Size.DEFAULT.value,
                    alt=title
                ),
                rx.chakra.vstack(
                    rx.chakra.text(title, style= styles.button_title_style),
                    rx.chakra.text(body, style= styles.button_body_style),
                    spacing=Size.SMALL.value,
                    margin= Size.ZERO.value,
                    align_items="start",
                    padding_right= Size.SMALL.value
                ),
                width="100%"
            ),
        ),
        href=url,
        is_external=True,
        width = "100%"

    )



