<!-- Propuesta de temario, lente: practica. Borrador de un agente diseñador, sin verificar; ver HANDOFF-auditoria-y-cursos-nuevos.md en la raíz. -->

# Desarrollo de Aplicaciones Móviles: one syllabus, two tracks (React Native and SwiftUI)

Proposal for David Escobar-Castillejos, Facultad de Ingeniería, Universidad Panamericana. Prepared 2026-10-05 from the original temario in `mobile-original.es.txt`. Lens: **practice-first**, meaning what a junior mobile developer has to be able to do in a first job between 2027 and 2030.

## 0. The proposal in brief

**Two courses share one syllabus.** Both have the same 17 session titles, the same objectives, the same assessment calendar and the same concept questions on every exam. They differ in each session's *realization*: what gets built and coded in React Native (iOS and Android) and what in SwiftUI (iOS only).

**One running case.** Every student builds **Bitácora**, a field-report app. You capture an observation with a photo, location, category, notes and a sensor reading, store it offline, sync it to a course API, see it on a list and a map, get reminders about it and share it. This is the kind of app juniors really maintain: inspections, maintenance tickets, field service, incident logs. It needs every capability the original syllabus names. Each lab ends in a tagged release (`v0.1` to `v0.15`). From week 9, teams fork one member's Bitácora and adapt it for a real stakeholder on campus. That fork becomes the final project, while each student keeps doing the weekly labs in their own repository.

**The job tasks behind the plan.** By the end, a student can:

1. Clone an unfamiliar app, run it on an emulator or simulator and on a phone, and find where a screen lives (S01, S03, final exam)
2. Build a screen from a design, accessible and localized (S04, S13)
3. Wire a form with validation and state that has one clear owner (S05, S07)
4. Add a route, a deep link and a notification that opens it (S06, S12)
5. Consume an API with loading, error and offline states (S08, S09)
6. Persist data and migrate a schema without losing user data (S09)
7. Use a device capability with the permission flow done right (S10, S11)
8. Test what they change and keep CI green (S02, S14)
9. Ship a signed build to testers and prepare a store submission (S15)
10. Review a pull request, including AI-generated code, and write a decision record for a new dependency (S07, S16)

**How the time-transcendent requirement is met:**

- Every session names one **mental model** (the part that lasts) and one **current instance** (the part that expires). The instance is verifiable, since it runs in the lab that same day.
- Product names and versions appear only in the session realizations and in the dated annex (section 5). The syllabus text names concepts. For example, it says "declarative UI", not "SwiftUI on iOS 26".
- Obsolete items are replaced by the concept they were an instance of. For example, *Máquina virtual Dalvik* becomes "how your code runs on the device", and ART, Swift AOT and Hermes are today's instances.
- An **evaluation thread** teaches students to judge the next tool: a fixed rubric (first used in S01, again in S07 and S09, formally in S16), timeboxed spikes and architecture decision records (ADRs) with a review date.
- Every code example on the slides also lives in a course sample repository that runs CI each term against the current stack. A red build is the signal that a slide has expired.

## 1. Audit of the original syllabus

Verdicts: **keep** (the concept stands and the item is taught under its own name), **reframe** (keep the need, teach it as the enduring concept), **replace** (the item is obsolete, so teach the concept it was an instance of), **merge** (a duplicate or near-duplicate folded into another item), **remove** (no place in the course).

Notes on the source. The block titled *CONTENIDO TEMÁTICO* sits between the two native units and contains only Android concepts (fragments, broadcast receivers, content providers, intents), so it is read here as the second half of the Android unit. Seven items appear in both native units and are merged. *Complementos* (O7) is ambiguous: it is read here as "app extensions and third-party packages", and the professor should confirm that.

### Introducción y conceptos básicos

| # | Original item | Verdict | Reason | Lands in |
|---|---|---|---|---|
| I1 | Tipos de dispositivos inteligentes | Reframe | A list of device types dates fast. A 2015 list would include Windows phones, whose last OS, Windows 10 Mobile, lost support in December 2019. The lasting idea is **form factors as constraints**: phone, tablet, foldable, watch, TV, car and XR headset, each with its own input, screen and session length. | S01, S13 |
| I2 | Ventajas de usar dispositivos inteligentes | Merge into I1 and reframe | Advantages are half the picture. The model is **affordances and constraints**: always with you and rich in sensors, but battery-bound, intermittently connected, interrupted and private. Each constraint has a design consequence. | S01 |
| I3 | Sensores | Keep (reframed) | Taught as **streams of noisy, timestamped samples** with a sampling rate, a battery cost and a permission. | S11 |
| I4 | Cámara | Keep (reframed) | Taught as a **permission-gated capture pipeline** with least privilege: the system picker first, a custom camera only when needed. | S10 |
| I5 | Introducción a herramientas y tecnologías para móviles | Reframe | Named tools expire, while toolchain anatomy (language, SDK, IDE, emulator or simulator, device, signing, store) does not. Tools move to the annex. | S01 |
| I6 | Tecnologías nativas y web | Merge with I7 and I15 | Becomes **the four ways to build an app**: platform-native, cross-platform with native UI, cross-platform with its own renderer, and web (PWA or WebView hybrid). | S01, S16 |
| I7 | Comparativa entre tecnologías | Reframe | A static comparison table rots. One written in 2015 would feature PhoneGap (Adobe discontinued it and shut down PhoneGap Build in 2020) and Xamarin (Microsoft ended support on May 1, 2024). It is replaced by a **reusable evaluation rubric and an ADR** that students apply themselves. | S01 (first pass), S16 |
| I8 | Conectividad e interacción | Reframe and split | Two different concepts share one line: **interaction** (touch, gestures, feedback) and **connectivity** (networking, offline, reacting to network changes). | S05, S08, S12 |
| I9 | Creación aplicaciones | Reframe | The five sub-items below form a lifecycle. That works better as a **thread through the running project** than as one lecture. | All, see I10 to I14 |
| I10 | Análisis del problema | Keep | Taught as problem statements, user stories and acceptance criteria. It is practiced on Bitácora and again on the team project proposal. | S01, S09 |
| I11 | Diseño de la aplicación | Keep | Covers UI design (wireframes, platform guidelines) and software design (layers, boundaries). | S04, S07 |
| I12 | Desarrollo de la aplicación | Keep | Taught as professional workflow: a git repository, small pull requests, code review and tagged releases every week. | S01, S07, all labs |
| I13 | Pruebas de funcionamiento | Reframe and expand | Manual "functional testing" alone is not job-ready. This becomes the **testing pyramid**: the first unit test in week 2, then component, UI and end-to-end tests, CI and device checks. | S02, S14 |
| I14 | Entrega | Reframe | "Delivery" becomes **release engineering** (signing, variants, versioning, testers, staged rollout, updates) plus the project demo. | S15, S16 |
| I15 | Aplicaciones híbridas | Reframe | "Hybrid" historically meant a native WebView shell around a web app. That lineage runs from PhoneGap/Cordova to Capacitor (1.0 in 2019), and Cordova is still an Apache project. It is taught as one branch of the four ways to build, kept separate from cross-platform native UI such as React Native. | S01, S16 |
| I16 | Tendencias futuras para el desarrollo de aplicaciones | Replace | A list of trends expires within a year. It is replaced by **a method for evaluating trends** (rubric, spike, ADR) applied to a dated trend radar that is reviewed every term. | S16, annex 5.5 |

### Aplicaciones nativas para Android

| # | Original item | Verdict | Reason | Lands in |
|---|---|---|---|---|
| A1 | ¿Qué es Android? | Keep | Covers the open-source base, OEMs, Google Play services, fragmentation and update cadence. It is taught side by side with iOS. | S03 |
| A2 | Descripción e instalación del entorno de desarrollo y dispositivos virtuales | Keep (reframed) | The concept is toolchain plus emulator plus device. The instance changed: Eclipse ADT gave way to Android Studio (1.0 in December 2014, with ADT support ending in 2015). RN track: Android Studio supplies the SDK and emulator. SwiftUI track: shown as the counterpart of Xcode and Simulator. | S01, S03 |
| A3 | Arquitectura de Android | Reframe | Taught as **layered OS stacks and the app sandbox**, comparing Linux kernel, HAL, ART and framework with the iOS layers, so students can place their own code in either stack. | S03 |
| A4 | Componentes de una aplicación | Reframe | The four components are taught as **entry points the OS can start**, each mapped to its iOS counterpart. | S03, S12 |
| A5 | Actividades | Reframe | The lasting part is screen **lifecycle and process death**. Since Jetpack Compose 1.0 (July 2021), a modern Android app is typically one activity that hosts many composable screens. | S03, S06 |
| A6 | Servicios | Reframe | Long-running services are no longer a free choice. Android 8.0 (2017) imposed background execution limits, Jetpack WorkManager (stable since 2019) handles deferrable work, and apps targeting Android 14 must declare foreground service types. The concept is **background work under OS limits**, with iOS BackgroundTasks as the counterpart. | S12 |
| A7 | Manifiesto | Merge with A12 | | S03 |
| A8 | Procesos en Android | Reframe | Taught as the **process lifecycle**: the OS may kill a backgrounded app, and the iOS counterpart is suspension and termination. It ties to state restoration. | S03, S12 |
| A9 | Máquina virtual Dalvik | Replace | Dalvik is gone. ART arrived as a preview in Android 4.4 (2013) and became the only runtime in Android 5.0 (2014). Since Android 7.0, ART mixes JIT with profile-guided AOT compilation, and since Android 12 it is updatable through Google Play system updates. The concept is **how your code runs on the device**: bytecode on a managed runtime (ART), native AOT code (Swift) and precompiled JS bytecode (Hermes in RN). | S03 |
| A10 | Proyectos | Merge with A11 | | S03 |
| A11 | Creación y estructura de un proyecto | Keep | Covers **project anatomy**: an Expo project and its generated native folders, or an Xcode project with targets and schemes. | S01, S03 |
| A12 | Archivo AndroidManifest.xml | Keep (reframed, absorbs A7) | Taught as **the app's contract with the OS** (identity, permissions, entry points, link handling) next to Info.plist and entitlements. In Expo, both files are generated from app config. | S03, S10, S12 |
| A13 | Manejo de componentes | Merge | Merged into UI composition and app architecture. | S04, S07 |

### Contenido temático (second half of the Android unit)

| # | Original item | Verdict | Reason | Lands in |
|---|---|---|---|---|
| T1 | Interfaz del usuario | Keep (reframed) | Taught as **declarative UI**, where the screen is a function of state. Google treats Jetpack Compose as the recommended Android UI toolkit, and Apple promotes SwiftUI. | S04 |
| T2 | Fragmentos | Replace | Fragments still exist and are not deprecated, but new Android UI has been built with Compose and navigation destinations since 2021. The concept was **reusable UI units plus navigable destinations**, taught as components and routes. | S04, S06 |
| T3 | Vistas | Reframe | The imperative View hierarchy inflated from XML is the previous instance. Students learn declarative views and components, and read one XML layout so they recognize it in legacy code. | S04 |
| T4 | Diseños | Reframe | XML layouts (LinearLayout, ConstraintLayout) are replaced by **layout models**: flexbox in RN, stacks and frames in SwiftUI, Row and Column in Compose. | S04 |
| T5 | Recursos | Keep | Resource qualifiers (density, locale, night mode) are still a core idea. Today's instances are asset catalogs, density variants, string catalogs or i18n files, and dark mode. | S10, S13 |
| T6 | Receptores de radiodifusión | Reframe | Android 8.0 (2017) stopped most implicit broadcasts from reaching manifest-declared receivers. The concept is **subscribing to system events** such as connectivity and app state. Counterparts are NetInfo, NWPathMonitor and NotificationCenter. | S12 |
| T7 | Proveedores de contenido | Reframe | App developers now mostly *consume* shared data through system pickers (the Android photo picker since Android 13, PhotosPicker since iOS 16) and the share sheet. Writing a provider is rare app work. The concept is **inter-app data sharing with least privilege**. | S10, S12 |
| T8 | Intentos implícitos y explícitos | Reframe | An explicit intent becomes **in-app navigation**. An implicit intent becomes **asking the OS who can handle this**: deep links, verified links (Android App Links and iOS Universal Links, both since 2015), the share sheet and opening URLs. | S06, S12 |
| T9 | Menús, diálogos y notificaciones | Keep (split) | Menus, toolbars and dialogs go to S06. Notifications go to S12, with Android channels (8.0) and the runtime permission (Android 13) or the iOS authorization flow. | S06, S12 |
| T10 | Publicación y distribución de la aplicación | Keep | Taught as the Google Play pipeline: Android App Bundle (required for new apps since August 2021) with Play App Signing, testing tracks, the yearly target-API requirement and the Data safety form. | S15 |

### Aplicaciones nativas para iOS

| # | Original item | Verdict | Reason | Lands in |
|---|---|---|---|---|
| O1 | ¿Qué es iOS? | Keep | Covers the closed ecosystem, App Review, fast OS adoption and year-based version names since iOS 26 (2025). It is taught side by side with Android. | S03 |
| O2 | Descripción e instalación del entorno de desarrollo y dispositivos virtuales | Keep | Xcode and Simulator, which need macOS. RN students without a Mac use Expo Go on an iPhone instead. | S01, S03 |
| O3 | Arquitectura de iOS | Reframe | The layers (Core OS, Core Services, Media, Cocoa Touch) are taught as the iOS half of the comparative stack, plus the sandbox. | S03 |
| O4 | Componentes de una aplicación | Merge with A4 | | S03, S12 |
| O5 | Ambiente de desarrollo (playground) | Reframe | The concept is **the fast feedback loop**. Its instances are Xcode playgrounds, `#Preview` (Xcode 15) and Fast Refresh in RN. It is used in the language ramp. | S02, S04 |
| O6 | Guion gráfico (storyboard) | Replace | Storyboards (iOS 5, 2011) belong to UIKit's Interface Builder. Apple's direction since SwiftUI (2019, iOS 13) is declarative UI. Students read one storyboard so they recognize it in maintenance work, but never build one. | S04 |
| O7 | Complementos | Reframe (confirm meaning) | Read as **extending an app**: third-party packages (Swift Package Manager, npm) and app extensions (widgets, share extensions) as additional entry points. | S07, S12 |
| O8 | Restricciones de visualización para multiplataformas | Reframe | Auto Layout constraints (iOS 6, 2012) and size classes (iOS 8, 2014) are one instance. The concept is **adaptive layout**: stacks and flexbox, safe areas, size classes, Dynamic Type, orientation and multiwindow. | S04, S13 |
| O9 | Proyectos | Merge with A10 and A11 | | S03 |
| O10 | Creación y estructura de un proyecto | Merge with A11 | | S01, S03 |
| O11 | Manejo de componentes | Merge with A13 | | S04, S07 |
| O12 | Interfaz del usuario | Merge with T1 | | S04 |
| O13 | Vistas | Merge with T3 | | S04 |
| O14 | Controles | Keep | Buttons, text fields, toggles, pickers and their states. | S04, S05 |
| O15 | Ventanas | Reframe | UIWindow became scenes in iOS 13 (2019), which SwiftUI exposes as `WindowGroup`. The concept is **windows, scenes and modality**: sheets and modals on phones, multiple windows on iPad. Apple has said UIScene lifecycle adoption will become mandatory after iOS 26 (verify). | S03, S06, S13 |
| O16 | Publicación y distribución de la aplicación | Keep | Covers signing (certificates and provisioning profiles), App Store Connect, TestFlight, App Review guidelines, privacy nutrition labels, privacy manifests (required since May 1, 2024) and in-app account deletion (required since June 30, 2022). | S15 |

**Tally:** 55 line items. 12 are kept, 5 are kept with a reframed delivery, 23 are reframed, 4 are replaced (Dalvik, Fragmentos, Guion gráfico, Tendencias), 11 are merged and none are removed. Every original concern has a home. What changed is the level of abstraction at which it is named.

## 2. What the original lacks

| # | Addition | Why it earns a place | Where |
|---|---|---|---|
| N1 | **Language ramp** (TypeScript or Swift) | Students know C#, Python and C++, but not TS or Swift. Without a planned ramp, weeks 4 to 8 turn into syntax support. There is one dedicated session plus a "language spotlight" in every later session. | S02, then every session |
| N2 | **State and data flow** | This is the central mental model of declarative UI and the source of most junior bugs ("the screen doesn't update"). The original has no state concept. | S05, S07 |
| N3 | **Navigation as architecture** | Stack, tabs, modals and deep links are where a real app's structure lives. The original only names intents. | S06, S12 |
| N4 | **Networking, async and API contracts** | Almost every app in a junior's job talks to a backend. Async/await and keeping the UI thread free are non-negotiable. | S08 |
| N5 | **Local persistence, offline-first and migrations** | Field apps work without signal. Shipping a schema change that wipes user data is a classic junior incident. | S09 |
| N6 | **Permissions and privacy by design** | Store review rejects apps for this, and Mexican data-protection law (LFPDPPP, new law in 2025, verify) applies. It is taught at the moment each capability appears. | S10 to S12, S15 |
| N7 | **Accessibility** | It is an ethical and legal expectation, and teams ask for it in reviews. Done well, it also makes UI tests easier to write. | S13, S14 |
| N8 | **Localization** | UP teaches in Spanish and English, and the apps students build should too. | S13 |
| N9 | **Automated testing and CI** | Job postings assume it. "Pruebas de funcionamiento" alone trains manual clicking. | S02, S14 |
| N10 | **Version control and code review** | First-job work is reading and reviewing other people's code. Every lab ships as a pull request. | S01, S07, all labs |
| N11 | **App architecture** (layers, boundaries, dependency injection) | It is what makes the tests and the store refactors possible, and what interviewers ask about. | S07 |
| N12 | **Performance and battery** | Lists, images, sensors and location are where mobile apps get slow or drain the battery. Profiling is a skill in its own right. | S06, S11, S14 |
| N13 | **Security baseline** | Students need to know that the app binary is readable, that secrets can't live in the bundle, about secure storage and TLS, and the OWASP MASVS categories. | S08, S09, S15 |
| N14 | **Release engineering** | Covers environments, versioning, testers, staged rollouts and over-the-air updates with their limits. The original stops at "publish". | S15 |
| N15 | **Observability** | Crash reports and logs with consent are how a team learns that production is broken. | S14, S15 |
| N16 | **Working with AI coding assistants** | Between 2027 and 2030, juniors will review and own generated code. Students review an AI-generated PR with planted defects and learn to use tests as the spec. This follows the course's Código de Honor. | S01, S07, S14 |
| N17 | **Evaluating tools and trends** | This is the core of the time-transcendent requirement: a rubric, spikes and ADRs with a review date. | S01, S07, S09, S16 |
| N18 | **Platform design conventions** (HIG and Material) | Users expect each platform to behave as it usually does, and App Review checks for it. | S04, S06 |
| N19 | **App lifecycle and state restoration** | Process death and suspension are where "works on my phone" apps lose user data. | S03, S12 |

## 3. The 17-session plan

### 3.0 Course frame

**Units and exams.** These units drive the roadmap slide in the course-intro deck.

| Unit | Sessions | Theme | Assessed in |
|---|---|---|---|
| 01 | S01 to S03 | Platform, language and system | Parcial 1 |
| 02 | S04 to S07 | Interface, state and architecture | Parcial 1 |
| 03 | S08 to S12 | Data and device | Parcial 2 |
| 04 | S13 to S16 | Quality, delivery and judgment | Project, Final |
| | S17 | Final exam session | |

Parcial 1 is taken at the end of week 8 and covers S01 to S07. Parcial 2 is taken at the end of week 13 and covers S08 to S12. Content taught in an exam week is assessed in the next instrument, so no one is examined on what they learned that same week. Weeks 8, 13 and 16 still teach their full topic and close with the exam or project logistics, as in COM102 and COM103.

**How each track honors the two native units.**

- **React Native course: both platforms are first-class.** A lab is accepted only with evidence on Android (emulator or device) *and* iOS (Expo Go on an iPhone, or the iOS Simulator on a Mac). Pairs are formed so every pair covers both. Platform sessions S03, S12 and S15 open the generated `android/` and `ios/` projects and read the AndroidManifest, the Info.plist and Gradle and Pod configuration. Platform differences are named where they appear: keyboard avoidance (S05), the back button (S06), permission dialogs (S10), sensor axes (S11), notification channels (S12), TalkBack versus VoiceOver (S13) and the two stores (S15). In S16, students write one native module in both Kotlin and Swift.
- **SwiftUI course: the Android unit becomes the platform-concepts unit.** It is taught as Android-to-iOS counterparts. Each platform session (S03, S04, S06, S10 to S13, S15) closes with an **Android counterpart** slide naming the Android mechanism, its Kotlin or Compose shape and an official doc link. Students keep a running **Rosetta table** (Android concept, iOS mechanism, API used in Bitácora) and turn it in during S12. The concept section of every exam is identical across tracks, so SwiftUI students are examined on Android concepts at the same depth as RN students.

**Hardware and accounts.**

| | React Native track | SwiftUI track |
|---|---|---|
| Computer | Any Windows, macOS or Linux laptop that can run Node.js and the Android emulator (verify current Android Studio requirements) | A Mac that runs the current Xcode. Apple silicon is recommended because macOS Tahoe 26 is the last macOS for Intel Macs. If students lack Macs, UP lab Macs are needed for labs and exams (verify availability). |
| Phone | Any Android phone or iPhone with Expo Go. No phone at all: Android emulator. | Optional. Simulator covers most labs, but it has no camera (S10) and only simulated motion (S11), so pairs share an iPhone. A free personal team can sign apps for one's own device with a 7-day profile. |
| Weeks 1 to 11 | Expo Go only. Every module used through S11 runs in Expo Go (verify each term). | Simulator plus an optional device |
| Weeks 12 to 16 | Development builds (local `npx expo run:android`, or EAS Build). iOS device builds need an Apple Developer team. Students without one validate iOS on the Simulator, if they have a Mac, or in Expo Go for the features it supports. | TestFlight needs an Apple Developer Program team. Use the faculty's team or the Apple university program if UP is enrolled (verify). Otherwise use Archive plus Simulator builds. |
| Fallback | | Swift Playgrounds on iPad (it has been able to build apps since version 4, December 2021) covers S01 to S07 with limits (verify which frameworks it supports). |

**Course infrastructure.** This consists of one template repository per track (Jest or Swift Testing preconfigured, a CI workflow and a PR template), a public **sample repository** containing every slide example, and the **Bitácora course API**. The API is an OpenAPI contract plus a small FastAPI reference server, since students already know Python. The contract is the durable part. Where it is hosted is chosen each term and recorded in the annex.

**Language ramp.** One spotlight per session, always tied to what that session needs.

| Session | TypeScript spotlight (RN) | Swift spotlight (SwiftUI) |
|---|---|---|
| S01 | A component is a function that returns JSX | A view is a struct that conforms to `View` |
| S02 | Types, inference, `?.` and `??`, unions, closures, `map`/`filter` | Structs and classes, optionals, enums with associated values, closures |
| S03 | Modules, `import`/`export`, JSON config | `@main`, attributes, protocols at a glance |
| S04 | TSX expressions, typed props, destructuring | Trailing closures, result builders, modifiers |
| S05 | Hooks and their rules, closures that capture state | Property wrappers, the `$` projection |
| S06 | Generics (`FlatList<Report>`) | `Identifiable`, `Hashable`, generics |
| S07 | Interfaces, structural typing | Protocols, access control, `final` |
| S08 | Promises, `async`/`await`, `try`/`catch`, `unknown` | `async throws`, `do`/`catch`, `Task`, `@MainActor` |
| S09 | Generic queries, template literals | Macros (`@Model`), key paths |
| S10 | Union types for permission states | Enums for states, UIKit interop |
| S11 | Cleanup functions, `Math` | `AsyncSequence`, `for try await` |
| S12 | Event listeners and unsubscribe functions | Actors, `Sendable` warnings read and fixed |
| S13 | Interpolation in translation keys | `LocalizedStringKey`, string interpolation |
| S14 | Mocks with `jest.fn` | `@testable import`, protocol-based fakes |
| S15 | Build-time environment variables | Build configurations, `#if DEBUG` |
| S16 | Reading Kotlin and Swift in a native module | Reading Kotlin and Compose |

### S01 · El dispositivo móvil como plataforma / The mobile device as a platform

- **Original items:** I1, I2, I5, I6, I7 (first pass), I9, I10, A2, O2, A11, O10 (first contact)
- **Mental model:** a mobile app is a guest on a personal, constrained, sensor-rich device, and the OS is the landlord.
- **Current instance:** an Expo project running in Expo Go and on the Android emulator (RN), and the Xcode App template running on the iOS Simulator (SwiftUI).
- **Topics**
  1. Device classes and form factors, and what each one constrains
  2. Mobile affordances and constraints: sensors, interruptions, battery, intermittent network, touch, privacy
  3. Four ways to build: platform-native, cross-platform with native UI, cross-platform with its own renderer, web (PWA or WebView hybrid)
  4. Toolchain anatomy: language, SDK, IDE, emulator or simulator, device, signing, store
  5. How the course works: Bitácora, one repo per student, a PR and a tag per lab, and the evaluation rubric as a preview
- **Objectives.** The student can:
  1. Run the starter app on an emulator or simulator and on a phone, and show a live edit appearing without reinstalling
  2. Classify four given apps into the four build approaches, citing one piece of evidence for each
  3. State three mobile constraints and one design consequence of each
  4. Write a problem statement and five user stories with acceptance criteria for Bitácora
- **React Native realization.** Create the project from the course template (an Expo TypeScript template with Jest preconfigured). Run `npx expo start`, open it in Expo Go by QR code and on an Android emulator from Android Studio's Device Manager. Use the iOS Simulator too on a Mac. Watch Fast Refresh.

  ```tsx
  import { Text, View } from 'react-native';

  export default function Home() {
    return (
      <View style={{ flex: 1, justifyContent: 'center' }}>
        <Text>Hola, Bitácora</Text>
      </View>
    );
  }
  ```

- **SwiftUI realization.** In Xcode, create a new project with the App template, the SwiftUI interface and Swift Testing. Run it on the Simulator, edit it in the `#Preview` canvas, and optionally run it on your own iPhone with a free personal team.

  ```swift
  import SwiftUI

  @main
  struct BitacoraApp: App {
      var body: some Scene {
          WindowGroup { ContentView() }
      }
  }

  struct ContentView: View {
      var body: some View { Text("Hola, Bitácora") }
  }

  #Preview { ContentView() }
  ```

- **Lab (artifact `v0.1`):** create the repo from the template. The app shows its name and the student's ID on two targets, with screenshots in the README. Open the first PR, merge it and tag it `v0.1`.
- **Homework:** write a problem statement and five user stories with acceptance criteria for Bitácora ("Como inspector, quiero..., para..."), plus a device inventory (OS version, storage) to plan pairs.
- **Quiz idea:** "An app draws its interface with native controls, but its logic runs in JavaScript. Which approach is it?" The four approaches are the options. The question is the same in both tracks.

### S02 · El lenguaje: tipos, valores y funciones / The language: types, values and functions

- **Original items:** O5 (playground, as the fast feedback loop), I13 (the first automated test)
- **Mental model:** a type system is a contract the compiler checks for you. Null safety and value semantics remove whole classes of bugs before the app runs.
- **Current instance:** TypeScript in strict mode with Jest (RN), and Swift 6 with Swift Testing (SwiftUI).
- **Topics**
  1. From C#, Python and C++ to TS or Swift: declarations, inference, annotations, functions
  2. The absence of a value: `undefined` with `?.` and `??` (TS); optionals with `if let`, `guard let` and `??` (Swift); why force-unwrapping is a smell
  3. Value and reference semantics: TS objects are references, while Swift has value-type `struct`s and reference-type `class`es
  4. Modeling with types: literal unions and discriminated unions (TS), enums with associated values (Swift), exhaustive `switch`
  5. Closures and collection pipelines: `map`, `filter`, `reduce`, sorting
  6. The first automated test: arrange, act, assert
- **Objectives.** The student can:
  1. Translate a given C# class with a nullable field into idiomatic TS or Swift that compiles under strict settings
  2. Predict the output of a copy-then-mutate snippet in both languages and explain the difference
  3. Model report status as a closed set so the compiler rejects an unhandled case
  4. Write three passing unit tests for pure functions over a list of reports
- **React Native realization.** Write `report.ts` with the domain types and pure functions, and `report.test.ts` with Jest.

  ```ts
  export type Status = 'draft' | 'pending' | 'synced';

  export type Report = {
    id: string;
    title: string;
    status: Status;
    note?: string;
  };

  export const pending = (rs: Report[]) =>
    rs.filter(r => r.status === 'pending');

  export const preview = (r: Report) =>
    r.note?.slice(0, 40) ?? '(sin nota)';
  ```

  ```ts
  import { pending, type Report } from './report';

  test('pending keeps only unsynced reports', () => {
    const rs: Report[] = [
      { id: '1', title: 'Fuga', status: 'pending' },
      { id: '2', title: 'Lámpara', status: 'synced' },
    ];
    expect(pending(rs).map(r => r.id)).toEqual(['1']);
  });
  ```

- **SwiftUI realization.** Write `Report.swift` in the app target and a test in the Swift Testing target. Use an Xcode playground, or the `#Playground` macro if available (Xcode 26, verify), for the copy-then-mutate experiment.

  ```swift
  import Foundation

  enum Status { case draft, pending, synced }

  struct Report {
      let id = UUID()
      var title: String
      var status: Status
      var note: String?
  }

  let a = Report(title: "Fuga", status: .draft)
  var b = a                 // copia: struct es valor
  b.title = "Lámpara"
  print(a.title)            // Fuga
  ```

  ```swift
  import Testing
  @testable import Bitacora

  @Test func pendingKeepsOnlyUnsynced() {
      let rs = [Report(title: "Fuga", status: .pending),
                Report(title: "Lámpara", status: .synced)]
      #expect(pending(rs).map(\.title) == ["Fuga"])
  }
  ```

- **Lab (artifact `v0.2`):** build the Bitácora domain model (`Report`, `Category`, `Status`) with sample data, plus `pending`, `countByCategory` and `preview`, and at least three green tests.
- **Homework:** a kata set of six functions with tests (sort by date, group by category, case-insensitive search, and so on), plus one paragraph on "what surprised me coming from C#".
- **Quiz idea:** copy-then-mutate. After `const b = a; b.title = 'Lámpara'`, printing `a.title` shows `Lámpara` in TS, while the Swift struct still shows `Fuga`. It is the same question with opposite answers, discussed across tracks.

### S03 · Android e iOS por dentro / Inside Android and iOS

- **Original items:** A1, A3, A4, A5, A7, A8, A9, A10, A11, A12, O1, O3, O4, O9, O10, O15 (scenes)
- **Mental model:** the OS owns the process. Your app is a signed, sandboxed bundle with a declared contract (identity, permissions, entry points), and its process can be paused or killed at any time.
- **Current instance:** the current Android and iOS releases (annex 5.3), Expo `app.json` with prebuild (RN), and Xcode target settings (SwiftUI).
- **Topics**
  1. Two layered stacks: Linux kernel, HAL, ART and native libraries, and framework (Android); Core OS, Core Services, Media and Cocoa Touch with SwiftUI on top (iOS)
  2. How code runs: from Dalvik to ART (and why the original item is obsolete), Swift compiled ahead of time to machine code, JS compiled to Hermes bytecode plus native modules
  3. Identity and sandbox: package name or bundle identifier, signing, per-app storage, the permission model
  4. The contract with the OS: AndroidManifest.xml, Info.plist and entitlements, and the config that generates them
  5. Entry points and lifecycle: the four Android components and their iOS counterparts; foreground, background, suspended and killed; process death
- **Objectives.** The student can:
  1. Place given parts of the app (a screen, an image, the JS bundle, the camera driver) on the right layer of each stack
  2. Explain what replaced Dalvik, since when, and what that changes for an app developer
  3. Change the app's display name, identifier and icon through declared configuration and verify the change on a device
  4. Log lifecycle transitions and predict what in-memory state is lost when the OS kills the app in the background
  5. Map each Android component to its iOS counterpart
- **React Native realization.** Set `name`, `slug`, `icon`, `ios.bundleIdentifier` and `android.package` in `app.json`. Run `npx expo prebuild` on a throwaway branch to read the generated `AndroidManifest.xml` and `Info.plist`. Learn the rule of Continuous Native Generation: never hand-edit generated folders, change config or use a config plugin. Add an `AppState` listener.

  ```json
  {
    "expo": {
      "name": "Bitácora",
      "slug": "bitacora",
      "ios": { "bundleIdentifier": "dev.tunombre.bitacora" },
      "android": { "package": "dev.tunombre.bitacora" }
    }
  }
  ```

  ```tsx
  useEffect(() => {
    const sub = AppState.addEventListener('change', state => {
      log(`${new Date().toISOString()} ${state}`);
    });
    return () => sub.remove();
  }, []);
  ```

- **SwiftUI realization.** Cover project anatomy: project and target, scheme, build settings, Signing & Capabilities, the Info tab, `Assets.xcassets` with the AppIcon, `@main` and `WindowGroup`, and `scenePhase`. **Android counterpart:** read a manifest next to an Info.plist, with a table of Activity and scene, Service and BackgroundTasks, BroadcastReceiver and observers, ContentProvider and pickers or app groups, Intent and URLs or App Intents.

  ```swift
  @main
  struct BitacoraApp: App {
      @Environment(\.scenePhase) private var phase

      var body: some Scene {
          WindowGroup { ContentView() }
              .onChange(of: phase) { _, newPhase in
                  Log.shared.add("\(Date.now) \(newPhase)")
              }
      }
  }
  ```

- **Lab (artifact `v0.3`):** give the app its own name, icon and identifier, plus a lifecycle logger screen. Commit a "where Bitácora lives" diagram to the repo, placing the app on both stacks.
- **Homework:** a comparison table (Android component, iOS counterpart, link to the official doc for each), with no tutorials as sources.
- **Quiz idea:** "What executes an Android app's bytecode on a 2026 phone?" Options: Dalvik, ART, the JVM, Hermes. Follow-up for RN: "and the app's JavaScript?"

### S04 · Interfaz declarativa: componentes y layout / Declarative UI: components and layout

- **Original items:** T1, T2 (replaced), T3, T4, O6 (replaced), O8 (part), O11, O12, O13, O14, A13, I11
- **Mental model:** UI = f(state). You describe the screen for the current data and the framework works out the changes. Screens are trees of small composable pieces.
- **Current instance:** RN core components with `StyleSheet` and flexbox (Yoga), and SwiftUI views with stacks and modifiers.
- **Topics**
  1. Imperative and declarative UI: XML layouts, storyboards and fragments as the previous instance, which students read but don't build
  2. Composition: components or views with typed inputs, reuse and previews
  3. Layout models: flexbox (column by default) in RN; stacks, frames, `Spacer` and modifier order in SwiftUI
  4. Core controls: text, image, icon, button, text field, toggle
  5. Platform conventions: HIG and Material as design languages, and going from wireframe to component tree
- **Objectives.** The student can:
  1. Decompose a wireframe into a named component tree with inputs before coding
  2. Build a static screen with at least three reusable components that matches the wireframe on a small and a large phone
  3. Predict the result of a layout snippet (flex direction or modifier order)
  4. Read a storyboard or an Android XML layout and name its declarative equivalent
- **React Native realization.** Use `View`, `Text`, `Image`, `Pressable`, `StyleSheet.create`, flexbox, typed props, `@expo/vector-icons` and `Platform.select`. A compare slide shows an Android XML layout next to the TSX.

  ```tsx
  type Props = { title: string; category: string };

  export function ReportCard({ title, category }: Props) {
    return (
      <View style={styles.card}>
        <Text style={styles.title}>{title}</Text>
        <Text style={styles.chip}>{category}</Text>
      </View>
    );
  }
  ```

- **SwiftUI realization.** Use struct views, `VStack`, `HStack` and `ZStack`, SF Symbols, modifier order and `#Preview` with sample data. One storyboard is shown for recognition. **Android counterpart:** a Compose `@Composable` next to the SwiftUI view.

  ```swift
  struct ReportRow: View {
      let report: Report

      var body: some View {
          HStack(spacing: 12) {
              Image(systemName: report.category.symbol)
              VStack(alignment: .leading) {
                  Text(report.title).font(.headline)
                  Text(report.createdAt, style: .date)
                      .foregroundStyle(.secondary)
              }
          }
      }
  }
  ```

- **Lab (artifact `v0.4`):** list and detail screens with static sample data, built from the provided wireframe. The PR includes the component-tree sketch.
- **Homework:** rebuild a screen of a real app from a screenshot as components, with a five-line justification of the decomposition.
- **Quiz idea:** SwiftUI asks for `Text("Fuga").padding().background(.yellow)` compared with the reversed order: which one shows a yellow margin? RN asks in which direction three children of an unstyled `View` stack.

### S05 · Estado e interacción / State and interaction

- **Original items:** I8 (interaction), O14, A13, O11
- **Mental model:** state has exactly one owner. Data flows down, events flow up, and the UI re-renders from state, never from mutations it can't see.
- **Current instance:** React hooks (`useState`, `useReducer`) in RN, and `@State` and `@Binding` in SwiftUI.
- **Topics**
  1. State and inputs: what a component owns and what it receives
  2. Single source of truth and one-way flow: lifting state, callbacks and bindings
  3. Forms: controlled inputs, validation, disabled states, the keyboard
  4. Touch: gestures, touch target size, pressed states, haptic feedback
  5. Re-rendering: what triggers an update, and why in-place mutation does not
- **Objectives.** The student can:
  1. Implement a new-report form whose Save is enabled only when the input is valid, with the rule unit-tested
  2. Decide and justify where state lives in three given scenarios
  3. Pass state down and changes up between a parent and a child
  4. Diagnose a "screen doesn't update" bug caused by in-place mutation or the wrong owner
- **React Native realization.** Use `useState`, a controlled `TextInput`, callbacks, `KeyboardAvoidingView` (its `behavior` differs between iOS and Android), a `Pressable` pressed style and `expo-haptics`.

  ```tsx
  export function NewReport({ onSave }: Props) {
    const [title, setTitle] = useState('');
    const valid = isValidTitle(title);

    return (
      <View style={{ gap: 12 }}>
        <TextInput value={title} onChangeText={setTitle}
                   placeholder="¿Qué observaste?" />
        <Button title="Guardar" disabled={!valid}
                onPress={() => onSave(title.trim())} />
      </View>
    );
  }
  ```

- **SwiftUI realization.** Use `@State`, `@Binding`, `Form`, `TextField`, `Picker`, `Toggle`, `@FocusState` and `.sensoryFeedback`.

  ```swift
  struct NewReportView: View {
      @State private var title = ""
      @State private var category = Category.facilities
      var onSave: (String, Category) -> Void

      var body: some View {
          Form {
              TextField("¿Qué observaste?", text: $title)
              CategoryPicker(selection: $category)
              Button("Guardar") { onSave(title, category) }
                  .disabled(!isValidTitle(title))
          }
      }
  }
  ```

- **Lab (artifact `v0.5`):** a create-report form (title, category, note) that adds to the in-memory list, with validation tests.
- **Homework:** edit an existing report by reusing the form, and test the validation edge cases (blank spaces, emoji, very long text).
- **Quiz idea:** "Why doesn't the list update?" RN: `reports.push(r); setReports(reports)` passes the same reference. SwiftUI: a button's action assigns to a plain `var` of the view (no `@State`) and the code doesn't compile. Ask why.

### S06 · Listas y navegación / Lists and navigation

- **Original items:** T2 (destinations), T8 (explicit), T9 (menus and dialogs), O15 (modality), A5 (screens)
- **Mental model:** navigation is state, a stack of destinations plus tabs and modals that the user, the app or a URL can change. Lists recycle rows, so every row needs a stable identity.
- **Current instance:** Expo Router (file-based, built on React Navigation 7) with `FlatList` in RN, and `NavigationStack`, `TabView` and `List` in SwiftUI.
- **Topics**
  1. Lists at scale: virtualization, stable keys or `Identifiable`, empty states, pull to refresh
  2. Navigation patterns: stack, tabs and modal, and when each fits
  3. Passing data: an ID in the route, with the object looked up in state
  4. Menus, toolbars and dialogs: confirming destructive actions, sheets
  5. Platform differences: Android system back and predictive back, iOS swipe back; the explicit intent as the Android ancestor of "push a screen"
- **Objectives.** The student can:
  1. Render 1,000 generated reports with stable identity and smooth scrolling on a device
  2. Implement tab plus stack navigation that passes an ID to a detail screen
  3. Confirm a destructive action with a platform-appropriate dialog
  4. Explain why an array index used as a key breaks after a delete, and fix it
- **React Native realization.** Use `FlatList` (`keyExtractor`, `ListEmptyComponent`, `refreshing`), Expo Router with `app/(tabs)/_layout.tsx` and `app/report/[id].tsx`, `Link`, `useLocalSearchParams` and `Alert.alert`. The Android hardware back button is handled by the router. FlashList is shown as an alternative instance (verify).

  ```tsx
  <FlatList
    data={reports}
    keyExtractor={r => r.id}
    renderItem={({ item }) => (
      <Link href={`/report/${item.id}`} asChild>
        <Pressable><ReportCard report={item} /></Pressable>
      </Link>
    )}
  />
  // app/report/[id].tsx
  const { id } = useLocalSearchParams<{ id: string }>();
  ```

- **SwiftUI realization.** Use `List` with `Identifiable`, `NavigationStack` with `navigationDestination(for:)` and a path, `TabView`, `.toolbar`, `.sheet`, `.confirmationDialog` and `.searchable`. **Android counterpart:** an explicit `Intent`, and a Navigation Compose destination.

  ```swift
  NavigationStack {
      List(reports) { report in
          NavigationLink(value: report) {
              ReportRow(report: report)
          }
      }
      .navigationTitle("Reportes")
      .navigationDestination(for: Report.self) { report in
          ReportDetail(report: report)
      }
  }
  ```

- **Lab (artifact `v0.6`):** tabs (Reportes, Mapa as a placeholder, Ajustes), the list to detail to edit flow, delete with confirmation, and search.
- **Homework:** "empty" and "no results" states, plus a sort menu (date, category), with a short screen recording in the PR.
- **Quiz idea:** the list uses the index as its key, and the user deletes row 2 while typing in row 3. What does the user see?

### S07 · Arquitectura de la app / App architecture

- **Original items:** I11, I12, A4 (internal organization), A13, O11, O7 (third-party packages)
- **Mental model:** separate what changes for different reasons. Views render, a store owns app state, and a repository hides where the data lives. Boundaries make code testable and replaceable.
- **Current instance:** a Zustand store with custom hooks (RN), an `@Observable` store injected through the environment (SwiftUI), and a repository interface or protocol in both.
- **Topics**
  1. Layers: view, state, domain and data, and the direction of dependencies
  2. Shared state across screens without passing props through every level
  3. Interfaces or protocols and dependency injection, with in-memory fakes for tests
  4. Dependencies: package managers, semantic versioning, lockfiles, and the first formal use of the evaluation rubric
  5. Code review: the PR description, small diffs, a checklist, and reviewing AI-generated code
- **Objectives.** The student can:
  1. Move logic from views into a store whose behavior is tested without rendering UI
  2. Share state between two tabs through one store
  3. Define a repository interface with an in-memory implementation and swap it in tests
  4. Review a PR that contains AI-generated code and leave at least three actionable comments that find at least two of the planted defects
  5. Fill in the evaluation rubric for one state-management library
- **React Native realization.** Use Zustand's `create` with selectors and a `useReports` hook, and Context for injecting the repository. Redux Toolkit is shown as the instance students will meet in older codebases. Cover `package.json` and the lockfile, and `npx expo install` for SDK-compatible versions.

  ```ts
  import { create } from 'zustand';

  type ReportState = {
    reports: Report[];
    add: (r: Report) => void;
    remove: (id: string) => void;
  };

  export const useReports = create<ReportState>()(set => ({
    reports: [],
    add: r => set(s => ({ reports: [...s.reports, r] })),
    remove: id => set(s => ({
      reports: s.reports.filter(r => r.id !== id) })),
  }));
  ```

- **SwiftUI realization.** Use an `@Observable final class ReportStore`, `@State` in the `App`, `.environment(store)`, `@Environment(ReportStore.self)`, `@Bindable`, a `ReportRepository` protocol and adding a Swift package. `ObservableObject` with `@Published` is shown as the legacy instance.

  ```swift
  @Observable
  final class ReportStore {
      private(set) var reports: [Report] = []
      private let repo: ReportRepository

      init(repo: ReportRepository) { self.repo = repo }

      func add(_ report: Report) {
          reports.append(report)
          repo.save(report)
      }
  }
  ```

- **Lab (artifact `v0.7`):** refactor to store plus repository, with store tests. A classmate reviews the PR, with rotating pairs.
- **Homework:** review a PR from the professor that contains AI-generated code with four planted defects: stale state, a missing cleanup, a wrong key and a force unwrap or unchecked `undefined`.
- **Quiz idea:** four snippets. Which layer does each one belong to, and which one breaks the dependency direction?

### S08 · Red y asincronía / Networking and asynchrony (closes with Parcial 1 logistics)

- **Original items:** I8 (connectivity)
- **Mental model:** the network is slow, fallible and asynchronous. Every remote call has four outcomes (loading, success, empty, error) and must never block the UI thread. The API contract is a type that you validate at the boundary.
- **Current instance:** `fetch` with `async`/`await` and zod, with TanStack Query as the library alternative (RN); `URLSession` with `async`/`await`, `Codable` and `.task` (SwiftUI).
- **Topics**
  1. HTTP and REST as contracts: methods, status codes, JSON, OpenAPI as the spec
  2. Asynchrony and the main thread: what ANR (Android) and watchdog termination (iOS) mean
  3. Decoding and validating at the boundary
  4. UI states with retry, and cancellation when leaving a screen
  5. Auth headers and timeouts, and why an API key shipped in the app is public
- **Objectives.** The student can:
  1. Fetch and decode categories from the course API into typed models and reject malformed payloads
  2. Render all four states with a working retry
  3. Cancel an in-flight request when the screen goes away and show that no stale update lands
  4. Explain what happens when the main thread blocks, using each platform's term
- **React Native realization.** Use `fetch`, `AbortController`, the discriminated-union state from S02 and a zod schema (verify version). `useQuery` is shown as the library that encapsulates the same pattern.

  ```tsx
  useEffect(() => {
    const ctrl = new AbortController();
    setState({ kind: 'loading' });
    fetchCategories(ctrl.signal)
      .then(data => setState({ kind: 'ok', data }))
      .catch(error => {
        if (!ctrl.signal.aborted) {
          setState({ kind: 'error', error });
        }
      });
    return () => ctrl.abort();
  }, []);
  ```

- **SwiftUI realization.** Use `URLSession.shared.data(from:)`, `Decodable`, `async throws`, `.task` (cancelled automatically when the view disappears), an `enum LoadState` with associated values, and `@MainActor` on the store.

  ```swift
  struct Category: Decodable, Identifiable {
      let id: String
      let label: String
  }

  func fetchCategories() async throws -> [Category] {
      let url = API.base.appending(path: "categories")
      let (data, resp) = try await URLSession.shared
          .data(from: url)
      guard (resp as? HTTPURLResponse)?.statusCode == 200
      else { throw URLError(.badServerResponse) }
      return try JSONDecoder()
          .decode([Category].self, from: data)
  }
  ```

- **Lab (artifact `v0.8`):** categories and shared public reports come from the course API, with an airplane-mode error state and retry.
- **Close:** Parcial 1 logistics (covers S01 to S07; ticket format, machines and allowed resources are in section 4).
- **Homework:** RN: replace the hand-rolled loading code with `useQuery` and write a five-line comparison in the rubric's terms. SwiftUI: add retry with backoff (`Task.sleep`) and a test showing that cancellation stops it.
- **Quiz idea:** the request takes 10 seconds and the user leaves the screen after 2. What happens with cancellation, and what happens without it?

### S09 · Persistencia local y trabajo sin conexión / Local persistence and offline work

- **Original items:** I8 (offline connectivity), T7 (data side); otherwise additions N5 and N13
- **Mental model:** the device is the first source of truth. Persist locally and sync opportunistically. Pick storage by the data's shape and sensitivity, and treat every schema change as a migration of real users' data.
- **Current instance:** `expo-sqlite`, AsyncStorage and `expo-secure-store` (RN); SwiftData, `@AppStorage` and Keychain (SwiftUI).
- **Topics**
  1. The storage spectrum (key-value, relational, files, secure storage), chosen by shape, size and sensitivity
  2. Relational persistence on the device: schema, parameterized queries, or models and queries
  3. Migrations: a versioned schema, and adding a field without losing data
  4. Offline-first: the local database as the source of truth, a sync queue with statuses, and last-write-wins as the baseline conflict policy
  5. The user session: token auth, secure storage, and logout clearing local data
- **Objectives.** The student can:
  1. Persist reports so they survive an app restart and a device reboot
  2. Write a migration that adds a field and show that existing rows survive it
  3. Store the auth token in secure storage and show it is absent from plain key-value storage
  4. Implement a sync queue that uploads pending reports when online and marks them as synced
  5. Justify a storage choice for four given data items
- **React Native realization.** Use `SQLiteProvider` with an `onInit` migration based on `PRAGMA user_version`, `useSQLiteContext`, and `runAsync` and `getAllAsync` with `?` parameters (linked to the MySQL course). AsyncStorage holds preferences and `expo-secure-store` holds the token. The S07 repository gets a SQLite implementation.

  ```ts
  async function migrate(db: SQLiteDatabase) {
    const row = await db.getFirstAsync<{ user_version: number }>(
      'PRAGMA user_version');
    let v = row?.user_version ?? 0;
    if (v < 1) {
      await db.execAsync(`CREATE TABLE report (
        id TEXT PRIMARY KEY, title TEXT NOT NULL,
        status TEXT NOT NULL)`);
      v = 1;
    }
    if (v < 2) {
      await db.execAsync(
        'ALTER TABLE report ADD COLUMN photo TEXT');
      v = 2;
    }
    await db.execAsync(`PRAGMA user_version = ${v}`);
  }
  ```

- **SwiftUI realization.** Use `@Model`, `.modelContainer(for:)`, `@Query`, and `modelContext.insert` and `delete`. Compare lightweight migration (adding an optional property) with `VersionedSchema` and `SchemaMigrationPlan`. Use `@AppStorage` for preferences and a course-provided Keychain helper. Discussion: `@Query` inside views (convenient) against the S07 repository (testable), as a real trade-off.

  ```swift
  @Model
  final class Report {
      var title: String
      var status: String = "pending"
      var createdAt: Date = Date.now
      var photoPath: String?

      init(title: String) { self.title = title }
  }

  @Query(sort: \Report.createdAt, order: .reverse)
  private var reports: [Report]
  ```

- **Lab (artifact `v0.9`):** offline persistence, a sync queue and a login screen.
- **Homework:** add a `severity` field through a migration with a default, and export reports to a JSON file (sharing it comes in S12).
- **Project milestone:** team proposal (stakeholder, problem statement, user stories, the two "beyond the course" features).
- **Quiz idea:** match the auth token, the theme preference, 5,000 reports and their photos to key-value storage, secure storage, the database and files.

### S10 · Cámara, fotos y archivos / Camera, photos and files

- **Original items:** I4, T5 (images and densities), T7 (system pickers), A12 (permissions)
- **Mental model:** device capabilities are permission-gated. Ask at the moment of need, explain why, handle denial, and prefer a system picker that needs no permission over full access (least privilege).
- **Current instance:** `expo-image-picker`, `expo-camera` and `expo-file-system` (RN); `PhotosPicker`, a camera wrapped from UIKit and `FileManager` (SwiftUI).
- **Topics**
  1. The permission model: declared purpose strings plus a runtime prompt; the states (not asked, granted, denied, limited); the denial path and a link to Settings
  2. System picker or custom camera, chosen by least privilege
  3. The capture pipeline: preview, capture, resize and compress, store in the sandbox, reference from the database
  4. Image resources: density variants (`@2x`/`@3x`, `mdpi` to `xxxhdpi`), asset catalogs, caching
  5. Sandbox directories: documents and cache, and cleaning up a report's files when it is deleted
- **Objectives.** The student can:
  1. Attach a photo through the system picker without requesting photo-library permission
  2. Build a capture screen that handles the not-asked, granted and denied states
  3. Store compressed photos in the sandbox, reference them from the database and delete them with their report
  4. Write purpose strings that are specific and state the user benefit
- **React Native realization.** Use `launchImageLibraryAsync` and `launchCameraAsync`, `CameraView` with `useCameraPermissions` and `takePictureAsync`, `expo-image-manipulator` to resize, `expo-file-system` (new File and Directory API, verify) and `expo-image`. Purpose strings go in `app.json`. The iOS Simulator has no camera, while the Android emulator offers a virtual one.

  ```tsx
  const [permission, requestPermission] = useCameraPermissions();
  const camera = useRef<CameraView>(null);

  if (!permission) return null;          // aún cargando
  if (!permission.granted) {
    return <Button title="Permitir cámara"
                   onPress={requestPermission} />;
  }
  return <CameraView ref={camera} style={{ flex: 1 }} />;
  ```

- **SwiftUI realization.** Use `PhotosPicker` with `loadTransferable`; the camera through a `UIViewControllerRepresentable` around `UIImagePickerController`, on a device only; `NSCameraUsageDescription`; the documents directory from `FileManager`; and resizing with `UIGraphicsImageRenderer`. **Android counterpart:** the photo picker (Android 13 and later) and runtime permissions.

  ```swift
  @State private var item: PhotosPickerItem?

  PhotosPicker("Adjuntar foto", selection: $item,
               matching: .images)
      .onChange(of: item) { _, newItem in
          Task {
              guard let data = try? await newItem?
                  .loadTransferable(type: Data.self)
              else { return }
              store.attachPhoto(data, to: report)
          }
      }
  ```

- **Lab (artifact `v0.10`):** photos on reports, all permission paths handled, and files cleaned up on delete.
- **Homework:** a storage budget. Measure 10 photos before and after compression, with a table in the README and a recommended setting.
- **Quiz idea:** "Which permission does the app need so the user can pick a photo with the system picker?" The answer is none, because the picker runs outside the app's process (verify Expo's behavior per SDK).

### S11 · Sensores y ubicación / Sensors and location

- **Original items:** I3, I8 (location), A6 (background location as a concept)
- **Mental model:** a sensor is a stream of noisy, timestamped samples. You trade sampling rate and accuracy against battery and privacy, filter the noise, and always unsubscribe.
- **Current instance:** `expo-sensors`, `expo-location` and `react-native-maps` (verify, or `expo-maps`) in RN; Core Motion, Core Location and MapKit for SwiftUI.
- **Topics**
  1. Sensor families: motion (accelerometer, gyroscope, magnetometer), environment (barometer, light), position; units and coordinate frames
  2. Streams: subscribe, sampling rate, cleanup, low-pass filtering
  3. Location: accuracy against battery, foreground and background access, approximate and precise permission
  4. Maps: markers, regions, opening the detail from a marker; geocoding as a network call
  5. Testing with simulated data: simulated locations, recorded samples as test fixtures
- **Objectives.** The student can:
  1. Build an inclinometer that measures a surface's slope within ±1° of a reference, on a physical device
  2. Tag a report with location at a justified accuracy and handle denied or approximate permission
  3. Show reports on a map and open a report from its marker
  4. Show that the sensor subscription stops when the user leaves the screen
- **React Native realization.** Use `Accelerometer.setUpdateInterval`, `addListener` and `remove`; `requestForegroundPermissionsAsync` and `getCurrentPositionAsync` with `Accuracy.Balanced`; `MapView` and `Marker`. A calibration step compares axis signs on Android and iOS (verify current behavior). This is a deliberate "both platforms first-class" moment.

  ```tsx
  useEffect(() => {
    Accelerometer.setUpdateInterval(100);   // ms
    const sub = Accelerometer.addListener(({ x, y, z }) => {
      const rad = Math.atan2(y, Math.hypot(x, z));
      setTilt(lowPass(rad * 180 / Math.PI));
    });
    return () => sub.remove();
  }, []);
  ```

- **SwiftUI realization.** Use `CMMotionManager`, `CLLocationUpdate.liveUpdates()` (iOS 17) with an authorization request (`CLServiceSession` in iOS 18, verify), `NSLocationWhenInUseUsageDescription`, `Map { Marker(...) }` (iOS 17) and Simulator location from a GPX file. **Android counterpart:** `SensorManager` and the fused location provider.

  ```swift
  .task {
      do {
          let updates = CLLocationUpdate.liveUpdates()
          for try await update in updates {
              guard let loc = update.location else { continue }
              draft.coordinate = loc.coordinate
              break        // una lectura basta para el reporte
          }
      } catch {
          draft.locationError = error
      }
  }
  ```

- **Lab (artifact `v0.11`):** a ramp-slope measurement attached to "accesibilidad" reports, compared against a code limit (for example, the 1:12 maximum in the ADA standards), plus location tags and a live map tab.
- **Homework:** implement the low-pass filter and compare 30 raw and filtered samples in a table, justifying the smoothing factor.
- **Quiz idea:** "The user leaves the screen and the subscription is never removed. Name two consequences."

### S12 · Integración con el sistema / System integration

- **Original items:** A4, A6, A8, T6, T7 (sharing), T8 (implicit), T9 (notifications), O4, O7 (app extensions)
- **Mental model:** an app talks to the rest of the system through a few doors: notifications and links come in, the share sheet goes out, system events come in, and background time is granted by the OS, never taken.
- **Current instance:** `expo-notifications`, Expo Router linking, `Share`, NetInfo and `expo-background-task` in a development build (verify) for RN; UserNotifications, `onOpenURL`, `ShareLink`, `NWPathMonitor`, BackgroundTasks and WidgetKit for SwiftUI.
- **Topics**
  1. Notifications: local and push, permission, Android channels, routing a tap to a screen
  2. Deep links: custom schemes and verified links (App Links, Universal Links); the implicit intent as their ancestor
  3. Sharing: the share sheet going out, system pickers as the consumer side of content providers
  4. System events: connectivity and app state; Android's broadcast restrictions since 8.0 and iOS observers
  5. Background work: what each OS allows (WorkManager and foreground services, BGTaskScheduler); widgets as additional entry points
  6. When the default setup is not enough: development builds instead of Expo Go (RN), capabilities and entitlements (SwiftUI)
- **Objectives.** The student can:
  1. Schedule a local reminder for a pending report that opens that report when tapped
  2. Open a specific report from `bitacora://report/<id>`, both when the app is closed and when it is running
  3. Share a report summary through the system share sheet
  4. Trigger sync when connectivity returns, without polling
  5. For each Android component in the original syllabus, name the iOS mechanism and the API their track uses
- **React Native realization.** Use `requestPermissionsAsync`, `setNotificationChannelAsync` (Android only) and `scheduleNotificationAsync` with a URL in `data`, a response listener that calls `router.push`, a `scheme` in `app.json` (Expo Router routes the link), `Share.share` and `NetInfo.addEventListener`. Move to a development build (`npx expo run:android` or EAS) and inspect the generated `intent-filter` and `CFBundleURLTypes`.

  ```ts
  const Trigger = Notifications.SchedulableTriggerInputTypes;

  await Notifications.scheduleNotificationAsync({
    content: {
      title: 'Reporte pendiente',
      body: report.title,
      data: { url: `bitacora://report/${report.id}` },
    },
    trigger: { type: Trigger.TIME_INTERVAL, seconds: 3600 },
  });
  ```

- **SwiftUI realization.** Use `UNUserNotificationCenter` (`requestAuthorization`, `add`, and the delegate for taps), URL types in the target, `.onOpenURL` with a `NavigationPath`, `ShareLink`, `NWPathMonitor`, and `.backgroundTask(.appRefresh)` with `BGTaskScheduler`. As a stretch, a WidgetKit widget showing the pending count. **Android counterpart:** the Rosetta table is due this week.

  ```swift
  .onOpenURL { url in
      // bitacora://report/<uuid>
      guard url.host() == "report",
            let id = UUID(uuidString: url.lastPathComponent)
      else { return }
      path.append(id)
  }
  ```

- **Lab (artifact `v0.12`):** reminders, deep links, sharing and auto-sync on reconnect.
- **Homework:** RN: a one-page "platform diff" of everything that behaved differently on Android and iOS in this lab. SwiftUI: the completed Rosetta table with Android doc links, plus a short Kotlin snippet explained line by line.
- **Project milestone:** alpha, with the main flow working end to end on a device.
- **Quiz idea:** a matching table with BroadcastReceiver, implicit Intent, ContentProvider and Service on one side, and the iOS mechanism and the track's API on the other.

### S13 · Accesibilidad, idiomas y pantallas / Accessibility, languages and screens (closes with Parcial 2 logistics)

- **Original items:** O8, T5 (strings, dark mode), I1 (tablets, foldables), O15 (iPad windows)
- **Mental model:** the same app must work for every user and every screen. That takes semantics for assistive technology, text that scales, strings that translate and layouts that adapt.
- **Current instance:** RN accessibility props, i18next and `useWindowDimensions`; SwiftUI accessibility modifiers, String Catalogs and size classes.
- **Topics**
  1. Semantics: labels, roles or traits, grouping and focus order, tested with TalkBack and VoiceOver
  2. Visual accessibility: text scaling, contrast, touch targets (44 pt on iOS, 48 dp on Android), reduced motion
  3. Localization: external strings, plurals, locale formats for dates, numbers and units
  4. Adaptive layout: safe areas, orientation, tablets and foldables, iPad windows, dark mode
  5. Auditing: Accessibility Inspector, Android Accessibility Scanner, automated audits in UI tests
- **Objectives.** The student can:
  1. Complete the create-report flow using only a screen reader
  2. Run the app at the largest text size with no critical information truncated
  3. Ship Spanish and English with correct plurals and locale-formatted dates
  4. Show list and detail as two panes on a tablet
- **React Native realization.** Use `accessibilityLabel` and `accessibilityRole` (or `role` and `aria-*`), grouping with `accessible`, `maxFontSizeMultiplier`, `useWindowDimensions`, `react-native-safe-area-context`, `useColorScheme`, `expo-localization` with i18next plurals and `Intl` formatting (verify Hermes `Intl` coverage).

  ```tsx
  <Pressable
    onPress={confirmDelete}
    accessibilityRole="button"
    accessibilityLabel={t('report.delete', { title: r.title })}
    hitSlop={8}
  >
    <Ionicons name="trash" size={24} />
  </Pressable>
  ```

- **SwiftUI realization.** Use `.accessibilityLabel`, `.accessibilityElement(children: .combine)`, Dynamic Type with `@ScaledMetric`, String Catalog plurals, `Text(date, format:)`, `horizontalSizeClass` with `NavigationSplitView`, `ViewThatFits`, and `performAccessibilityAudit()` in a UI test. **Android counterpart:** TalkBack, `sp` versus `dp`, and `values-es` resources.

  ```swift
  @Environment(\.horizontalSizeClass) private var size

  var body: some View {
      if size == .regular {
          NavigationSplitView {
              ReportList()
          } detail: {
              ReportDetailPlaceholder()
          }
      } else {
          NavigationStack { ReportList() }
      }
  }
  ```

- **Lab (artifact `v0.13`):** an accessibility audit with before-and-after evidence, Spanish and English, and a tablet layout.
- **Close:** Parcial 2 logistics (covers S08 to S12).
- **Homework:** an accessibility report listing each issue, its fix and the screenshot or recording that proves it.
- **Quiz idea:** a screen reader reaches an icon-only delete button with no label. What does the user hear, and which of four fixes is correct?

### S14 · Calidad: pruebas, depuración e integración continua / Quality: testing, debugging and CI

- **Original items:** I13, I12
- **Mental model:** tests are executable specifications at different costs: many fast unit tests, fewer component tests, a handful of end-to-end flows, and checks on a real device. CI makes "it works on my machine" irrelevant.
- **Current instance:** Jest, React Native Testing Library, Maestro and GitHub Actions (RN); Swift Testing, XCUITest and `xcodebuild` on GitHub Actions or Xcode Cloud (SwiftUI).
- **Topics**
  1. The testing pyramid and what each level catches
  2. Test doubles: a fake repository, a mocked network, deterministic time and IDs
  3. UI tests that query by role and label, so accessibility pays off twice
  4. Debugging and profiling: breakpoints, logs, network inspection, render and frame profiling
  5. Continuous integration: type check, lint and tests on every PR, with a protected main branch
  6. Production observability: crash reports and logs with consent
- **Objectives.** The student can:
  1. Write a component or UI test that drives the create-report form and asserts its disabled and enabled states
  2. Write one end-to-end flow (create a report, see it in the list) that runs on an emulator or simulator
  3. Configure CI that blocks a failing PR, and show a PR going from red to green
  4. Find and fix a planted performance bug with a profiler, with before-and-after measurements
  5. Write a failing regression test before fixing a reported bug
- **React Native realization.** Use `jest-expo`, `render`, `screen.getByRole` and `fireEvent` or `userEvent`, `jest.fn`, a Maestro flow, the React Native DevTools profiler (verify), and a GitHub Actions job running `tsc --noEmit`, `expo lint` and `jest --ci`.

  ```tsx
  test('save is disabled until the title is valid', () => {
    render(<NewReport onSave={jest.fn()} />);
    const save = screen.getByRole('button', { name: 'Guardar' });
    expect(save).toBeDisabled();

    fireEvent.changeText(
      screen.getByPlaceholderText('¿Qué observaste?'), 'Fuga');
    expect(save).toBeEnabled();
  });
  ```

  ```yaml
  appId: dev.tunombre.bitacora
  ---
  - launchApp
  - tapOn: "Nuevo reporte"
  - inputText: "Fuga en laboratorio"
  - tapOn: "Guardar"
  - assertVisible: "Fuga en laboratorio"
  ```

- **SwiftUI realization.** Use parameterized `@Test`, `#expect` and `#require`, XCUITest, Instruments (Time Profiler, plus the SwiftUI instrument, verify), the view debugger, and `xcodebuild test` on a macOS runner.

  ```swift
  @Test(arguments: ["", "   ", "ab"])
  func shortTitlesAreInvalid(title: String) {
      #expect(isValidTitle(title) == false)
  }

  func testCreateReport() throws {
      let app = XCUIApplication()
      app.launch()
      app.buttons["Nuevo reporte"].tap()
      let field = app.textFields["¿Qué observaste?"]
      field.tap()
      field.typeText("Fuga")
      app.buttons["Guardar"].tap()
      XCTAssertTrue(app.staticTexts["Fuga"].exists)
  }
  ```

- **Lab (artifact `v0.14`):** a test suite, CI green on main, and the planted performance bug fixed with measurements.
- **Homework:** a regression test (written failing first) for a bug from the course issue tracker, plus coverage of the store and repository.
- **Project milestone:** beta, with CI green, the core flow covered by an end-to-end test and an issue list triaged.
- **Quiz idea:** five failure scenarios (wrong validation rule, broken route, decoding change, slow list, crash on one OS version). Which test level catches each, and which none does?

### S15 · Seguridad, privacidad y publicación / Security, privacy and release

- **Original items:** T10, O16, I14
- **Mental model:** shipping is a pipeline of identity and signing, build variants, versioning, privacy disclosures, testers, staged release and updates. Security starts from assuming an attacker will read the binary.
- **Current instance:** EAS Build, Submit and Update with Google Play Console and App Store Connect (RN); Xcode Archive with TestFlight and App Store Connect (SwiftUI).
- **Topics**
  1. Signing: the upload key and Play App Signing; certificates and provisioning profiles; what each one protects
  2. Build variants and configuration: development, preview and production, and what ends up inside the bundle
  3. Versioning: semantic versions for people, build numbers for stores (`versionName`/`versionCode`, `CFBundleShortVersionString`/`CFBundleVersion`)
  4. Store requirements: privacy labels and the Data safety form, privacy manifests, permission justifications, account deletion, review guidelines
  5. Distribution: internal testing, TestFlight, staged rollout, over-the-air updates and their limits
  6. Security baseline: OWASP MASVS categories, TLS and App Transport Security, secure storage, no secrets in the bundle
- **Objectives.** The student can:
  1. Produce a signed release candidate that at least three classmates install
  2. Bump both version identifiers correctly for a patch release
  3. Fill in Bitácora's privacy disclosure, justifying each data type against the code
  4. Find and fix three security issues in a given code sample
  5. Decide whether a given change can ship over the air or needs a store build, and justify it
- **React Native realization.** Set up `eas.json` profiles, `eas build -p android --profile preview` (an APK for internal distribution) or a local release build, `eas submit`, EAS Update channels with `runtimeVersion`, and `app.config.ts`. Teach that `EXPO_PUBLIC_*` values are public. Android: an AAB and Play internal testing. iOS: requires an Apple Developer team (see 3.0).

  ```json
  {
    "build": {
      "development": { "developmentClient": true,
                       "distribution": "internal" },
      "preview": { "distribution": "internal",
                   "android": { "buildType": "apk" } },
      "production": { "autoIncrement": true }
    }
  }
  ```

- **SwiftUI realization.** Cover Product > Archive, the Organizer, automatic signing, the App Store Connect record, TestFlight internal testers, `PrivacyInfo.xcprivacy` (`@AppStorage` uses UserDefaults, a "required reason" API), build configurations and `#if DEBUG`. **Android counterpart:** Play Console tracks, the AAB and the Data safety form.

  ```xml
  <key>NSPrivacyAccessedAPITypes</key>
  <array>
    <dict>
      <key>NSPrivacyAccessedAPIType</key>
      <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
      <key>NSPrivacyAccessedAPITypeReasons</key>
      <array><string>CA92.1</string></array>
    </dict>
  </array>
  ```

  (Verify the reason code against Apple's current list.)

- **Lab (artifact `v0.15`):** a release candidate distributed to classmates, plus a store listing package (Spanish and English description, screenshots, privacy answers, release notes).
- **Homework:** a PR fixing the security issues found in their own app, each with a one-line threat explanation.
- **Project milestone:** release candidate, installed by at least five testers outside the team.
- **Quiz idea:** RN: "Is `EXPO_PUBLIC_MAPS_KEY` secret?" SwiftUI: "Can you hide an API key inside the compiled binary?" The answer is no in both, and the follow-up is where the key should live instead.

### S16 · Evaluar la siguiente herramienta / Evaluating the next tool (closes with project delivery)

- **Original items:** I6, I7, I15, I16, I14 (demo)
- **Mental model:** tools are instances of concepts. You evaluate any new one with a fixed rubric, a timeboxed spike and a written decision record that carries a review date.
- **Current instance:** the course ADR template and rubric, plus a menu of spikes.
- **Topics**
  1. The evaluation rubric and the ADR (context, options, decision, consequences, review date)
  2. Hybrid and web: WebView shells (from Cordova to Capacitor), PWAs, and when each is the right answer
  3. The cross-platform landscape as a decision: RN, Flutter, Kotlin and Compose Multiplatform, Swift outside Apple platforms (verify status), and native
  4. Going below the framework: native modules (RN), UIKit interop and Swift packages (SwiftUI)
  5. Current trends run through the rubric: on-device AI, new form factors (wearables, foldables, XR), design-language shifts (Liquid Glass in iOS 26, Material 3 Expressive), passkeys
- **Objectives.** The student can:
  1. Evaluate an unfamiliar tool with the rubric and write an ADR with a review date
  2. Recommend native, cross-platform or hybrid for three scenarios and justify the trade-offs
  3. Complete a timeboxed spike and report its evidence as works, doesn't work or unknown
  4. Demo the team project and defend their individual code contributions
- **React Native realization.** Compare a `react-native-webview` screen with its native counterpart. Write a local Expo module (`create-expo-module --local`) exposing low-power-mode status in Swift *and* Kotlin, the place where both platforms meet in one feature.

  ```swift
  import ExpoModulesCore

  public class PowerModule: Module {
    public func definition() -> ModuleDefinition {
      Name("Power")
      Function("isLowPowerMode") {
        ProcessInfo.processInfo.isLowPowerModeEnabled
      }
    }
  }
  ```

  ```kotlin
  class PowerModule : Module() {
    override fun definition() = ModuleDefinition {
      Name("Power")
      Function("isLowPowerMode") {
        val ctx = appContext.reactContext
          ?: return@Function false
        val pm = ctx.getSystemService(Context.POWER_SERVICE)
          as PowerManager
        pm.isPowerSaveMode
      }
    }
  }
  ```

- **SwiftUI realization.** Choose one spike: SwiftUI's `WebView` (iOS 26, verify) or a `WKWebView` representable; the Foundation Models framework, which needs an Apple Intelligence-capable device (verify API and Spanish support); or a WidgetKit widget. Then read a Compose Multiplatform snippet next to its SwiftUI equivalent.

  ```swift
  import FoundationModels

  let session = LanguageModelSession(instructions:
      "Resume el reporte en una sola línea.")
  let answer = try await session.respond(to: report.notes)
  report.summary = answer.content
  ```

- **Lab:** one spike plus its ADR, peer-reviewed against the rubric.
- **Close:** project delivery and demo-day logistics.
- **Homework:** final project delivery (see section 4).
- **Quiz idea:** a fictional framework's release notes ("1.0 in two months, one maintainer, MIT, rewrites your navigation"). Apply three rubric criteria and decide adopt, trial, assess or hold.

### S17 · Examen final / Final exam

- **Original items:** all, cumulative
- **Mental model:** the sixteen models reviewed as one map, from device constraints to the evaluation method.
- **Current instance:** the exam repository for each track.
- **Topics**
  1. The sixteen mental models, one slide each, with the instance taught for each
  2. The final exam format and rules
  3. A walkthrough of a sample maintenance ticket
  4. A course retrospective: what changed in the stack during the term, and how the annex recorded it
- **Objectives.** The student can:
  1. Apply any session's mental model to an unseen scenario
  2. Navigate an unfamiliar repository and find the code responsible for a behavior
  3. Fix a bug with a regression test, under exam conditions
- **React Native and SwiftUI realization:** a sample ticket on the exam template repo for each track, with the same ticket text in both tracks.
- **Lab:** a mock ticket, solved and discussed. **Homework:** none. **Quiz idea:** five sample concept questions drawn from the shared bank.
- The deck stays short, as COM102's week 17 does, because the session goes to questions.

## 4. Assessment plan and the running case

### 4.1 Weights

| Component | What it covers | When | Weight |
|---|---|---|---|
| Labs and homework | Weekly tagged releases `v0.1` to `v0.15` and homework artifacts | All term | 20 % |
| Parcial 1 | S01 to S07, as a ticket exam plus concepts | End of week 8 | 20 % |
| Parcial 2 | S08 to S12, as a ticket exam plus concepts plus a PR review | End of week 13 | 20 % |
| Proyecto | Team fork of Bitácora for a real stakeholder | Milestones from week 9, delivered in week 16 | 25 % |
| Examen final | Cumulative: a maintenance ticket plus concepts | Week 17 | 15 % |

If the faculty requires the five-equal-parts scheme used in COM102, set Proyecto and Examen final to 20 % each. Nothing else changes.

### 4.2 What each instrument looks like (mirrors real work)

- **Labs (graded on four criteria, each pass/fail):** (1) it runs: the tag builds from a clean clone; (2) acceptance: the user story's criteria are met, with evidence from a device or emulator in the PR; (3) engineering: tests for new logic, a meaningful PR description, no secrets committed; (4) explanation: at random spot-checks, the student explains a function the professor chooses (Código de Honor). RN adds a fifth criterion: evidence on both platforms. Homework follows the house style of a rubric per assignment.
- **Partials as ticket exams.** Each student receives a starter repository they have never seen and two tickets written like real issues, with acceptance criteria. They deliver a PR with tests. Practical part 70 %, concept part 30 %. The concept part is identical for both tracks and platform-neutral. It includes Android-and-iOS counterpart questions, which is how the SwiftUI course is held to the Android unit. Parcial 2 adds a code-review item: find the defects in a provided PR. The SwiftUI exam needs Macs in the room, so book the lab.
- **Final as a maintenance ticket.** An unfamiliar codebase, one bug fixed with a regression test, one small feature, and a concept section that includes a tool-evaluation scenario scored with the rubric.

### 4.3 The running case: Bitácora

The professor provides the domain, the API contract (OpenAPI) and the wireframes. Each week adds one capability, delivered as a PR and a tag.

| Tag | Session | Capability | Acceptance check |
|---|---|---|---|
| v0.1 | S01 | Runs on two targets | Screenshots from the emulator or simulator and from a phone |
| v0.2 | S02 | Domain model and pure functions | At least 3 green tests |
| v0.3 | S03 | Own identity and lifecycle log | New name, icon and identifier on a device; log shows background and foreground |
| v0.4 | S04 | List and detail UI | Matches the wireframe on two screen sizes |
| v0.5 | S05 | Create and edit form | Save disabled until valid; validation tested |
| v0.6 | S06 | Tabs, navigation, delete, search | 1,000 rows scroll smoothly; delete is confirmed |
| v0.7 | S07 | Store and repository | Store tests pass with an in-memory fake; PR reviewed by a peer |
| v0.8 | S08 | Categories from the API | Four states visible, including airplane mode |
| v0.9 | S09 | Offline persistence, sync, login | Survives restart; migration keeps data; token in secure storage |
| v0.10 | S10 | Photos | Picker needs no permission; camera handles denial; files cleaned up |
| v0.11 | S11 | Inclinometer, location, map | Within ±1° of a reference; marker opens the report |
| v0.12 | S12 | Reminders, deep links, share, auto-sync | A link opens the report from cold start |
| v0.13 | S13 | Accessibility, Spanish and English, tablet | Screen-reader walkthrough recorded |
| v0.14 | S14 | Tests and CI | Main branch protected; E2E flow green |
| v0.15 | S15 | Release candidate | Installed by 3 classmates; store package complete |

### 4.4 The team project (25 %)

Teams of two or three fork one member's Bitácora at S09 and adapt it for **a real stakeholder on campus**. Members keep doing the weekly labs in their own repositories and bring into the project only the capabilities the stakeholder needs, so the project adds work on the domain, not a second copy of every lab. Examples are a lab that inspects equipment, the facilities office tracking maintenance, an accessibility audit of buildings, or a student group's event logistics. The professor approves each stakeholder in S09. Each team adds **two features the course did not teach**, and each needs an ADR that applies the rubric.

| Milestone | Session | Deliverable |
|---|---|---|
| Proposal | S09 | Stakeholder, problem statement, user stories, the two extra features |
| Alpha | S12 | Main flow end to end on a device |
| Beta | S14 | CI green, E2E flow, triaged issue list |
| Release candidate | S15 | Signed build with at least 5 outside testers; store package |
| Demo and defense | S16 | Live demo to the stakeholder; each member explains code the professor chooses |

| Criterion | Weight within the project |
|---|---|
| Fit to the stakeholder's acceptance criteria (stakeholder sign-off counts) | 20 % |
| Engineering: architecture, tests, CI, PR history | 25 % |
| Platform quality: accessibility, Spanish and English, permissions, offline behavior | 20 % |
| Release: signed build installed by testers, store package, privacy disclosure | 15 % |
| ADRs for the two extra features | 10 % |
| Individual oral defense | 10 % (individual) |

Individual grades can move away from the team grade based on git history and the defense.

### 4.5 Código de Honor and AI

This keeps the existing rule: *you may use AI to understand; you may not submit code you can't explain*. In labs and the project, AI assistants are allowed if disclosed in the PR description (what was generated and how it was verified). Spot-checks apply. During the partials and the final, documentation is allowed, and the AI policy is the professor's decision, stated in the S01 deck. The S07 review exercise trains the skill directly.

## 5. Current-stack annex (as of October 2026)

Legend: **checked** means read from the npm registry on 2026-10-05. **(verify)** means it comes from knowledge earlier than this term and must be confirmed before the course runs. The syllabus body never cites these versions; only this annex does.

### 5.1 React Native track

| Concept | Current instance | Status |
|---|---|---|
| Cross-platform native UI | React Native 0.86.3 | checked |
| UI library | React 19.2.3 | checked |
| Framework and toolchain | Expo SDK 57 (`expo` 57.0.26), which bundles RN 0.86.3 and React 19.2.3 | checked |
| Runtime architecture | New Architecture (Fabric, TurboModules), the default since RN 0.76 (Oct 2024) and the only option since 0.82 (verify) | partly verify |
| JS engine | Hermes, the default since RN 0.70 (2022), which compiles JS to bytecode at build time | stable |
| Language | TypeScript, the default for new RN projects since 0.71; version pinned by the Expo template (verify) | verify version |
| Routing | Expo Router 57.0.24, built on React Navigation (`@react-navigation/native` 7.5.0, `native-stack` 7.20.0) | checked |
| Local state | `useState`, `useReducer`, Context | stable |
| App store (state) | Zustand 5.x (verify); Redux Toolkit 2.x for legacy reading (verify) | verify |
| Server state | TanStack Query v5 (verify) | verify |
| Runtime validation | zod 4.x (verify) | verify |
| Relational storage | `expo-sqlite` 57.0.3 | checked |
| Key-value storage | `@react-native-async-storage/async-storage` 3.1.1 (read the v3 migration notes) | checked |
| Secure storage | `expo-secure-store` (verify version) | verify |
| Files and images | `expo-file-system` (File and Directory API, verify), `expo-image`, `expo-image-manipulator` | verify |
| Device APIs | `expo-camera` (`CameraView`), `expo-image-picker`, `expo-location`, `expo-sensors`, `expo-notifications`, `expo-haptics`, `@react-native-community/netinfo` | verify versions |
| Maps | `react-native-maps` or `expo-maps` (verify status and Expo Go support) | verify |
| Background work | `expo-background-task`, which replaced `expo-background-fetch` (verify) | verify |
| Localization | `expo-localization` with i18next and react-i18next (verify) | verify |
| Unit and component tests | Jest with `jest-expo` (verify), `@testing-library/react-native` 14.0.1 | partly checked |
| End-to-end tests | Maestro (verify); Detox as an alternative | verify |
| Debugging | React Native DevTools (verify) | verify |
| Lint and format | ESLint through `npx expo lint`, Prettier | verify |
| Build and release | EAS CLI: Build, Submit, Update (verify free-tier quotas); local `npx expo run:android` and `run:ios` | verify |
| Dev client on phones | Expo Go, which supports only the latest SDK (verify); development builds after S12 | verify |
| Native toolchains | Android Studio with the SDK and JDK version RN 0.86 requires (verify); Xcode version RN 0.86 requires (verify); CocoaPods status for RN iOS builds (verify, see 5.4) | verify |
| Node.js | The LTS line Expo SDK 57 requires (verify) | verify |

### 5.2 SwiftUI track

| Concept | Current instance | Status |
|---|---|---|
| Language | Swift 6.2 shipped with Xcode 26 (Sept 2025); check for a newer 6.x (verify) | verify current |
| IDE | Xcode 26.x; Xcode 27 expected after WWDC 2026 (verify). Check the minimum macOS (verify). macOS Tahoe 26 is the last release for Intel Macs. | verify |
| OS | iOS 26 (Sept 2025, year-based naming, Liquid Glass design); iOS 27 expected Sept 2026 (verify) | verify |
| Deployment target | Policy: current major minus one, never below iOS 17 (the floor for `@Observable`, SwiftData, `Map` content builders and `CLLocationUpdate`) | decide each term |
| Concurrency defaults | Swift 6 language mode; Xcode 26 templates default to MainActor isolation (verify) | verify |
| UI | SwiftUI; `NavigationStack` and `NavigationSplitView` (iOS 16) replaced the deprecated `NavigationView` | stable |
| Observation | `@Observable` (iOS 17); `ObservableObject` as legacy | stable |
| Persistence | SwiftData (iOS 17), `@AppStorage`, Keychain Services; Core Data as legacy reading | stable |
| Networking | `URLSession` with `async`/`await`, `Codable` | stable |
| Device APIs | `PhotosPicker` (iOS 16), AVFoundation, Core Location (`CLLocationUpdate` iOS 17, `CLServiceSession` iOS 18, verify), Core Motion, MapKit for SwiftUI (iOS 17), UserNotifications, BackgroundTasks, WidgetKit, App Intents | partly verify |
| Previews and playgrounds | `#Preview` (Xcode 15); `#Playground` macro (Xcode 26, verify) | partly verify |
| Localization | String Catalogs `.xcstrings` (Xcode 15) | stable |
| Tests | Swift Testing (Xcode 16); XCTest and XCUITest for UI; `performAccessibilityAudit` (Xcode 15) | stable |
| Profiling | Instruments; SwiftUI instrument (verify) | verify |
| Dependencies | Swift Package Manager | stable |
| On-device AI | Foundation Models framework (iOS 26, Apple Intelligence devices; verify API and Spanish support) | verify |
| Web content | SwiftUI `WebView` (iOS 26, verify); `WKWebView` | verify |
| Lint and format | `swift-format` in the toolchain (verify), SwiftLint (verify) | verify |
| CI | GitHub Actions macOS runners (verify minutes and images); Xcode Cloud (verify included hours) | verify |
| Release | App Store Connect, TestFlight (100 internal and up to 10,000 external testers); Apple Developer Program 99 USD per year; Apple university program for UP (verify) | partly verify |

### 5.3 Store and platform policies (cited in S10, S12 and S15)

| Rule | Status |
|---|---|
| Google Play: AAB plus Play App Signing required for new apps since August 2021 | stable |
| Google Play: yearly target-API deadline (API 35 by Aug 31, 2025; API 36 for 2026, verify) | verify |
| Google Play: new personal developer accounts must run a closed test before production (12 testers for 14 days, verify) | verify |
| Google Play: one-time 25 USD registration | stable |
| Android developer verification for apps installed outside Play, rolling out from 2026 (verify scope and dates). It may affect sharing APKs with classmates. | verify |
| Android: notification permission (13), photo picker (13), foreground service types (14), edge-to-edge for apps targeting API 35 (15). Current version is Android 16 (June 2025); Android 17 (verify). | partly verify |
| Apple: privacy manifests (May 1, 2024), in-app account deletion (June 30, 2022), App Tracking Transparency (iOS 14.5) | stable |
| Apple: minimum SDK and Xcode for App Store uploads (verify current rule) | verify |
| Apple: UIScene lifecycle becoming mandatory after iOS 26 (verify) | verify |
| Security reference: OWASP MASVS v2 (verify current version) | verify |
| Mexico: Ley Federal de Protección de Datos Personales en Posesión de los Particulares, new law of 2025 (verify) | verify |

### 5.4 Watch list for 2027 to 2030

These are the items most likely to force a slide change. Each one is a **concept that stays** with an **instance that may move**.

- Navigation: React Navigation 8 and Expo Router changes (verify)
- iOS dependencies under RN: CocoaPods trunk going read-only (announced for late 2026, verify) and a move to Swift Package Manager
- Hermes evolution (static Hermes and Hermes V1, verify) and the React Compiler becoming the default (verify)
- Swift outside Apple platforms (the Android workgroup and SDK, verify), and Kotlin with Compose Multiplatform on iOS (verify)
- Liquid Glass and Material 3 Expressive design changes in templates
- Android sideloading policy, and iOS distribution changes in other regions (EU, DMA)
- On-device AI APIs on both platforms, and their language coverage

### 5.5 What to re-check every term (two weeks before the course starts)

1. **Versions.** Run `npm view` for every package in 5.1, and `npx expo install --check` on both templates. Adopt a new Expo SDK only if Expo Go in both stores supports it. Record the date and versions at the top of this annex.
2. **Changelogs.** Read the Expo SDK and RN release notes since last term, and the Xcode and Swift release notes. List every removed or deprecated API that a slide uses (grep the sample repo).
3. **The staleness detector.** Run the sample repository's CI (every slide example, both tracks) on the new stack. A red job is a slide to fix. Keep each code example within the card caps of 63 characters and about 13 rows.
4. **Machines.** Check the lab Macs (macOS version, Xcode, Simulator runtimes), Android Studio, emulator images, and the Node.js LTS.
5. **Policies.** Check the Play target-API deadline, Play testing rules and developer verification, the Apple SDK minimum, privacy-manifest reason codes, and App Review Guidelines changes. Update the S15 slides.
6. **Accounts.** Check the Apple team or university program status, the EAS organization and free quota, GitHub Classroom and Actions minutes.
7. **Course API.** Confirm the host is alive and the OpenAPI contract is unchanged (a contract change is a version bump announced in S08).
8. **Trend radar.** Update the S16 radar (adopt, trial, assess, hold) with one to three changes, each with a one-line reason.
9. **Retirement rule.** When an instance dies, its replacement goes into this annex and into the realization line. The syllabus text, which names the concept, does not change.

### 5.6 Notes for building the decks in this repository

- Suggested folders (subject name and course code to confirm with the faculty): `ppts/react-native/desarrollo-de-aplicaciones-moviles/{es,en}` and `ppts/swift/desarrollo-de-aplicaciones-moviles/{es,en}`, each with `w01.0` (encuadre: roadmap, grading table, tools, Código de Honor) and `w01` to `w17`. Covers read "Sesión N de 17".
- The kit is ready. `kit/tokens.py` already defines the `react` and `swift` palettes, and `kit/highlight.py` handles `tsx`/`ts`/`typescript`, `swift`, `kotlin`, `json`, `xml`/`plist` and `bash`. Set `meta.language: react` or `swift`.
- The code examples above respect the code-card caps (at most 63 characters per line and about 13 rows) or split cleanly into two slides. The longer ones (S09 migration, S14 UI test) are written to be shown as two cards.
- Each session's deck pairs a `concept` slide (the mental model) with `code` slides (the instance), a `lab` slide, a `homework` slide with its rubric, and a `quiz` and `trace` pair. On the SwiftUI side, the Android counterpart fits the `compare` or `table` layout.