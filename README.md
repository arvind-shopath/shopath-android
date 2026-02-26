# 📱 Shopath Android App

**वही दुकान, सही सामान**

Shopath का official Android WebView App — [shopath.in](https://shopath.in) को Android पर उपलब्ध कराता है।

---

## ✨ Features

- 🌐 **WebView** — shopath.in पूरी तरह से load होता है
- 🔄 **Pull to Refresh** — नीचे खींचकर page refresh
- ⬅️ **Back Navigation** — Android back button से browser history में navigate
- 📶 **No Internet Screen** — हिंदी में error message और retry button  
- ⚡ **Splash Screen** — App logo के साथ beautiful opening screen
- 📁 **File Upload** — photo/file upload support
- 🔒 **Secure** — HTTPS only, secure connection

---

## 🚀 APK Download (Latest Build)

GitHub Actions tab में जाएं → Latest workflow run → Artifacts section  
**Shopath-Debug-APK** download करें और install करें।

---

## 🏗️ Automatic Build (GitHub Actions)

हर बार जब `main` branch पर code push होता है, GitHub automatically APK बनाता है।

### Build Status
![Build APK](https://github.com/arvind-shopath/shopath-android/actions/workflows/build-apk.yml/badge.svg)

---

## 📋 Project Structure

```
shopath-android/
├── .github/workflows/    # GitHub Actions (automatic build)
├── app/
│   └── src/main/
│       ├── java/in/shopath/app/
│       │   ├── SplashActivity.kt    # Opening screen
│       │   └── MainActivity.kt     # WebView with all features
│       ├── res/
│       │   ├── layout/             # Screen layouts
│       │   ├── drawable/           # Icons & graphics
│       │   └── values/             # Colors, strings, themes
│       └── AndroidManifest.xml
├── build.gradle
└── settings.gradle
```

---

## 📱 App Details

| Property | Value |
|----------|-------|
| Package Name | `in.shopath.app` |
| Min Android | 5.0 (API 21) |
| Target Android | 14 (API 34) |
| Version | 1.0.0 |
| Website | https://shopath.in |

---

## 🔑 Play Store के लिए (Future)

Play Store पर publish करने के लिए:
1. Signing keystore बनाना होगा
2. GitHub Secrets में add करना होगा
3. Release APK build होगी

---

Made with ❤️ for Shopath
