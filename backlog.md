# Development Backlog

## 1. Add household and member models
Create a household model and a member profile linked to Django's built-in user model, with Admin and Member roles. Register the models in Django admin and add migrations.

**Done when:** migrations apply successfully and tests cover household membership and role choices.

## 2. Model chores and assignment types
Add chore models that support recurring rotation chores and claimable shared-pool chores, including point values, due dates, and assignment state.

**Done when:** both chore types can be represented and validated, with migrations and focused model tests.

## 3. Add role-aware chore management
Let admins create and manage household chores, and let members see chores for their household. Enforce household boundaries and role permissions.

**Done when:** core pages are usable and tests verify authorized and unauthorized access.

## 4. Implement chore assignment and completion
Build the rotation and shared-pool workflows: assign or claim chores, mark them complete, undo accidental completion, and request backup for a rotation chore.

**Done when:** rotation advances correctly, pool chores can be claimed, and tests cover completion, undo, and backup transitions.

## 5. Add points and rewards
Award points for completed chores and let members redeem available points for admin-configured household rewards.

**Done when:** point balances update correctly and tests cover earning points and valid or insufficient-balance redemptions.

## 6. Make the app mobile-friendly and add reminders
Create a responsive, installable PWA experience and send supportive reminders for due or overdue chores and backup requests.

**Done when:** key chore flows work on mobile-sized screens and notification behavior is tested.

## Later
Defer workload analytics and complex custom recurrence rules until after family testing.
