ALLOW = {"search": False}  # default: tools are OFF until responsibility is acknowledged


def responsibility_handshake():
    global ALLOW
    print("\nP-04 Responsibility Handshake:")
    print("I confirm I am accountable for outcomes of tool use.")
    ok = input("Type YES to proceed: ").strip().upper() == "YES"
    ALLOW["search"] = ok


def tool_search(query: str):
    if not ALLOW["search"]:
        raise PermissionError("BLOCKED: upstream responsibility not installed (P-04).")
    return f"[tool] searching for: {query}"


def agent(prompt: str):
    if "search:" in prompt:
        q = prompt.split("search:", 1)[1].strip()
        return tool_search(q)
    return "No tool needed."


if __name__ == "__main__":
    try:
        print(agent("search: reversible entanglement battery paper"))
    except Exception as e:
        print("->", e)

    responsibility_handshake()
    print(agent("search: reversible entanglement battery paper"))  
