Feature: ING akceptacja ciasteczek

  Scenario Outline: użytkownik może pomyślnie dostosować ustawienia plików cookie
    Given użytkownik jest na stronie startowej
    When użytkownikowi wyświetla się okno wyboru cieasteczek
    And użytkownik akceptuje ciasteczka analityczne
    And użytkownik akceptuje zaznaczone zgody
    Then ciasteczka, w tym analityczne, są zapisane

    @fast
    Examples:
      | Numer testu  |
      | Test 1       |
    @multiple
    Examples:
      | Numer testu  |
      | Test 1       |
      | Test 2       |
      | Test 3       |
      | Test 4       |