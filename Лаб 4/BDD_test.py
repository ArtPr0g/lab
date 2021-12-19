from behave import *
from TDD_test import *

@given("Computer_Builder")
def first_step(context):
    context.a = Computer_Builder_Test()

@when("test_electro_builder return OK")
def test_electro_builder(context):
    context.a.test_shatura_builder()

@when("test_elcomp_builder return OK")
def test_elcomp_builder(context):
    context.a.test_elcomp_builder()

@then("Good job")
def last_step(context):
    pass

