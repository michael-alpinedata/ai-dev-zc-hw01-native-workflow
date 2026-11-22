# Family Chore Management Tool — Product Specification (v1)

## 1. Product Vision & Tone
A supportive (*bienveillant*), mobile-first household management tool designed for families. Instead of relying on guilt, strict penalties, or constant parental micromanagement, the app encourages positive reinforcement, shared responsibility, and mutual support.

---

## 2. Target Users & Roles
The app supports individual family profiles with two distinct role levels:

* **Admins (Parents):**
  * Create, edit, and delete recurring rotation tasks and pool tasks.
  * Assign point values and configure the reward catalog.
  * Participate in chores and earn/redeem points alongside everyone else.
* **Members (Kids / Teens):**
  * View their personal assigned rotation tasks and the shared pool.
  * Mark tasks as complete (or undo accidental clicks).
  * Request backup on overdue or overwhelming rotation tasks.
  * Redeem earned points for family rewards.

---

## 3. Core Mechanics

### A. Hybrid Chore Distribution
1. **Automated Rotation (Recurring Essentials):**
   * Chores that happen on a predictable schedule (e.g., unloading the dishwasher, taking out the trash, feeding pets).
   * Automatically cycles through assigned family members upon completion or schedule reset.
2. **Shared Point Pool (Flexible & Ad-Hoc Chores):**
   * Tasks that sit in a shared backlog (e.g., vacuuming the living room, washing the car, organizing shoes).
   * Any family member can claim and complete tasks from the pool at their convenience.

### B. Effort-Weighted Points & Gamified Rewards
* **Effort-Weighted Scoring:** Tasks are assigned point values based on time and effort (e.g., `1 pt` for a quick 5-minute tidy, `5 pts` for a deep clean).
* **Weekly Baseline:** Each member has a friendly weekly target to encourage balanced participation.
* **Reward Catalog:** Surplus points (or accumulated points) can be redeemed for real-world family perks defined by the household—such as choosing Friday night's movie, picking dinner, or using a "Skip My Rotation Turn" pass.

### C. Completion & Supportive Overdue Handling
* **Honor System + Undo:** Tapping **Done** immediately logs completion, advances the rotation, and awards points—no approval bottleneck required. An **Undo** option allows users to reverse accidental taps.
* **Supportive Reminders + "Request Backup" (Zero-Guilt Policy):**
  * Points only ever go *up*, never down.
  * If a rotation task passes its due time, it gently rolls over with a supportive push notification.
  * If a member is busy or overwhelmed, they can tap **"Request Backup"** to voluntarily release their rotation task into the shared pool (optionally with a small bonus point incentive) so another family member can step in to help.

---

## 4. Platform & Technical Scope (v1 MVP)
* **Interface:** Mobile-first Progressive Web App (PWA) accessible from any smartphone browser and installable to the home screen.
* **Notifications:** Web Push notifications for daily reminders, gentle overdue nudges, and "Backup Requested" alerts to the family.
* **MVP Boundaries (Included in v1):**
  * Family profile & role management (Admin vs. Member).
  * Automated rotation engine + Shared task pool.
  * Effort-weighted point tracking + Reward redemption catalog.
  * Instant completion with Undo + "Request Backup" workflow.
  * Push notifications.
* **Deferred to v2 (Post-Family Testing):**
  * Historical analytics and long-term workload fairness charts.
  * Complex custom recurrence rules or calendar integrations.

---

## 5. Next Steps for Family Discussion
* [ ] Agree on the initial list of recurring rotation chores vs. shared pool chores.
* [ ] Decide on point scales (e.g., 1–5 scale) and weekly targets per age group.
* [ ] Brainstorm 5–10 fun, motivating rewards for the catalog together.