from behave import Given, When, Then
from function.filed import field, goods
import ast

@Given('There is a list of goods')
def for_given(text):
    text.data_dictonary = goods
    test = text.data_dictonary
    print(test)

@When("Enter {arguments} to get meanings")
def for_when(text, arguments):
    text.results = field(text.data_dictonary, arguments)

@Then("Output the meanings of {result}")
def for_then(text, result):
    assert text.results == ast.literal_eval(result)