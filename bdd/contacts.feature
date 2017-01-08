Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <lastname>, <firstname>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | lastname | firstname |
    | Ivanov   | Ivan      |
    | Petrov   | Peter     |
    | Sidorov  | Oleg      |


Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old list without the deleted contact

Scenario Outline: Modify a contact
    Given a non-empty contact list
    Given a random contact from the list
    Given a new contact data <lastname>, <firstname>
    When I modify the contact from the list
    Then the new contact list is equal to the old list with changed contact data

    Examples:
      | lastname | firstname |
      | Ivanov3  | Ivan3     |


Scenario: Delete all contacts
    Given a non-empty contact list
    When I delete all contacts from the list
    Then the new contact list is empty