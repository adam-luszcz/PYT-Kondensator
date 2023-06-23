# PYT-Kondensator

Aplikacja będąca prostym klonem znanego w polsce serwisu "elektroda.pl", wykonana na zaliczenie przedmiotu PYT.

## REST API

#### GET

* http://127.0.0.1:5000/api/thread/<thread_id>/get-posts - zwraca wszystkie posty w danym wątku
* http://127.0.0.1:5000/api/get-all-posts - zwraca wszystkie posty
* http://127.0.0.1:5000/api/get-topics - zwraca wszystkie tematy
* http://127.0.0.1:5000/api/topic/<topic_id>/get-threads - zwraca wszystkie wątki w danym temacie

#### POST

* http://127.0.0.1:5000/api/add-topic - dodaje nowy temat, musi on zostać przekazany w formacie JSON:

```
{
    "name": "nazwa_tematu"
}
```