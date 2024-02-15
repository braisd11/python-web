import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as constant


def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces de Contacto"),
        link_button(
            "LinkedIn", 
            "Mi experiencia laboral",
            constant.LINKEDIN_URL
        ),
        link_button(
            "GitHub", 
            "Mis proyectos y repositorios",
            constant.GITHUB_URL
        ),
        link_button(
            "YouTube (canal secundario)", 
            "Tutoriales semanales",
            constant.REFEX_URL
        ),
        link_button(
            "Discord", 
            "El chat de la comunidad",
            constant.REFEX_URL
        ),
        title("Contacto"),
        link_button(
            "Email", 
            constant.EMAIL_URL,
            f"mailto: {constant.EMAIL_URL}"
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )