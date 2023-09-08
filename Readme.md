<h2>TP24 Technical Test - Description</h2>
Domain Overview

```
The technical team at TP24 build technology to support the wider organisation in its B2B lending business. 
A key part in how we do this is by ingesting and analysing receivables from prospective clients to help our organisation decide if we should lend to a business, and how much we are comfortable providing.

Receivables are debts owed to a company for goods or services which have been provided but not yet paid for. Invoices and credit notes can be considered types of receivables.
```

Brief

```
Write a basic set of HTTP APIs which follows best practices to provide the following capabilities:

  ● Accept a payload containing receivables data (see example payload below) and store it
  ● Return summary statistics about the stored receivables data; specifically the value of open and closed invoices

The test is open ended and candidates should make and document assumptions about their solution.
Candidates are free to interpret the data and apply business logic as they see fit, however the format of the payload should not differ from the example below.
```

Guidance and Additional Notes
```
  ● The solution should be easily runnable and well tested
  ● The completed test can be submitted either as a GitHub repository or as a zip via email
  ● We encourage candidates to note how much time they spend on the test in the readme
  ● Your solution will be reviewed and then discussed during the technical interview
```



<h2>How to run.</h2>

- Install python
- Install pip

```cmd
pip install flask
pip install flask_sqlalchemy
python .\app.py 
```

<h2>How to test api</h2>

Use postman.

[Post]
http://127.0.0.1:5000/api/receivables

- payload
```
[
  {
    "reference": "require",
    "currencyCode": "require",
    "issueDate": "require",
    "openingValue": 1234.56,
    "paidValue": 1234.56,
    "dueDate": "require",
    "closedDate": "optional",
    "cancelled": true,
    "debtorName": "require",
    "debtorReference": "string",
    "debtorAddress1": "optional",
    "debtorAddress2": "optional", 
    "debtorTown": "optional",
    "debtorState": "optional",
    "debtorZip": "optional",
    "debtorCountryCode": "require",
    "debtorRegistrationNumber": "optional"
  }
]
```

[Get]
http://127.0.0.1:5000/api/receivables/summary