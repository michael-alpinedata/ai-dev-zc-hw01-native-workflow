# Family Chore Management — MVP Task Backlog

## 1. Establish the Django foundation and family membership model
Goal: Have a runnable Django project with a tested family-member domain foundation.
Description: Initialize or verify the Django project and app structure, dependencies, database configuration, migrations, and test command. Add the family (or household) and membership models, link memberships to Django users, and define Admin and Member roles. Register the models in Django admin and enforce one membership per user per family.
Acceptance criteria:
- [ ] The application starts successfully and the root route returns a successful response.
- [ ] A smoke test passes.
- [ ] Family and membership migrations apply from an empty database.
- [ ] Duplicate memberships are prevented by a database constraint.
- [ ] A focused model test covers role choices and membership behavior.
Out of scope:
- Family creation pages and chore functionality.
Constraints:
- Keep project setup and domain code inside the Django project and existing app.
- Use Django migrations and the existing test framework.

## 2. Build family onboarding and membership management
Goal: Let an authenticated user create a family and maintain its member roster.
Description: Add the create-family flow, family profile edit/list views, and member-management forms. Support assigning Admin or Member roles. Family members should not be able to view or change families they do not belong to.
Acceptance criteria:
- [ ] An authenticated user can create a family.
- [ ] The creator can view and edit the family profile.
- [ ] An Admin can add or change a member's role within the family.
- [ ] A Member cannot perform Admin-only membership actions.
- [ ] A user outside a family receives an authorization response rather than family data.
- [ ] Focused tests cover allowed and denied family-management scenarios.
Out of scope:
- Email invitations and external account provisioning.
Constraints:
- Server-side authorization is required in addition to UI hiding.
- Do not promise or implement invitations unless the requirements are extended.

## 3. Add recurring and shared-pool chore models
Goal: Represent both chore distribution mechanisms in a consistent, validated domain model.
Description: Add recurring chore fields for name, schedule/due information, effort points, ordered rotation participants, optional description, and active/paused state. Add shared-pool fields for title, optional description, effort points, availability/claim/completion state, and family ownership. Include validation for effort points and required assignments.
Acceptance criteria:
- [ ] Both recurring and pool chore types are persisted through migrations.
- [ ] Model tests cover valid values and invalid effort-point or status combinations.
- [ ] A recurring chore can store an ordered participant list.
- [ ] A pool chore can represent available, claimed, completed, and backed-up states.
- [ ] Chores are associated with exactly one family.
Out of scope:
- Recurrence-rule engines and administrative screens.
- Claim, completion, and rotation workflows.
Constraints:
- Keep recurring and pool chores as distinct models or clearly separated type structures.
- Use Django model constraints or validation rather than allowing invalid data silently.

## 4. Build recurring chore administration
Goal: Let family Admins create and maintain recurring rotation chores.
Description: Implement list, create, edit, pause/resume, and archive/delete views for recurring chores. Collect the ordered participating member list and enforce family ownership. Hide privileged actions from Members while still allowing all family members to view recurring chores relevant to their family.
Acceptance criteria:
- [ ] An Admin can create and edit a recurring chore with a participant order.
- [ ] An Admin can pause, resume, or archive a recurring chore.
- [ ] A Member can view recurring chores but cannot use Admin actions.
- [ ] Every view uses the current user's family scope.
- [ ] Tests cover authorized actions and cross-family denied access.
Out of scope:
- Rotation advancement and task completion.
Constraints:
- Reuse the family authorization pattern introduced in task 2.
- Preserve the participant order and inactive state.

## 5. Build shared-pool chore administration and claiming
Goal: Let Admins manage pool chores and Members claim available work.
Description: Implement the pool list and Admin create/edit/remove screens. Add a claim action that assigns an available task to a family Member and a view of claimed tasks. Keep all queries restricted to the user's family.
Acceptance criteria:
- [ ] An Admin can create, edit, and remove pool chores.
- [ ] A Member can claim an available pool chore.
- [ ] A claimed pool chore is visible to its claimant and eligible family members according to the established UI rules.
- [ ] A pool chore cannot be claimed twice by separate requests.
- [ ] Pool views reject cross-family access.
- [ ] Tests cover Admin management, Member claiming, stale claims, and unauthorized access.
Out of scope:
- Point awards and task-completion undo.
Constraints:
- Use an atomic database transition for claiming.
- Prevent duplicate claims from concurrent or repeated requests.

## 6. Implement the recurring rotation engine
Goal: Automatically determine the correct next assignee for recurring chores.
Description: Add the business rule that creates the first assignment and advances to the next eligible participant after completion or a schedule reset. Skip removed, unavailable, or inactive members without losing the original participant history.
Acceptance criteria:
- [ ] A first assignment selects the first eligible participant.
- [ ] Ordinary completion advances to the next eligible participant.
- [ ] Repeated rotations return to the start of the eligible cycle.
- [ ] Removing or deactivating a participant skips that member.
- [ ] Assignment history is retained after the current assignee changes.
- [ ] Tests cover first assignment, ordinary advancement, skipped members, and repeated cycles.
Out of scope:
- Complex recurrence rules or calendar integrations.
Constraints:
- Keep rotation logic separate from HTTP views.
- Make assignment changes persisted and repeatable.

## 7. Add completion, undo, and effort-point ledger
Goal: Immediately reward completed work while safely reversing accidental taps.
Description: Add completion actions for recurring and pool chores and record a traceable point event for every award or reversal. Add an explicit Undo action with stale-request protection. Keep balances derived or persisted as ledger totals rather than editable profile fields.
Acceptance criteria:
- [ ] Completing a recurring chore advances it and awards its effort points.
- [ ] Completing a pool chore marks it complete and awards the claimant's points.
- [ ] An Undo reverses only the completion that has not already been reversed.
- [ ] Undo reverses the corresponding point event without creating a negative balance.
- [ ] Repeated or stale completion/undo requests do not award or reverse work twice.
- [ ] Tests cover recurring completion, pool completion, undo, and duplicate requests.
Out of scope:
- Redemption and backup bonus policy.
Constraints:
- Use atomic database transitions.
- Points never decrease except as an explicitly reversed completion.

## 8. Implement the Request Backup workflow
Goal: Let an assigned member release an overwhelming recurring chore without losing history.
Description: Add Request Backup for overdue or assigned recurring chores. Release the chore into the shared pool, record the requester, and optionally add a configured small bonus for the family member who completes it. Preserve the recurring chore and its assignment history.
Acceptance criteria:
- [ ] An assigned Member or eligible family role can request backup.
- [ ] Requesting backup creates or marks a pool task for the same underlying work.
- [ ] The original recurring chore remains in the system and its history is preserved.
- [ ] The requester is recorded on the backup/pool transition.
- [ ] A repeated backup request cannot create duplicate pool tasks.
- [ ] The optional bonus is awarded only when the backed-up task is completed.
- [ ] Tests cover release, duplicate requests, completion, and family isolation.
Out of scope:
- Automatic backup assignment or paid task marketplaces.
Constraints:
- Keep recurring assignment history separate from pool claim/completion data.

## 9. Build the personal mobile dashboard
Goal: Give each member one focused view of their work and points.
Description: Add a mobile-first dashboard showing signed-in Member assigned recurring chores, claimed pool chores, available pool chores, current point balance, and weekly point target. Keep reminders and reward details in separate views.
Acceptance criteria:
- [ ] The dashboard lists only the signed-in user's family data.
- [ ] Assigned recurring chores and claimed pool chores are shown in separate sections.
- [ ] Available pool chores can be discovered and claimed from the dashboard.
- [ ] The current point balance and weekly target are visible.
- [ ] The layout is usable at a smartphone viewport.
- [ ] Empty states are clear and supportive.
Out of scope:
- Analytics charts and historical trends.
Constraints:
- Reuse the same chore transitions and authorization rules as the management screens.
- Prefer server-rendered responsive behavior unless the project already establishes another pattern.

## 10. Build the reward catalog
Goal: Let families define redeemable real-world rewards.
Description: Add reward models and Admin management screens for name, description, point cost, availability, and optional inventory or quantity limits. Add validation so point costs and inventory cannot be negative.
Acceptance criteria:
- [ ] An Admin can create, edit, and archive or remove family rewards.
- [ ] Reward costs and quantity limits reject negative values.
- [ ] Members can view available family rewards.
- [ ] Reward records are isolated to their family.
- [ ] Model and view tests cover valid rewards and invalid values.
Out of scope:
- Redemption transaction processing.
Constraints:
- Keep catalog administration separate from redemption.

## 11. Implement reward redemption
Goal: Let Members spend earned points safely and preserve transaction history.
Description: Add a redemption action that checks balance and reward availability, records the redemption, and deducts the corresponding cost. Provide Member and Admin views for pending/completed family redemptions and prevent duplicate redemption submissions.
Acceptance criteria:
- [ ] A Member can redeem a reward only when enough points are available.
- [ ] Insufficient balance produces no transaction or balance change.
- [ ] A redemption records reward cost and family/member details.
- [ ] Inventory is reduced without overselling if quantity limits are present.
- [ ] Duplicate submissions do not create duplicate redemptions.
- [ ] Member and Admin redemption views respect family and role boundaries.
- [ ] Tests cover success, insufficient balance, inventory limits, and duplicate requests.
Out of scope:
- External purchase or payment integrations.
Constraints:
- Use atomic database transitions for balance and inventory updates.
- Preserve transaction history.

## 12. Add weekly targets and supportive progress
Goal: Encourage balanced participation without penalties.
Description: Add configurable weekly point targets for each family member and calculate current-week progress from completion ledger data. Add supportive progress text that never describes missed targets as lost points or penalties.
Acceptance criteria:
- [ ] An Admin or Member with the appropriate role can configure the member's weekly target.
- [ ] The dashboard reports points earned in the current week.
- [ ] Progress text is supportive and never negative.
- [ ] Target changes do not retroactively rewrite historical point events.
- [ ] Tests cover week boundaries and target calculation.
Out of scope:
- Historical analytics, rankings, or long-term workload fairness charts.
Constraints:
- Use family timezone or a documented application-time rule for week boundaries.

## 13. Configure Web Push subscriptions
Goal: Let family members opt into browser push notifications securely.
Description: Add subscription storage and a settings page where a Member can enable or remove push notifications for the family. Display unavailable/not-enabled/enabled status and keep VAPID/private keys outside source control.
Acceptance criteria:
- [ ] A Member can add and remove their browser push subscription.
- [ ] Subscription records are scoped to the member and family.
- [ ] The settings page accurately reports unavailable, disabled, and enabled states.
- [ ] Private keys and subscription secrets are read from environment configuration.
- [ ] Tests cover subscription creation/removal and unauthorized access.
Out of scope:
- Sending scheduled reminder content.
Constraints:
- Use documented Django push dependencies or existing project conventions.
- Never commit real credentials.

## 14. Send supportive scheduled reminders
Goal: Notify families about due work and backup requests without repeated or guilt-oriented messaging.
Description: Implement scheduled jobs or management commands for daily due reminders, overdue nudges, and Backup Requested alerts. Deduplicate notifications by task and unchanged state. Document local execution and production scheduling.
Acceptance criteria:
- [ ] A management command sends due, overdue, and backup notifications at the documented times.
- [ ] Notifications include only relevant family members.
- [ ] Repeating the command does not resend an unchanged notification.
- [ ] Message copy remains supportive and non-penalty-oriented.
- [ ] Local and production scheduling are documented.
- [ ] Tests cover recipient selection and deduplication.
Out of scope:
- Real-time notification infrastructure outside browser Web Push.
Constraints:
- Keep scheduling logic callable by Django management commands.

## 15. Add installable PWA support
Goal: Make the application installable and usable as a mobile-first PWA.
Description: Add the web app manifest, service worker, and basic offline shell behavior for previously loaded pages and assets. Verify secure responses and network recovery. Do not implement offline mutations or synchronization.
Acceptance criteria:
- [ ] A valid manifest allows home-screen installation.
- [ ] The service worker caches an appropriate offline shell.
- [ ] The app communicates that network-dependent actions require connectivity.
- [ ] Reload after connectivity is restored resumes normal behavior.
- [ ] Offline task completion or cross-device synchronization is not claimed or implemented.
- [ ] PWA configuration has a smoke test or documented checklist.
Out of scope:
- Offline data changes and conflict resolution.
Constraints:
- Preserve secure HTTPS requirements for production.

## 16. Apply responsive and accessible styling
Goal: Give the MVP a consistent, supportive mobile-first interface.
Description: Apply shared styling to dashboards, forms, task actions, reward screens, and notification settings. Use accessible labels, keyboard-operable controls, visible focus states, sufficient color contrast, and supportive status/error copy.
Acceptance criteria:
- [ ] Core views have a consistent responsive layout at mobile and desktop widths.
- [ ] Controls are keyboard-operable and labeled for assistive technology.
- [ ] Focus states are visible.
- [ ] Text and controls meet agreed contrast requirements.
- [ ] Forms and actions show accessible success/error feedback.
- [ ] Copy avoids guilt, penalties, and alarming error states.
- [ ] Focused UI/accessibility checks cover the primary workflows.
Out of scope:
- Brand redesign or an external design system.
Constraints:
- Keep styles shared and avoid page-specific copies of the same behavior.

## 17. Add family and task isolation integration tests
Goal: Verify every family-facing surface protects its data boundaries.
Description: Add integration tests for family profiles, memberships, recurring chores, pool tasks, point events, rewards, redemptions, backup workflows, subscriptions, and reminders. Cover both Member and Admin roles and cross-family read/write attempts.
Acceptance criteria:
- [ ] A logged-in user cannot read or change another family's profile or members.
- [ ] Cross-family recurring and pool task access is denied.
- [ ] Cross-family point, reward, redemption, and backup data is denied.
- [ ] Member and Admin access differences are covered in integration tests.
- [ ] The full focused test suite passes.
Out of scope:
- New feature behavior beyond boundary verification.
Constraints:
- Reuse test factories/fixtures if established; add only focused shared setup.

## 18. Write MVP deployment documentation and release checks
Goal: Make local setup and production deployment repeatable.
Description: Document setup, environment variables, database configuration, migrations, scheduled jobs, PWA requirements, push secrets, static assets, and production settings differences. Add a concise release checklist and smoke-test sequence.
Acceptance criteria:
- [ ] A clean local setup follows documented commands successfully.
- [ ] Required environment variables are listed without real secret values.
- [ ] Migration, scheduled-job, PWA, and push deployment steps are documented.
- [ ] Production settings clearly differ from development settings where required.
- [ ] A release checklist covers migrations, smoke tests, notifications, and PWA assets.
Out of scope:
- Provider-specific infrastructure provisioning.
Constraints:
- Keep credentials in environment variables.
- Do not include real secrets or private keys in the repository.
