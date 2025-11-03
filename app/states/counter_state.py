import reflex as rx


class CounterState(rx.State):
    """The state for the counter application."""

    count: int = 0

    @rx.event
    def increment(self):
        """Increment the count."""
        self.count += 1

    @rx.event
    def decrement(self):
        """Decrement the count."""
        self.count -= 1