
'''
Ref: https://semaphoreci.com/community/tutorials/bdd-testing-a-restful-web-application-in-python
Allow defining steps and store values to be used across each step in the
world object.
'''
from lettuce import step, world, before
from nose.tools import assert_equals
from app.application import app, USERS
import json
#from app.views import USERS

@before.all
def before_all():
    world.app = app.test_client()

@step(u'Given some users are in the system')
def given_some_users_are_in_the_system(step):
    USERS.update({'david01': {'name': 'David'}})

@step(u'When I retrieve the customer \'(.*)\'')
def when_i_retrieve_the_customer_group1(step, username):
    '''
    A capture group is used in the regular expression allowing us to
    pass in variables to the step. This allows for the reuse of steps.
    '''
    world.response = world.app.get('/user/{}'.format(username))

@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And the following user details are returned:')
def and_the_following_user_details(step):
    assert_equals(step.hashes, [json.loads(world.response.data)])

