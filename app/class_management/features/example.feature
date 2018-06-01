Feature: showing off behave


#  @old
#  Scenario: run a simple test
#    Given we have behave installed
#      When we implement a test
#      Then behave will test it for us
#
#  @new
#  Scenario: run a different simple test
#    Given we have behave installed
#      When we implement another test
#      Then behave will test it for us

  Scenario: Add Department
  Given I am on the department add page
  When I click add button
  And I enter valid data
  Then I should see a success message

#Feature: Testing waters with BDD stack in Django.

#  Scenario: Basic test case.
#    Given we have behave installed
#    When we implement 5 tests
#    Then behave will test them for us!