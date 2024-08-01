# Created by rocco at 7/16/2024
Feature: Test for Cart functionality
  # Enter feature description here

  Scenario: Validate that the "Your cart is empty" message is shown
    Given Open target main page
    When Click on cart icon
    Then Verify correct message is shown