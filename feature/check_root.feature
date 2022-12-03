Feature: The biquadrate equation

   # Нет корней
  Scenario Outline: Checking the roots of biquadrate equations: NO ROOT
    Given I have a function calculation root
    And I get coefficient: <A>, <B>, <C>
    When Calculating
    Then Watch roots: <root1>, <root2>, <root3>, <root4>

    Examples:
      | A | B | C  | root1 | root2 | root3 | root4 |
      | 1 | 0 | 10 | 0     | 0     | 0     | 0     |


    # Два корня
  Scenario Outline: Checking the roots of biquadrate equations: TWO ROOTS
    Given I have a function calculation root
    And I get coefficient: <A>, <B>, <C>
    When Calculating
    Then Watch roots: <root1>, <root2>, <root3>, <root4>

    Examples:
      | A | B  | C   | root1 | root2 | root3 | root4 |
      | 1 | -4 | 4   | 1.41  | -1.41 | 0     | 0     |
      | 1 | -5 | -36 | 3     | -3    | 0     | 0     |


    # Три корня
  Scenario Outline: Checking the roots of biquadrate equations: TWO ROOTS
    Given I have a function calculation root
    And I get coefficient: <A>, <B>, <C>
    When Calculating
    Then Watch roots: <root1>, <root2>, <root3>, <root4>

    Examples:
      | A  | B  | C | root1 | root2 | root3 | root4 |
      | -4 | 16 | 0 | 0     | 2     | -2    | 0     |


    # Четыре корня
  Scenario Outline: Checking the roots of biquadrate equations: FOUR ROOTS
    Given I have a function calculation root
    And I get coefficient: <A>, <B>, <C>
    When Calculating
    Then Watch roots: <root1>, <root2>, <root3>, <root4>

    Examples:
      | A | B  | C | root1 | root2 | root3 | root4 |
      | 1 | -5 | 6 | 1.73  | -1.73 | 1.41  | -1.41 |
      | 1 | -5 | 4 | 2.0   | -2.0  | 1.0   | -1.0  |