"""Python frameworks overview.

This module introduces several popular Python frameworks used for web development,
API creation, and backend services.
"""

from dataclasses import dataclass
from collections.abc import Callable


@dataclass(frozen=True)
class FrameworkProfile:
    """A structured profile for a Python framework."""

    name: str
    category: str
    use_case: str
    strengths: tuple[str, ...]


FRAMEWORKS = (
    FrameworkProfile(
        name="Flask",
        category="Micro web framework",
        use_case="Small to medium APIs and web apps with minimal boilerplate.",
        strengths=("Simple", "Flexible", "Easy to learn"),
    ),
    FrameworkProfile(
        name="Django",
        category="Full-stack web framework",
        use_case="Large, database-driven web applications with built-in admin and ORM.",
        strengths=("Batteries included", "Secure", "Scalable"),
    ),
    FrameworkProfile(
        name="FastAPI",
        category="Modern API framework",
        use_case="High-performance REST APIs and async backend services.",
        strengths=("Fast", "Type safe", "Automatic docs"),
    ),
    FrameworkProfile(
        name="Pyramid",
        category="General-purpose web framework",
        use_case="Custom web applications that need flexibility and extensibility.",
        strengths=("Flexible", "Extensible", "Good for enterprise apps"),
    ),
    FrameworkProfile(
        name="Sanic",
        category="Async web framework",
        use_case="High-throughput applications that benefit from async I/O.",
        strengths=("Async-first", "Fast", "Good for real-time services"),
    ),
)


class CustomFramework:
    """A tiny example of building a framework around reusable routing logic."""

    def __init__(self) -> None:
        self._routes: dict[tuple[str, str], Callable[[], str]] = {}

    def route(self, path: str, method: str = "GET") -> Callable:
        """Register a handler with a decorator, for example @app.route('/')."""

        def register(handler: Callable[[], str]) -> Callable[[], str]:
            self._routes[(method.upper(), path)] = handler
            return handler

        return register

    def dispatch(self, path: str, method: str = "GET") -> tuple[int, str]:
        """Run the handler for a route, or return a simple not-found response."""

        handler = self._routes.get((method.upper(), path))
        if handler is None:
            return 404, "Not Found"
        return 200, handler()


def show_frameworks() -> None:
    """Print a simple summary of the frameworks in this module."""

    for framework in FRAMEWORKS:
        print(f"{framework.name} - {framework.category}")
        print(f"  Use case: {framework.use_case}")
        print(f"  Strengths: {', '.join(framework.strengths)}")
        print()


def best_for_project(project_type: str) -> str:
    """Return a suggested framework based on the type of project."""

    recommendations = {
        "api": "FastAPI",
        "small_web_app": "Flask",
        "large_business_app": "Django",
        "async_service": "Sanic",
        "custom_app": "Pyramid",
    }

    return recommendations.get(project_type, "Flask")


if __name__ == "__main__":
    print("Frameworks in Python\n")
    show_frameworks()
    print(f"Recommended for a REST API: {best_for_project('api')}")

    app = CustomFramework()

    @app.route("/hello")
    def hello() -> str:
        return "Hello from a custom framework!"

    status, response = app.dispatch("/hello")
    print(f"\nCustom framework response ({status}): {response}")

