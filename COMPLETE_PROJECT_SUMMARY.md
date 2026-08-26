# HRL International Private Limited — Comprehensive Project Status & Architecture
**Company**: HRL International Pvt. Ltd. (Corporate Entity)  
**Founder & Managing Director**: Pavan Kumar Sadashiv (B.E. AI, SCEM, Mangaluru, Karnataka, India)  
**Public GitHub Repository**: [https://github.com/hrlpavan/hrl-international-website-](https://github.com/hrlpavan/hrl-international-website-)  
**Live Production Website**: [https://hrlpavan.github.io/hrl-international-website-/](https://hrlpavan.github.io/hrl-international-website-/) | [https://hrl-brand-seo.vercel.app/](https://hrl-brand-seo.vercel.app/)  
**Last Updated**: August 27, 2026

---

##  Key Accomplishments & Deliverables

### 1.  Mobile-Proof Voice AI & Audio Unlocking Engine
* **iOS WebKit Garbage Collection Fix**: Fixed the Mobile Safari bug where speech synthesis was abruptly terminated after 3–5 seconds by maintaining a persistent global memory reference (`window.activeSpeechUtterance`).
* **Synchronous Touch Activation**: Unlocks browser audio context directly on the user touch event to comply with iOS and Android autoplay security policies.
* **Keepalive Pulse**: Automated background keepalive mechanism preventing mobile OS sleep cycles from pausing narration mid-sentence.
* **Pre-warmed Voice Pool**: Pre-loads browser speech voices on page initialization for instant 0ms latency playback.

### 2.  Single-Line Mobile Preset Bar (`[ Story ] [ Overview ] [ VFX ] [ Tech ]`)
* **Symmetrical 4-Column Bar**: Refactored the preset selector into a single, clean Apple-style segmented control (`grid-template-columns: repeat(4, 1fr)`) with zero multi-line wrapping on mobile screens.
* **Crisp Executive Labels**:
  1. **`Story`**: 45s corporate narrative & verified network handles.
  2. **`Overview`**: Corporate entity background & focus.
  3. **`VFX`**: Hollywood splatter movie promotions & DaVinci Resolve color science.
  4. **`Tech`**: JPMorgan Chase & Deloitte software architecture.

### 3.  `@hrlflix` Specialization in Hollywood Splatter Movie Promotions
* Integrated `@hrlflix` as the official channel for **Hollywood splatter movie promotions**, cinematic trailer grading, and viral movie previews across:
  * Voice AI 45s story script (`voiceScripts[0]` and `voiceScripts[2]`).
  * JSON-LD Schema `Organization` / `Corporation` metadata.
  * Verified Socials HUD and Ecosystem Bento cards.

### 4.  SCEM "Eureka! Pitching 2026" (E-Cell Sahyadri × IIT Bombay) Submission
* **Complete Form Answers**: Tailored all 5 competition fields with exact word limits (<150 words).
* **Disruptive Problem/Solution**: Highlights the democratization of post-production software plugins for **Blackmagic DaVinci Resolve 20/21** and **Adobe After Effects**, disrupting legacy **₹30,000+** bloated effect packages with lightweight, studio-grade OFX tools.
* **Executive Summary Document**: Published [`HRL_International_Eureka_Pitch_Summary.md`](./HRL_International_Eureka_Pitch_Summary.md) for direct competition upload.

### 5.  Official Brand Accent `#D1002D`
* Updated the primary hero eyebrow headline **"HRL International Private Limited"** to brand color code `#D1002D` (Crimson Red).

### 6.  Enriched Bento Cards & Clean Architecture
* Removed redundant inline blue links from inside the three Bento cards.
* Enriched each card with deep, technical capability data (DaVinci Resolve 21 OFX plugins, multi-channel monetization across 2.5M+ views, Kafka stream computing, REST APIs).

### 7.  `/liquid-v2` Physics Engine & Unified Smart Play/Pause Button
* **`/liquid-v2` Canvas Engine**: Upgraded fluid frequencies with 6 harmonic plasma metablobs, chromatic dispersion flares, 24 orbital sound-wave spectrum bars, and smooth cubic Chladni nodal curves.
* **Unified Smart Action Pill**: Replaced separate play and stop buttons with a single smart toggle button (` Play Voice`  ` Stop Voice` with active pulsing crimson aura).

### 8.  Voice Character: "Priyanka - Calm, Neutral and Relaxed"
* Replaced Antoni with **Priyanka** in the Voice AI Studio.
* Implemented **character-specific acoustic mapping** so Priyanka and Rachel are distinctly different:
  * **Priyanka**: Pitch `0.90`, Rate `0.88x`, British/Global velvety, calm narration.
  * **Rachel**: Pitch `1.10`, Rate `1.02x`, American bright, dynamic broadcaster.

### 9.  ElevenLabs MCP Server & Antigravity MCP Health (100% Fixed)
* Created standalone native JSON-RPC Python MCP server at `~/.gemini/config/elevenlabs_mcp_server.py`.
* Resolved `context` socket `ENOENT` error by removing stale socket proxy and routing context through `data-agent-kit`.
* Fixed `datacloud_dataproc_remote` region security violation.
* Created backwards-compatibility symlink `googlecloudtools.datacloud-0.7.2-universal -> 0.9.1-universal`.

### 10.  Continuous Deployment CI/CD Pipeline
* Configured automated GitHub Actions workflow (`.github/workflows/deploy.yml`) for instant worldwide deployment on every `git push`.
* Synced across `main` and `gh-pages` branches.
