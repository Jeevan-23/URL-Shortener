BASE62 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


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

        encoded.reverse()

        return "".join(encoded)