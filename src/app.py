"""Main module for forgekit - Python utility library."""

def greet(name: str = "Developer") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to forgekit."

def process_data(items: list) -> dict:
    """Process a list of items and return summary statistics."""
    if not items:
        return {"count": 0, "sum": 0, "average": 0}
    return {
        "count": len(items),
        "sum": sum(items),
        "average": sum(items) / len(items)
    }

if __name__ == "__main__":
    print(greet())
    print("Data processed:", process_data([10, 20, 30, 40]))

# Helper added in commit #10
def helper_10():
    return "real-change-10"

# Helper added in commit #21
def helper_21():
    return "real-change-21"
