from behave import Given, When, Then
from function.get_roots import get_roots


@Given('I have a function calculation root')
def step_impl(context):
    pass


@Given("I get coefficient: {A}, {B}, {C}")
def given_increment(context, A, B, C):
    context.A = int(A)
    context.B = int(B)
    context.C = int(C)
    print(f'Коэффициенты: {A}, {B}, {C}')


@When("Calculating")
def given_increment(context):
    roots = get_roots(context.A, context.B, context.C)
    context.results = roots
    # print(f'Корни: {roots}')


@Then("Watch roots: {root1}, {root2}, {root3}, {root4}")
def then_results(context, root1, root2, root3, root4):
    len_roots = len(context.results)

    # Вывод корней
    if len_roots == 0:
        # assert (context.results == 0)
        print('Нет корней')
    elif len_roots == 1:
        assert context.results == float(root1)
        # print('Один корень {}'.format(round(root1, 2)))
    elif len_roots == 2:
        assert round(context.results[0], 2) == float(root1)
        assert round(context.results[1], 2) == float(root2)
        print('Два корня: {} и {}'.format(root1, root2))
    elif len_roots == 3 and int(root1) == 0.0:
        assert round(context.results[0], 2) == float(root1)
        assert round(context.results[1], 2) == float(root2)
        assert round(context.results[2], 2) == float(root3)
        print('Три корня: {} и {} и {}'.format(root1, root2, root3))
    elif len_roots == 3:
        assert round(context.results[0], 2) == float(root1)
        assert round(context.results[1], 2) == float(root2)
        print('Два корня: {} и {}'.format(root1, root2))
    elif len_roots == 4:
        assert round(context.results[0], 2) == float(root1)
        assert round(context.results[1], 2) == float(root2)
        assert round(context.results[2], 2) == float(root3)
        assert round(context.results[3], 2) == float(root4)
        print('Четыре корня: {} и {} и {} и {}'.format(root1, root2, root3, root4))
    else:
        print('Ошибка! Корней нет!')
