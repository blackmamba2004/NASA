class FilterMixin:
    @property
    def query_string(self) -> str:
        return (
            "".join(
                f"{field}={value}&"
                for field, value in self.__dict__.items()
                if value is not None
            )
        ).rstrip("&")
    