# FreeGPTAPI - Unofficial API for ChatGPT

FreeGPT is a Python script that allows interaction with ChatGPT via a headless Firefox browser, automating queries and retrieving responses programmatically.

## Setup Instructions

1. **Install Dependencies:**
   - Ensure you have Python 3.x installed.
   - Install Selenium: `pip install selenium`.

2. **Download Geckodriver:**
   - Download Geckodriver from [Mozilla's Github page](https://github.com/mozilla/geckodriver/releases).
   - Place the executable (`geckodriver.exe` for Windows) in a directory accessible from your Python environment.

3. **Configure Firefox Profile:**
   - Ensure Firefox is installed.
   - Identify your Firefox profile directory (`profile_path` in the script) where cookies and preferences are stored.

4. **Modify Script Variables:**
   - Update `driver_path`, `binary`, and `profile_path` variables in `freegpt.py` with your local paths.

## Script Capabilities

- **Automated Interaction:**
  - Sends a predefined question (`QUESTION`) to ChatGPT via a specified URL (`CHAT_GPT_URL`).
  - Retrieves and prints the response from ChatGPT.

- **Headless Mode:**
  - Runs Firefox in headless mode (`--headless` option) for background execution.

## Video Showcase

Watch the video below to see FreeGPT in action:



https://github.com/GoliathReaper/FreeGPTAPI/assets/77969919/21bff5af-682b-4b83-841c-94187f0c72da



## Usage

1. Modify the `QUESTION` variable in `freegpt.py` with your desired query.
2. Run `python freegpt.py`.
3. View the output response from ChatGPT in the terminal.

## Disclaimer

This script is an unofficial API and may not be endorsed or supported by OpenAI. Use responsibly and adhere to ChatGPT's usage policies.

## License

MIT License. See LICENSE file for details.
