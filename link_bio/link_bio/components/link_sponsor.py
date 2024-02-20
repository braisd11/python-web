import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_sponsor(image: str, url: str, alt: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=image,
            height=Size.VERY_BIG.value,
            width="auto",
            alt=alt
        ),
        href=url,
        is_external=True
    )
    