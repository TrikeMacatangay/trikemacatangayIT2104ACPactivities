from capybara import Capybara

def main():
    test_case_number = int(input("Enter the test case number: "))
    if test_case_number == 1:
        capybara = Capybara("Biscoff", "M", 5)
        print(f"Test Case {test_case_number}: Name: {capybara.name}, Gender: {capybara.gender}, Age: {capybara.age} years old")

main()
