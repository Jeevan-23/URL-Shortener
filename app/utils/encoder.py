BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Base62Encoder:

    @staticmethod
    def encode(number: int) -> str:

        if number == 0:
            return BASE62[0]

        encoded = []

        while number > 0:

            remainder = number % 62

            encoded.append(BASE62[remainder])

            number //= 62

        return "".join(reversed(encoded))

    @staticmethod
    def decode(value: str) -> int:

        decoded = 0

        for ch in value:

            decoded *= 62

            decoded += BASE62.index(ch)

        return decoded