Feature: Test
    Scenario: Test Builder
      Given Computer_Builder
      When test_electro_builder return OK
      And test_elcomp_builder return OK
      Then Good job
