from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

class Transformer(ABC):
    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def get_name(self):
        pass

class UpperCaseTransformer(Transformer):
    def transform(self, data):
        return [item.upper() for item in data]

    def get_name(self):
        return "UpperCase"

class TrimTransformer(Transformer):
    def transform(self, data):
        return [item.strip() for item in data]

    def get_name(self):
        return "Trim"

# Defining the runtime-checkable Protocol
@runtime_checkable
class TransformerProtocol(Protocol):
    def transform(self, data):
        ...

    def get_name(self):
        ...

# New class – no inheritance from Transformer or TransformerProtocol
class ReverseTransformer:
    def transform(self, data):
        return [item[::-1] for item in data]

    def get_name(self):
        return "Reverse"

upper = UpperCaseTransformer()
trim = TrimTransformer()
reverse = ReverseTransformer()

upper_abc = isinstance(upper, Transformer)
reverse_abc = isinstance(reverse, Transformer)
upper_proto = isinstance(upper, TransformerProtocol)
reverse_proto = isinstance(reverse, TransformerProtocol)

print(upper_abc, reverse_abc, upper_proto, reverse_proto)
# True False True True