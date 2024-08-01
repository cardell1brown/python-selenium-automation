# Created by rocco at 7/23/2024
Feature: Target main page search test using scenario outlines
  # Enter feature description here

  Scenario: User can search for a truck on target
    Given Open target main page
    When Search for truck
    Then Verify search worked for truck
    Then Verify correct url is displayed for <string>

  Scenario: User can search for a ps5 on target
    Given Open target main page
    When Search for ps5
    Then Verify search worked for ps5
    Then Verify correct url is displayed for <string>

  Scenario: User can search for a xbox on target
    Given Open target main page
    When Search for xbox
    Then Verify search worked for xbox
    Then Verify correct url is displayed for <string>

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search worked for <expected_result>
    Then Verify correct url is displayed for <expected_result>
    Examples:
    |product |expected_result  |
    |coffee  |coffee           |
    |tea     |tea              |
    |iphone  |iphone           |