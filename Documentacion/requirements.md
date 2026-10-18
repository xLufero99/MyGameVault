# Functional and Non-Functional Requirements — Video Game Tracking Platform

## Context

**Problem:** gamers don't have a centralized way to track which video games they have played, are currently playing, want to play, or dropped — nor to rate them and discover new games.

**Goal:** a MyAnimeList/Backloggd-style platform for video games: catalog, personal progress tracking, ratings/reviews, and discovery.

**Out of scope (v1):** multiplayer/chat, store integrations (Steam/PSN), a custom achievements system, monetization, premium/semi-admin roles.

**Actors:** Guest, Registered user, Admin. (Dev staff and the external game API are technical/secondary actors, documented separately, outside this file.)

---

## FR — Guest (not registered)

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | The system must allow any guest to browse the game catalog | MVP |
| FR-02 | The system must allow filtering the catalog by genre, platform, and year | MVP |
| FR-03 | The system must allow searching games by name | MVP |
| FR-04 | The system must display a game detail page with info, screenshots, and average rating | MVP |
| FR-05 | The system must display the reviews associated with a game | MVP |
| FR-06 | The system must allow viewing a registered user's profile if it is public | MVP |
| FR-07 | The system must display only the username if the profile is private, hiding list, ratings, reviews, and stats | MVP |
| FR-08 | The system must redirect to the register/login screen when a guest attempts to rate, review, or add a game to a list | MVP |
| FR-09 | The system must allow a guest to search games via advanced recommendation filters (e.g. open world, available on Steam) | Phase 2 |
| FR-10 | The system must allow a guest to read forum posts without being able to participate | Phase 2 |
| FR-11 | The system must allow a guest to read published articles | Phase 2 |

---

## FR — Registered user

*(inherits all Guest FRs)*

| ID | Requirement | Priority |
|---|---|---|
| FR-12 | The system must allow a user to register with email and password | MVP |
| FR-13 | The system must allow a user to log in | MVP |
| FR-14 | The system must allow a user to log out | MVP |
| FR-15 | The system must allow a user to add a game to their personal list with a status (playing, completed, on hold, dropped, plan to play) | MVP |
| FR-16 | The system must allow a user to change the status of a game on their list | MVP |
| FR-17 | The system must allow a user to record a start date and end date for playing a title | MVP |
| FR-18 | The system must allow a user to rate a game on a 1-to-10 scale | MVP |
| FR-19 | The system must allow a user to write a review for a game | MVP |
| FR-20 | The system must allow a user to edit their own review | MVP |
| FR-21 | The system must allow a user to delete their own review | MVP |
| FR-22 | The system must allow a user to mark a game as favorite | MVP |
| FR-23 | The system must allow a user to set their profile visibility (public/private) | MVP |
| FR-24 | The system must allow a user to edit their profile (avatar, bio) | MVP |
| FR-25 | The system must display basic user stats (completed games, favorite genre) | MVP |
| FR-26 | The system must allow a user to delete their own account | MVP |
| FR-27 | The system must allow a user to create custom themed lists | Phase 2 |
| FR-28 | The system must allow a user to add custom tags to a game | Phase 2 |
| FR-29 | The system must allow a user to comment on another user's review | Phase 2 |
| FR-30 | The system must allow a user to mark another user's review as helpful | Phase 2 |
| FR-31 | The system must allow a user to compare their list with another user's | Phase 2 |
| FR-32 | The system must notify a user about relevant interactions (comments, etc.) | Phase 2 |
| FR-33 | The system must allow a user to export their list as CSV/JSON | Phase 2 |
| FR-34 | The system must display recent activity history on a user's profile | Phase 2 |
| FR-35 | The system must allow a user to log granular playtime | Phase 2 |
| FR-36 | The system must allow a user to post on the forum | Phase 2 |
| FR-37 | The system must allow a user to write articles | Phase 2 |
| FR-38 | The system must allow a user to follow other users | Phase 2 |

---

## FR — Admin

| ID | Requirement | Priority |
|---|---|---|
| FR-39 | The system must allow the admin to add a game to the catalog | MVP |
| FR-40 | The system must allow the admin to edit an existing game's information | MVP |
| FR-41 | The system must allow the admin to remove a game from the catalog | MVP |
| FR-42 | The system must allow the admin to manage genres, categories, and platforms | MVP |
| FR-43 | The system must allow the admin to delete reviews/comments that violate community rules | Phase 2 |
| FR-44 | The system must allow the admin to delete forum posts | Phase 2 |
| FR-45 | The system must allow the admin to review a queue of reported content | Phase 2 |
| FR-46 | The system must allow the admin to apply progressive sanctions to a user (warning, temporary ban, permanent ban) | Phase 2 |
| FR-47 | The system must allow the admin to view a user's sanction history | Phase 2 |
| FR-48 | The system must notify a user when they receive a sanction | Phase 2 |

---

## Non-Functional Requirements (NFR)

*Adapted for a personal/portfolio project, with no client or commercial SLA, built by 4 people.*

### Performance

| ID | Requirement | Priority |
|---|---|---|
| NFR-01 | Catalog and search pages must respond in under 1 second with up to 10,000 indexed games | MVP |
| NFR-02 | Database queries for listings must use pagination (max 20-50 results per page) | MVP |
| NFR-03 | Images (screenshots, covers) must be served optimized/compressed or via CDN | Phase 2 |

### Security

| ID | Requirement | Priority |
|---|---|---|
| NFR-04 | Passwords must be stored hashed (bcrypt/argon2), never in plain text | MVP |
| NFR-05 | Authentication must use JWT with expiration and token renewal | MVP |
| NFR-06 | Write endpoints (rate, review, edit profile, admin) must validate role-based authorization on the backend, not only hide buttons on the frontend | MVP |
| NFR-07 | The system must sanitize/validate all user input to prevent SQL injection and XSS | MVP |
| NFR-08 | Sensitive variables (API keys, JWT secrets, DB credentials) must be kept out of source code (environment variables, non-versioned `.env`) | MVP |
| NFR-09 | The system must implement basic rate limiting on login/registration endpoints to mitigate brute force attacks | Phase 2 |

### Usability

| ID | Requirement | Priority |
|---|---|---|
| NFR-10 | The interface must be responsive (usable on desktop and mobile) | MVP |
| NFR-11 | Forms must display clear, specific error messages | MVP |
| NFR-12 | Main navigation must be reachable within 2 clicks from any screen | Should |

### Availability and Maintainability

| ID | Requirement | Priority |
|---|---|---|
| NFR-13 | The system must run automated tests (unit + integration for critical endpoints) on every push via CI | MVP |
| NFR-14 | The code must follow a consistent style standard (configured linter) | MVP |
| NFR-15 | The system must log backend errors for debugging | MVP |
| NFR-16 | The system must have a development environment separate from production | MVP |
| NFR-17 | The system must have automated database backups in production | Phase 2 |
| NFR-18 | The uptime target is "best effort" (no commercial SLA), documented as an internal reference goal | Phase 2 |

### Scalability

| ID | Requirement | Priority |
|---|---|---|
| NFR-19 | The data model must support catalog growth without redesign (indexes on genre, platform, title) | MVP |
| NFR-20 | The architecture must allow adding new user roles without modifying the authentication schema | MVP |

### Compatibility

| ID | Requirement | Priority |
|---|---|---|
| NFR-21 | The system must work correctly on the most-used modern browsers (Chrome, Firefox, Safari, Edge — last 2 versions) | MVP |

### Legal / Privacy

| ID | Requirement | Priority |
|---|---|---|
| NFR-22 | The system must allow a user to delete their account and associated data (linked to FR-26) | MVP |
| NFR-23 | The system must disclose in a basic privacy notice what data is collected and why | Should |

---

## Business Rules (BR)

*Domain constraints that are not "features" in themselves, but govern how the FRs behave. They map directly to the data model and backend validations.*

### Users and accounts

| ID | Rule |
|---|---|
| BR-01 | A user's email must be unique across the system |
| BR-02 | The username must be unique, and always publicly visible even if the profile is private |
| BR-03 | A user cannot have two simultaneous roles (the `role` field is a single value per user, not a list) |
| BR-04 | If a user's profile is private, only username, avatar, and registration date are exposed. List, ratings, reviews, and stats stay hidden from anyone but the owner |
| BR-05 | When a user deletes their account, whether their reviews are cascade-deleted or anonymized ("Deleted user") is **pending a decision** |

### Ratings and reviews

| ID | Rule |
|---|---|
| BR-06 | A user can only rate a given game once (rating again updates the existing value, it does not create a new one) |
| BR-07 | The rating must be an integer between 1 and 10 |
| BR-08 | A user can only write one review per game (same as rating: rewriting updates, does not duplicate) |
| BR-09 | Only the review's author can edit or delete it (except the Admin, who can remove it for rule violations — Phase 2) |
| BR-10 | A game's average rating is recalculated every time a rating is added, edited, or removed |

### Personal game list

| ID | Rule |
|---|---|
| BR-11 | A game can only have one status at a time within a user's list (playing, completed, on hold, dropped, plan to play) — no simultaneous multiple statuses |
| BR-12 | The end date cannot be earlier than the start date, if both are recorded |
| BR-13 | A user can only mark as favorite a game already in their list (cannot favorite without adding it first) — **to be validated whether this applies, or whether favorite is independent of status** |

### Catalog

| ID | Rule |
|---|---|
| BR-14 | A game's title does not need to be unique (remakes/remasters can share a name), but the combination title + year + platform must be unique |
| BR-15 | A game must have at least one genre assigned to be published in the catalog |
| BR-16 | Only the Admin can create, edit, or delete catalog entries |

### Visibility and permissions

| ID | Rule |
|---|---|
| BR-17 | Any write action (rate, review, add to list, edit profile) requires an authenticated session, validated on the backend, not only on the frontend |
| BR-18 | An unauthenticated user attempting any write action must be redirected to login/register without losing the context of the action they intended (e.g. return to the game page after logging in) |

---

## Design notes derived from these requirements

- The `role` field should be modeled as an extensible enum (not a boolean), to support future roles (premium, semi-admin) without redesigning the schema.
- Read endpoints (FR-01 to FR-07) are public; write endpoints require authentication via middleware (JWT).
- FR-07 implies the user profile endpoint always returns 200, but with empty content fields if the profile is private and the requester is not the owner.
- Pending decision: source of the game catalog (fully manual entry via FR-39, or sync from an external API such as RAWG/IGDB with later admin curation). This affects the "add game" form design.
