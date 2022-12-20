Feature: Checking the output of the argument from the list of goods


  # Проверка вывода данных с 1 аргументом
  Scenario Outline: Checking data output with one argument
    Given There is a list of goods
    When Enter <arguments> to get meanings
    Then Output the meanings of <result>

    Examples:
      | arguments | result                                             |
      | title     | [{'title': 'Ковер'},{'title': 'Диван для отдыха'}] |
      | color     | [{'color': 'green'},{'color': 'black'}]            |
      | price     | [{'price': 2000},{'price': 5300}]                  |


  # Проверка вывода данных с 2 аргументами
  Scenario Outline: Checking the output with two arguments
    Given There is a list of goods
    When Enter <arguments> to get meanings
    Then Output the meanings of <result>

    Examples:
      | arguments   | result                                                                                 |
      | title color | [{'title': 'Ковер', 'color': 'green'},{'title': 'Диван для отдыха', 'color': 'black'}] |
      | color price | [{'color': 'green', 'price': 2000},{'color': 'black', 'price': 5300}]                  |


  # Проверка вывода данных с 3 аргументами
  Scenario Outline: Checking the output with three arguments
    Given There is a list of goods
    When Enter <arguments> to get meanings
    Then Output the meanings of <result>

    Examples:
      | arguments         | result                                                                                                                |
      | title color price | [{'color': 'green', 'price': 2000, 'title': 'Ковер'}, {'color': 'black', 'price': 5300, 'title': 'Диван для отдыха'}] |