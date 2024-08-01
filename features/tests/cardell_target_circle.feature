# Created by rocco at 7/19/2024
Feature: Target circle verification
  # Enter feature description here

  Scenario: Validate that the target circle page will open and ten benefit cells are present
    Given Open target circle page
    Then Verify 10 benefit cells are present