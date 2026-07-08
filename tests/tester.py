from app.utils.encoder import Base62Encoder
from app.utils.obfuscator import Obfuscator

id = 123456

obfuscated = Obfuscator.obfuscate(id)

encoded = Base62Encoder.encode(obfuscated)

decoded = Base62Encoder.decode(encoded)

original = Obfuscator.deobfuscate(decoded)

print(id)
print(original)

assert id == original