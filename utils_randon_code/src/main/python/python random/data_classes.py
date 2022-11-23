from dataclasses import dataclass, field

@dataclass(frozen=True)
class Person:
    name: str
    address: str
    id: str = field(init=False)
    email_addresses: list[str] = field(default_factory = list)
    active: bool = True
    
    
    
    