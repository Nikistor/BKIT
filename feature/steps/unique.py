from behave import Given, When, Then
from function.unique import Unique
import ast

@Given('There is a class of unique meanings')
def for_given(text):
    pass

@Given("Get the list: {LIST}")
def for_given_and(text, LIST):
    text.LIST = list(ast.literal_eval(LIST))
    print(f'Список: {LIST}')

@When("Search for unique elements using: {CASE}")
def for_when(text, CASE):
    check = bool(int(CASE))
    if (check == True):
        unique_list = Unique(text.LIST, ignore_case=check)
    else:
        unique_list = Unique(text.LIST)
    text.results = unique_list

@Then("Output unique elements: {UNIQUE}")
def for_then(text, UNIQUE):
    assert text.results.arr == ast.literal_eval(UNIQUE)
    print(f'Уникальные элементы: {text.results.arr}')