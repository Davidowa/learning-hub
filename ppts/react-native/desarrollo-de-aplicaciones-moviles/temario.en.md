# Mobile Application Development

This course organizes concepts, implementation and evidence across 17 sessions. Each lab uses only the current and earlier session concepts.React Native builds for Android and iOS. SwiftUI builds for iOS and studies Android through conceptual counterparts.

## Assessment

| Component | Weight | Due |
|---|---:|---|
| Midterm 1 | 20 % | w08 |
| Midterm 2 | 20 % | w13 |
| Project | 20 % | w16 |
| Final exam | 20 % | w17 |
| Homework and labs | 20 % | w01-w16 |

## Sessions

### 01. The mobile device as a platform

- Device classes and form factors, and what each one constrains
- Mobile affordances and constraints: sensors, interruptions, battery, intermittent network, touch, privacy
- Four ways to build: platform-native, cross-platform with native UI, cross-platform with its own renderer, web (PWA or WebView hybrid)
- Toolchain anatomy: language, SDK, IDE, emulator or simulator, device, signing, store
- How the course works: Bitácora, one repo per student, a PR and a tag per lab, and the evaluation rubric as a preview

Lab: Show the app on a simulator and a device. Submit an identifiable commit and evidence of the result.

### 02. The language: types, values and functions

- From C#, Python and C++ to TS or Swift: declarations, inference, annotations, functions
- The absence of a value: `undefined` with `?.` and `??` (TS); optionals with `if let`, `guard let` and `??` (Swift); why force-unwrapping is a smell
- Value and reference semantics: TS objects are references, while Swift has value-type `struct`s and reference-type `class`es
- Modeling with types: literal unions and discriminated unions (TS), enums with associated values (Swift), exhaustive `switch`
- Closures and collection pipelines: `map`, `filter`, `reduce`, sorting
- The first automated test: arrange, act, assert

Lab: Model reports and test pure functions. Submit an identifiable commit and evidence of the result.

### 03. Inside Android and iOS

- Two layered stacks: Linux kernel, HAL, ART and native libraries, and framework (Android); Core OS, Core Services, Media and Cocoa Touch with SwiftUI on top (iOS)
- How code runs: from Dalvik to ART (and why the original item is obsolete), Swift compiled ahead of time to machine code, JS compiled to Hermes bytecode plus native modules
- Identity and sandbox: package name or bundle identifier, signing, per-app storage, the permission model
- The contract with the OS: AndroidManifest.xml, Info.plist and entitlements, and the config that generates them
- Entry points and lifecycle: the four Android components and their iOS counterparts; foreground, background, suspended and killed; process death

Lab: Configure identity and log lifecycle transitions. Submit an identifiable commit and evidence of the result.

### 04. Declarative UI: components and layout

- Imperative and declarative UI: XML layouts, storyboards and fragments as the previous instance, which students read but don't build
- Composition: components or views with typed inputs, reuse and previews
- Layout models: flexbox (column by default) in RN; stacks, frames, `Spacer` and modifier order in SwiftUI
- Core controls: text, image, icon, button, text field, toggle
- Platform conventions: HIG and Material as design languages, and going from wireframe to component tree

Lab: Compose a list and a detail view. Submit an identifiable commit and evidence of the result.

### 05. State and interaction

- State and inputs: what a component owns and what it receives
- Single source of truth and one-way flow: lifting state, callbacks and bindings
- Forms: controlled inputs, validation, disabled states, the keyboard
- Touch: gestures, touch target size, pressed states, haptic feedback
- Re-rendering: what triggers an update, and why in-place mutation does not

Lab: Validate and save form inputs. Submit an identifiable commit and evidence of the result.

### 06. Lists and navigation

- Lists at scale: virtualization, stable keys or `Identifiable`, empty states, pull to refresh
- Navigation patterns: stack, tabs and modal, and when each fits
- Passing data: an ID in the route, with the object looked up in state
- Menus, toolbars and dialogs: confirming destructive actions, sheets
- Platform differences: Android system back and predictive back, iOS swipe back; the explicit intent as the Android ancestor of "push a screen"

Lab: Navigate between list and detail using stable identity. Submit an identifiable commit and evidence of the result.

### 07. App architecture

- Layers: view, state, domain and data, and the direction of dependencies
- Shared state across screens without passing props through every level
- Interfaces or protocols and dependency injection, with in-memory fakes for tests
- Dependencies: package managers, semantic versioning, lockfiles, and the first formal use of the evaluation rubric
- Code review: the PR description, small diffs, a checklist, and reviewing AI-generated code

Lab: Separate the repository and test it with in-memory data. Submit an identifiable commit and evidence of the result.

### 08. Networking and asynchrony

- HTTP and REST as contracts: methods, status codes, JSON, OpenAPI as the spec
- Asynchrony and the main thread: what ANR (Android) and watchdog termination (iOS) mean
- Decoding and validating at the boundary
- UI states with retry, and cancellation when leaving a screen
- Auth headers and timeouts, and why an API key shipped in the app is public

Lab: Represent loading, success, empty and error states. Submit an identifiable commit and evidence of the result.

### 09. Local persistence and offline work

- The storage spectrum (key-value, relational, files, secure storage), chosen by shape, size and sensitivity
- Relational persistence on the device: schema, parameterized queries, or models and queries
- Migrations: a versioned schema, and adding a field without losing data
- Offline-first: the local database as the source of truth, a sync queue with statuses, and last-write-wins as the baseline conflict policy
- The user session: token auth, secure storage, and logout clearing local data

Lab: Preserve data across restarts and migrate the schema. Submit an identifiable commit and evidence of the result.

### 10. Camera, photos and files

- The permission model: declared purpose strings plus a runtime prompt; the states (not asked, granted, denied, limited); the denial path and a link to Settings
- System picker or custom camera, chosen by least privilege
- The capture pipeline: preview, capture, resize and compress, store in the sandbox, reference from the database
- Image resources: density variants (`@2x`/`@3x`, `mdpi` to `xxxhdpi`), asset catalogs, caching
- Sandbox directories: documents and cache, and cleaning up a report's files when it is deleted

Lab: Attach a photo and handle denied permissions. Submit an identifiable commit and evidence of the result.

### 11. Sensors and location

- Sensor families: motion (accelerometer, gyroscope, magnetometer), environment (barometer, light), position; units and coordinate frames
- Streams: subscribe, sampling rate, cleanup, low-pass filtering
- Location: accuracy against battery, foreground and background access, approximate and precise permission
- Maps: markers, regions, opening the detail from a marker; geocoding as a network call
- Testing with simulated data: simulated locations, recorded samples as test fixtures

Lab: Record samples with units and cancel subscriptions. Submit an identifiable commit and evidence of the result.

### 12. System integration

- Notifications: local and push, permission, Android channels, routing a tap to a screen
- Deep links: custom schemes and verified links (App Links, Universal Links); the implicit intent as their ancestor
- Sharing: the share sheet going out, system pickers as the consumer side of content providers
- System events: connectivity and app state; Android's broadcast restrictions since 8.0 and iOS observers
- Background work: what each OS allows (WorkManager and foreground services, BGTaskScheduler); widgets as additional entry points
- When the default setup is not enough: development builds instead of Expo Go (RN), capabilities and entitlements (SwiftUI)

Lab: Open a report through a validated link. Submit an identifiable commit and evidence of the result.

### 13. Accessibility, languages and screens

- Semantics: labels, roles or traits, grouping and focus order, tested with TalkBack and VoiceOver
- Visual accessibility: text scaling, contrast, touch targets (44 pt on iOS, 48 dp on Android), reduced motion
- Localization: external strings, plurals, locale formats for dates, numbers and units
- Adaptive layout: safe areas, orientation, tablets and foldables, iPad windows, dark mode
- Auditing: Accessibility Inspector, Android Accessibility Scanner, automated audits in UI tests

Lab: Complete the flow with a screen reader and two languages. Submit an identifiable commit and evidence of the result.

### 14. Quality: testing, debugging and CI

- The testing pyramid and what each level catches
- Test doubles: a fake repository, a mocked network, deterministic time and IDs
- UI tests that query by role and label, so accessibility pays off twice
- Debugging and profiling: breakpoints, logs, network inspection, render and frame profiling
- Continuous integration: type check, lint and tests on every PR, with a protected main branch
- Production observability: crash reports and logs with consent

Lab: Fix a defect and add a regression test. Submit an identifiable commit and evidence of the result.

### 15. Security, privacy and release

- Signing: the upload key and Play App Signing; certificates and provisioning profiles; what each one protects
- Build variants and configuration: development, preview and production, and what ends up inside the bundle
- Versioning: semantic versions for people, build numbers for stores (`versionName`/`versionCode`, `CFBundleShortVersionString`/`CFBundleVersion`)
- Store requirements: privacy labels and the Data safety form, privacy manifests, permission justifications, account deletion, review guidelines
- Distribution: internal testing, TestFlight, staged rollout, over-the-air updates and their limits
- Security baseline: OWASP MASVS categories, TLS and App Transport Security, secure storage, no secrets in the bundle

Lab: Prepare a signed build for test distribution. Submit an identifiable commit and evidence of the result.

### 16. Evaluating the next tool

- The evaluation rubric and the ADR (context, options, decision, consequences, review date)
- Hybrid and web: WebView shells (from Cordova to Capacitor), PWAs, and when each is the right answer
- The cross-platform landscape as a decision: RN, Flutter, Kotlin and Compose Multiplatform, Swift outside Apple platforms (verify status), and native
- Going below the framework: native modules (RN), UIKit interop and Swift packages (SwiftUI)
- Current trends run through the rubric: on-device AI, new form factors (wearables, foldables, XR), design-language shifts (Liquid Glass in iOS 26, Material 3 Expressive), passkeys

Lab: Evaluate a tool using a reversible pilot. Submit an identifiable commit and evidence of the result.

### 17. Final exam

- The sixteen mental models, one slide each, with the instance taught for each
- The final exam format and rules
- A walkthrough of a sample maintenance ticket
- A course retrospective: what changed in the stack during the term, and how the annex recorded it

Lab: Resolve and defend a maintenance ticket. Submit an identifiable commit and evidence of the result.

## Submission rules

Disclose assistance tools and keep reproducible evidence. Each member must explain the work. Each exam specifies the permitted materials.
