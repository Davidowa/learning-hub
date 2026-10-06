<!-- Propuesta de temario, lente: durabilidad. Borrador de un agente diseñador, sin verificar; ver HANDOFF-auditoria-y-cursos-nuevos.md en la raíz. -->

# Desarrollo de Aplicaciones Móviles: one syllabus, two tracks (React Native · SwiftUI)

**Durability-first proposal** · Prepared for David Escobar-Castillejos, Universidad Panamericana · Snapshot date: 2026-10-06

**How the facts were checked.** Version facts come from three kinds of source, all read on 2026-10-05 and 2026-10-06:
- the npm registry;
- developer.apple.com: the Releases page, the Xcode system-requirements page, the Xcode 27 release notes and the Upcoming Requirements page;
- developer.android.com: the Android Studio releases page and the developer-verification page.

Anything I could only confirm through secondary sources is marked **(verify)**. The repo's `/tmp/claude-0/newcourses/stack-facts.txt` matches what I found on npm.

---

## 0. Decisions at a glance

1. **The structure is one concept per session.** The original has an Android unit and an iOS unit, which teach each idea twice in two vocabularies. Instead, each session teaches one transferable model, then builds one current instance of it per track.
2. **The two courses share the same session titles, objectives and assessment.** Only the "realization" block differs.
   - **React Native track:** Android and iOS are both first-class. Every lab is checked on both platforms, the generated `android/` and `ios/` projects are read, a native module is written in Kotlin and Swift, and builds are made for both stores.
   - **SwiftUI track:** iOS is built. The Android unit becomes platform concepts taught as Android-to-iOS counterparts, with a counterpart slide in S7, S8, S12, S13 and a Compose-to-SwiftUI port in S15.
3. **Product names and versions never appear in session titles or objectives.** They live in the dated annex (section 5) and in a lab sheet that is reviewed every term.
4. **There is a planned language ramp.** S2 and S3 each spend one block on the language. Four self-study ramp decks per track follow the repo's `w01.1…w01.5` precedent, and async gets its own ramp deck before S9.
5. **Hardware is a hard constraint for SwiftUI.** Xcode 27 "will only install and run on Apple silicon Macs" and needs macOS Tahoe 26.6 or later (Apple's Xcode 27 release notes). React Native with Expo runs on any laptop plus a phone, but two things need a Mac or a paid Apple account (section 3.4): the iOS half of the native module in S15 and iOS release builds in S16.
6. **Students learn to judge new tools themselves.** A six-question *ficha de evaluación de tecnología* is introduced in S2 and delivered twice (S2 and S15). It is applied to a trend in S16 and tested in every exam through a "transfer item".

---

## 1. Audit of the original syllabus

**Verdicts:** keep, reframe, replace, merge or remove. **Sessions:** S1 to S17 (section 3).

| # | Original item | Verdict | Reason (obsolescence facts where they apply) | Lands in |
|---|---|---|---|---|
| H1 | INTRODUCCIÓN Y CONCEPTOS BÁSICOS | keep, renamed | Becomes Unit 1, *Fundamentos*. | S1–S3 |
| 1 | Tipos de dispositivos inteligentes | reframe | Lists of device types age fastest. BlackBerry OS services ended in January 2022 and Windows 10 Mobile support ended in January 2020. The durable idea is *form factors defined by constraints*: screen, input, power, connectivity and context of use. The current list (phones, tablets, foldables, watch, TV, car, XR headsets and glasses) goes in the annex. | S1, annex |
| 2 | Ventajas de usar dispositivos inteligentes | reframe | It is one-sided. It becomes *affordances and costs*: context, sensors and presence against battery, privacy and attention. | S1 |
| 3 | Sensores | keep | Sampling rate, energy, permissions and coordinate frames are all durable. | S11 (overview in S1) |
| 4 | Cámara | keep | Durable topics: capture versus system picker, permissions and image metadata. | S11; S15 (SwiftUI bridge) |
| 5 | Introducción a herramientas y tecnologías para móviles | reframe | Tool names are version-bound. Teach the toolchain by role (SDK, compiler, build system, package manager, emulator or simulator, signing). The names go in the annex. | S1, S2, annex |
| 6 | Tecnologías nativas y web | reframe | A two-way native/web split no longer describes React Native, Flutter or Kotlin Multiplatform. "Native" has three independent axes: language, UI toolkit and renderer. | S2 |
| 7 | Comparativa entre tecnologías | replace | A static comparison table expires within a year. It is replaced by a method (the *ficha*) plus a dated table in the annex. | S2, S15, S16, annex |
| 8 | Conectividad e interacción | reframe, split | Ambiguous, so it is split four ways. Connectivity becomes networking, offline handling and HTTPS (S9). Short-range radios (Bluetooth LE, NFC) are an optional block in S11. Interaction becomes touch, gestures and input (S4, S5). Interaction between apps goes to S12. | S9, S5, S11, S12 |
| 9 | Creación aplicaciones | keep, fix the name | Should read "Creación *de* aplicaciones". The development lifecycle is durable and becomes the spine of the team project. | S3, project |
| 10 | Análisis del problema | keep | Durable. | S3 |
| 11 | Diseño de la aplicación | keep, expand | Add user flows, wireframes, platform guidelines (HIG, Material), and accessibility and localization from day one. | S3, S5 |
| 12 | Desarrollo de la aplicación | merge | This is the body of the course. | S4–S13 |
| 13 | Pruebas de funcionamiento | reframe, expand | Functional testing is one level only. Teach the test pyramid (unit, component, end-to-end) plus accessibility and performance evidence. | S14 (tests from S3 on) |
| 14 | Entrega | merge | Same concept as both "Publicación" lines, plus maintenance after release. | S16 |
| 15 | Aplicaciones hibridas | reframe, fix the accent ("híbridas") | The term is ambiguous. It used to mean WebView apps: PhoneGap (2009); Adobe discontinued PhoneGap and PhoneGap Build in 2020; Apache Cordova continues and Capacitor is the common current instance. Today it has to be told apart from cross-platform native UI (React Native) and own-renderer toolkits (Flutter). | S2 |
| 16 | Tendencias futuras… | replace | A list of trends is obsolete by design. It is replaced by a method for judging a trend, plus a dated "trends to watch" section in the annex. | S2, S16, annex |
| H2 | APLICACIONES NATIVAS PARA ANDROID | replace (structure) | One unit per platform duplicates installation, projects, UI and publication. Replaced by one concept per session with an Android realization (section 3.2). | S7, S8, S12, S13, S15 |
| 17 | ¿Qué es Android? | merge with 40 | Governance, distribution and update model are taught side by side for both platforms. | S1, S2 |
| 18 | Descripción e instalación del entorno de desarrollo y dispositivos virtuales (Android) | reframe | Installation steps change with every release. Android Studio replaced Eclipse ADT in 2014–2015; today's stable channel is Android Studio Rabbit 1 (2026.2.1). Keep the concept (emulator versus device) and move the steps to a dated lab sheet. | S1 (RN), S15 optional (SwiftUI) |
| 19 | Arquitectura de Android | keep | The layering (Linux kernel, HAL, ART, native libraries, framework, apps) has been stable for over a decade. | S8 |
| 20 | Componentes de una aplicación | keep | The four components (activity, service, broadcast receiver, content provider) are still how the OS sees an app. | S8 |
| 21 | Actividades | reframe | Still the entry point, but modern apps use a single activity with Compose screens. Concept: an entry point and a screen whose lifecycle the OS owns. | S7, S8 |
| 22 | Servicios | reframe | Free-running background services ended with the Android 8.0 limits (API 26, 2017). Since Android 14 (API 34), foreground services must declare a type, and deferrable work goes to WorkManager. Concept: background work within a budget the OS sets. | S13 |
| 23 | Manifiesto | keep, merge with 28 | A declarative contract with the OS. | S8 |
| 24 | Procesos en Android | keep | Process death is the durable reason state restoration exists. | S8 |
| 25 | Máquina virtual Dalvik | replace | **Obsolete.** ART shipped as an option in Android 4.4 (2013) and replaced Dalvik entirely in Android 5.0 (2014). Concept: managed runtime and execution model (interpreter, JIT, AOT), compared with Swift's ahead-of-time native code and Hermes bytecode in React Native. | S8 |
| 26 | Proyectos | merge (26, 27, 48, 49) | Duplicated per platform. | S1, S3, S8 |
| 27 | Creación y estructura de un proyecto | merge | Project anatomy is taught once per track, including the native folders. | S1, S8 |
| 28 | Archivo AndroidManifest.xml | merge into 23 | The RN track reads the version generated from `app.json` by `npx expo prebuild`. The SwiftUI track reads it as the counterpart of Info.plist. | S8 |
| 29 | Manejo de componentes | reframe | Vague. Becomes composition of UI components and communication between them. | S4, S6 |
| H3 | CONTENIDO TEMÁTICO | remove (misnamed) | A generic heading (literally "thematic content") sitting over Android framework topics. Its items are redistributed. | n/a |
| 30 | Interfaz del usuario | merge with 51 | One UI-paradigm session per track. | S4 |
| 31 | Fragmentos | replace | Fragments (Android 3.0, 2011) still exist in AndroidX, but Google's recommended UI toolkit is Jetpack Compose (1.0 stable, July 2021). Concept: a reusable UI unit plus a navigation destination. | S4, S7 |
| 32 | Vistas | reframe, merge with 52 | The imperative View tree becomes declarative views (Compose, SwiftUI, React Native components). | S4 |
| 33 | Diseños | reframe | XML layouts become the general concept of a layout system: flexbox, stacks and size negotiation. | S5 |
| 34 | Recursos | keep | Resource qualifiers (density, locale, night mode) and asset catalogs are durable. | S5, S10 |
| 35 | Receptores de radiodifusión | reframe | A literal translation of "broadcast receiver"; keep the English term in parentheses because that is how docs and errors name it. Implicit broadcasts have been restricted since Android 8.0 (2017). Concept: subscribing to system events. | S12, S8 |
| 36 | Proveedores de contenido | reframe | Apps rarely write providers now. They consume shared data through system pickers: the Android photo picker (Android 13, 2022), PHPicker (iOS 14, 2020) and SwiftUI's PhotosPicker (iOS 16, 2022). Concept: controlled data sharing across the app boundary. | S12, S10, S11 |
| 37 | Intentos implícitos y explícitos | keep, split | A durable messaging model. Explicit intents become navigation inside the app; implicit intents become delegating a task to another app through the OS. | S7, S12 |
| 38 | Menús, diálogos y notificaciones | keep, reframe | The options menu became the app bar (Action Bar in Android 3.0, Toolbar in 2014). Notifications need channels since Android 8.0 and a runtime permission since Android 13. iOS has required authorization since UserNotifications in iOS 10 (2016). Concept: a ladder of how much attention each interruption costs. | S13 (bar menus in S7) |
| 39 | Publicación y distribución (Android) | merge with 55 | Android App Bundles have been required for new Play apps since August 2021. There is a yearly target-API deadline, a closed-test rule for new personal accounts, and developer verification from 2026 (annex). | S16 |
| H4 | APLICACIONES NATIVAS PARA iOS | replace (structure) | Same reasoning as H2. | across sessions |
| 40 | ¿Qué es iOS? | merge with 17 | Taught side by side with Android. | S1, S2 |
| 41 | Descripción e instalación del entorno de desarrollo y dispositivos virtuales (iOS) | reframe | Xcode 27 installs only on Apple silicon Macs and needs macOS Tahoe 26.6 or later. The Simulator has no camera. Steps go to the dated lab sheet. | S1 |
| 42 | Arquitectura de IOS | keep, fix the casing ("iOS") | The classic layers (Core OS, Core Services, Media, Cocoa Touch) are still a useful teaching model. Present them as a model, because Apple's overview that used this wording may be archived (verify). | S8 |
| 43 | Componentes de una aplicación (iOS) | reframe | UIApplication, AppDelegate and view controllers give way to App, Scene (UIScene since iOS 13, 2019) and View, plus app extensions. | S8, S12 |
| 44 | Ambiente de desarrollo (playground) | reframe | Concept: a scratchpad that gives fast feedback. Instances: Xcode playgrounds, the `#Playground` macro (present in Xcode 27), `#Preview`, and for React Native the TypeScript Playground or `npx tsx`. | S2, S3, S4 |
| 45 | Guion gráfico (storyboard) | replace | Since 2019, SwiftUI defines UI and navigation in code with live previews. Storyboards still exist for UIKit (the Xcode 27 notes still ship Interface Builder changes) but are not the default for SwiftUI apps. The concept survives as the user-flow and navigation map. | S3, S4, S7 |
| 46 | Complementos | reframe (ambiguous: confirm the meaning) | If it means **dependencies**: CocoaPods gave way to Swift Package Manager (built into Xcode 11, 2019), and CocoaPods trunk goes read-only on December 2, 2026. If it means **app extensions**: widgets, share extensions and App Intents. Both concepts are kept. | S15, S12 |
| 47 | Restricciones de visualización para multiplataformas | reframe (misnamed) | This is Auto Layout constraints (iOS 6, 2012), whose job is adapting to sizes and orientations, not to "multiple platforms". Concept: adaptive layout. Instances: SwiftUI stacks, the `Layout` protocol (iOS 16), size classes, and flexbox in React Native. | S5 |
| 48 | Proyectos (iOS) | merge | | S1, S8 |
| 49 | Creación y estructura de un proyecto (iOS) | merge | | S1, S8 |
| 50 | Manejo de componentes (iOS) | merge with 29 | | S4, S6 |
| 51 | Interfaz del usuario (iOS) | merge with 30 | | S4 |
| 52 | Vistas (iOS) | merge with 32 | UIView becomes a SwiftUI View: a value that describes UI. | S4 |
| 53 | Controles | keep | Input controls and forms. | S4, S6 |
| 54 | Ventanas | reframe | UIWindow gave way to scenes (iOS 13) and WindowGroup. iPad and Android large screens run apps in resizable windows. Concept: the app's container can be resized and there can be more than one. | S5, S8 |
| 55 | Publicación y distribución (iOS) | merge with 39 | Apple sets a yearly SDK minimum: since April 28, 2026, uploads must use Xcode 26 and the iOS 26 SDK. Also TestFlight and privacy disclosures. | S16 |

---

## 2. Additions the original lacks

| Addition | Why it earns a place | Lands in |
|---|---|---|
| **The language itself** (TypeScript or Swift) | Students know C#, Python and C++ but not these two. Learning a platform and a language at the same time without a plan is where courses fail. The ramp leans on C#: TypeScript and C# share their lead designer (Anders Hejlsberg), and both TypeScript and Swift have `?.` and `??` like C#. | S2, S3, ramp decks, async ramp before S9 |
| **Declarative UI and state as a paradigm** | SwiftUI (2019), Jetpack Compose (2021) and React all share the "UI is a function of state" model. The original assumes imperative views. | S4, S6 |
| **Asynchrony and networking** | "Conectividad" is not a skill. Almost every app consumes an API, and both languages now have async/await. | S9 |
| **Local persistence and data modeling** | The original only has content providers. Choosing storage tiers and versioning a schema are durable skills. Students already took the MySQL course in this repo. | S8 (key-value), S10 |
| **Architecture and testable design** | Separating logic from views and injecting dependencies is what makes testing and porting possible. | S6, S10, S14 |
| **Security and privacy by design** | Permission flows, a secure store, HTTPS by default, validating deep links and privacy disclosures. Mexico's data-protection law was renewed in 2025 (verify the date and scope). | S9–S12, S16 |
| **Accessibility** | Screen readers, Dynamic Type and font scale, contrast and touch targets are durable (WCAG). Xcode 27 adds `XCUIVoiceOverService` for VoiceOver UI tests. | S5, S14 |
| **Localization (es and en)** | The courses themselves are bilingual, and keeping strings out of code is a 30-year-old practice. | S5 onward |
| **Testing strategy** | Replaces the single "pruebas de funcionamiento" line with evidence at the right level. | S14 (tests start in S3) |
| **Version control and team workflow** | The project is done in teams, and the Code of Honor review relies on git history. | S3 onward |
| **Release engineering and maintenance** | Signing, versioning, beta channels, over-the-air updates, crash reports, and platform deadlines that move every year. | S16 |
| **Design guidelines and UX basics** | HIG and Material give a shared vocabulary. Using system components means design-language changes (such as iOS 26's Liquid Glass) arrive for free. | S3, S5 |
| **Evaluating technology, plus the annex** | This is what keeps the course "trascendente en el tiempo": students learn to judge the next tool themselves. | S2, S15, S16, every exam |
| **Responsible AI-assisted development** | Xcode 27 ships coding agents, and React Native developers use assistants too. Policy: you may use AI, but you must explain every line you submit, and tests are how generated code gets verified. | S1 (policy), S14 |
| **Energy and performance** | Battery is the constraint that most separates mobile from desktop. | S11, S14 |

---

## 3. The 17-session plan

### 3.1 Units, exams and durability rules

| Unit | Sessions | Assessment |
|---|---|---|
| 1 · Fundamentos: plataforma, lenguaje y proceso | S1–S3 | |
| 2 · Interfaz, estado, navegación y ciclo de vida | S4–S8 | **Parcial 1** at the end of S8 (S1–S8) |
| 3 · La app y el sistema: red, datos, sensores, otras apps, segundo plano | S9–S13 | **Parcial 2** at the end of S13 (S9–S13) |
| 4 · Calidad, código nativo y entrega | S14–S16 | **Proyecto** at S16 |
| Cierre | S17 | **Examen final** |

Weeks 8, 13 and 16 teach their full topic and close with exam or project logistics, as in COM102 and COM103.

**Durability rules for the decks**
1. Titles and objectives never name a product or a version.
2. Every session states one **durable model** (true in 10 years) and one **current instance** per track.
3. Slide code uses APIs that have been stable for at least two major releases. Anything newer gets one slide labeled *Novedad de la versión actual*.
4. Versions, installation steps and store rules live only in the annex, the w01.0 tools slide and the dated lab sheet.
5. Week N's exercise uses only what weeks 1 to N taught. For example, SwiftUI camera capture needs a UIKit bridge, so it waits until S15. Until then S11 uses the system photo picker.
6. A labs repository with CI builds every week's solution against the annex versions. A red build is the signal to review the annex.

### 3.2 How both tracks honor the Android unit and the iOS unit

| Android concept (original) | RN track (both platforms first-class) | SwiftUI track (iOS built, Android as counterpart) | Session |
|---|---|---|---|
| Activity, Fragment | Expo Router screens; read the generated `MainActivity` | Scene, root View, navigation destination | S7, S8 |
| Explicit intent | `router.push` | `NavigationLink(value:)`, path array | S7 |
| Implicit intent | `Linking.openURL`; `adb shell am start -a android.intent.action.VIEW` | `openURL`, `ShareLink`, universal links | S12 |
| Broadcast receiver | `AppState`, `Linking` events | `scenePhase`, `NotificationCenter` | S8, S12 |
| Content provider | System pickers, `expo-sharing` | App Groups, extensions, `PhotosPicker` | S11, S12 |
| Service | `expo-background-task`, which wraps WorkManager and BGTaskScheduler | `BGTaskScheduler`, `.backgroundTask` | S13 |
| AndroidManifest.xml | Generated from `app.json` by `npx expo prebuild`, then read | Compared with Info.plist and entitlements | S8 |
| Dalvik and ART | Hermes bytecode compared with ART | Native ARM64 binary compared with ART | S8 |
| Views, XML layouts, Compose | React Native components (native widgets on each OS) | Port a Compose screen to SwiftUI | S4, S15 |
| Android publication | Signed AAB or APK with EAS, Play testing tracks | Play rules taught as a counterpart of TestFlight and App Review | S16 |

In the RN track, every lab is checked on Android and iOS. Teams of two or three must include at least one device or emulator per platform. The Android emulator runs on any OS, and Expo Go runs on any phone.

In the SwiftUI track, each platform-concept session ends with a `table` slide titled "La contraparte en Android". Exam Section A includes one Android-to-iOS mapping item in both courses, so the objective is the same.

### 3.3 Language ramp

| Deck | TypeScript track | Swift track |
|---|---|---|
| w02.1 | Values, types, inference, `const`/`let`, union types, strict null checks | Values, types, `let`/`var`, optionals |
| w02.2 | Functions, arrow functions, `map`/`filter`/`reduce`, destructuring, spread | Functions, closures, collections, key paths |
| w02.3 | Object types, interfaces, discriminated unions, modules | `struct` versus `class`, enums with associated values, protocols |
| w09.1 | Promises, `async`/`await`, errors, `AbortController` | `throws`, `async`/`await`, `Task`, `@MainActor` |

Each ramp deck opens with a C# ↔ TypeScript ↔ Swift (or C# ↔ Swift) table slide. These are self-study decks, as in COM102.

### 3.4 Hardware and accounts

| Need | RN track | SwiftUI track |
|---|---|---|
| Computer | Windows, macOS or Linux with Node LTS. The Android emulator needs hardware virtualization and plenty of RAM (16 GB recommended, verify). | Mac with Apple silicon, macOS Tahoe 26.6 or later, Xcode 27 (official requirements). Students without one use the university's Mac lab. |
| Phone | Any Android phone or iPhone with Expo Go, which must support the course's SDK (verify each term). | Optional iPhone. Xcode 27 debugs on-device only on **iOS 17 or later** (official); iPhone 8 and iPhone X stop at iOS 16. The Simulator has no camera and no real accelerometer, so the S11 and S15 device parts need a phone or a lab device. |
| Accounts | A free Expo account. iOS device builds through EAS and TestFlight need the Apple Developer Program (99 USD a year). Publishing on Google Play needs a 25 USD one-time registration. | A free Apple Account (Personal Team) for your own device; profile limits apply (verify). TestFlight needs the paid program or a university program (verify that Apple's iOS Developer University Program fits). |
| Without a Mac (RN) | The Swift half of S15 is written in class and built on a lab Mac or with a teammate. The iOS release in S16 is shown with the instructor's account. | n/a |

Expo Go is used from S1 to S14. A development build is needed when the app has its own native code (S15). Custom permission strings and a custom URL scheme also need one, which is optional from S11.

### 3.5 Sessions

Each session lists: original items covered (audit #), the durable model, topics, objectives, the realization in each track with slide-worthy code, the lab, the homework and a quiz idea. The running lab case in both tracks is **"Bitácora de campo"**: a field log of campus observations with a title, note, category (from a course API), photo, location and date. Section 4 describes it.

---

#### S1 · El dispositivo móvil como plataforma / The mobile device as a platform
Plus the w01.0 course-intro deck.

**Original items:** 1, 2, 5, 8 (part), 17, 18, 26, 27, 40, 41, 48, 49

**Durable model:** A phone is a personal computer that runs on a battery, has intermittent connectivity and is full of sensors. The OS, not your app, owns its lifecycle, its permissions and its distribution.

**Topics**
1. Form factors (phone, tablet, foldable, watch, TV, car, XR) and the constraints they share.
2. The platform model: sandbox, permissions, a lifecycle the OS owns, and the store as gatekeeper. Android's governance (open-source base plus OEMs) compared with iOS's (a single vendor).
3. What mobile uniquely enables (context, camera, sensors, notifications, identity) and what it costs (battery, privacy, attention).
4. Toolchain anatomy by role: SDK, compiler, build system, package manager, emulator or simulator versus a real device, signing.
5. Course framing (w01.0): roadmap, grading, project, Code of Honor and AI policy, hardware.

**Objectives.** The student will be able to:
- name four constraints that set mobile apart from desktop, with one design consequence each;
- say who decides lifecycle, permissions and distribution on each platform;
- identify each tool in the toolchain by its role;
- run a new project on an emulator or simulator and on a physical device.

**React Native:** create the app with `npx create-expo-app@latest`, then run its `reset-project` script. Open it in Expo Go with the QR code, plus the Android emulator.

```tsx
import { Platform, Text, View } from "react-native";

export default function Inicio() {
  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <Text>Hola desde {Platform.OS}, versión {String(Platform.Version)}</Text>
    </View>
  );
}
```

Annotation: `Platform.Version` is a number (the API level) on Android and a string on iOS. Same line of code, two types.

**SwiftUI:** a new App project in Xcode, run on the Simulator, then on your own iPhone through a Personal Team. Developer Mode must be turned on (required since iOS 16).

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        let so = ProcessInfo.processInfo.operatingSystemVersionString
        Text("Hola desde iOS, \(so)")
            .padding()
    }
}

#Preview { ContentView() }
```

**Lab:** "Hola, plataforma". Create the project, run it on two targets, and record one difference between them.

**Homework:** a device inventory: OS version, sensors listed in the spec sheet, and whether the phone can be a debug target for the course. Add a paragraph on what you expect from the course.

**Quiz:** "Your app is in the background and the user opens the camera. Who decides whether your process keeps running?" Options: your code, the OS, the user, the store. Answer: the OS.

---

#### S2 · Panorama tecnológico y el lenguaje I / The technology landscape and the language, part 1

**Original items:** 5, 6, 7, 15, 16 (method), 17, 40, 44

**Durable model:** "Native" has three independent axes: language, UI toolkit and renderer. Every cross-platform tool is a trade-off along those axes, and you judge it with a fixed set of questions, not with a ranking.

**Topics**
1. The three axes, and a six-point spectrum:
   - native SDK;
   - cross-platform with native widgets;
   - own renderer;
   - shared logic with native UI;
   - web inside a native shell;
   - web app or PWA.
2. The *ficha de evaluación* asks six questions:
   - Which durable concept does the tool implement?
   - Who governs and funds it?
   - How often does it release, and how does it deprecate?
   - What is the escape hatch?
   - What evidence is there, from primary sources only?
   - What does it cost in hardware, accounts, license and learning?
3. Why this track and what the other track does.
4. Language I: types and inference, immutability, null safety, functions, higher-order functions over collections.
5. The scratchpad loop for fast feedback.

**Objectives.** The student will be able to:
- place six named technologies on the spectrum and justify each placement with the three axes;
- fill in a *ficha* using only primary sources;
- write typed, null-safe functions over collections;
- predict the result of optional-chaining and nil-coalescing expressions.

**React Native (TypeScript, strict mode, TS Playground or `npx tsx`):**

```ts
type Observacion = {
  id: string;
  titulo: string;
  nota?: string;
  creada: Date;
};

function conNota(lista: Observacion[]): string[] {
  return lista.filter((o) => o.nota !== undefined).map((o) => o.titulo);
}

const largoNota = (o: Observacion) => o.nota?.length ?? 0;
```

**SwiftUI (Swift in `#Playground` or an Xcode playground):**

```swift
struct Observacion {
    let id: UUID
    var titulo: String
    var nota: String?
    let creada: Date
}

func conNota(_ lista: [Observacion]) -> [String] {
    lista.filter { $0.nota != nil }.map(\.titulo)
}

let largoNota = { (o: Observacion) in o.nota?.count ?? 0 }
```

**Lab:** a language kata (six small functions over a list of observations), then place six technologies on the spectrum.

**Homework:** *Ficha* #1 on one technology from a list: Flutter, Kotlin Multiplatform, Capacitor, .NET MAUI, PWA, or the other track's tool. Also read ramp deck w02.1.

**Quiz:** "What does `largoNota` return for an observation with no note?" Answer: 0, in both languages.

---

#### S3 · Del problema al diseño, y el lenguaje II / From problem to design, and the language, part 2

**Original items:** 9, 10, 11, 12 (start), 26, 27, 44, 45 (as a flow map)

**Durable model:** An app starts as a problem, a user and a context of use. The design artifacts (user flows, wireframes, domain model) outlive whatever tool drew or coded them.

**Topics**
1. Problem framing: user, context, job to be done, constraints. MVP scope (must, should, won't).
2. User flows and a navigation map (the heir of the storyboard); low-fidelity wireframes; HIG and Material as a shared vocabulary.
3. Domain modeling in code: value versus reference semantics, unions and enums for screen state, interfaces and protocols.
4. Project skeleton and version control: branches, pull requests, ignoring native build folders.

**Objectives.** The student will be able to:
- write a one-page problem brief with user, context and MVP scope;
- draw a navigation map and wireframes for at least three screens;
- model screen states with a union or enum and handle every case exhaustively;
- predict how mutation behaves under value and reference semantics.

**React Native:**

```ts
type Estado =
  | { tipo: "cargando" }
  | { tipo: "listo"; datos: Observacion[] }
  | { tipo: "error"; mensaje: string };

function describir(e: Estado): string {
  switch (e.tipo) {
    case "cargando": return "Cargando…";
    case "listo": return `${e.datos.length} observaciones`;
    case "error": return e.mensaje;
  }
}
```

**SwiftUI:**

```swift
enum Estado {
    case cargando
    case listo([Observacion])
    case error(String)
}

func describir(_ e: Estado) -> String {
    switch e {
    case .cargando: "Cargando…"
    case .listo(let datos): "\(datos.count) observaciones"
    case .error(let mensaje): mensaje
    }
}
```

**Lab:** form the teams. Each team writes a brief, draws a navigation map and writes the domain model as a file that compiles.

**Homework:** project milestone **H1**: brief, map, wireframes and domain model in code. Also read ramp decks w02.2 and w02.3.

**Quiz (same question, different answer per track):** copy `a` into `b`, change `b.titulo`, and print `a.titulo`.
- In TypeScript, a shared object reference prints "Fuga".
- In Swift, a struct copy prints "Lámpara".

This difference is exactly why React needs new objects when state changes, and why SwiftUI favors value types.

---

#### S4 · Interfaz declarativa: componentes y composición / Declarative UI: components and composition

**Original items:** 29, 30, 31, 32, 45 (previews), 50, 51, 52, 53

**Durable model:** UI is a function of state. You describe the screen for the current data and the framework works out what to change. A screen is a tree of small components with stable identity.

**Topics**
1. Imperative UI (mutating views) versus declarative UI (describing them).
2. Components as functions or values of their inputs.
3. Built-in primitives: text, image, button, text input, toggle, system icons.
4. Lists built from data with stable identity, and why using the index as the key breaks.
5. The feedback loop: Fast Refresh in React Native, Previews in SwiftUI.
6. Android counterpart: View plus XML layout, and Fragment, became the Composable.

**Objectives.** The student will be able to:
- decompose a wireframe into a component tree;
- build a reusable row component parameterized by its data;
- render a list with stable identity and explain what breaks with index keys;
- explain the difference between describing UI and mutating it.

**React Native:**

```tsx
type Props = { obs: Observacion; onPress: () => void };

function Fila({ obs, onPress }: Props) {
  return (
    <Pressable onPress={onPress} style={{ padding: 16 }}>
      <Text style={{ fontWeight: "600" }}>{obs.titulo}</Text>
      {obs.nota ? <Text>{obs.nota}</Text> : null}
    </Pressable>
  );
}

<FlatList
  data={observaciones}
  keyExtractor={(o) => o.id}
  renderItem={({ item }) => <Fila obs={item} onPress={() => {}} />}
/>
```

**SwiftUI:**

```swift
struct Fila: View {
    let obs: Observacion

    var body: some View {
        VStack(alignment: .leading) {
            Text(obs.titulo).font(.headline)
            if let nota = obs.nota {
                Text(nota).font(.subheadline)
            }
        }
    }
}

List(observaciones) { obs in Fila(obs: obs) }   // Observacion: Identifiable
```

**Lab:** the Bitácora list and detail screens, using static data.

**Homework:** two static screens of the team project.

**Quiz**
- React Native: what happens with `{obs.fotos.length && <Text>…</Text>}` when there are no photos? React renders `0` outside a `<Text>`, and React Native raises an error.
- SwiftUI: what goes wrong with `var id: UUID { UUID() }`? Every redraw creates new identities, so rows lose their state and animations.

---

#### S5 · Diseño adaptable, recursos y ventanas / Adaptive layout, resources and windows

**Original items:** 8 (interaction), 11, 33, 34, 47, 54

**Durable model:** Layout is a negotiation between a container and its children, under constraints you do not control: screen and window size, text size, cutouts and language. Resources live outside the code so the system can pick the right variant.

**Topics**
1. Layout models: flexbox (React Native, Yoga) versus "parent proposes, child chooses" (SwiftUI).
2. Safe areas, cutouts and edge-to-edge. Android 15 enforces edge-to-edge for apps that target it.
3. Size classes and breakpoints, orientation, resizable windows on iPad and on Android large screens and foldables.
4. Resources: image density, color sets and dark mode, Dynamic Type and font scale. Touch targets: 44 pt in HIG, 48 dp in Material.
5. Localization in es and en: strings out of code, plurals, date and number formats.
6. Prefer system components so that design-language changes arrive for free.

**Objectives.** The student will be able to:
- predict the layout of a small tree;
- adapt one screen to compact and regular widths without duplicating it;
- support dark mode and the largest text size without clipping;
- localize a screen into es and en, including a date.

**React Native:**

```tsx
const { width } = useWindowDimensions();
const columnas = width >= 600 ? 2 : 1;

<FlatList
  key={columnas}            // changing numColumns requires a fresh list
  numColumns={columnas}
  data={observaciones}
  keyExtractor={(o) => o.id}
  renderItem={({ item }) => <Fila obs={item} onPress={abrir} />}
/>
```

Also on slides: `StyleSheet.create` with `flexDirection`, `gap` and `flex: 1`, plus `useColorScheme`, `SafeAreaView` from `react-native-safe-area-context`, and `getLocales()` from `expo-localization`.

**SwiftUI:**

```swift
struct DetalleView: View {
    @Environment(\.horizontalSizeClass) private var ancho
    let obs: Observacion

    var body: some View {
        let layout = ancho == .regular
            ? AnyLayout(HStackLayout(spacing: 24))
            : AnyLayout(VStackLayout(spacing: 12))
        layout {
            FotoView(obs: obs)
            DatosView(obs: obs)
        }
        .padding()
    }
}
```

Also on slides: String Catalogs, color assets and `@ScaledMetric`.

**Android counterpart:** `res/values-es`, `drawable-xxhdpi` and `-night` resource qualifiers.

**Lab:** make Bitácora work on tablet and in landscape, in dark mode, and in es and en.

**Homework:** a screenshot matrix of the project: 2 sizes × 2 themes × 2 languages.

**Quiz**
- React Native: what is the default `flexDirection`? Answer: column, unlike the web.
- SwiftUI: compare `.padding().background(.yellow)` with `.background(.yellow).padding()`. Which colors the larger area?

---

#### S6 · Estado y flujo de datos / State and data flow

**Original items:** 12, 29 (communication between components), 53

**Durable model:** Each piece of data has exactly one source of truth. The UI is derived from it. Values flow down, and events (or bindings) flow up.

**Topics**
1. Source of truth: local versus shared state, and derived state ("compute it, don't store it").
2. Controlled inputs, validation and error messages.
3. Data down, events up; lifting state; bindings.
4. Immutable updates (React) versus value semantics plus observation (SwiftUI).
5. Sharing state across screens, and when a library is worth it (annex).

**Objectives.** The student will be able to:
- identify the source of truth for every piece of data on a screen;
- build a form that can only be submitted when its input is valid;
- share state between two screens without copying it;
- diagnose and fix a stale-state bug.

**React Native:**

```tsx
function NuevaObservacion({ onGuardar }: { onGuardar: (t: string) => void }) {
  const [titulo, setTitulo] = useState("");
  const valido = titulo.trim().length >= 3;   // derived, not stored

  return (
    <View style={{ gap: 12, padding: 16 }}>
      <TextInput value={titulo} onChangeText={setTitulo} placeholder="Título" />
      <Button title="Guardar" disabled={!valido} onPress={() => onGuardar(titulo)} />
    </View>
  );
}

// shared: Context + immutable update
const agregar = (titulo: string) =>
  setObservaciones((prev) => [...prev, nuevaObservacion(titulo)]);
```

A `useBitacora()` hook wraps `useContext` and throws an error if it is used outside its provider.

**SwiftUI:**

```swift
@Observable
final class Bitacora {
    var observaciones: [Observacion] = []
    func agregar(_ titulo: String) { observaciones.append(Observacion(titulo: titulo)) }
}

struct NuevaObservacion: View {
    @Environment(Bitacora.self) private var bitacora
    @State private var titulo = ""
    private var valido: Bool { titulo.trimmingCharacters(in: .whitespaces).count >= 3 }

    var body: some View {
        Form {
            TextField("Título", text: $titulo)
            Button("Guardar") { bitacora.agregar(titulo) }.disabled(!valido)
        }
    }
}
```

**Lab:** a form to add observations, sharing one store with the list.

**Homework:** the project's main create or edit flow, with validation.

**Quiz**
- React Native: `setN(n + 1); setN(n + 1);` runs on one tap. What is `n` afterwards? Answer: 1. The fix is `setN(p => p + 1)`.
- SwiftUI: a child view declares `@State var titulo` and initializes it from its parent. Why does it not update when the parent changes?

---

#### S7 · Navegación y estructura de la app / Navigation and app structure

**Original items:** 21, 31, 37 (explicit intents), 38 (bar menus), 54

**Durable model:** Navigation is state: a stack of destinations, plus tabs and modals. Because it is data, it can be written down, and therefore it can be a URL.

**Topics**
1. Patterns: stack, tabs and modal or sheet, and when to use each.
2. Navigation as data: pass IDs, not objects.
3. Back behavior: the Android system back gesture versus the iOS edge swipe and back button.
4. Toolbars, titles and menus in the bar.
5. Android counterpart: activities, fragments, explicit intents and the Navigation component.

**Objectives.** The student will be able to:
- choose and justify a navigation pattern for each project flow;
- implement a stack, tabs and a modal;
- pass a parameter by ID and handle an ID that no longer exists;
- explain how an explicit intent and a navigation push express the same idea.

**React Native (Expo Router):**

```tsx
// app/_layout.tsx
export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
      <Stack.Screen name="nueva" options={{ presentation: "modal", title: "Nueva" }} />
    </Stack>
  );
}

// app/observacion/[id].tsx
export default function Detalle() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const obs = useBitacora().observaciones.find((o) => o.id === id);
  if (!obs) return <Text>No existe la observación {id}</Text>;
  return <Text>{obs.titulo}</Text>;
}
```

The list links to the detail with `<Link href={{ pathname: "/observacion/[id]", params: { id: obs.id } }}>`.

**SwiftUI:**

```swift
NavigationStack {
    List(bitacora.observaciones) { obs in
        NavigationLink(obs.titulo, value: obs.id)
    }
    .navigationDestination(for: UUID.self) { id in DetalleView(id: id) }
    .navigationTitle("Bitácora")
}

TabView {
    Tab("Bitácora", systemImage: "list.bullet") { ListaView() }
    Tab("Ajustes", systemImage: "gear") { AjustesView() }
}
```

**Lab:** tabs (List, a placeholder Map, Settings), a detail push and a modal for new observations.

**Homework:** milestone **H2**: a navigable skeleton of the project that matches the H1 map.

**Quiz:** "Why pass the ID and not the whole object?" Answer: there is one source of truth, the address stays valid, and S12 will turn it into a URL.

---

#### S8 · La plataforma por dentro: arquitectura y ciclo de vida / Inside the platform: architecture and lifecycle
Closes with **Parcial 1** logistics.

**Original items:** 19, 20, 21, 22 (preview), 23, 24, 25, 27, 28, 42, 43, 49, 54

**Durable model:** The OS is a layered system that starts, suspends and kills your process when it needs to. Your app is a set of declared components plus a manifest, which is its contract with the OS.

**Topics**
1. The layers on each OS.
   - Android: kernel, HAL, ART, framework.
   - iOS: Core OS, Core Services, Media, Cocoa Touch and SwiftUI.
2. Execution models.
   - ART (JIT plus AOT) replaced Dalvik.
   - Swift compiles ahead of time to native code.
   - In React Native, the JS engine (Hermes) runs precompiled bytecode.
3. Components the OS knows: Android's four, and iOS's app, scenes and extensions.
4. The manifest as a contract: AndroidManifest.xml ↔ Info.plist plus entitlements.
5. Lifecycle and process death; saving small UI state in a key-value store. Tiers of storage come in S10.

**Objectives.** The student will be able to:
- draw the layer diagram of both OSes and place their own code and the runtime in it;
- map Android's four components to their iOS counterparts;
- read a manifest and say what the app declares;
- keep a draft through backgrounding and process death.

**React Native:** run `npx expo prebuild`, open the generated `android/app/src/main/AndroidManifest.xml` and `ios/…/Info.plist`, then delete the folders again. In React Native these files are generated from `app.json`.

```tsx
useEffect(() => {
  const sub = AppState.addEventListener("change", (estado) => {
    if (estado === "background") AsyncStorage.setItem("borrador", titulo);
  });
  return () => sub.remove();
}, [titulo]);
```

```xml
<activity android:name=".MainActivity" android:exported="true">
  <intent-filter>
    <action android:name="android.intent.action.MAIN" />
    <category android:name="android.intent.category.LAUNCHER" />
  </intent-filter>
</activity>
```

Annotation: `android:exported` has been mandatory for components with intent filters since Android 12.

**SwiftUI:** the App, Scene and View hierarchy, plus Info.plist. The S8 Android counterpart table is the one in section 3.2.

```swift
struct NuevaObservacionView: View {
    @SceneStorage("borrador.titulo") private var titulo = ""
    @Environment(\.scenePhase) private var fase
    // …
}
```

Annotation: the draft is restored when the *system* ends the process, not after the user force-quits.

**Lab:** a lifecycle logger. Reproduce the lost draft, then fix it.
- Android: turn on Developer options > "Don't keep activities".
- iOS: stop the app from Xcode while it is in the background.

**Homework:** a practice set for Parcial 1.

**Quiz:** "The form is half filled, the user opens the camera, and the OS kills the process. What does the user see when they come back if you saved nothing?" Answer: an empty form.

---

#### S9 · Asincronía y servicios remotos / Asynchrony and remote services

**Original items:** 8 (connectivity)

**Durable model:** The UI thread must never wait. Network calls are asynchronous, can fail or never finish, and their data is untrusted until it is validated.

**Topics**
1. The main thread: the JS event loop and Swift's `@MainActor`; why blocking freezes the screen.
2. `async`/`await` and cancellation tied to the screen's lifetime.
3. HTTP, REST and JSON. HTTPS is the default on both platforms: App Transport Security since iOS 9, and Android blocks cleartext by default when targeting API 28 or later.
4. The type system does not check the network: decode and validate.
5. Loading, error, empty and content states, using the union from S3; offline and retries.

**Objectives.** The student will be able to:
- predict the execution order of async code;
- fetch and decode a JSON resource and show all four states;
- cancel a request when its screen goes away;
- survive a malformed response without crashing.

The data source is a read-only JSON catalog published from the course repository. Because the course controls it, a third-party API cannot disappear mid-term.

**React Native:**

```tsx
useEffect(() => {
  const control = new AbortController();
  fetch(URL_CATALOGO, { signal: control.signal })
    .then((r) => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); })
    .then((datos) => setEstado({ tipo: "listo", datos: datos as Categoria[] }))
    .catch((e) => {
      if (!control.signal.aborted) setEstado({ tipo: "error", mensaje: String(e) });
    });
  return () => control.abort();
}, []);
```

Annotation: `as Categoria[]` is a promise to the compiler, not a check.

**SwiftUI:**

```swift
struct Categoria: Codable, Identifiable { let id: Int; let nombre: String }

func cargarCatalogo() async throws -> [Categoria] {
    let (datos, respuesta) = try await URLSession.shared.data(from: urlCatalogo)
    guard (respuesta as? HTTPURLResponse)?.statusCode == 200 else {
        throw URLError(.badServerResponse)
    }
    return try JSONDecoder().decode([Categoria].self, from: datos)
}

// in the view; .task cancels itself when the view disappears
.task {
    do { estado = .listo(try await cargarCatalogo()) }
    catch { estado = .error(error.localizedDescription) }
}
```

**Lab:** a catalog screen with all four states, tested in airplane mode and on a throttled network.

**Homework:** the project uses one remote resource and shows all four states. Also read ramp deck w09.1.

**Quiz**
- TypeScript: `console.log("A"); cargar().then(() => console.log("C")); console.log("B");` prints A, B, C.
- Swift: what happens when the JSON lacks `nombre`? Decoding throws, and the error state is shown.

---

#### S10 · Persistencia local / Local persistence

**Original items:** 12, 34 (part), 36 (part)

**Durable model:** Choose storage by the shape and sensitivity of the data:
- key-value for preferences;
- files for blobs;
- a database for records you query;
- the OS secure store for secrets.

Schemas change over time, so give them a version number.

**Topics**
1. A matrix of storage tiers.
2. SQLite on the device (recapping the relational course) and object persistence.
3. Schema versions and migrations.
4. A repository layer: the UI never knows how data is stored.
5. Secrets in Keychain or Keystore.
6. Offline-first and sync conflicts (concept only).

**Objectives.** The student will be able to:
- pick and justify a storage tier for five data items;
- persist records that survive a restart;
- write a migration that adds a field without losing data;
- store a secret in the platform's secure store.

**React Native (expo-sqlite, expo-secure-store):**

```tsx
<SQLiteProvider databaseName="bitacora.db" onInit={migrar}>…</SQLiteProvider>

async function migrar(db: SQLiteDatabase) {
  const fila = await db.getFirstAsync<{ user_version: number }>("PRAGMA user_version");
  if ((fila?.user_version ?? 0) < 1) {
    await db.execAsync(`CREATE TABLE observacion (
      id TEXT PRIMARY KEY NOT NULL, titulo TEXT NOT NULL, creada INTEGER NOT NULL);
      PRAGMA user_version = 1;`);
  }
}

const db = useSQLiteContext();
await db.runAsync("INSERT INTO observacion (id, titulo, creada) VALUES (?, ?, ?)",
  id, titulo, Date.now());
```

**SwiftUI (SwiftData, @AppStorage):**

```swift
@Model
final class Observacion {
    var titulo: String
    var nota: String?
    var creada: Date
    init(titulo: String, nota: String? = nil, creada: Date = .now) {
        self.titulo = titulo; self.nota = nota; self.creada = creada
    }
}

@Query(sort: \Observacion.creada, order: .reverse) private var observaciones: [Observacion]
@Environment(\.modelContext) private var contexto
// WindowGroup { … }.modelContainer(for: Observacion.self)
```

Annotation: the model changes from a struct to a class. This is the S3 lesson about value and reference semantics, now applied.

**Lab:** persist Bitácora, then add a `categoria` field through a migration.

**Homework:** milestone **H3**: the project with persistence and its remote resource.

**Quiz:** choose a tier for each item: theme preference, auth token, 5,000 records you query, a photo. Answer: key-value, secure store, database, file.

---

#### S11 · Sensores, cámara y ubicación / Sensors, camera and location

**Original items:** 1 (sensors), 3, 4, 8 (Bluetooth LE and NFC, optional), 12

**Durable model:** Device capabilities are privileges the user grants for a purpose. Declare the purpose, ask at the moment of use, design the path for when the user says no, and sample only as much as you need.

**Topics**
1. The permission lifecycle: purpose string, asking in context, denied or limited access, sending the user to Settings.
   - Android: after a second denial, the system stops showing the dialog (Android 11 and later).
   - iOS: you can ask only once.
2. System pickers need no permission, because they run outside your process.
3. Camera and images: size, and EXIF metadata including location.
4. Location: accuracy levels, approximate location, "when in use", battery cost.
5. Motion sensors: sampling interval, coordinate frame, unsubscribing.
6. What only a real device can test.

**Objectives.** The student will be able to:
- implement a complete permission flow, including denial and a link to Settings;
- attach an image and a location to a record;
- read a motion sensor at a set interval and stop it when the screen goes away;
- state which data is sensitive and how the app minimizes it.

**React Native:**

```tsx
const [permiso, pedirPermiso] = useCameraPermissions();
const camara = useRef<CameraView>(null);

if (!permiso) return null;
if (!permiso.granted) return <Button title="Permitir cámara" onPress={pedirPermiso} />;
return <CameraView ref={camara} style={{ flex: 1 }} facing="back" />;
// const foto = await camara.current?.takePictureAsync();

const { status } = await Location.requestForegroundPermissionsAsync();
if (status === "granted") {
  const pos = await Location.getCurrentPositionAsync({ accuracy: Location.Accuracy.Balanced });
}
```

The purpose strings go in the `expo-camera` plugin config in `app.json`. They take effect in a development build; Expo Go shows its own strings.

**SwiftUI:**

```swift
PhotosPicker("Elegir foto", selection: $seleccion, matching: .images)
    .onChange(of: seleccion) { _, item in
        Task {
            if let datos = try? await item?.loadTransferable(type: Data.self),
               let ui = UIImage(data: datos) { imagen = Image(uiImage: ui) }
        }
    }

for try await actualizacion in CLLocationUpdate.liveUpdates() {
    if let ubicacion = actualizacion.location { coordenada = ubicacion.coordinate; break }
}
```

Also on slides: the Info.plist key `NSLocationWhenInUseUsageDescription`, and `CMMotionManager` with `accelerometerUpdateInterval`. Camera capture waits for S15 because it needs a UIKit bridge.

**Lab:** each observation gets an image and a location. Optional: a level indicator using the accelerometer.

**Homework:** one device capability in the project with the complete permission flow, plus a short privacy note.

**Quiz:** "Which of these shows a permission prompt?" Answer: the system photo picker does not.

---

#### S12 · Comunicación con otras apps y con el sistema / Talking to other apps and the system

**Original items:** 8 (interaction), 35, 36, 37 (implicit intents), 43, 46 (extensions)

**Durable model:** The OS is a broker. You describe what you want done and it routes the request to an app. Your app has addresses that other apps can call, and every incoming address is untrusted input.

**Topics**
1. Implicit intents ↔ URL schemes, verified links and the share sheet.
2. Deep links: a custom scheme can be claimed by another app; verified https links (App Links, Universal Links) prevent that. Routing a URL to a screen.
3. Sharing content out and receiving it in.
4. System events: broadcast receivers ↔ `scenePhase`, `AppState` and system notifications.
5. Exposing data and functions: content providers ↔ App Groups and app extensions (widgets, share, App Intents).

**Objectives.** The student will be able to:
- open a location in the user's maps app;
- make a screen reachable by URL and validate its parameters;
- explain why a custom scheme can be hijacked and how verified links fix it;
- map broadcast receivers and content providers to their iOS mechanisms.

**React Native:**

```tsx
async function abrirEnMapa(lat: number, lon: number) {
  const url = Platform.select({
    ios: `https://maps.apple.com/?ll=${lat},${lon}`,
    android: `geo:${lat},${lon}?q=${lat},${lon}`,
    default: `https://www.openstreetmap.org/?mlat=${lat}&mlon=${lon}`,
  });
  await Linking.openURL(url);
}
await Share.share({ message: `Observación: ${obs.titulo}` });
```

```bash
adb shell am start -W -a android.intent.action.VIEW -d "bitacora://observacion/42"
xcrun simctl openurl booted "bitacora://observacion/42"
```

Annotation: the `adb` line *is* an implicit intent. Expo Router makes every route deep-linkable. In Expo Go the address starts with `exp://…/--/`; in a development build it is the app's own scheme.

**SwiftUI:**

```swift
@Environment(\.openURL) private var openURL

ShareLink(item: "Observación: \(obs.titulo)")
Button("Abrir en Mapas") { openURL(URL(string: "https://maps.apple.com/?ll=\(lat),\(lon)")!) }

NavigationStack(path: $ruta) { … }
    .onOpenURL { url in
        guard url.scheme == "bitacora", url.host() == "observacion",
              let id = UUID(uuidString: url.lastPathComponent) else { return }
        ruta.append(id)
    }
```

**Lab:** share an observation, open it in the maps app, and open the app on a given observation from the terminal.

**Homework:** milestone **H4**: one outgoing handoff, one incoming link and one device capability, plus an "intent table" for the project.

**Quiz:** "Two apps both register `bitacora://`. Which one opens?" Answer: it is not defined, which is why verified links exist.

---

#### S13 · Atención del usuario y trabajo en segundo plano / User attention and background work
Closes with **Parcial 2** logistics.

**Original items:** 12, 22, 35 (system events), 38

**Durable model:** Interrupting the user has a ladder of costs: inline feedback, then a menu, then a dialog, then a notification. Background time is a budget the OS grants, not a right.

**Topics**
1. The attention ladder: menus and context menus, confirming destructive actions, undo versus confirm.
2. Local notifications: permission, content, schedule, and a tap that deep-links (using S12).
3. Push architecture (concept and instructor demo): server → APNs or FCM → device token. It needs paid accounts and a development build (annex).
4. Limits on background execution and OS-scheduled work.
5. Android counterpart: services, foreground service types, notification channels.

**Objectives.** The student will be able to:
- choose the right level of interruption for five scenarios;
- confirm a destructive action with the platform's dialog;
- schedule a local notification that opens a specific screen;
- explain why the OS delays background work.

**React Native:**

```tsx
Alert.alert("Eliminar observación", "No se puede deshacer.", [
  { text: "Cancelar", style: "cancel" },
  { text: "Eliminar", style: "destructive", onPress: () => eliminar(obs.id) },
]);

const { granted } = await Notifications.requestPermissionsAsync();
if (granted) {
  await Notifications.scheduleNotificationAsync({
    content: { title: "Bitácora", body: "¿Registraste tu observación de hoy?", data: { url: "/nueva" } },
    trigger: { type: Notifications.SchedulableTriggerInputTypes.DAILY, hour: 18, minute: 0 },
  });
}
```

**SwiftUI:**

```swift
.confirmationDialog("¿Eliminar observación?", isPresented: $confirmar, titleVisibility: .visible) {
    Button("Eliminar", role: .destructive) { eliminar(obs) }
}

let contenido = UNMutableNotificationContent()
contenido.title = "Bitácora"
contenido.body = "¿Registraste tu observación de hoy?"
var hora = DateComponents(); hora.hour = 18
let solicitud = UNNotificationRequest(identifier: "recordatorio-diario", content: contenido,
    trigger: UNCalendarNotificationTrigger(dateMatching: hora, repeats: true))
let centro = UNUserNotificationCenter.current()
if try await centro.requestAuthorization(options: [.alert, .sound]) { try await centro.add(solicitud) }
```

In SwiftUI, a tap on the notification is handled by a small `UNUserNotificationCenterDelegate`, which hands the URL to the S12 router.

**Lab:** a daily reminder that opens "new observation", delete with confirmation, and a context menu on each row.

**Homework:** a practice set for Parcial 2.

**Quiz:** for five scenarios (validation error, irreversible delete, sync finished, a reminder, a copied link), choose the rung on the ladder.

---

#### S14 · Calidad: pruebas, accesibilidad y rendimiento / Quality: testing, accessibility and performance

**Original items:** 13

**Durable model:** Quality is evidence:
- automated tests at the right level;
- an app that can be used without sight or with very large text;
- measurements taken before any optimization.

**Topics**
1. The test pyramid: what unit tests, component or UI tests, and end-to-end tests on a device each catch.
2. Testable design: inject the network and storage.
3. Accessibility: roles, labels, focus order, text scaling, contrast, touch targets; testing with a screen reader.
4. Performance and energy: profiling, list virtualization, unnecessary re-renders, work on the main thread.
5. Using tests to verify code produced with AI help.

**Objectives.** The student will be able to:
- write unit tests for domain logic and one component or UI test;
- automate one end-to-end flow;
- audit a screen with the screen reader and fix three issues;
- measure one performance problem before and after a fix.

**React Native (Jest via jest-expo, React Native Testing Library, Maestro):**

```tsx
test("Guardar se habilita con tres letras", () => {
  render(<NuevaObservacion onGuardar={jest.fn()} />);
  fireEvent.changeText(screen.getByPlaceholderText("Título"), "Río");
  expect(screen.getByRole("button", { name: "Guardar" })).toBeEnabled();
});
```

```yaml
appId: mx.up.bitacora
---
- launchApp
- tapOn: "Nueva"
- inputText: "Lámpara fundida en el pasillo B"
- tapOn: "Guardar"
- assertVisible: "Lámpara fundida en el pasillo B"
```

**SwiftUI (Swift Testing, XCUITest, Accessibility Inspector, Instruments):**

```swift
import Testing
@testable import Bitacora

@Test(arguments: ["", "  ", "ab"])
func tituloInvalido(_ titulo: String) {
    #expect(!esTituloValido(titulo))
}

func testCrearObservacion() throws {          // XCUITest
    let app = XCUIApplication(); app.launch()
    app.buttons["Nueva"].tap()
    let campo = app.textFields["Título"]; campo.tap(); campo.typeText("Lámpara fundida")
    app.buttons["Guardar"].tap()
    XCTAssertTrue(app.staticTexts["Lámpara fundida"].waitForExistence(timeout: 2))
}
```

*Novedad* slide: `XCUIVoiceOverService` (Xcode 27) drives VoiceOver from a UI test.

**Lab:** tests plus an accessibility audit of Bitácora.

**Homework:** milestone **H5**: a quality report (tests, accessibility audit, one measurement).

**Quiz:** "An icon-only delete button has no label. What does the screen reader say?" Then: "Which test level catches a missing purpose string in Info.plist?" Answer: an end-to-end test on a device.

---

#### S15 · Más allá de la abstracción: código nativo y dependencias / Beyond the abstraction: native code and dependencies

**Original items:** 6, 18 (optional Android Studio, SwiftUI track), 41, 46; the Android unit's ideas revisited (19–37)

**Durable model:** Every abstraction leaks. Know where its boundary is and how to cross it with a bridge. Treat every dependency as code you now maintain.

**Topics**
1. Reasons to leave the abstraction: a platform-only API, a new OS feature, performance.
2. Bridges: Expo Modules (Swift and Kotlin) in React Native; UIKit representables in SwiftUI.
3. Platform-specific code paths and availability checks (`Platform.OS`, `.ios.tsx`, `if #available`).
4. Dependencies: npm and SwiftPM, the CocoaPods trunk read-only date, lockfiles, licenses, supply-chain risk, judging a package with the *ficha*.
5. The other platform: reading Kotlin and Compose.

**Objectives.** The student will be able to:
- decide when to write native code and when to look for a module;
- implement a native bridge and call it;
- carry the same function across both platforms (RN: write it in Kotlin and in Swift; SwiftUI: port a Compose screen);
- evaluate a dependency with the *ficha*.

**React Native:** create a local module with `npx create-expo-module@latest --local`. This requires a development build. `expo-battery` already does the same job; the point is to see the bridge.

```swift
public class BateriaModule: Module {
  public func definition() -> ModuleDefinition {
    Name("Bateria")
    AsyncFunction("nivel") { () -> Float in
      UIDevice.current.isBatteryMonitoringEnabled = true
      return UIDevice.current.batteryLevel          // -1 on the Simulator: unknown
    }.runOnQueue(.main)
  }
}
```

```kotlin
class BateriaModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("Bateria")
    AsyncFunction("nivel") {
      val contexto = requireNotNull(appContext.reactContext)
      val bm = contexto.getSystemService(Context.BATTERY_SERVICE) as BatteryManager
      bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY) / 100f
    }
  }
}
// JS: requireNativeModule<{ nivel(): Promise<number> }>("Bateria") from "expo-modules-core"
```

**SwiftUI:** camera capture through a bridge to UIKit, plus a "Rosetta" exercise.

```swift
struct CamaraPicker: UIViewControllerRepresentable {
    @Binding var imagen: UIImage?
    @Environment(\.dismiss) private var cerrar

    func makeUIViewController(context: Context) -> UIImagePickerController {
        let picker = UIImagePickerController()
        picker.sourceType = .camera
        picker.delegate = context.coordinator
        return picker
    }
    func updateUIViewController(_ vc: UIImagePickerController, context: Context) {}
    func makeCoordinator() -> Coordinador { Coordinador(self) }

    final class Coordinador: NSObject, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
        let padre: CamaraPicker
        init(_ padre: CamaraPicker) { self.padre = padre }
        func imagePickerController(_ picker: UIImagePickerController,
            didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey: Any]) {
            padre.imagen = info[.originalImage] as? UIImage
            padre.cerrar()
        }
    }
}
```

```kotlin
@Composable
fun Contador() {
    var cuenta by remember { mutableStateOf(0) }
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text("Observaciones: $cuenta")
        Button(onClick = { cuenta++ }) { Text("Agregar") }
    }
}
```

Students port the Compose screen to SwiftUI and map the pieces: `remember { mutableStateOf }` ↔ `@State`, state hoisting ↔ `@Binding`.

**Lab**
- React Native: the battery module on both platforms. The Android half is built locally; the iOS half on a lab Mac or with a teammate.
- SwiftUI: camera capture in Bitácora, plus the Compose port.

**Homework:** *Ficha* #2 on a dependency the project uses or is considering, and integrate the result.

**Quiz**
- React Native: "Which of these forces you out of Expo Go?"
- SwiftUI: "When does `updateUIViewController` run?"

---

#### S16 · Publicación, distribución y evolución / Release, distribution and evolution
Closes with **Proyecto** demo-day logistics.

**Original items:** 14, 16 (applied), 39, 55

**Durable model:** Shipping means four things:
- proving identity by signing;
- declaring what the app does with data;
- passing a gatekeeper;
- committing to maintenance, because the platform moves every year.

**Topics**
1. Signing and identity: certificates and provisioning on iOS, keystore and Play App Signing on Android.
2. Build configurations; no secrets in the bundle; the user-facing version versus the build number.
3. Channels: internal, then beta (TestFlight, Play testing tracks), then the store. Alternative distribution: EU marketplaces, sideloading and Android developer verification.
4. Review, policies and privacy disclosures: App Privacy, Data safety, privacy manifest.
5. After release: crash reports, analytics with consent, what over-the-air updates cannot change, yearly platform deadlines.
6. Apply the *ficha* to one trend from the annex.

**Objectives.** The student will be able to:
- produce a signed release build;
- set the version and build numbers for an update;
- fill in privacy disclosures from what the app actually does;
- decide which changes can ship over the air and which need review.

**React Native:**

```json
{
  "build": {
    "preview": { "distribution": "internal", "android": { "buildType": "apk" } },
    "production": { "autoIncrement": true }
  }
}
```

```bash
eas build --profile preview --platform android
eas update --channel production --message "Corrige texto de ayuda"
```

**SwiftUI:**

```bash
xcodebuild -scheme Bitacora -configuration Release \
  -archivePath build/Bitacora.xcarchive archive
```

Also on slides: the `MARKETING_VERSION` and `CURRENT_PROJECT_VERSION` build settings, and `PrivacyInfo.xcprivacy`.

**Lab:** a release build plus a draft store listing and privacy disclosures.

**Project:** demo day (rubric in section 4).

**Quiz:** "Which of these can ship as an over-the-air update: a new color, a new camera permission, a native module?" Answer: only the color.

---

#### S17 · Examen final / Final exam
A short deck in the style of COM102's w17: what the exam covers, a review of the four durable models per unit, a transfer-item practice, and questions.

### 3.6 Deck layout in the repo

- `ppts/react-native/desarrollo-de-aplicaciones-moviles/{es,en}/`
- `ppts/swiftui/desarrollo-de-aplicaciones-moviles/{es,en}/`

Each folder holds `w01.0`, `w01`–`w17`, `w02.1`–`w02.3` and `w09.1`: 22 decks per language per track, 88 in total.

Kit settings:
- `meta.language`: `react-native` or `swiftui` (both palettes already exist in `kit/tokens.py`).
- Code `lang`: `tsx`, `ts`, `swift`, `kotlin`, `json`, `bash`, `xml`. YAML has no highlighter, so use `text` for Maestro flows.
- The preflight already rejects em dashes.
- Concept slides (models, ladders, Android-to-iOS tables) share the same figures in both tracks.
- Footer: "DESARROLLO DE APLICACIONES MÓVILES · \<CLAVE\> · REACT NATIVE" or "… · SWIFTUI".

---

## 4. Assessment plan and running project

### 4.1 Weights
This follows the house five-by-twenty scheme from COM102.

| Component | Content | When | Weight |
|---|---|---|---|
| Parcial 1 | Units 1 and 2 (S1–S8) | End of week 8 | 20 % |
| Parcial 2 | Unit 3 (S9–S13) | End of week 13 | 20 % |
| Proyecto | Team app with milestones H1–H5 and a final demo | Week 16 | 20 % |
| Examen final | Whole course | Week 17 | 20 % |
| Tareas y laboratorios | Labs 8, homework 8, two *fichas* 4 | All term | 20 % |

**Exam format (same for both courses)**
- **Section A, shared, 60 %.** Identical items in both courses:
  - conceptual questions;
  - one Android-to-iOS mapping item;
  - one **transfer item**: a documentation excerpt from a tool not taught (for example Flutter for RN students, Compose for SwiftUI students). The student names the concept and predicts the behavior.

  The final exam adds a fictional release note, and the student decides what the app must change.
- **Section B, track, 40 %.** Parallel items checked for equal difficulty: trace or predict output, find the bug, write a small component or function.

In-deck quizzes are formative.

### 4.2 Running case: "Bitácora de campo" (labs, both tracks)

| Session | What the lab adds |
|---|---|
| S1–S3 | Platform check, domain model, screen states |
| S4–S5 | List and detail, made adaptive and localized |
| S6–S7 | Form, shared store, tabs, stack and modal |
| S8 | Draft kept through process death |
| S9 | Category catalog from the course JSON API |
| S10 | Persistence and a migration |
| S11 | Image and location, with the full permission flow |
| S12 | Share, maps handoff, deep link |
| S13 | Daily reminder, confirmation dialog |
| S14 | Tests and accessibility fixes |
| S15 | Native bridge (battery in RN, camera capture in SwiftUI) |
| S16 | Release build |

### 4.3 Team project (2 or 3 students, individual grade)

Teams pick a problem, approved by S3. Suggested themes:
- reporting incidents on campus;
- lending lab equipment;
- a log for professional practice.

**Required capabilities**
- at least four screens using a stack plus tabs or a modal;
- a validated form;
- persistence with a migration;
- one remote resource with all four states;
- one device capability with the complete permission flow;
- one incoming link and one outgoing share or notification;
- es and en localization;
- at least 8 unit tests, 1 component or UI test and 1 end-to-end flow;
- an accessibility audit;
- a signed release build with privacy disclosures;
- RN track only: verified on Android and iOS.

**Project grade (100)**

| Part | Points |
|---|---|
| H1 brief, map and wireframes (S3) | 10 |
| H2 navigable skeleton (S7) | 10 |
| H3 data and network (S10) | 10 |
| H4 device and system integration (S12) | 10 |
| H5 quality report (S14) | 10 |
| Final demo | 20 |
| Release build and disclosures | 10 |
| Code quality and tests | 10 |
| Individual oral defense | 10 |

- The individual factor (0 to 1) comes from the oral defense, the git history and peer evaluation.
- House rule: a project that does not run caps at 30 %.
- Code of Honor: AI help is allowed, but the instructor may ask any student to explain any function they submitted.

---

## 5. Current-stack annex (as of October 2026)

Source key:
- **npm**: npm registry, 2026-10-05 and 2026-10-06.
- **Apple**: developer.apple.com.
- **Android**: developer.android.com.
- **(verify)**: secondary sources only.

### 5.1 React Native track

| Layer | Current instance | Notes |
|---|---|---|
| Framework | **Expo SDK 57** (expo 57.0.26; 57.0.0 published 2026-06-30), npm | SDK 58 has been on npm under the `next` tag since 2026-09-29, bundling RN 0.88.0-rc.3 and React 19.3.0. It may become stable before a January 2027 term (verify). Pin one SDK per term. |
| Runtime | React Native **0.86.3** (bundled by SDK 57). npm `latest` is 0.87.1; 0.88.0-rc.3 is in release candidate. npm | New Architecture is default since 0.76 (October 2024) and the only architecture since 0.82 (October 2025). Hermes V1 default since 0.84 (verify). |
| React | 19.2.3 (SDK 57), npm | |
| Language | TypeScript **~6.0.3** in the SDK 57 default template. TypeScript 7.0.2 (native compiler) has been npm `latest` since 2026-07-08. npm | Follow the template, not npm `latest`. |
| Navigation | expo-router 57.0.24 (versions now follow the SDK number); React Navigation 7.x stable (7.5.0). npm | React Navigation 8 still pre-release; Expo Router dropped its React Navigation dependency in SDK 56 (both verify). |
| State | Built-in hooks and Context; Zustand 5.0.15; TanStack Query 5.104.1. npm | |
| Storage | expo-sqlite 57.0.3; expo-secure-store 57.0.4; AsyncStorage **pinned at 2.2.0 by the SDK** while npm `latest` is 3.1.1. npm | Always install with `npx expo install`. |
| Device and system | expo-camera 57.0.6, expo-location 57.0.20, expo-sensors 57.0.3, expo-notifications 57.0.21, expo-background-task 57.0.21, expo-localization 57.0.2, expo-linking ~57.0.11, expo-sharing ~57.0.22. npm | |
| UI helpers | react-native-safe-area-context ~5.7.0, react-native-screens ~4.26.0, @expo/ui ~57.0.21 (SwiftUI and Compose primitives from JS; maturity verify). npm | |
| Testing | jest-expo 57.0.5; @testing-library/react-native 14.0.1 (npm). Maestro for end-to-end (version verify); React Native DevTools. | Check how the RNTL matchers are set up. |
| Release | eas-cli 24.11.0 (npm); EAS Build, Submit and Update; local builds with `npx expo run:android` and `npx expo run:ios`. | Free-tier limits (verify). |
| Android toolchain | Android Studio Rabbit 1 (2026.2.1), Android. Android 17 (API 37) stable since June 2026 (verify). | |
| iOS toolchain for RN | Xcode 27 (see 5.2). CocoaPods trunk read-only on 2026-12-02. RN 0.87 has experimental SwiftPM support (verify). | |
| Node | Node LTS as listed by the Expo SDK docs; RN 0.87 needs Node 22 or later (verify). | |

### 5.2 SwiftUI track

| Layer | Current instance | Notes |
|---|---|---|
| IDE | **Xcode 27** (27A266a), released 2026-09-14; 27.1 RC 2026-10-05; 27.2 beta 2. Apple | Needs macOS Tahoe 26.6 or later and Apple silicon. On-device debugging iOS 17+. Deployment targets iOS 15 to 27. |
| OS | iOS 27 (27.0.1 on 2026-09-28; 27.2 beta 3 on 2026-10-05). Apple | |
| Course deployment target | **iOS 18** | Runs on the same iPhones as iOS 17 and gives the `Tab` API. Every course API exists from iOS 17 or earlier, except `Tab`. |
| Language | Swift **6.4** (Xcode 27; language modes 6, 5, 4.2, 4). Apple | Swift 6.3 (March 2026) shipped an official Android SDK (verify). New Xcode projects default to MainActor isolation (verify). |
| UI | SwiftUI: `@Observable` (iOS 17), `NavigationStack` (iOS 16), `Tab` (iOS 18), `PhotosPicker` (iOS 16) | iOS 27 additions such as `@State` becoming a macro (verify). |
| Data | SwiftData (iOS 17), `@AppStorage`, `@SceneStorage`, Keychain | |
| Testing | Swift Testing (since Xcode 16), XCTest and XCUITest; `XCUIVoiceOverService` new in Xcode 27. Apple | |
| Scratchpad and previews | `#Preview`, `#Playground` (both in the Xcode 27 notes). Apple | |
| AI in the IDE | Xcode 27 coding agents, MCP tools, agent plug-ins with skills, Gemini in the assistant. Apple | Matters for the Code of Honor. |
| Release | App Store Connect and TestFlight. Since 2026-04-28, uploads must use Xcode 26 or later with the iOS 26 SDK. Since 2026-09-09, apps must target iOS 13 or later. Apple | Developer Program 99 USD a year. |
| Dependencies | Swift Package Manager. CocoaPods trunk read-only from 2026-12-02. | |

### 5.3 Platform and policy facts (both tracks)
- **Google Play**
  - Since 2026-08-31, new apps and updates must target API 36 (Android 16) (verify on Play Console Help).
  - New personal accounts created after 2023-11-13 must run a closed test with 12 testers for 14 days (verify).
  - App Bundles are required for new apps (since August 2021). Registration costs 25 USD once.
- **Android developer verification** (Android, official page)
  - August 2026: developer APIs, limited-distribution accounts and an "advanced flow" for power users.
  - 2026-09-30: installs from unverified developers are blocked on certified devices running Android 7 or later in Brazil, Indonesia, Singapore and Thailand.
  - 2027: global rollout.
- **Apple:** age-rating questionnaire due 2026-01-31 (official). EU alternative marketplaces since iOS 17.4.
- **Market share in Mexico:** Android is the large majority (verify the exact share on StatCounter). This matters for the SwiftUI track's reach discussion in S2.

### 5.4 Trends to watch this term
Each of these is an instance to run through the *ficha* in S16, not syllabus content.
- On-device AI models: Apple's Foundation Models framework since iOS 26; Gemini Nano on Android (verify).
- Coding agents inside IDEs (Xcode 27).
- Cross-platform approaches converging: Expo UI exposing SwiftUI and Compose from React Native (verify); Swift on Android (verify); Kotlin Multiplatform.
- New form factors: developer.android.com now lists XR headsets, XR glasses and AI glasses.
- Changes in how apps are distributed: the EU's Digital Markets Act, Android developer verification.

### 5.5 Re-check each term (instructor checklist)
1. Which Expo SDK npm tags as `latest`; whether Expo Go supports it; its bundled RN, React and TypeScript versions; its minimum iOS and Android versions.
2. Xcode system requirements (macOS, Apple silicon, on-device debugging minimum) and the current iOS release.
3. Apple's Upcoming Requirements page (SDK minimum, deployment minimum) and Play's target-API page.
4. Android developer verification status in Mexico.
5. Deprecations that touch slide code: Expo SDK changelog, React Native release blog, Xcode release notes, Swift changelog.
6. The CI in the labs repo is green against the annex versions; fix the decks before the term if it is red.
7. Pricing and free-tier limits: Apple Developer Program, Google Play, EAS.
8. Lab hardware inventory: Apple silicon Macs and their macOS version, test phones and their OS versions.
9. Refresh section 5.4 and the *ficha* reading list.

---

## 6. Open questions for the professor
1. What are the official course name, code and credits? I used "Desarrollo de Aplicaciones Móviles" and left the code as a placeholder.
2. What did "Complementos" mean: dependencies, app extensions, or both? Both are covered now.
3. How many Apple silicon Macs are in the lab, and on which macOS? Is there an Apple Developer Program or University Program membership for TestFlight and for the iOS half of the RN track?
4. Should the courses start on Expo SDK 58 if it is stable before the term begins, or stay on SDK 57?
5. Is the course JSON API to be published from this repository (for example with GitHub Pages)?