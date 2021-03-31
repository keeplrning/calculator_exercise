# calculator_exercise

### Prefix Calculator

Assumptions:

- The system should support the operators {+, -, *, /} which all take exactly two args.
- The input literals are positive integers
- Calculations can be done in the floating-point or integer domain
- Handling division by zero is unimportant; program can crash or do anything if that arises.
- You don't need to consider operator presidence
- You are free to use any programming language of choice but please provide any requirements to run the code EG: Python version or Pip dependencies

### Infix Calculator

Assumptions:

- The system should support the operators {+, -, *, /} which all take exactly two args.
- The input literals are positive integers
- Calculations can be done in the floating-point or integer domain
- Handling division by zero is unimportant; program can crash or do anything if that arises.
- You don't need to consider operator presidence
- You are free to use any programming language of choice but please provide any requirements to run the code EG: Python version or Pip dependencies

### Infix Calculator

The API can be called as:

    http://127.0.0.1:5000/api/v1/calculate_prefix?expression=%2B%203%201
    Result - Calculation Results - 4

    http://127.0.0.1:5000/api/v1/calculate_prefix?exp=%2B%203%201
    Result - Invalid Request!
