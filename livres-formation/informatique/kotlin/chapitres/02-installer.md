# Installer Kotlin

## Ce qu'il te faut

- **IntelliJ IDEA** (Community gratuit) ou Android Studio pour le mobile.
- Le compilateur Kotlin est inclus dans IntelliJ.

## Installation rapide

1. Telecharge IntelliJ IDEA sur jetbrains.com/idea.
2. Installe le plugin Kotlin (pre-installe dans les versions recentes).
3. File > New > Project > Kotlin > JVM.

Verification :

```bash
kotlinc -version
```

## Gradle (projets Android / backend)

La plupart des projets Kotlin utilisent Gradle :

```kotlin
// build.gradle.kts
plugins {
    kotlin("jvm") version "2.0.0"
}
```

> **Astuce DanielCraft** - IntelliJ + Kotlin = auto-completion, refactoring et erreurs en temps reel. C'est l'environnement ideal.

## Petite histoire

Max installe IntelliJ, cree un projet Kotlin JVM, tape `fun main()` et lance. Le programme s'execute en un clic.

## A retenir

- IntelliJ IDEA = IDE de reference.
- Android Studio pour le mobile.
- Gradle pour les projets professionnels.
