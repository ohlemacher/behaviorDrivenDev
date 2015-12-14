# -*- coding: utf-8 -*-

'''
Allow defining steps and store values to be used across each step in the
world object.
'''
from lettuce import step, world, before
from nose.tools import assert_equals
from app.application import app, USERS
import json

# Test user query
@before.all
def before_all():
    '''Setup for testing.'''
    world.app = app.test_client()

@step(u'Given some users are in the system')
def given_some_users_are_in_the_system(step):
    '''Add a user to USERS for testing against.'''
    USERS.update({'david01': {'name': 'David'}})

@step(u'When I retrieve the user \'(.*)\'')
def when_i_retrieve_the_user_group1(step, username):
    '''
    A capture group is used in the regular expression allowing us to
    pass in variables to the step. This allows for the reuse of steps.
    '''
    world.response = world.app.get('/users/{}'.format(username))

@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
    '''Check the status_code.'''
    assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And the following user details are returned:')
def and_the_following_user_details(step):
    '''Check the correct user data is in the response.'''
    assert_equals(step.hashes, [json.loads(world.response.data)])


# Test existing user deletion
@step(u'When I delete the user \'([^\']*)\'')
def when_i_delete_the_user_group1(step, username):
    world.response = world.app.delete('/users/{}'.format(username))

@step(u'And the message \'([^\']*)\' is returned')
def and_the_message_group1_is_returned(step, group1):
    assert_equals(world.response.data, group1)

@step(u'And the user \'([^\']*)\' is removed')
def and_the_user_group1_is_removed(step, group1):
    world.response = world.app.get('/users/{}'.format(group1))
    assert_equals(world.response.status_code, int(404))

