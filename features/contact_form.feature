Feature: Test a contact form

Scenario: Test Contact form
  Given I am on my contact page
  When I send a filled contact form
  Then I see a success message
