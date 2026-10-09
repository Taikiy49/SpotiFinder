<div align="center">
  <h1>SpotiFinder</h1>
  <p><strong>Flask music-discovery prototype that turns natural-language requests into Gemini suggestions and YouTube results.</strong></p>
  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-303840?style=flat-square" />
    <img alt="Flask" src="https://img.shields.io/badge/Flask-303840?style=flat-square" />
    <img alt="Gemini" src="https://img.shields.io/badge/Gemini-303840?style=flat-square" />
    <img alt="YouTube" src="https://img.shields.io/badge/YouTube-303840?style=flat-square" />
  </p>
  <p><a href="#overview">Overview</a> · <a href="#getting-started">Getting started</a> · <a href="#repository-map">Repository map</a></p>
</div>

---

## Overview

A natural-language music discovery experiment. Flask sends a request to Gemini for a song title, then looks up matching videos through the YouTube Data API.

## What’s inside

- Browser chat interface for describing a song or mood.
- Gemini-generated song-title suggestions.
- YouTube search results returned through a Flask JSON endpoint.

## Getting started

Use Python 3 and supply your own Gemini and YouTube Data API credentials:

```sh
python -m pip install Flask google-generativeai requests
export GEMINI_API_KEY="your-own-gemini-key"
export YOUTUBE_API_KEY="your-own-youtube-key"
python app.py
```

Open the local Flask development server. API usage requires provider access and available quota.

## Repository map

| Location | Purpose |
| --- | --- |
| [`app.py`](./app.py) | Flask routes and model interaction |
| [`youtube.py`](./youtube.py) | YouTube search helper |
| [`templates/`](./templates/) | Landing and chat pages |
| [`static/`](./static/) | Styles and images |

## Project status

Prototype. The current code searches YouTube; Spotify playlist creation and audio generation are not implemented. The historical Gemini model configuration may need updating. Previously committed API keys require rotation.
