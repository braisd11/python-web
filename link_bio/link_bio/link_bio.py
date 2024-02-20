import reflex as rx

from link_bio.styles.styles import Size as Size
import link_bio.styles.styles as styles
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
from link_bio.views.sponsors.sponsors import sponsors



class State(rx.State):
    pass



def index() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(),
                links(), 
                #sponsors(),
                max_width = styles.MAX_WIDTH,
                width="100%",
                margin_y = Size.BIG.value,
                padding = Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style = styles.BASE_STYLE
)
app.add_page(
    index,
    title="Brais Díaz | Carta de presentación",
    description="Web diseñada con Reflex y Python"
)