from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()

    pq.enqueue({"name_file": "a", "qtd_linhas": 10})
    pq.enqueue({"name_file": "b", "qtd_linhas": 3})
    pq.enqueue({"name_file": "c", "qtd_linhas": 9})

    assert len(pq) == 3

    search_pq = pq.search(1)
    assert search_pq["name_file"] == "a"
    assert search_pq["qtd_linhas"] == 10

    pq.dequeue()
    assert len(pq) == 2

    pq.dequeue()
    assert len(pq) == 1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(999)
