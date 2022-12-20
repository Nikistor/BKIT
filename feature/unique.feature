Feature: Calculating and obtaining unique meanings

  # Уникальные элементы числового типа
  Scenario Outline: Get unique meaning from a list of numbers
    Given There is a class of unique meanings
    And Get the list: <LIST>
    When Search for unique elements using: <CASE>
    Then Output unique elements: <UNIQUE>

    Examples:
      | LIST                           | UNIQUE       | CASE |
      | [1, 1, 2, 2, 2, 3, 3, 3, 4, 4] | [1, 2, 3, 4] | 0    |
      | [2, 3, 1, 1, 5, 3, 2, 5, 2, 1] | [2, 3, 1, 5] | 0    |
      | [1, 1, 1, 1, 3, 1, 2, 1, 2, 1] | [1, 3, 2]    | 0    |

  # Уникальные элементы символьного типа
  Scenario Outline: Get unique meaning from a list of symbols
    Given There is a class of unique meanings
    And Get the list: <LIST>
    When Search for unique elements using: <CASE>
    Then Output unique elements: <UNIQUE>

    Examples:
      | LIST                                     | UNIQUE                         | CASE |
      | ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'] | ['a', 'A', 'b', 'B']           | 0    |
      | ['c', 'C', 'b', 'A', 'C', 'a', 'c', 'B'] | ['c', 'C', 'b', 'A', 'a', 'B'] | 0    |
      | ['n', 'D', 'm', 'N', 'd', 'n', 'M', 'N'] | ['n', 'D', 'm', 'N', 'd', 'M'] | 0    |


  # Уникальные элементы символьного типа без чувствительного регистра
     # Если <CASE> равен 1, то это верно
  Scenario Outline: Get unique meaning from the ignore_case symbol list
    Given There is a class of unique meanings
    And Get the list: <LIST>
    When Search for unique elements using: <CASE>
    Then Output unique elements: <UNIQUE>

    Examples:
      | LIST                                     | UNIQUE          | CASE |
      | ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'] | ['a', 'b']      | 1    |
      | ['c', 'C', 'b', 'A', 'C', 'a', 'c', 'B'] | ['c', 'b', 'a'] | 1    |

  # Уникальные элементы смешанного типа
     # Если <CASE> равен 1, то это верно
  Scenario Outline: Get unique meanings from a mixed type list
    Given There is a class of unique meanings
    And Get the list: <LIST>
    When Search for unique elements using: <CASE>
    Then Output unique elements: <UNIQUE>

    Examples:
      | LIST                                     | UNIQUE                         | CASE |
      | ['a', 'A', 'b', 'B', '1', '1', '2', '2'] | ['a', 'A', 'b', 'B', '1', '2'] | 0    |
      | ['a', 'A', 'b', 'B', '1', '1', '2', '2'] | ['a', 'b', '1', '2']           | 1    |