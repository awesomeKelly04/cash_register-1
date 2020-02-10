# cash_register
A transaction logging and tracking application. A zero to hero application on building a transaction logging and management.

## Milestones
- Functional implementation of transaction log input and storage (Data structure)
- Functional implementation and CLI search of transactions based on time parameters
- Refactoring to OOP
- Connecting with MySql Database
- Designing a UI to collect and visualize the inputs (HTML / CSS/ Bootstrap)
- Asynchronous Calls (AJAX with JAvaScript) and Backend Development with Flask (Python)

## Milestone 1
The application at the satged will be developed in python using just functions to collect, validate, store and retrieve input details about the transactions. The choice of data structure is __*List of Dictionaries*__. The information structure is destribed below

>[
>    {
>        "customer_name": "james",
>        "product": [
>            {
>                "product_name": "spoon",
>                "product_quantity": 20.0,
>                "product_price": 12.0
>            },
>            {
>                "product_name": "50",
>                "product_quantity": 5.0,
>                "product_price": 100.0
>            }
>            ...another product detail dictionary
>        ],
>        "time": "10/02/2020 10:57"
>    },
>    ...another transaction dictionary
>]
