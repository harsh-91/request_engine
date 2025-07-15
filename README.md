# Request Engine

A modular HTTPS request automation tool with TLS spoofing, proxy rotation, logging, and Prometheus metrics.

## Features

- 🔁 Rotating proxies (round-robin)
- 🧠 TLS fingerprint headers (Chrome/Firefox profiles)
- 📤 Async HTTPS requests using `httpx`
- 📄 Structured logging via `loguru`
- 📊 Prometheus metrics on `/metrics` (port 8000)

## Project Structure

