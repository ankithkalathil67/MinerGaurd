# How to contribute

## The workflow

1. **Pick an Issue** on GitHub and click "Assign yourself."
2. **Make a branch** in GitHub Desktop (Current branch → New branch).
   Name it after your feature, like `st-pats-countdown`.
3. **Write your code** and test it on your laptop.
4. **Commit** with a short message saying what you did.
5. **Push** your branch (Publish branch / Push origin).
6. **Open a pull request** on GitHub. Mention your Issue, like "Closes #4".
7. **Someone reviews it.** Fix anything they ask for, then it gets merged.

Nobody pushes straight to `main`. Every change goes through a pull request.

## Adding a tool for the AI agent

A tool is a normal Python function with `@tool` on top. The docstring tells
the AI **when** to use it, so make it clear.

```python
from langchain.tools import tool

@tool
def st_pats_countdown() -> str:
    """Return how many days until St. Pat's at Missouri S&T.
    Use this when someone asks about St. Pat's."""
    ...
```

Test it on its own first, no Discord needed:

```python
print(st_pats_countdown.invoke({}))
```

Once it works, add it to the `TOOLS = [...]` list in `bot.py`.

## Rules

- **Never commit `.env` or any token.** If you do by accident, tell an officer right away.
- Test your code before opening a pull request.
- Keep pull requests small: one feature each.
- Stuck? Comment on your Issue or message an officer.
