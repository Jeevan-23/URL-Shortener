from app.config import SECRET_KEY


class Obfuscator:

    @staticmethod
    def obfuscate(id: int) -> int:
        return id ^ SECRET_KEY

    @staticmethod
    def deobfuscate(value: int) -> int:
        return value ^ SECRET_KEY