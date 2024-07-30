# Intro
It'a collections of all pattern help me on working time to do the unit test, It's a fake ecommerce web


# How to run

# Topic cover
- []Stubs
- []Mocks
- []Spies
- []Fakes
- []Dummies
- []Test Doubles
- []Dummy Objects
- []Fake Object

# Anti-pattern
## Story I
Description
As an emergency maintenance engineer, I need to directly modify the order status in the database to quickly resolve customer complaints without going through the existing business logic and use cases.
Acceptance Criteria

	1.	In the event of an order status error, I can directly connect to the database and change the order status without using the application layer or business logic.
	2.	The updated order status should take effect immediately and be reflected in the front-end interface.
	3.	The modification should not trigger any business logic or event handling (such as notifying the user or updating inventory).