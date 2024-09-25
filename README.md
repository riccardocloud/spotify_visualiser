# PLAYLIST VISUALISER

#### Video Demo: https://youtu.be/pyXGtBLXjQ4
#### Project Title: playlist_visualiser
#### Name: Riccardo Murciano
#### GitHub username: riccardocloud
#### HarvardX username: riccardomurciano
#### City: Rotterdam
#### Country: Netherlands
#### Recording Date: 25.09.2024

## 1. Overview

This Python-based program allows you to fet insights into your Spotify playlists by visualising the different features of its tracks. Such features include:

1. Energy
2. Danceability
3. Acousticness
4. Instrumentalness
5. Liveness
6. Speechiness
7. Valence

The program fetches track data using the openly available Spotify API, allowing the user to then visualise the data on a comprehensive scatterplot for track comparison on 2 dimensions of choice (i.e. energy and danceability).

[Spotify's Web API documentation](https://developer.spotify.com/documentation/web-api/reference/get-audio-features) offers a great overview of the 12 available audio features per track. As per simplicity, this program includes solely the ones that range for 0 to 1, to allow simple visualisation without the need for normalisation techniques.

The inspiration for this project comes from a strong desire to be able to access and experiment with unreleased functionalities provided by Spotify, but not available on the main application available on our smartphone and desktop interfaces. As a developer-beta enthusiast, I wanted a simple way to explore my playlists based on features that matter most to me. The potential behind this program also resides in having a way to "find your best songs based on audio characteristics".

I hope you will have fun using this program and feel free to continue reading if you want to know more about how to set everything up! Cheers!

## 2. Features

- **Spotify Integration**: Fetches Spotify playlists and track data via the Spotify API.
- **Customizable Visualization**: Choose two audio features (e.g., energy, danceability) to visualize on a scatter-plot.
- **Interactive Plot**: Generates an HTML scatter plot with clickable links to individual Spotify tracks.
- **Future Potential**: Could be expanded into a program that finds your favorite songs based on specific features, though this would require additional sorting algorithms.

## Prerequisites

To run this program, you'll need:

- Python 3.x
- A Spotify Developer account to get your own `client_id` and `client_secret` from the Spotify API Dashboard.
- The following Python libraries:
    - `requests`
    - `plotly`
    - `pyfiglet`
    - `re`

Install dependencies via `pip`:

```bash
pip install requests plotly pyfiglet
```

## Setup

1. **Clone the repository**:

```bash
git clone github.com/riccardocloud/spotify_visualiser.git cd playlist-visualiser
```

2. **Set up Spotify API credentials**:

Replace the `client_id` and `client_secret` in the code with your own from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

3. **Run the program**:

 ```bash
python spotify_visualiser.py
```

## How to Use

1. **Start the program**:
	- The program will prompt you for a Spotify playlist URL.

2. **Enter your playlist URL**:
	- Paste the Spotify playlist URL (e.g., `https://open.spotify.com/playlist/xyz`) into the terminal.

3. **Confirm the playlist name**:
	- The program will retrieve and display the playlist name. Confirm if the playlist is correct.

4. **Choose audio features**:
	- Select two audio features from the ones available to compare in a scatter plot:

5. **View the plot**:
	- The program generates an HTML scatter plot file, which will automatically open in your default browser.
	- If you click on the track names, a hyperlink will redirect you and play the song on spotify on your desktop of mobile device!

> [!NOTE] Beware!
> if ran locally on windows or mac, linux-based VMs will only create the file and then it's up to you to download it and open it in your browser

## Debugging and Development Notes

During development, this code snippet was used to check what data was being retrieved from the API. The data retrieved was always in JSON format, containing embedded lists of dictionaries.

```python
with open('api_call.txt', 'w') as file:
    json.dump(audio_features, file, indent=4)
```

This snippet writes the retrieved audio features to a file (`api_call.txt`) for inspection, helping ensure that the data structure is as expected.

## Example Output

![[README.md CS50P.png|631]]

## Future Directions

This project can be further developed to:

- Add more interactive features to the visualizations (i.e. choosing a plot type).
- Implement algorithms to suggest tracks based on personalized features.
- Integrate playlist sorting and analysis tools based on your preferred audio characteristics.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or new features.

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request for review.

## References and links:

_Web API Reference | Spotify for Developers_. [Online]. Available at: https://developer.spotify.com/documentation/web-api/reference/get-audio-features [Accessed 25 September 2024].

_Web API Reference | Spotify for Developers_. [Online]. Available at: https://developer.spotify.com/documentation/web-api/reference/get-audio-features [Accessed 25 September 2024].

_spotify-for-developers_. [Online]. Available at: https://developer.spotify.com/dashboard [Accessed 25 September 2024].

_Final Project - CS50’s Introduction to Programming with Python_. [Online]. Available at: https://cs50.harvard.edu/python/2022/project/ [Accessed 25 September 2024].

_plotly.graph_objects.Scatter — 5.24.1 documentation_. [Online]. Available at: https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html [Accessed 25 September 2024].

_plotly.graph_objects.Layout — 5.24.1 documentation_. [Online]. Available at: https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html [Accessed 25 September 2024].
