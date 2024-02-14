import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size



def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Brais Díaz", size="xl"),
            rx.vstack(
                rx.heading(
                    "Brais Díaz",
                    size="lg"
                ),
                rx.text(
                    "@braisdr11",
                    padding_top = "0px !important"
                ),
                rx.hstack(
                    link_icon("https://x.com"),
                    link_icon("https://x.com"),
                    link_icon("https://x.com")
                ),
                align_items="start"
            ),
            spacing=Size.BIG.value
        ),

        rx.flex(
            info_text("+13", "años de experiencia"),
            rx.spacer(),
            info_text("+13", "años de experiencia"),
            rx.spacer(),
            info_text("+13", "años de experiencia"),
            width="100%"
        ),

        rx.text("""Soy ingeniero de software desde hace más de 12 años.
                Actualmente trabajo como freelance full-stack developer iOS y Android.
                Además creo contenido formativo sobre programación y tecnología en redes.
                Aquí podrás encontrar todos mis enlaces de interés. ¡Bienvenida!)"""),
        spacing= Size.DEFAULT.value,
        align_items= "start"
    )