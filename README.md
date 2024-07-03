# FreeGPTAPI - Unofficial API for ChatGPT

FreeGPTAPI ![_b706f79a-a156-4464-a43b-9b7c1d23a364](https://github.com/GoliathReaper/FreeGPTAPI/assets/77969919/a4224823-10a2-4c25-97c0-d4f4305f7eed)
is a Python script that allows interaction with ChatGPT via a headless Firefox browser, automating queries and retrieving responses programmatically.

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

Watch the video below to see FreeGPTAPI in action:



https://github.com/GoliathReaper/FreeGPTAPI/assets/77969919/6ac41a1f-bb44-4e19-a4c1-fe95a3620ea3



## Usage

1. Modify the `QUESTION` variable in `FreeGPTAPI.py` with your desired query.
2. Run `python FreeGPTAPI.py`.
3. View the output response from ChatGPT in the terminal.

## Disclaimer

This script is an unofficial API and may not be endorsed or supported by OpenAI. Use responsibly and adhere to ChatGPT's usage policies.

## License

MIT License. See LICENSE file for details.
