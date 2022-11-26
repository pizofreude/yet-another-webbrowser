# yet-another-webbrowser

Using established web browser the likes of Google Chrome, Safari and so on is too mainstream.

Why allow web tracker when we can opt for privacy. Long live GDPR!

Henceforth, YaWB!

Search engine: [Brave](https://brave.com/search/)

## Necessary libraries/modules

1. PyQt5 - `pip install PyQt5`
2. PyQt5WebEngine (5.15.6)- `pip install PyQtWebEngine`

## Project Structure

1. Installing PyQt5 and PyQt5WebEngine
   - PyQt5 is a module for building Graphical User Interface apps in python.
   - PyQt5WebEngine framework embeds the web content in the application.
2. Importing modules
3. Creating a class
4. Creating various buttons on the top of the window
5. App Initialization

## Bugs

- Internal bug

  ```mingw-w64
  $ py barebone-web-browser.py
  js: Unrecognized feature: 'clipboard-write'.
  js: The resource https://i.ytimg.com/generate_204 was preloaded using link preload but not used within a few seconds from the window's load event. Please make sure it has an appropriate `as` value and it is preloaded intentionally.
  js: 'HTMLVideoElement.webkitExitFullscreen()' is deprecated. Please use 'Document.exitFullscreen()' instead.

  ```

- Add blocker none existent
- Fullscreen in YouTube not functioning

## Contributing

Feel free to fork, git clone, git checkout -b feature-name, git remote add upstream, git add ., git commit -m "your-message", git push origin main, create a pull request in GitHub.

Thanks in advance for your awesome contribution!
