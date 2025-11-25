from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import requests

st.set_page_config('Pokemon Stats Data', '📊', layout='wide')
st.title('Pokemon Stats')

@st.cache_data
def scrape_pokemon_stats():
    
    # Task 1: Scrape the pokemon stats from the website amd process into a dataframe
    # Paste your code from Part 1 here ===============================================================================================================
    html_string = requests.get("https://pokemondb.net/pokedex/stats/height-weight")
    soup = BeautifulSoup(html_string.content, 'html.parser')
    
    tb = soup.select_one("table")
    pokemons = tb.select("tbody tr")
    pokemons_clean = [[p.select_one("img")["src"]] + [i.get_text().strip() for i in p.select("td")] for p in pokemons]
    
    pokemon_db = pd.DataFrame(pokemons_clean, columns=["Image", "Number", "Name", "Type", "Height (ft)", "Height (m)", "Weight (lbs)", "Weight (kg)", "BMI"])
    
    pokemon_db["Height (m)"] = pokemon_db["Height (m)"].astype(float)
    pokemon_db["Weight (kg)"] = pokemon_db["Weight (kg)"].astype(float)
    
    pokemon_db[['Type 1', 'Type 2']] = pokemon_db['Type'].str.split(' ', expand=True, n=1)

	print pokemon_db.head()
    
    return pokemon_db.loc[:, ["Image", "Number", "Name", "Type", "Height (m)", "Weight (kg)", "BMI", "Type 1", "Type 2"]]

    # Paste your code from Part 1 here ===============================================================================================================

# This function processes the pokemon types to create a type combination matrix
# e.g.
# Type 2	Bug	Dark	Dragon	Electric	...
# Type 1																		
# Bug	    25	1	0	...
# Dark	    0	16	4	...
# Dragon	0	1	13	...
# Electric	0	2	4	...
# ...
# We will use the matrix stored in types to create a bar chart showing the counts of each type combination
@st.cache_data
def process_pokemon_types(df):
    # Extract type 1 and type 2 into separate columns

    df["Type 2"].fillna(df["Type 1"], inplace=True)
    
    types = df[["Type 1", "Type 2"]].groupby(["Type 1", "Type 2"]).size().unstack(fill_value=0)
    
    return types

df = scrape_pokemon_stats()
typing = process_pokemon_types(df)
colors = {
	"normal": '#A8A77A',
	"fire": '#EE8130',
	"water": '#6390F0',
	"electric": '#F7D02C',
	"grass": '#7AC74C',
	"ice": '#96D9D6',
	"fighting": '#C22E28',
	"poison": '#A33EA1',
	"ground": '#E2BF65',
	"flying": '#A98FF3',
	"psychic": '#F95587',
	"bug": '#A6B91A',
	"rock": '#B6A136',
	"ghost": '#735797',
	"dragon": '#6F35FC',
	"dark": '#705746',
	"steel": '#B7B7CE',
	"fairy": '#D685AD',
}

# Task 2: Preprocess color for the color argumet
# Paste your code from Part 2 here ===============================================================================================================

color = [colors[i.lower()] for i in typing.index]

# ================================================================================================================================================

# Task 3: Create a bar chart showing the counts of each type combination
# Here we create a bar chart using the typing dataframe created above and the color list created in Task 2
# Find out in the documentation how to pass a list of colors to the bar_chart function: https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart
# Enter your code below ===========================================================================================================================

st.bar_chart(typing, color=color)

# =================================================================================================================================================

# We create two columns here, the argument [3,2] means the first column is 3/5 of the page width and the second column is 2/5 of the page width
# Refer to https://docs.streamlit.io/develop/api-reference/layout/st.columns for more information
col1, col2 = st.columns([3,2])

# Task 4: Preprocess options for the pills widget
# Paste your code from Part 4 here ================================================================================================================
options = typing.index.tolist()
# =================================================================================================================================================

# Task 5: Create a pills widget to filter by types which will be used to filter the scatter plot and data table later
# Find out in the documentation how to create a pills widget: https://docs.streamlit.io/develop/api-reference/widgets/st.pills
# The few arguements you should set to replicate the intended behavior are:
# - label: str - A short label explaining to the user what this widget is for.
# - options: list - A list of options to choose from
# - selection_mode: 'single' | 'multi' - Whether the user can select a single option or multiple options. Which one did I use here?
# - default: list - The default selected option(s)
# - width: 'content' | 'stretch' | int - The width of the pills component. Which one did I use here?
# return type: list - The selected option(s) will be returned by this function. Store it in a variable called chosen_type
# Enter your code below ===========================================================================================================================
chosen_type = col2.pills("Filter by types", options=options, selection_mode='multi', default=options, width='content',)

# =================================================================================================================================================

# Task 5: Check if chosen_type is not empty before creating the scatter plot and data table
# First we check if chosen_type is not empty
# If chosen_type is empty, we do not display anything
# If chosen_type is not empty, we create a scatter plot and data table which are filtered
# Create an if statement to check if chosen_type is not empty here: ===============================================================================
if chosen_type:
    
    # This part should be inside the if statement
    # Task 6: Filter the dataframe df to include only rows where Type 1 or Type 2 is in chosen_type
    # Paste your code from Part 6 here ============================================================================================================
    
    filtered_df = df[df["Type 1"].isin(chosen_type) | df["Type 2"].isin(chosen_type)]
    
    # =============================================================================================================================================

    # Task 7: Create a data table in col1 with the filtered dataframe
    # First look back at the documentation for st.columns to see how to create a data table inside a column: https://docs.streamlit.io/develop/api-reference/layout/st.columns. There are 2 notations you can use: the `with` keyword or directly calling col1.dataframe.
    # Find out in the documentation how to create a data table: https://docs.streamlit.io/develop/api-reference/data/st.dataframe
    # The few arguements you should set to replicate the intended behavior are:
    # - data: pd.DataFrame - The data to be displayed
    # - column_config: dict - A dictionary mapping column names to column configuration objects. Here we use st.column_config.ImageColumn to display the images in the "Image" column. Your argument should be: {"Image": st.column_config.ImageColumn("Image",help="Pokemon Image",width=50)}
    # Enter your code below ========================================================================================================================
    col1.dataframe(filtered_df["Image", "Number", "Name", "Type", "Height (m)", "Weight (kg)", "BMI"], column_config={
        "Image": st.column_config.ImageColumn(
            "Image",
            help="Pokemon Image",
            width=50
        )
    }, height=700)

    # Task 8: Create a scatter plot in col2 with the filtered dataframe
    # First look back at the documentation for st.columns to see how to create a data table inside a column: https://docs.streamlit.io/develop/api-reference/layout/st.columns. There are 2 notations you can use: the `with` keyword or directly calling col2.scatter_chart.
    # Find out in the documentation how to create a scatter plot: https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart
    # The few arguements you should set to replicate the intended behavior are:
    # - data: pd.DataFrame - The data to be visualized
    # - x: str - The column name to be used for the x-axis
    # - y: str - The column name to be used for the y-axis
    # - color: str - The column name to be used for the color of the points. Here we use "Name" to give each pokemon a different color.
    # Enter your code below ========================================================================================================================
    col2.scatter_chart(filtered_df, x="Height (m)", y="Weight (kg)", color="Name", height=600)

    # ==============================================================================================================================================
    
    # =============================================================================================================================================
    
    # Task 9: Designing your own Streamlit app (OPTIONAL)
    # You can add more widgets and visualizations to make your app more interactive and informative
    # For example, you can add a slider to filter by height or weight, or a histogram to show the distribution of BMI
    # You can rearrage the layout to make it more appealing
    # Be creative and have fun!
    
# =================================================================================================================================================

