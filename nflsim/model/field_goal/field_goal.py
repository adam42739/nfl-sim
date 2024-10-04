MADE = "made"
MISSED = "missed"
BLOCKED = "blocked"
RECOVERED = "recovered"
YARDS_RETURNED = "yards_returned"


class Model:
    def __init__(self):
        pass

    def build(self):
        pass

    def sample(self) -> dict:
        """
        Randomly sample from the model.

        Return
        ------

        ```
        {
            "made" : bool,
            "missed" : bool,
            "blocked" : bool,
            "recovered" : bool,
            "yards_returned" : int
        }
        ```
        """
