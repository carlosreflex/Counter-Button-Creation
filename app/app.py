import reflex as rx
from app.states.counter_state import CounterState


def counter_button(text: str, on_click: rx.event.EventType, icon: str) -> rx.Component:
    """A styled button for the counter."""
    return rx.el.button(
        rx.icon(icon, class_name="h-5 w-5"),
        rx.el.span(text),
        on_click=on_click,
        class_name="flex items-center justify-center gap-2 px-6 py-3 text-sm font-bold text-white bg-indigo-600 rounded-lg shadow-[0px_4px_8px_rgba(0,0,0,0.15)] hover:bg-indigo-700 hover:shadow-[0px_8px_16px_rgba(0,0,0,0.2)] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-300 ease-in-out",
    )


def index() -> rx.Component:
    """The main page of the app."""
    return rx.el.main(
        rx.el.div(
            rx.el.h1(
                "Counter App",
                class_name="text-3xl font-bold text-gray-800 mb-4 font-['Lora']",
            ),
            rx.el.p(
                "A simple counter built with Reflex and Material Design 3 principles.",
                class_name="text-gray-600 mb-12 text-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        CounterState.count,
                        class_name="text-7xl font-bold text-indigo-600 font-['Lora'] tabular-nums",
                    ),
                    class_name="flex items-center justify-center w-48 h-48 bg-white rounded-full shadow-[0px_1px_3px_rgba(0,0,0,0.12)] mb-8",
                ),
                rx.el.div(
                    counter_button("Decrement", CounterState.decrement, "minus"),
                    counter_button("Increment", CounterState.increment, "plus"),
                    class_name="flex items-center gap-4",
                ),
                class_name="flex flex-col items-center p-8 bg-gray-50 rounded-2xl shadow-[0px_4px_8px_rgba(0,0,0,0.15)] border border-gray-200",
            ),
            class_name="flex flex-col items-center justify-center text-center min-h-screen",
        ),
        class_name="font-['Lora'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lora:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)