Feature: ING akceptacja ciasteczek

  Scenario: użytkownik może pomyślnie dostosować ustawienia plików cookie
    Given użytkownik jest na stronie startowej
    When użytkownikowi wyświetla się okno wyboru cieasteczek
    And użytkownik akceptuje ciasteczka analityczne
    And użytkownik akceptuje zaznaczone zgody
    Then ciasteczka, w tym analityczne, są zapisane
