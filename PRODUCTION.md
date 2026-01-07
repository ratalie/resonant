# Production Workflow - Resonant Bonds

Complete workflow for rendering MIDI files to audio and creating final video deliverables.

---

## 🎼 Rendering MIDI to Audio in Reaper

### Step 1: Import MIDI
1. Open **Reaper**
2. **File → Insert → Media File**
3. Navigate to `midi/` folder and select the `.mid` file
4. The MIDI track will appear in the timeline

### Step 2: Set Project Tempo
Configure the tempo for each track (double-click on BPM in toolbar):
- **Track 1**: 60 BPM
- **Track 2**: 56 BPM
- **Track 3**: 88 BPM
- **Track 4**: 52 BPM
- **Track 5**: 96 BPM

### Step 3: Add Virtual Instrument
1. Right-click on the track → **FX**
2. Add a soft piano or pad instrument (examples):
   - **LABS** by Spitfire Audio (free)
   - **Ample Piano Lite** (free)
   - Any piano/pad VST with ambient character
3. Adjust settings for soft, spacious sound

### Step 4: Set Tuning (Optional - for specific frequencies)
If creating frequency-specific versions:
1. Add **ReaPitch** plugin after the instrument
2. Set pitch shift in cents:
   - Track 1 (432 Hz): 0 cents (already at 432)
   - Track 2 (528 Hz): +31.77 cents
   - Track 3 (396 Hz): -151.32 cents
   - Track 4 (639 Hz): +68.83 cents
   - Track 5 (417 Hz): -57.66 cents

### Step 5: Mix Settings
- **Track fader**: -14 to -18 dB
- Add subtle **reverb** for spaciousness (Valhalla Supermassive or similar)
- Ensure **master peak** stays below -1 dB

### Step 6: Render to WAV
1. **File → Render** (or Ctrl+Alt+R)
2. Configure:
   - **Source**: Master mix
   - **Bounds**: Time selection (or full project)
   - **Format**: WAV
   - **Sample rate**: 44100 Hz
   - **Bit depth**: 24-bit
   - **Channels**: Stereo
3. **Directory**: Save to project's `audio/` folder
4. **File name**: `N_Healing_[Name]_Track[N].wav`

---

## 🔄 Automation Scripts

After rendering all 5 tracks to WAV, use the automation scripts:

### Create 5-Minute Audio Loops

```bash
cd resonant
python scripts/create_audio_loops.py
```

This script:
- Reads audio files from `audio/`
- Calculates exact loop count for 5 minutes without cuts
- Creates looped versions in `audio/loops/`
- Preserves audio quality with stream copy

### Generate Videos (Audio + Visual Background)

```bash
python scripts/create_videos.py
```

This script:
- Reads looped audio from `audio/loops/`
- Combines with `source video.mp4`
- Loops video to match audio duration
- Outputs H.264 videos to `videos/`
- Ready for YouTube upload

---

## 📤 Upload to YouTube

### Playlist Setup
1. Go to YouTube Studio
2. Create new playlist: "Resonant Bonds"
3. Set description with project overview

### Video Upload (for each track)
1. Upload video from `videos/`
2. **Title format**: `Track [N]: Healing [Name] - Resonant Bonds`
3. **Description template**:

```
[Track description from README]

Dedicated to [Name]

---

Resonant Bonds is a meditative music project created as a gift of presence and care.

Original frequency: [XXX Hz]
Also available in universal 432 Hz

---

🎵 Full Project: [GitHub link]
🌿 Con amor y presencia
```

4. **Tags**: ambient, meditation, healing music, 432hz, lofi, instrumental
5. **Visibility**: Choose "Unlisted" or "Public"
6. Add to "Resonant Bonds" playlist

### Video Settings
- **Category**: Music
- **Allow embedding**: Yes
- **Publish to subscriptions feed**: Your choice
- **Comments**: Enable or disable based on preference

---

## 📁 File Organization

Final project structure:

```
resonant/
├── scores/              # MusicXML partituras
├── midi/                # MIDI files
├── audio/               # Rendered WAV files (source)
│   └── loops/          # 5-minute looped versions
├── videos/              # Final videos for YouTube
├── scripts/             # Automation scripts
└── source video.mp4     # Visual background
```

---

## ✅ Production Checklist

### Phase 1: MIDI Conversion ✓
- [x] Track 1: Healing Clarity
- [x] Track 2: Healing Containment
- [x] Track 3: Healing Balance
- [x] Track 4: Healing Depth
- [x] Track 5: Healing Activation

### Phase 2: Audio Rendering
- [ ] Track 1 → WAV
- [ ] Track 2 → WAV
- [ ] Track 3 → WAV
- [ ] Track 4 → WAV
- [ ] Track 5 → WAV

### Phase 3: Loop Creation
- [ ] Run `create_audio_loops.py`
- [ ] Verify 5 looped files in `audio/loops/`

### Phase 4: Video Generation
- [ ] Run `create_videos.py`
- [ ] Verify 5 video files in `videos/`

### Phase 5: YouTube Upload
- [ ] Create playlist "Resonant Bonds"
- [ ] Upload Track 1 with description
- [ ] Upload Track 2 with description
- [ ] Upload Track 3 with description
- [ ] Upload Track 4 with description
- [ ] Upload Track 5 with description
- [ ] Configure visibility settings

---

*Documentation for Resonant Bonds project*
