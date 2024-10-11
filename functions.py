from dataclasses import dataclass
import random


@dataclass
class MultiplicationTable:
    table: str
    question: str
    answer: int


def generate_random_tables(tables):
    multiplication_tables = []
    for table in tables:
        for i in range(1, 11):
            multiplication_tables.append(MultiplicationTable(table, f"{table} x {i} =", int(table) * i))
    random.shuffle(multiplication_tables)
    return multiplication_tables