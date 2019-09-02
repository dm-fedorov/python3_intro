# annotation_for.py
from typing import TypeVar, Iterable, Optional

Num = TypeVar('Num', int, float)

def sum(items: Iterable[Num]) -> Num:
    # Если вы пометите переменную типом int и попытаетесь присвоить ей float, будет ошибка.
    # Аннотация Optional позволяет указать опциональный тип.
    accum: Optional[float] 
    accum = 0
    for item in items:
        accum += item
    return accum

print(sum([1.0, 2, 3]))