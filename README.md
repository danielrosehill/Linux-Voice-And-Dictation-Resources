# Linux Voice And Dictation Resources

![alt text](banner.png)

## A snapshot of the evolving STT ecosystem for Linux  

![Last Updated](https://img.shields.io/badge/Last%20Updated-November%2026%2C%202025-blue?style=flat-square)
![Repository Type](https://img.shields.io/badge/Type-Index-green?style=flat-square)
![Resources](https://img.shields.io/badge/Resources-100%2B-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

## Keywords

- Speech to text (STT) 
- Automatic speech recognition (ASR) 
- Linux note transcription 
- Linux voice control 
- Linux transcription 
- Linux dictation 

## The Boom In Linux STT/ASR (Whisper - Present) 

For a long time, voice support on Linux was very partial: the platform was mostly ignored by major dictation providers, owing to small desktop share, and voice assistant tools were hampered, in large part, by that fact - transcription being required for "assistants" which convert understood commands into shell commands/actions.

Since OpenAI open-sourced Whisper, there has been an explosion of tools. We now have a familiar Linux problem: lots of splintered projects!

I created this repo because - having been using voice for most typing for about a year now - I wanted to gather a list of projects to "check out" (over time). 

## Quick Navigation

[![STT Tools](https://img.shields.io/badge/🎤_STT_Tools-Real_Time_&_Async-blue?style=for-the-badge)](#speech-to-text---real-time)
[![Cloud STT](https://img.shields.io/badge/☁️_Cloud_STT-OpenAI_&_Deepgram-purple?style=for-the-badge)](#cloud-stt--api-based-tools)
[![Voice Assistants](https://img.shields.io/badge/🤖_Voice_Assistants-Linux_Compatible-green?style=for-the-badge)](#voice-assistants)
[![Projects by Stars](https://img.shields.io/badge/⭐_All_Projects-Sorted_by_Stars-gold?style=for-the-badge)](projects-by-stars.md)

## Inclusion Criteria

While text to spech functionalities are often integrated into voice applications, the focus here is on speech to text/transcription. TTS is another - and also vibrant! - tech ecosystem!

| Scope | Category | Description |
|-------|----------|-------------|
| ✅ In Scope | STT | Speech-to-text tools and applications |
| ✅ In Scope | Voice Assistants | Voice-controlled assistant applications |
| ✅ In Scope | Voice-to-X | Voice-to-MCP, voice-to-commands, and similar tools |
| ❌ Out of Scope | TTS | Text-to-speech synthesis tools |
| ❌ Out of Scope | TTS Applications | Voice cloning and other TTS applications |

 
### STT Deployment Patterns

Projects typically support either **local STT** or **cloud STT**, and less commonly both:

- **Local-only STT**: These implementations usually assume or install a local copy of Whisper or other models, offering complete privacy and offline functionality
- **Cloud-only STT**: Apps that rely exclusively on cloud inference, either supporting a single provider or offering multiple provider choices
- **Hybrid approaches**: Some projects enable users to choose between local or commercial/cloud-hosted STT

Among cloud STT integrations, **Whisper** (via OpenAI or other providers) remains the most common integration. However, a small but growing selection of projects are emerging that use **Deepgram** for cloud-based STT.

## Categorizing Whisper Implementations

Given the very long list of Whisper implementations, an attempt is made here to categorize them into groups. The most significant divisions are:

- **Wayland support**: Projects explicitly supporting Wayland virtual input (important for modern Linux desktop users)
- **Hardware focus**: CPU-centric vs. GPU-optimized implementations
- **Transcription mode**: Real-time (streaming) vs. asynchronous (batch/upload) focused

The first category of solutions in the STT landscape is "pure play" STT solutions. These may be CLIs, desktop GUIs, or web UIs. They may be synchronous tools which try to do STT on the fly (challenging!) or asynchronous (like: upload and transcribe apps). Or they may offer both. 

Many of the emerging and AI-centric voice technologies combine first pass STT with second pass LLM text optimisation. Whether this two-pass process happens entirely locally, entirely through cloud API calls, or either, these can be grouped together by the commonality that they all send a raw STT transcript through an LLM for rewording into a desired specific textual format (like an email) or simply to remove typos. I call these "STT and rewrite".

Finally, we have STT tools which firstly do STT and then translate the resulting natural language into some other format. These include STT-to-code, STT to MCP, STT to computer use agents (etc). I call these "STT and do stuff."

---

## Largest Projects (1000+ Stars)

The most popular repositories in this collection. For the complete list sorted by stars with live data, see **[Projects by Stars](projects-by-stars.md)**.

| Repository | Stars | Description | Language |
|------------|-------|-------------|----------|
| [**NVIDIA NeMo**](https://github.com/NVIDIA/NeMo) | ![Stars](https://img.shields.io/github/stars/NVIDIA/NeMo?style=flat-square) | Enterprise ASR toolkit with Conformer/Parakeet models | Python |
| [**SpeechBrain**](https://github.com/speechbrain/speechbrain) | ![Stars](https://img.shields.io/github/stars/speechbrain/speechbrain?style=flat-square) | PyTorch speech toolkit for ASR, speaker recognition | Python |
| [**Buzz**](https://github.com/chidiwilliams/buzz) | ![Stars](https://img.shields.io/github/stars/chidiwilliams/buzz?style=flat-square) | Offline transcription GUI. Flatpak/Snap available | Python |
| [**faster-whisper**](https://github.com/SYSTRAN/faster-whisper) | ![Stars](https://img.shields.io/github/stars/SYSTRAN/faster-whisper?style=flat-square) | 4x faster Whisper with CTranslate2 | Python |
| [**insanely-fast-whisper**](https://github.com/Vaibhavs10/insanely-fast-whisper) | ![Stars](https://img.shields.io/github/stars/Vaibhavs10/insanely-fast-whisper?style=flat-square) | Fastest Whisper CLI with batching | Python |
| [**Silero VAD**](https://github.com/snakers4/silero-vad) | ![Stars](https://img.shields.io/github/stars/snakers4/silero-vad?style=flat-square) | Enterprise-grade Voice Activity Detector | Python |
| [**FunASR**](https://github.com/modelscope/FunASR) | ![Stars](https://img.shields.io/github/stars/modelscope/FunASR?style=flat-square) | End-to-end speech recognition toolkit from Alibaba | Python |
| [**Vosk**](https://github.com/alphacep/vosk-api) | ![Stars](https://img.shields.io/github/stars/alphacep/vosk-api?style=flat-square) | Offline STT API, lightweight, 20+ languages | Python |
| [**RealtimeSTT**](https://github.com/KoljaB/RealtimeSTT) | ![Stars](https://img.shields.io/github/stars/KoljaB/RealtimeSTT?style=flat-square) | Low-latency STT with VAD and wake words | Python |
| [**WhisperLive**](https://github.com/collabora/WhisperLive) | ![Stars](https://img.shields.io/github/stars/collabora/WhisperLive?style=flat-square) | Real-time Whisper from Collabora | Python |
| [**NoiseTorch**](https://github.com/noisetorch/NoiseTorch) | ![Stars](https://img.shields.io/github/stars/noisetorch/NoiseTorch?style=flat-square) | Real-time microphone noise suppression on Linux | Go |
| [**easyeffects**](https://github.com/wwmm/easyeffects) | ![Stars](https://img.shields.io/github/stars/wwmm/easyeffects?style=flat-square) | Audio effects for PipeWire - noise reduction, equalization | C++ |

📊 **[View all 120+ projects sorted by stars →](projects-by-stars.md)**

---

## Getting Started

**New to Linux STT?** 

Check out [Getting Started Guide](starting-points.md) for step-by-step setup instructions, hardware recommendations, and model selection guidance.

## AI / Human Division Of Labor 

Me: raw notes, resource location, categorisation. 
Claude: updating readme, polishing language. 

## Inclusion Criteria

This repository focuses on modern ASR projects from the current AI-accelerated era, excluding pre-Whisper legacy STT tools. For detailed scope information, see our [Inclusion Criteria](inclusion-criteria.md) page.

---

## Foundations Of Transription: Models + Wrappers

The foundations of speech to text (in the modern era) are ASR models. 

Typically these are chained with other smaller models to:

- Add puncutation 
- Add voice activity detection (some tools) 
- Add speaker identification/diarisation (some tools) 

ASR is inherently a-lingual. However, models are fine-trained on datasets of language-specific models. Major world languages are widely available while others are works in progress.

Because Whisper is open source, you'll encounter more than one type of Whisper: 

- Whisper variants (Faster Whisper, Crisper Whisper, etc) 
- The original Whisper (as maintained by OpenAI) 
- Various wrappers that intend to bridge between local inference and other languages 

Some of what you'll find on a Github Whisper crawl is ready-to-use tooling (e.g. GUIs/CLIs that do the bundling). 

In other cases, it's components that you assemble yourself: model + component + frontend (or CLI) = useable solution. 

Hotkey support is also very common: I use a simple $5 USB button from Aliexpress (one of my greatest Ali buys!). But you can use a keyboard shortcut. Either way, after a few minutes of voice typing, the need is quickly apparent.

A few other notes:

### GPU Acceleration

For STT/voice typing, you'll find that GPU acceleration is often limited to NVIDIA/CUDA. Having an NVIDIA GPU makes life easier when running local models!

### Wayland Compatibility

Wayland presents challenges with virtual keyboards.

[ydotool](https://github.com/ReimuNotMoe/ydotool) (and its daemon) are commonly used to attempt to provide virtual keyboard suport while other implementations implement at the kernel level.

---

## STT Tools with Wayland Support

Projects with explicit Wayland support. These are particularly valuable for users on modern Linux desktops (GNOME, KDE Plasma on Wayland, Hyprland, Sway, niri, etc.) where X11 virtual input methods don't work. Note that Wayland compatibility can vary—some tools may require additional configuration or have limitations depending on your compositor.

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**hyprvoice**](https://github.com/LeonardoTrapani/hyprvoice) | ![Stars](https://img.shields.io/github/stars/LeonardoTrapani/hyprvoice?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/LeonardoTrapani/hyprvoice?style=flat-square) | Voice dictation for Hyprland |
| [**hyprwhspr**](https://github.com/goodroot/hyprwhspr) | ![Stars](https://img.shields.io/github/stars/goodroot/hyprwhspr?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/goodroot/hyprwhspr?style=flat-square) | Whisper-based voice input for Hyprland |
| [**freespeak**](https://github.com/Zetaphor/freespeak) | ![Stars](https://img.shields.io/github/stars/Zetaphor/freespeak?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Zetaphor/freespeak?style=flat-square) | Voice dictation with Wayland support |
| [**wayland-voice-dictation**](https://github.com/MasonRhodesDev/wayland-voice-dictation) | ![Stars](https://img.shields.io/github/stars/MasonRhodesDev/wayland-voice-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/MasonRhodesDev/wayland-voice-dictation?style=flat-square) | Voice dictation designed for Wayland |
| [**whisper-wayland**](https://github.com/Andrewske/whisper-wayland) | ![Stars](https://img.shields.io/github/stars/Andrewske/whisper-wayland?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Andrewske/whisper-wayland?style=flat-square) | Whisper integration for Wayland |
| [**niri-transcribe**](https://github.com/sevos/niri-transcribe) | ![Stars](https://img.shields.io/github/stars/sevos/niri-transcribe?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/sevos/niri-transcribe?style=flat-square) | Transcription tool for niri compositor |
| [**swictation**](https://github.com/robertelee78/swictation) | ![Stars](https://img.shields.io/github/stars/robertelee78/swictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/robertelee78/swictation?style=flat-square) | Voice dictation for Sway/Wayland |
| [**voice-typing-linux**](https://github.com/GitJuhb/voice-typing-linux) | ![Stars](https://img.shields.io/github/stars/GitJuhb/voice-typing-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/GitJuhb/voice-typing-linux?style=flat-square) | Voice typing for Linux with Wayland support |
| [**whispy**](https://github.com/daaku/whispy) | ![Stars](https://img.shields.io/github/stars/daaku/whispy?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/daaku/whispy?style=flat-square) | STT tool with Wayland support |
| [**dictation-tools**](https://github.com/gfreeau/dictation-tools) | ![Stars](https://img.shields.io/github/stars/gfreeau/dictation-tools?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/gfreeau/dictation-tools?style=flat-square) | Dictation tools with Wayland support |
| [**local-dictation-assistant**](https://github.com/Wiecek-K/local-dictation-assistant) | ![Stars](https://img.shields.io/github/stars/Wiecek-K/local-dictation-assistant?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Wiecek-K/local-dictation-assistant?style=flat-square) | Local dictation assistant with Wayland support |

---

### GUI or CLI

As always in Linux, you'll notice a bias towards CLIs and (more AI/ML than Linux) a heavy bias towards Python. But there are projects that take a ... human friendlier approach ... and try to make voice tech accessible. I will always go out of my way to highlight those as they align closely with my own philosophy!

---

# Projects 

## GUIs

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Buzz**](https://github.com/chidiwilliams/buzz) | ![Stars](https://img.shields.io/github/stars/chidiwilliams/buzz?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/chidiwilliams/buzz?style=flat-square) | Offline audio transcription and translation. Supports Whisper, Whisper.cpp, Faster-Whisper. Available via Flatpak/Snap. Vulkan GPU support |
| [**dsnote**](https://github.com/mkiol/dsnote) | ![Stars](https://img.shields.io/github/stars/mkiol/dsnote?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/mkiol/dsnote?style=flat-square) | Speech Note Linux app. Note taking, reading and translating with offline Speech to Text, Text to Speech and Machine translation. |
| [**whisply**](https://github.com/tsmdt/whisply) | ![Stars](https://img.shields.io/github/stars/tsmdt/whisply?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/tsmdt/whisply?style=flat-square) | A simple GUI for OpenAI Whisper |
| [**whisper-to-input-desktop**](https://github.com/Rosbifbr/whisper-to-input-desktop) | ![Stars](https://img.shields.io/github/stars/Rosbifbr/whisper-to-input-desktop?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Rosbifbr/whisper-to-input-desktop?style=flat-square) | A simple desktop application that uses OpenAI's Whisper to transcribe audio and input it as text |
| [**maVoice-Linux**](https://github.com/lliWcWill/maVoice-Linux) | ![Stars](https://img.shields.io/github/stars/lliWcWill/maVoice-Linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/lliWcWill/maVoice-Linux?style=flat-square) | Voice control for Linux |
| [**aTrain**](https://github.com/JuergenFleiss/aTrain) | ![Stars](https://img.shields.io/github/stars/JuergenFleiss/aTrain?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/JuergenFleiss/aTrain?style=flat-square) | Audio transcription training tool |
| [**wispr-lite**](https://github.com/dosment/wispr-lite) | ![Stars](https://img.shields.io/github/stars/dosment/wispr-lite?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/dosment/wispr-lite?style=flat-square) | Lightweight Whisper-based transcription tool |
| [**OpenWispr**](https://github.com/imsidharthj/OpenWispr) | ![Stars](https://img.shields.io/github/stars/imsidharthj/OpenWispr?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/imsidharthj/OpenWispr?style=flat-square) | Open source Whisper-based voice assistant |

### CLIs

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whispertux**](https://github.com/cjams/whispertux) | ![Stars](https://img.shields.io/github/stars/cjams/whispertux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/cjams/whispertux?style=flat-square) | A simple CLI wrapper for OpenAI's Whisper speech-to-text model |
| [**whispertrigger**](https://github.com/RetroTrigger/whispertrigger) | ![Stars](https://img.shields.io/github/stars/RetroTrigger/whispertrigger?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RetroTrigger/whispertrigger?style=flat-square) | A simple script to trigger OpenAI Whisper with a hotkey |
| [**BlahST**](https://github.com/QuantiusBenignus/BlahST) | ![Stars](https://img.shields.io/github/stars/QuantiusBenignus/BlahST?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/QuantiusBenignus/BlahST?style=flat-square) | Offline, real-time, streaming speech-to-text transcription using OpenAI Whisper |
| [**blurt**](https://github.com/QuantiusBenignus/blurt) | ![Stars](https://img.shields.io/github/stars/QuantiusBenignus/blurt?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/QuantiusBenignus/blurt?style=flat-square) | Whisper.cpp-based STT tool |
| [**whispy**](https://github.com/daaku/whispy) | ![Stars](https://img.shields.io/github/stars/daaku/whispy?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/daaku/whispy?style=flat-square) | STT tool with **Wayland support** 🎉 |
| [**dictation-tools**](https://github.com/gfreeau/dictation-tools) | ![Stars](https://img.shields.io/github/stars/gfreeau/dictation-tools?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/gfreeau/dictation-tools?style=flat-square) | Dictation tools with **Wayland support** 🎉 |
| [**niri-transcribe**](https://github.com/sevos/niri-transcribe) | ![Stars](https://img.shields.io/github/stars/sevos/niri-transcribe?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/sevos/niri-transcribe?style=flat-square) | Transcription tool with **Wayland support** 🎉 |
| [**local-dictation-assistant**](https://github.com/Wiecek-K/local-dictation-assistant) | ![Stars](https://img.shields.io/github/stars/Wiecek-K/local-dictation-assistant?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Wiecek-K/local-dictation-assistant?style=flat-square) | Local dictation assistant with **Wayland support** 🎉 |
| [**whisprd**](https://github.com/AgenticToaster/whisprd) | ![Stars](https://img.shields.io/github/stars/AgenticToaster/whisprd?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/AgenticToaster/whisprd?style=flat-square) | A daemon for OpenAI Whisper |
| [**froshine**](https://github.com/AdrianScott/froshine) | ![Stars](https://img.shields.io/github/stars/AdrianScott/froshine?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/AdrianScott/froshine?style=flat-square) | Voice recognition tool |
| [**whisper-hotkey-linux**](https://github.com/atkvishnu/whisper-hotkey-linux) | ![Stars](https://img.shields.io/github/stars/atkvishnu/whisper-hotkey-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/atkvishnu/whisper-hotkey-linux?style=flat-square) | Whisper hotkey for Linux |
| [**speech-assistant**](https://github.com/Mohamad-Hussein/speech-assistant) | ![Stars](https://img.shields.io/github/stars/Mohamad-Hussein/speech-assistant?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Mohamad-Hussein/speech-assistant?style=flat-square) | Faster Whisper-based speech assistant |
| [**linux-voice-to-text-ai**](https://github.com/trebormc/linux-voice-to-text-ai) | ![Stars](https://img.shields.io/github/stars/trebormc/linux-voice-to-text-ai?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/trebormc/linux-voice-to-text-ai?style=flat-square) | Linux voice to text AI |
| [**speak-to-ai**](https://github.com/AshBuk/speak-to-ai) | ![Stars](https://img.shields.io/github/stars/AshBuk/speak-to-ai?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/AshBuk/speak-to-ai?style=flat-square) | Speak to AI assistant |
| [**voxd**](https://github.com/jakovius/voxd) | ![Stars](https://img.shields.io/github/stars/jakovius/voxd?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/jakovius/voxd?style=flat-square) | Voice input daemon |
| [**whisp-away**](https://github.com/madjinn/whisp-away) | ![Stars](https://img.shields.io/github/stars/madjinn/whisp-away?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/madjinn/whisp-away?style=flat-square) | Whisper-based dictation tool |
| [**linux_dictation**](https://github.com/mysticaltech/linux_dictation) | ![Stars](https://img.shields.io/github/stars/mysticaltech/linux_dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/mysticaltech/linux_dictation?style=flat-square) | Linux dictation with voice control focus |
| [**pywhisper-dictation**](https://github.com/eddiedunn/pywhisper-dictation) | ![Stars](https://img.shields.io/github/stars/eddiedunn/pywhisper-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/eddiedunn/pywhisper-dictation?style=flat-square) | Python Whisper dictation tool |
| [**whisper-dictation**](https://github.com/NicolasHuberty/whisper-dictation) | ![Stars](https://img.shields.io/github/stars/NicolasHuberty/whisper-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/NicolasHuberty/whisper-dictation?style=flat-square) | Whisper dictation implementation |
| [**Whisper-Dictation**](https://github.com/LumenYoung/Whisper-Dictation) | ![Stars](https://img.shields.io/github/stars/LumenYoung/Whisper-Dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/LumenYoung/Whisper-Dictation?style=flat-square) | Whisper dictation tool |
| [**FasterWhisper**](https://github.com/CGAlei/FasterWhisper) | ![Stars](https://img.shields.io/github/stars/CGAlei/FasterWhisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/CGAlei/FasterWhisper?style=flat-square) | Faster Whisper for Arch Linux with CUDA support |
| [**keyless**](https://github.com/hate/keyless) | ![Stars](https://img.shields.io/github/stars/hate/keyless?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/hate/keyless?style=flat-square) | CUDA-enabled dictation tool |
| [**WhisperHelper**](https://github.com/nacmonad/WhisperHelper) | ![Stars](https://img.shields.io/github/stars/nacmonad/WhisperHelper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/nacmonad/WhisperHelper?style=flat-square) | A simple GUI for OpenAI Whisper |
| [**voice2chatgpt**](https://github.com/RemiFabre/voice2chatgpt) | ![Stars](https://img.shields.io/github/stars/RemiFabre/voice2chatgpt?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RemiFabre/voice2chatgpt?style=flat-square) | Voice to ChatGPT |
| [**nerd-dictation**](https://github.com/ideasman42/nerd-dictation) | ![Stars](https://img.shields.io/github/stars/ideasman42/nerd-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/ideasman42/nerd-dictation?style=flat-square) | Simple, hackable offline speech to text - using the VOSK-API. |
| [**multi-dictate**](https://github.com/makelinux/multi-dictate) | ![Stars](https://img.shields.io/github/stars/makelinux/multi-dictate?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/makelinux/multi-dictate?style=flat-square) | Multi-platform dictation tool |
| [**dictator**](https://github.com/chris17453/dictator) | ![Stars](https://img.shields.io/github/stars/chris17453/dictator?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/chris17453/dictator?style=flat-square) | Voice dictation tool for Linux |
| [**ptt-dictate**](https://github.com/arturo-jc/ptt-dictate) | ![Stars](https://img.shields.io/github/stars/arturo-jc/ptt-dictate?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/arturo-jc/ptt-dictate?style=flat-square) | Push-to-talk dictation tool |
| [**Dictation**](https://github.com/VanQWisher/Dictation) | ![Stars](https://img.shields.io/github/stars/VanQWisher/Dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/VanQWisher/Dictation?style=flat-square) | Dictation tool |
| [**whisper-dictation**](https://github.com/ananjiani/whisper-dictation) | ![Stars](https://img.shields.io/github/stars/ananjiani/whisper-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/ananjiani/whisper-dictation?style=flat-square) | Whisper-based dictation tool |
| [**dicti**](https://github.com/tksimson/dicti) | ![Stars](https://img.shields.io/github/stars/tksimson/dicti?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/tksimson/dicti?style=flat-square) | Dictation tool |
| [**VocalFLow**](https://github.com/R3DK3LL/VocalFLow) | ![Stars](https://img.shields.io/github/stars/R3DK3LL/VocalFLow?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/R3DK3LL/VocalFLow?style=flat-square) | Voice flow dictation tool |

### Additional Whisper Implementations

More Whisper-based tools for Linux:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Linux-Dictation-Project**](https://github.com/wheeler01/Linux-Dictation-Project) | ![Stars](https://img.shields.io/github/stars/wheeler01/Linux-Dictation-Project?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/wheeler01/Linux-Dictation-Project?style=flat-square) | Linux dictation project |
| [**LinuxWhisper**](https://github.com/vitali87/LinuxWhisper) | ![Stars](https://img.shields.io/github/stars/vitali87/LinuxWhisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/vitali87/LinuxWhisper?style=flat-square) | Whisper for Linux |
| [**WhisperNow**](https://github.com/shinglyu/WhisperNow) | ![Stars](https://img.shields.io/github/stars/shinglyu/WhisperNow?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/shinglyu/WhisperNow?style=flat-square) | Real-time Whisper transcription |
| [**whisper-ui**](https://github.com/schnoddelbotz/whisper-ui) | ![Stars](https://img.shields.io/github/stars/schnoddelbotz/whisper-ui?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/schnoddelbotz/whisper-ui?style=flat-square) | Whisper UI interface |
| [**whisperer**](https://github.com/mike-cr/whisperer) | ![Stars](https://img.shields.io/github/stars/mike-cr/whisperer?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/mike-cr/whisperer?style=flat-square) | Whisper-based tool |
| [**mint-whisper**](https://github.com/codankra/mint-whisper) | ![Stars](https://img.shields.io/github/stars/codankra/mint-whisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/codankra/mint-whisper?style=flat-square) | Whisper for Linux Mint |
| [**whisper-toggle**](https://github.com/bradjmsu/whisper-toggle) | ![Stars](https://img.shields.io/github/stars/bradjmsu/whisper-toggle?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/bradjmsu/whisper-toggle?style=flat-square) | Toggle-based Whisper control |
| [**whisper-transcribe**](https://github.com/geraschenko/whisper-transcribe) | ![Stars](https://img.shields.io/github/stars/geraschenko/whisper-transcribe?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/geraschenko/whisper-transcribe?style=flat-square) | Whisper transcription tool |
| [**handsfree**](https://github.com/achyudh/handsfree) | ![Stars](https://img.shields.io/github/stars/achyudh/handsfree?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/achyudh/handsfree?style=flat-square) | Hands-free computing |
| [**dictation-service**](https://github.com/sanastasiou/dictation-service) | ![Stars](https://img.shields.io/github/stars/sanastasiou/dictation-service?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/sanastasiou/dictation-service?style=flat-square) | Dictation service |
| [**transcribeAnywhere**](https://github.com/naren200/transcribeAnywhere) | ![Stars](https://img.shields.io/github/stars/naren200/transcribeAnywhere?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/naren200/transcribeAnywhere?style=flat-square) | Universal transcription tool |
| [**WhisperVoiceInput**](https://github.com/V0v1kkk/WhisperVoiceInput) | ![Stars](https://img.shields.io/github/stars/V0v1kkk/WhisperVoiceInput?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/V0v1kkk/WhisperVoiceInput?style=flat-square) | Whisper voice input tool |
| [**WhisperVoice**](https://github.com/SarwadnyaMahajan/WhisperVoice) | ![Stars](https://img.shields.io/github/stars/SarwadnyaMahajan/WhisperVoice?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/SarwadnyaMahajan/WhisperVoice?style=flat-square) | Whisper voice processing tool |
| [**whisper**](https://github.com/Nutlope/whisper) | ![Stars](https://img.shields.io/github/stars/Nutlope/whisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Nutlope/whisper?style=flat-square) | Whisper implementation |
| [**deepin-voice-note**](https://github.com/linuxdeepin/deepin-voice-note) | ![Stars](https://img.shields.io/github/stars/linuxdeepin/deepin-voice-note?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/linuxdeepin/deepin-voice-note?style=flat-square) | Deepin voice note application |
| [**TermlAi**](https://github.com/rohitkr150015/TermlAi) | ![Stars](https://img.shields.io/github/stars/rohitkr150015/TermlAi?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/rohitkr150015/TermlAi?style=flat-square) | Terminal AI assistant with voice |

### Voice Notes & AI-Enhanced Transcription

Apps focused on capturing voice notes with AI processing:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**notesGPT**](https://github.com/Nutlope/notesGPT) | ![Stars](https://img.shields.io/github/stars/Nutlope/notesGPT?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Nutlope/notesGPT?style=flat-square) | Voice notes with GPT processing |
| [**whisper-notes-pro**](https://github.com/mzazakeith/whisper-notes-pro) | ![Stars](https://img.shields.io/github/stars/mzazakeith/whisper-notes-pro?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/mzazakeith/whisper-notes-pro?style=flat-square) | Professional whisper notes application |
| [**ScribeWizard**](https://github.com/Bklieger/ScribeWizard) | ![Stars](https://img.shields.io/github/stars/Bklieger/ScribeWizard?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Bklieger/ScribeWizard?style=flat-square) | Transcription wizard tool |

### STT with Post-processing

Tools that leverage Whisper etc for STT but also add a layer for text cleanup after initial transcription:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Whisper-Notepad-For-Linux**](https://github.com/danielrosehill/Whisper-Notepad-For-Linux) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square) | Whisper notepad with post-processing |
| [**Thought-Pad**](https://github.com/danielrosehill/Thought-Pad) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Thought-Pad?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Thought-Pad?style=flat-square) | Thought capture with STT |
| [**obsidian-scribe**](https://github.com/Mikodin/obsidian-scribe) | ![Stars](https://img.shields.io/github/stars/Mikodin/obsidian-scribe?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Mikodin/obsidian-scribe?style=flat-square) | Obsidian voice note transcription |
| [**whisper-notes**](https://github.com/AsyncFuncAI/whisper-notes) | ![Stars](https://img.shields.io/github/stars/AsyncFuncAI/whisper-notes?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/AsyncFuncAI/whisper-notes?style=flat-square) | Whisper-powered note processing |

### Proof of Concepts

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisperai**](https://github.com/jorgecastro05/whisperai) | ![Stars](https://img.shields.io/github/stars/jorgecastro05/whisperai?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/jorgecastro05/whisperai?style=flat-square) | Whisper AI proof of concept |
| [**stt-linux**](https://github.com/samcole8/stt-linux) | ![Stars](https://img.shields.io/github/stars/samcole8/stt-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/samcole8/stt-linux?style=flat-square) | STT Linux proof of concept |

### General STT Tools

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**linux-stt-input**](https://github.com/fengwk/linux-stt-input) | ![Stars](https://img.shields.io/github/stars/fengwk/linux-stt-input?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/fengwk/linux-stt-input?style=flat-square) | Linux STT input method |
| [**sonori**](https://github.com/0xPD33/sonori) | ![Stars](https://img.shields.io/github/stars/0xPD33/sonori?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/0xPD33/sonori?style=flat-square) | Voice recognition tool |
| [**stt-linux**](https://github.com/afif-malghani/stt-linux) | ![Stars](https://img.shields.io/github/stars/afif-malghani/stt-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/afif-malghani/stt-linux?style=flat-square) | STT for Linux |
| [**super-stt**](https://github.com/jorge-menjivar/super-stt) | ![Stars](https://img.shields.io/github/stars/jorge-menjivar/super-stt?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/jorge-menjivar/super-stt?style=flat-square) | Enhanced STT tool |
| [**wvcr**](https://github.com/bakeryproducts/wvcr) | ![Stars](https://img.shields.io/github/stars/bakeryproducts/wvcr?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/bakeryproducts/wvcr?style=flat-square) | Wave voice control recorder |
| [**STT-Assistant-linux**](https://github.com/4lext/STT-Assistant-linux) | ![Stars](https://img.shields.io/github/stars/4lext/STT-Assistant-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/4lext/STT-Assistant-linux?style=flat-square) | STT assistant for Linux |
| [**voicekeyboard**](https://github.com/sam1am/voicekeyboard) | ![Stars](https://img.shields.io/github/stars/sam1am/voicekeyboard?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/sam1am/voicekeyboard?style=flat-square) | Voice keyboard implementation |

## Vendor Projects

### Deepgram

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**fortuna**](https://github.com/deepgram-devs/fortuna) | ![Stars](https://img.shields.io/github/stars/deepgram-devs/fortuna?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/deepgram-devs/fortuna?style=flat-square) | Deepgram Fortuna project |
| [**voice-keyboard-linux**](https://github.com/deepgram/voice-keyboard-linux) | ![Stars](https://img.shields.io/github/stars/deepgram/voice-keyboard-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/deepgram/voice-keyboard-linux?style=flat-square) | Deepgram voice keyboard |
| [**Deepgram-Voice-Keyboard-Ubuntu**](https://github.com/danielrosehill/Deepgram-Voice-Keyboard-Ubuntu) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Deepgram-Voice-Keyboard-Ubuntu?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Deepgram-Voice-Keyboard-Ubuntu?style=flat-square) | STT project using Deepgram API for Ubuntu |

---

## Self Hosted

Docker-deployed tools and web interfaces that can be deployed locally or on a server for self-hosted STT solutions.

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Whisper-WebUI**](https://github.com/jhj0517/Whisper-WebUI) | ![Stars](https://img.shields.io/github/stars/jhj0517/Whisper-WebUI?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/jhj0517/Whisper-WebUI?style=flat-square) | A Gradio-based browser interface for Whisper. You can use it as an Easy Subtitle Generator! |
| [**Scriberr**](https://github.com/rishikanthc/Scriberr) | ![Stars](https://img.shields.io/github/stars/rishikanthc/Scriberr?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/rishikanthc/Scriberr?style=flat-square) | Voice transcription tool |

---

## Speech-to-Text - Real-Time Streaming

Libraries and tools for real-time, streaming speech-to-text transcription. These are designed for live dictation, meeting transcription, and low-latency applications.

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**RealtimeSTT**](https://github.com/KoljaB/RealtimeSTT) | ![Stars](https://img.shields.io/github/stars/KoljaB/RealtimeSTT?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/KoljaB/RealtimeSTT?style=flat-square) | Low-latency STT library with VAD, wake word activation. Uses WebRTCVAD + SileroVAD + Faster-Whisper |
| [**WhisperLive**](https://github.com/collabora/WhisperLive) | ![Stars](https://img.shields.io/github/stars/collabora/WhisperLive?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/collabora/WhisperLive?style=flat-square) | Real-time Whisper transcription from Collabora. OpenVINO support, browser extensions, iOS client |
| [**WhisperLiveKit**](https://github.com/QuentinFuxa/WhisperLiveKit) | ![Stars](https://img.shields.io/github/stars/QuentinFuxa/WhisperLiveKit?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/QuentinFuxa/WhisperLiveKit?style=flat-square) | 2025 SOTA streaming STT with speaker diarization. Simul-Whisper for ultra-low latency |
| [**whisper_streaming**](https://github.com/ufal/whisper_streaming) | ![Stars](https://img.shields.io/github/stars/ufal/whisper_streaming?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/ufal/whisper_streaming?style=flat-square) | Real-time streaming Whisper with self-adaptive latency using local agreement policy |
| [**whisper_real_time**](https://github.com/davabase/whisper_real_time) | ![Stars](https://img.shields.io/github/stars/davabase/whisper_real_time?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/davabase/whisper_real_time?style=flat-square) | Real-time transcription with OpenAI Whisper |

---

## Speech-to-Text - Asynchronous

Web UIs for Whisper etc for transcribing prerecorded audio and meeting processing.

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**meeting-minutes**](https://github.com/Zackriya-Solutions/meeting-minutes) | ![Stars](https://img.shields.io/github/stars/Zackriya-Solutions/meeting-minutes?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Zackriya-Solutions/meeting-minutes?style=flat-square) | Self-hostable meeting transcription and minutes generation |


---

## Developer Tools

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisper.cpp-cli**](https://github.com/charliermarsh/whisper.cpp-cli) | ![Stars](https://img.shields.io/github/stars/charliermarsh/whisper.cpp-cli?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/charliermarsh/whisper.cpp-cli?style=flat-square) | Whisper.cpp CLI wrapper |
| [**mt_stt**](https://github.com/RhinoDevel/mt_stt) | ![Stars](https://img.shields.io/github/stars/RhinoDevel/mt_stt?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RhinoDevel/mt_stt?style=flat-square) | C wrapper for speech-to-text |

---

## Subtitle Generation

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisper-subs**](https://github.com/GhostNaN/whisper-subs) | ![Stars](https://img.shields.io/github/stars/GhostNaN/whisper-subs?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/GhostNaN/whisper-subs?style=flat-square) | Whisper subtitle generation |
| [**auto-subs**](https://github.com/tmoroney/auto-subs) | ![Stars](https://img.shields.io/github/stars/tmoroney/auto-subs?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/tmoroney/auto-subs?style=flat-square) | Automatic subtitle generation |

---

## WhatsApp Voice Processing

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whatsapp_voice_transcription**](https://github.com/nerveband/whatsapp_voice_transcription) | ![Stars](https://img.shields.io/github/stars/nerveband/whatsapp_voice_transcription?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/nerveband/whatsapp_voice_transcription?style=flat-square) | WhatsApp voice message transcription |

---

## API Services

Local API servers and services for STT:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisper-fastapi**](https://github.com/heimoshuiyu/whisper-fastapi) | ![Stars](https://img.shields.io/github/stars/heimoshuiyu/whisper-fastapi?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/heimoshuiyu/whisper-fastapi?style=flat-square) | Whisper FastAPI service |

---

## Cloud STT / API-Based Tools

Projects that use cloud STT APIs for transcription. These may support only cloud inference, or offer it alongside local options. Cloud APIs often provide faster processing and don't require local GPU resources.

### OpenAI Whisper API

Tools that support the OpenAI Whisper API (or compatible endpoints like Azure, Groq, etc.):

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisper-fastapi**](https://github.com/heimoshuiyu/whisper-fastapi) | ![Stars](https://img.shields.io/github/stars/heimoshuiyu/whisper-fastapi?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/heimoshuiyu/whisper-fastapi?style=flat-square) | FastAPI server with OpenAI Whisper API compatibility |
| [**Whisper-Notepad-For-Linux**](https://github.com/danielrosehill/Whisper-Notepad-For-Linux) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square) | Whisper notepad with OpenAI API support and post-processing |
| [**Whisper-Notepad-Simple**](https://github.com/danielrosehill/Whisper-Notepad-Simple) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Whisper-Notepad-Simple?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Whisper-Notepad-Simple?style=flat-square) | Simplified Whisper notepad using OpenAI API |
| [**speech2keys**](https://github.com/vanviegen/speech2keys) | ![Stars](https://img.shields.io/github/stars/vanviegen/speech2keys?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/vanviegen/speech2keys?style=flat-square) | Speech to keystrokes using OpenAI Whisper API |
| [**whisply**](https://github.com/tsmdt/whisply) | ![Stars](https://img.shields.io/github/stars/tsmdt/whisply?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/tsmdt/whisply?style=flat-square) | GUI for OpenAI Whisper with API support |
| [**whisper-to-input-desktop**](https://github.com/Rosbifbr/whisper-to-input-desktop) | ![Stars](https://img.shields.io/github/stars/Rosbifbr/whisper-to-input-desktop?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Rosbifbr/whisper-to-input-desktop?style=flat-square) | Desktop app using OpenAI's Whisper to transcribe and input text |

### Deepgram API

Tools that support the Deepgram STT API:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**fortuna**](https://github.com/deepgram-devs/fortuna) | ![Stars](https://img.shields.io/github/stars/deepgram-devs/fortuna?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/deepgram-devs/fortuna?style=flat-square) | Deepgram Fortuna project |
| [**voice-keyboard-linux**](https://github.com/deepgram/voice-keyboard-linux) | ![Stars](https://img.shields.io/github/stars/deepgram/voice-keyboard-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/deepgram/voice-keyboard-linux?style=flat-square) | Deepgram voice keyboard for Linux |
| [**Deepgram-Voice-Keyboard-Ubuntu**](https://github.com/danielrosehill/Deepgram-Voice-Keyboard-Ubuntu) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Deepgram-Voice-Keyboard-Ubuntu?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Deepgram-Voice-Keyboard-Ubuntu?style=flat-square) | STT project using Deepgram API for Ubuntu |

---

# Models

STT models

### Hugging Face ASR Models

Browse and discover ASR models on Hugging Face:

| Resource | Description |
|----------|-------------|
| [ASR Models (Trending)](https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&sort=trending) | Trending automatic speech recognition models on Hugging Face |

## Open AI Whisper

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Whisper on Hugging Face**](https://huggingface.co/spaces/openai/whisper) | N/A | N/A | OpenAI Whisper on Hugging Face |

To add: 

- Model training 
- STT finetuning (utilities, frameworks, scripts) 


---

# Voice Assistants

## Privacy-Focused Voice Assistants

Open source voice assistants emphasizing local processing and privacy:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**OpenVoiceOS**](https://github.com/OpenVoiceOS/ovos-core) | ![Stars](https://img.shields.io/github/stars/OpenVoiceOS/ovos-core?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/OpenVoiceOS/ovos-core?style=flat-square) | Community-driven voice assistant framework. Local processing, privacy-focused. Continuation of Mycroft |
| [**Neon AI**](https://github.com/NeonGeckoCom/NeonCore) | ![Stars](https://img.shields.io/github/stars/NeonGeckoCom/NeonCore?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/NeonGeckoCom/NeonCore?style=flat-square) | Privacy-first voice assistant. Offline-capable, customizable. Maintains Mycroft community forums |
| [**Project Alice**](https://github.com/project-alice-assistant/ProjectAlice) | ![Stars](https://img.shields.io/github/stars/project-alice-assistant/ProjectAlice?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/project-alice-assistant/ProjectAlice?style=flat-square) | Modular smart assistant, fully offline. Built around Snips, guarantees privacy |
| [**SEPIA Framework**](https://github.com/SEPIA-Framework/sepia-assist-server) | ![Stars](https://img.shields.io/github/stars/SEPIA-Framework/sepia-assist-server?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/SEPIA-Framework/sepia-assist-server?style=flat-square) | Self-hosted, privacy-compliant voice assistant ecosystem. Extendable and server-based |

## General

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**linux-voice-control**](https://github.com/omegaui/linux-voice-control) | ![Stars](https://img.shields.io/github/stars/omegaui/linux-voice-control?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/omegaui/linux-voice-control?style=flat-square) | Linux voice control system |
| [**LinuxVoiceAssistant**](https://github.com/aydinnyunus/LinuxVoiceAssistant) | ![Stars](https://img.shields.io/github/stars/aydinnyunus/LinuxVoiceAssistant?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/aydinnyunus/LinuxVoiceAssistant?style=flat-square) | Linux voice assistant |
| [**Personal-Voice-Assistent**](https://github.com/Cyborgscode/Personal-Voice-Assistent) | ![Stars](https://img.shields.io/github/stars/Cyborgscode/Personal-Voice-Assistent?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Cyborgscode/Personal-Voice-Assistent?style=flat-square) | Personal voice assistant |
| [**tempest**](https://github.com/lavafroth/tempest) | ![Stars](https://img.shields.io/github/stars/lavafroth/tempest?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/lavafroth/tempest?style=flat-square) | Voice assistant framework |
| [**jarvis_linux**](https://github.com/morrolinux/jarvis_linux) | ![Stars](https://img.shields.io/github/stars/morrolinux/jarvis_linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/morrolinux/jarvis_linux?style=flat-square) | Jarvis for Linux |
| [**vosk-cli-dictation**](https://github.com/RonanDavalan/vosk-cli-dictation) | ![Stars](https://img.shields.io/github/stars/RonanDavalan/vosk-cli-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RonanDavalan/vosk-cli-dictation?style=flat-square) | Vosk CLI dictation |
| [**Local-Voice**](https://github.com/shashank2122/Local-Voice) | ![Stars](https://img.shields.io/github/stars/shashank2122/Local-Voice?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/shashank2122/Local-Voice?style=flat-square) | Local voice assistant |


## More Specific

These projects leverage voice but for more specific capabilities than general dictation.

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**home-assistant-assist-desktop**](https://github.com/timmo001/home-assistant-assist-desktop) | ![Stars](https://img.shields.io/github/stars/timmo001/home-assistant-assist-desktop?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/timmo001/home-assistant-assist-desktop?style=flat-square) | Home Assistant desktop client |
| [**voice2json**](https://github.com/synesthesiam/voice2json) | ![Stars](https://img.shields.io/github/stars/synesthesiam/voice2json?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/synesthesiam/voice2json?style=flat-square) | Voice to JSON converter |
| [**Handy**](https://github.com/cjpais/Handy) | ![Stars](https://img.shields.io/github/stars/cjpais/Handy?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/cjpais/Handy?style=flat-square) | Voice-controlled computer interface - [handy.computer](https://handy.computer/) |
| [**numen**](https://sr.ht/~geb/numen/) | N/A | N/A | Voice-controlled interface (hosted on SourceHut) |

## Voice Operating Systems

Full voice-enabled operating systems and distributions:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**ovos-buildroot**](https://github.com/OpenVoiceOS/ovos-buildroot) | ![Stars](https://img.shields.io/github/stars/OpenVoiceOS/ovos-buildroot?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/OpenVoiceOS/ovos-buildroot?style=flat-square) | OpenVoiceOS - A minimalistic Linux OS bringing the open source voice assistant to IoT and embedded devices |

## Service-Specific Voice Tools

Voice tools designed for specific platforms and services:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**overlayed**](https://github.com/overlayeddev/overlayed) | ![Stars](https://img.shields.io/github/stars/overlayeddev/overlayed?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/overlayeddev/overlayed?style=flat-square) | Voice overlay for Discord on Linux |

## Voice Biometrics

Tools for voice authentication and identification:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**voiceprint**](https://github.com/Raymo111/voiceprint) | ![Stars](https://img.shields.io/github/stars/Raymo111/voiceprint?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Raymo111/voiceprint?style=flat-square) | Voice biometric authentication for Linux |

---

## Complementary Tools

These tools aren't STT/dictation tools themselves, but they help make the most out of voice typing and recording:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**easyeffects**](https://github.com/wwmm/easyeffects) | ![Stars](https://img.shields.io/github/stars/wwmm/easyeffects?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/wwmm/easyeffects?style=flat-square) | Audio effects for PipeWire applications - noise reduction, equalization, and more |
| [**NoiseTorch**](https://github.com/noisetorch/NoiseTorch) | ![Stars](https://img.shields.io/github/stars/noisetorch/NoiseTorch?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/noisetorch/NoiseTorch?style=flat-square) | Real-time microphone noise suppression on Linux |

### Voice Activity Detection (VAD) & Diarisation

These technologies complement voice systems by detecting when speech is happening (VAD) and identifying different speakers (diarisation):

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Silero VAD**](https://github.com/snakers4/silero-vad) | ![Stars](https://img.shields.io/github/stars/snakers4/silero-vad?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/snakers4/silero-vad?style=flat-square) | Enterprise-grade Voice Activity Detector. MIT license, <1ms per chunk on CPU, supports 6000+ languages |
| [**pyannote-audio**](https://github.com/pyannote/pyannote-audio) | ![Stars](https://img.shields.io/github/stars/pyannote/pyannote-audio?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/pyannote/pyannote-audio?style=flat-square) | Neural building blocks for speaker diarization: speech activity detection, speaker embedding, clustering |
| [**WebRTC VAD**](https://github.com/wiseman/py-webrtcvad) | ![Stars](https://img.shields.io/github/stars/wiseman/py-webrtcvad?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/wiseman/py-webrtcvad?style=flat-square) | Python interface to WebRTC Voice Activity Detector. Lightweight, widely used |
| [**wyoming-openwakeword**](https://github.com/rhasspy/wyoming-openwakeword) | ![Stars](https://img.shields.io/github/stars/rhasspy/wyoming-openwakeword?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/rhasspy/wyoming-openwakeword?style=flat-square) | Wyoming server for openWakeWord. Custom wake word detection for Home Assistant |

---

## Toolkits & Frameworks

ASR/STT toolkits and frameworks for building voice applications. These are development libraries rather than end-user applications:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**FunASR**](https://github.com/modelscope/FunASR) | ![Stars](https://img.shields.io/github/stars/modelscope/FunASR?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/modelscope/FunASR?style=flat-square) | End-to-end speech recognition toolkit from Alibaba. Industrial-grade models |
| [**NVIDIA NeMo**](https://github.com/NVIDIA/NeMo) | ![Stars](https://img.shields.io/github/stars/NVIDIA/NeMo?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/NVIDIA/NeMo?style=flat-square) | Enterprise ASR toolkit with Conformer/Parakeet models. GPU-accelerated training and inference |
| [**SpeechBrain**](https://github.com/speechbrain/speechbrain) | ![Stars](https://img.shields.io/github/stars/speechbrain/speechbrain?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/speechbrain/speechbrain?style=flat-square) | PyTorch-based speech toolkit for ASR, speaker recognition, speech enhancement |
| [**Vosk**](https://github.com/alphacep/vosk-api) | ![Stars](https://img.shields.io/github/stars/alphacep/vosk-api?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/alphacep/vosk-api?style=flat-square) | Offline speech recognition API. Lightweight, 20+ languages, works on Raspberry Pi |
| [**Coqui STT**](https://github.com/coqui-ai/STT) | ![Stars](https://img.shields.io/github/stars/coqui-ai/STT?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/coqui-ai/STT?style=flat-square) | Deep learning STT toolkit (continuation of Mozilla DeepSpeech). Custom model training |
| [**fairseq**](https://github.com/facebookresearch/fairseq) | ![Stars](https://img.shields.io/github/stars/facebookresearch/fairseq?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/facebookresearch/fairseq?style=flat-square) | Meta's sequence modeling toolkit. Includes Wav2Vec 2.0 for self-supervised ASR |

### Whisper Variants & Optimizations

Optimized implementations and variants of OpenAI's Whisper model:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**faster-whisper**](https://github.com/SYSTRAN/faster-whisper) | ![Stars](https://img.shields.io/github/stars/SYSTRAN/faster-whisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/SYSTRAN/faster-whisper?style=flat-square) | CTranslate2 reimplementation. 4x faster, less memory, 8-bit quantization support |
| [**whisper.cpp**](https://github.com/ggerganov/whisper.cpp) | ![Stars](https://img.shields.io/github/stars/ggerganov/whisper.cpp?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/ggerganov/whisper.cpp?style=flat-square) | C/C++ port of Whisper. CPU inference, minimal dependencies, runs on edge devices |
| [**insanely-fast-whisper**](https://github.com/Vaibhavs10/insanely-fast-whisper) | ![Stars](https://img.shields.io/github/stars/Vaibhavs10/insanely-fast-whisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Vaibhavs10/insanely-fast-whisper?style=flat-square) | CLI for fastest Whisper inference. Batching, flash attention, distil-whisper support |
| [**distil-whisper**](https://github.com/huggingface/distil-whisper) | ![Stars](https://img.shields.io/github/stars/huggingface/distil-whisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/huggingface/distil-whisper?style=flat-square) | HuggingFace's distilled Whisper. 6x faster, 49% smaller, within 1% WER |
| [**whisper-plus**](https://github.com/kadirnar/whisper-plus) | ![Stars](https://img.shields.io/github/stars/kadirnar/whisper-plus?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/kadirnar/whisper-plus?style=flat-square) | Advanced Whisper pipelines with diarization, translation, and video transcription support |
| [**wyoming-faster-whisper**](https://github.com/rhasspy/wyoming-faster-whisper) | ![Stars](https://img.shields.io/github/stars/rhasspy/wyoming-faster-whisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/rhasspy/wyoming-faster-whisper?style=flat-square) | Wyoming protocol server for faster-whisper. Home Assistant integration |
| [**wyoming-whisper-api-client**](https://github.com/ser/wyoming-whisper-api-client) | ![Stars](https://img.shields.io/github/stars/ser/wyoming-whisper-api-client?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/ser/wyoming-whisper-api-client?style=flat-square) | Wyoming protocol client for Whisper APIs. Centralizes STT for Home Assistant |

---

## Community Resources

### GitHub Topics

GitHub topics worth following to discover new STT and voice projects:

| Topic | Description |
|-------|-------------|
| [speech-to-text](https://github.com/topics/speech-to-text) | General speech-to-text projects |
| [asr](https://github.com/topics/asr) | Automatic speech recognition |
| [dictation](https://github.com/topics/dictation) | Dictation tools and applications |
| [voice-dictation](https://github.com/topics/voice-dictation) | Voice dictation specific projects |
| [transcription](https://github.com/topics/transcription) | Audio/video transcription tools |
| [voice](https://github.com/topics/voice) | General voice technology projects |
| [voice-assistant](https://github.com/topics/voice-assistant) | Voice assistant applications |
| [voice-recognition](https://github.com/topics/voice-recognition) | Voice recognition systems |
| [voice-commands](https://github.com/topics/voice-commands) | Voice command implementations |
| [voice-control](https://github.com/topics/voice-control) | Voice control tools |

### Subreddits

Relevant Reddit communities for STT, voice technology, and related topics:

| Subreddit | Focus |
|-----------|-------|
| [r/VoiceTech](https://www.reddit.com/r/VoiceTech/) | Voice technology and applications |
| [r/speechrecognition](https://www.reddit.com/r/speechrecognition/) | Speech recognition systems and discussion |
| [r/TextToSpeech](https://www.reddit.com/r/TextToSpeech/) | TTS technology (complementary to STT) |
| [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) | Local LLMs (frequently covers voice topics) |
| [r/accessibility](https://www.reddit.com/r/accessibility/) | Accessibility tools including voice control |
| [r/opensource](https://www.reddit.com/r/opensource/) | Open source projects including voice tools |

---

 