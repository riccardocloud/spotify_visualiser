import json
import requests
import plotly.graph_objs as go
import plotly.io as pio
import base64
import pyfiglet
import re


# Global variables
client_id = 'df1e2b4953fb469291e7211b63afc6db'
client_secret = 'db77c4ade47d4cc6aba9d740f60cae78'

def authenitcate(id,secret):
    encoded_credentials = base64.b64encode(f"{id}:{secret}".encode()).decode()
    auth_headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'client_credentials',
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers=auth_headers, data=data)
    access_token = response.json().get('access_token')
    return access_token


def starting_program():
    ascii_text = pyfiglet.figlet_format("PLAYLIST VISUALISER")
    signature = "By Riccardo Murciano"
    references = "email: riccardo.murciano@gmail.com"
    print(ascii_text)
    print(signature)
    print(references)

def main():
    starting_program()
    access_token = authenitcate(client_id, client_secret)
    headers = {'Authorization': f'Bearer {access_token}'}

    while True:
        playlist = input("Please paste your playlist's URL here: ")

        try:
            playlist_id = playlist_id_extractor(playlist)
        except AttributeError:
            print("Error: Invalid URL format. Please check and try again.")
            continue

        playlist_details_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
        playlist_response = requests.get(playlist_details_url, headers=headers)

        try:
            playlist_name = playlist_name_extractor(playlist_response)
        except Exception:
            print("Error: Unable to extract playlist name. Please try again.")
            continue

        confirm = input(f"Is your playlist: '{playlist_name}'? (y for yes, n for no): ").lower().strip()

        if confirm == 'y':
            input("Alright, now comes the exciting part!\nPress enter to continue...")

            while True:
                try:
                    user_input1 = int(input(f"You can choose between: \n[1] Energy \n[2] Danceability \n[3] Acousticness \n[4] Instrumentalness \n[5] Liveness \n[6] Speechiness \n[7] Valence: \n\nSo choose your first feature! \n\nFeature (i.e. 1 for Energy): ").strip())

                    if user_input1 not in range(1, 8):
                        raise ValueError("Feature must be between 1 and 7.")

                    user_input2 = int(input(f"Awesome! Now choose your second feature: \nFeature (i.e. 2 for Danceability): ").strip())

                    if user_input2 not in range(1, 8):
                        raise ValueError("Feature must be between 1 and 7.")

                    break  # Break out of the loop if both inputs are valid

                except ValueError:
                    print("Invalid input. Please provide a number between 1 and 7.")

            break
        else:
            print("Let's try again!")

    playlist_tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    response = requests.get(playlist_tracks_url, headers=headers)


    if response.status_code == 200:
        tracks_data = response.json()
        track_info = []


        # Extract track IDs, names, and URIs from the playlist data
        for item in tracks_data['items']:
            track = item['track']
            if track:  # Ensure track is not None
                track_info.append({
                    'id': track['id'],
                    'name': track['name'],
                    'uri': track['uri'],  # Track URI to create hyperlink
                })

        # Collect the track IDs into a comma-separated string
        ids_string = ','.join([track['id'] for track in track_info][:100])  # Max 100 track IDs per request
        # Step 3: Get audio features for the tracks
        audio_features_url = f'https://api.spotify.com/v1/audio-features?ids={ids_string}'
        features_response = requests.get(audio_features_url, headers=headers)

        if features_response.status_code == 200:
            audio_features = features_response.json()

            # Map audio features to track info by ID
            for track in track_info:
                for feature in audio_features['audio_features']:
                    if feature['id'] == track['id']:
                        track.update(feature)

            # Step 4: Plot the data using Plotly with hyperlinks and playlist title
            track_names = [f'<a href="https://open.spotify.com/track/{track["id"]}dnoLq?si=" target="_blank">{track["name"]}</a>' for track in track_info]  # Create hyperlinks
            energy = [track.get('energy', 0) for track in track_info]
            danceability = [track.get('danceability', 0) for track in track_info]
            acousticness = [track.get('acousticness', 0) for track in track_info]
            instrumentalness = [track.get('instrumentalness', 0) for track in track_info]
            liveness = [track.get('liveness', 0) for track in track_info]
            speechiness = [track.get('speechiness', 0) for track in track_info]
            valence = [track.get('valence', 0) for track in track_info]

            # User choice logic
            try:
                if user_input1 == 1:
                    x_axis_value = energy
                    x_axis_name = "Energy"
                elif user_input1 == 2:
                    x_axis_value = danceability
                    x_axis_name = "Danceability"
                elif user_input1 == 3:
                    x_axis_value = acousticness
                    x_axis_name = "Acousticness"
                elif user_input1 == 4:
                    x_axis_value = instrumentalness
                    x_axis_name = "instrumentalness"
                elif user_input1 == 5:
                    x_axis_value = liveness
                    x_axis_name = "Liveness"
                elif user_input1 == 6:
                    x_axis_value = speechiness
                    x_axis_name = "Speechiness"
                elif user_input1 == 7:
                    x_axis_value = valence
                    x_axis_name = "Valence"

                if user_input2 == 1:
                    y_axis_value = energy
                    y_axis_name = "Energy"
                elif user_input2 == 2:
                    y_axis_value = danceability
                    y_axis_name = "Danceability"
                elif user_input2 == 3:
                    y_axis_value = acousticness
                    y_axis_name = "Acousticness"
                elif user_input2 == 4:
                    y_axis_value = instrumentalness
                    y_axis_name = "Instrumentalness"
                elif user_input2 == 5:
                    y_axis_value = liveness
                    y_axis_name = "Liveness"
                elif user_input2 == 6:
                    y_axis_value = speechiness
                    y_axis_name = "Speechiness"
                elif user_input2 == 7:
                    y_axis_value = valence
                    y_axis_name = "Valence"
            except UnboundLocalError:
                print("",end="")

            # Creating the scatter plot
            scatter = go.Scatter(
                x=x_axis_value,
                y=y_axis_value,
                mode='markers+text',
                text=track_names,  # Display clickable track names
                hoverinfo='text',
                marker=dict(
                    size=12,
                    color='rgba(152, 0, 0, .8)',
                    line=dict(
                        width=2,
                    ),
                ),
                textposition='top center'
            )

            # Define layout with four quadrants and playlist title
            layout = go.Layout(
                title=f'Playlist: {playlist_name}',  # Display playlist title at the top
                xaxis=dict(
                    title=f"{x_axis_name} (Low to High)",
                    range=[0, 1],  # Ensure the x-axis is between 0 and 1
                    zeroline=True,
                    zerolinewidth=2,
                    zerolinecolor='black',
                    showgrid=True,
                    gridwidth=1,
                    gridcolor='LightGray'
                ),
                yaxis=dict(
                    title=f"{y_axis_name} (Low to High)",
                    range=[0, 1],  # Ensure the y-axis is between 0 and 1
                    zeroline=True,
                    zerolinewidth=2,
                    zerolinecolor='black',
                    showgrid=True,
                    gridwidth=1,
                    gridcolor='LightGray'
                ),
                shapes=[
                    # Horizontal line at y=0.5
                    dict(
                        type='line',
                        y0=0.5, y1=0.5,
                        x0=0, x1=1,
                        line=dict(color='black', width=2)
                    ),
                    # Vertical line at x=0.5
                    dict(
                        type='line',
                        x0=0.5, x1=0.5,
                        y0=0, y1=1,
                        line=dict(color='black', width=2)
                    )
                ],
                showlegend=False
            )

            fig = go.Figure(data=[scatter], layout=layout)

            # Save the plot as an HTML file
            filename = "spotify_tracks_scatter.html"
            pio.write_html(fig, file=filename, auto_open=True)

            print(f"HTML file with scatter plot created: {filename}")

        else:
            print(f"Error fetching audio features: {features_response.status_code}")


def playlist_id_extractor(url):
    match = re.search(r'playlist\/([a-zA-Z0-9]+)', url)
    while True:
        if match:
            return match.group(1)
        else:
            raise AttributeError("Not a valid Spotify playlist URL. Please check and try again.")

def playlist_name_extractor(response):
    if response.status_code == 200:
        print("Successful connection: retrieving playlist data...")
        playlist_details = response.json()
        playlist_name = playlist_details['name']
        return playlist_name
    else:
        print(f"Failed to retrieve playlist. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    main()
