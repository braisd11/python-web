import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as constant


def links() -> rx.Component:
    return rx.chakra.vstack(
        title("Sobre Mi"),
        link_button(
            "LinkedIn", 
            "Mi experiencia laboral",
            constant.LINKEDIN_ICO,
            constant.LINKEDIN_URL
        ),
        link_button(
            "GitHub", 
            "Mis proyectos y repositorios",
            constant.GITHUB_ICO,
            constant.GITHUB_URL
        ),
        # link_button(
        #     "YouTube (canal secundario)", 
        #     "Tutoriales semanales",
        #     constant.YOUTUBE_ICO,
        #     constant.REFLEX_URL
        # ),
        # link_button(
        #     "Discord", 
        #     "El chat de la comunidad",
        #     constant.DISCORD_ICO,
        #     constant.REFLEX_URL
        # ), 
        title("Contacto y Enlaces de Interés"),
        link_button(
            "Email", 
            constant.EMAIL_URL,
            constant.EMAIL_ICO,
            f"mailto: {constant.EMAIL_URL}"
        ),
        link_button(
            "Spotify", 
            "Lo que me gusta escuchar",
            constant.SPOTIFY_ICO,
            constant.SPOTIFY_URL
        ),
        link_button(
            "Reflex Library", 
            "Libreria con los componentes de Reflex",
            constant.R_ICO,
            constant.REFLEX_URL
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )