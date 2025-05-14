# capstone-mtg-streamlit-app

Streamlit app for visualising data from the most recently updated list of Magic: The Gathering cards 06/05/2025

## Deployed App URL: https://mtgsetanalysis.streamlit.app/

| **As a...**              | **I want to...**                                                                 | **So that I can...**                                                                                   |
|---------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Magic: The Gathering fan | Explore the a dataset that only contains cards that have been printed in paper and only one version of said card               | get a sense of how sets were designed by looking at accurate data for each set without considering alternative arts and extra printings of the game piece.                                                     |
| Magic: The Gathering fan | Explore the distribution of mono-colored cards in a selected set                | Understand the prevalence of each color in the set                                                    |
| Magic: The Gathering fan | Explore the distribution of multi-colored cards in a selected set               | See how often different color combinations are used                                                   |
| Magic: The Gathering fan | View the most printed card in a selected set                                    | Learn which card has been reprinted the most and its significance                                     |
| Magic: The Gathering fan | Filter cards by set name                                                        | Focus on specific sets of interest                                                                    |
| Magic: The Gathering fan | View the count of different creature types in a selected set                    | Analyze the diversity of creatures in the set                                                         |
| Data analyst             | Replace unicode color characters with actual symbols from the game (e.g., ⚪, 🔵, ⚫, 🔴, 🟢)       | Easily interpret mana costs and card text visually                                                    |
| Magic: The Gathering fan | View the total number of cards in a selected set                                | Get an overview of the size of the set                                                                |
| Magic: The Gathering fan | Explore gameplay data such as mana cost, type, text, power, and toughness       | Gain insights into the gameplay mechanics of the cards                                                |
| Magic: The Gathering fan | Understand the distribution of card types (e.g., creatures, artifacts, spells)  | See which types of cards are most common in the selected set                                          |
| Magic: The Gathering fan | View the color identity distribution of cards                                   | Analyze how colors are represented across the selected set                                            |
| Magic: The Gathering fan | View visualizations of card data in an interactive format                       | Gain insights through engaging and easy-to-understand charts and tables                               |
| Magic: The Gathering fan | See Images of the cards when I mouse over them                       | Quickly get a sense of the card's theme check if I like the art, it would also make mroe visually engaging                               |

## Features
- Visualize mono-colored and multi-colored card distributions.
- Explore the most printed cards in a selected set.
- Analyze the diversity of creature types in a set.
- Filter cards by set name and view detailed gameplay data.
- Replace mana symbols with visual representations for better readability.
- Interactive charts and tables for engaging data exploration.
- Hover over cards to see their images for a more immersive experience.
  
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/capstone-mtg-streamlit-app.git

OR simply clone it on github with the URL

2. Navigate to the project directory:
    ```bash
    cd capstone-mtg-streamlit-app

3. Create a virtual environment:
   ```bash
    python -m venv venv
4. Activate Virtual Environment
   ```bash
    venv\Scripts\activate  #Windows
    source venv/bin/activate #macOS/Linux
5. Install Required Dependencies:
   ```bash
    pip install -r requirements.txt
6. Run the App:
   ```bash
    streamlit run mtg_streamlit/mtg_app.py

## ETL Pipeline
The ETL (Extract, Transform, Load) pipeline is used to process the raw Magic: The Gathering dataset into a cleaned format (`cleaned_cards.csv`) that is used by the app.

### Steps to Run the ETL Pipeline
1. Navigate to the ETL script directory:
   ```bash
   cd etl
2. Should you have a more up to date csv file containing more recently released sets, name it cards.csv and replace the older version in the data folder at the root of the directory
3. Remove the cleaned_cards.csv file from the data folder
4. Run the etl script called load.py
   ```bash
   python load.py
5. Verify that the cleaned dataset (cleaned_cards.csv) is generated in the data directory.


## Technologies Used (The tech stack, not to be confused with "The Stack")
- **Python**: Programming language for the app.
- **Streamlit**: Framework for building interactive web apps.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib/Seaborn**: Data visualization libraries.
- **Git**: Version control.

## Dataset
-The app uses a cleaned dataset of Magic: The Gathering cards, stored in [cleaned_cards.csv]
-Original Dataset found at https://mtgjson.com/downloads/all-files/
- I used the AllPrintingsCSVFiles as this was going to be the most difficult to clean