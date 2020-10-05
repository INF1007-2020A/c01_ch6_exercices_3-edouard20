#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from structs import Queue, Stack
from collections import deque

def reverse_data(data: list = None):
    # TODO: Demander 10 valeurs à l'utilisateur,
    # les stocker dans une structure de données,
    # et les retourner en ordre inverse, sans utiliser de liste.

    if data is None:
       data = [input("Entrez une valeur: ") for _ in range(10)] 
      # Stocker le résultat ici
    s = Stack()
    s.put_many(data)

    return [s.get() for _ in range(len(s))]


def delete_nth_from_stack(data: Stack, position: int) -> Stack:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    temp_stack = Stack()
    for i in range(len(data) - position - 1):
        temp_stack.get(data.put(i))
    data.put(position)
    for i in range(len(data)):
        data.get(temp_stack.put(i))

    return data


def delete_nth_from_queue(data: Queue, position: int) -> Queue:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.

    return Queue()


def sort_stack(data: Stack) -> Stack:
    # TODO: Retourner la séquence triée
    return Stack()


def sort_queue(data: Queue) -> Queue:
    # TODO: Retourner la séquence triée
    return Queue()


def string_and_structs(string: str) -> tuple:
    # TODO: Parcourez la chaîne de caractères.
    # Si le caractère est une lettre, on l'ajoute dans fifo.
    # Sinon, on retire un élément de fifo pour l'insérer dans lifo.

    fifo, lifo = Queue(), Stack()

    return fifo, lifo


def main() -> None:
    # print("On inverse des données...")
    # print(f"Résultat: {reverse_data()}")

    n = 4
    lifo = Stack()
    lifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la pile et on obtient: {delete_nth_from_stack(lifo, n)}")

    # n = 6
    # fifo = Queue()
    # fifo.put_many([i for i in range(20)])
    # print(f"On retire l'élément à la position {n} de la file et on obtient: {delete_nth_from_queue(fifo, n)}")

    # lifo = Stack()
    # lifo.put_many([randint(0, 1000) for _ in range(20)])
    # print(f"On ordonne une file: {sort_stack(lifo)}")

    # fifo = Queue()
    # fifo.put_many([randint(0, 1000) for _ in range(20)])
    # print(f"On ordonne une file: {sort_queue(fifo)}")

    # sequence = "te!eYy.E6e/T"
    # print(f"Le résulat de la manipulation de la séquence: {string_and_structs(sequence)}")


if __name__ == '__main__':
    main()
