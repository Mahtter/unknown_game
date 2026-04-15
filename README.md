# LangQuest: Learning Languages through Interactive Gaming

LangQuest is an innovative, gamified software application designed to aid the process of learning human-spoken languages through interactive gameplay. Developed as a proof-of-concept for the Final Pi Project at Houston Christian University, this project won the **"Best Technical Award"** at the Final Pi Project Design Expo.

The application immerses players in an adventure where they must escape from an ominous mansion by gathering specific items while strategically navigating rooms and avoiding a mysterious entity.

## Features
* **Modular Architecture**: The system is split into a **Translation Module (TM)** and a **Game Module (GM)**, allowing the translation logic to be reused in other applications.
* **Dynamic Translation**: Integrated with the Google Translate API (via the `deep_translator` library) to process text and output translations in a target language.
* **Adjustable Difficulty**: Supports both individual word-level and full-sentence translation to cater to different proficiency levels.
* **Interactive Gameplay**: A text-based adventure featuring original pixel art, sound effects, and a "chase" mechanic where a mysterious entity tracks player movement and mistakes.
* **Integrated Minigames**: Engaging translation-based challenges required to collect key items.

## Authors
* **Colby E. Kurtz** – Undergraduate Cyber Engineering Student, Houston Christian University.
* **Matthew Z. Blanchard** – Undergraduate Cyber Engineering Student, Houston Christian University.
* **Marian K. Zaki** – Assistant Professor of Computer Science, Houston Christian University.

## Project Structure
* `Unknown_main.py`: The main game driver containing the Room and Game classes, GUI setup (Tkinter), and core gameplay logic.
* `TranslationProgram.py`: The backend Translation Module (TM) that handles API calls to Google Translate, frequency-based translation, and punctuation correction.
* `minigame.py`: Logic for random word and sentence generation used in the translation guessing games.
* `Languages.txt`: A reference list of supported languages and their corresponding ISO codes.
* `ASEE_Learning_Languages_through_Interactive_Gaming_FINAL.pdf`: The full technical paper presented to the American Society for Engineering Education.

## Installation & Prerequisites
To run LangQuest, you need Python installed along with the following libraries:

```bash
pip install deep_translator pygame wonderwords
```
*Note: `tkinter` is also required (usually included with standard Python installations).*

## How to Play
1.  **Start**: Run `Unknown_main.py` and type "start game" to begin.
2.  **Objective**: You must find and "take" the **key**, **chalice**, **book**, and **painting** to unlock the escape route.
3.  **Commands**:
    * `go [direction]` (e.g., north, south, east, west, secrettunnel).
    * `look [item]` (e.g., look piano, look rug).
    * `take [grabbable]` (e.g., take chalice).
    * `open inventory` to view your current items.
4.  **Survival**: Avoid backtracking to your previous room or making too much "noise" (taking too many actions), as the mysterious entity will catch you.

## Technical Architecture
* **Translation Module (TM)**: Uses regular expressions to split text into sentences or words and reconstructs them after translation to ensure original structures are preserved.
* **Game Module (GM)**: Manages the front-end, including rendering the GUI, handling user text input, and tracking player progress and state.

## Citation
If you use this work, please refer to the included technical paper:
> Kurtz, C. E., Blanchard, M. Z., & Zaki, M. K. (2025). *Learning Languages through Interactive Gaming*. American Society for Engineering Education (ASEE).
