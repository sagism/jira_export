Feature: Export JIRA issues to CSV
  Scenario: Run the export script successfully
    Given the script is configured for two JIRA instances
    When the script is executed
    Then a CSV file is created with results from both instances
    And the log file is created with required entries

