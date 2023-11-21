import instaloader

def download_profile_pictures(profile_name):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Get profile information
        profile = instaloader.Profile.from_username(loader.context, profile_name)

        # Iterate through the profile's posts and download images
        for post in profile.get_posts():
            loader.download_post(post, target=profile_name)

        print(f"All pictures from profile '{profile_name}' downloaded successfully.")

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'profile_name' with the desired Instagram profile username
    profile_name = '----- fill the user name here ------'
    
    download_profile_pictures(profile_name)
    
    
    # RUN SCRIPT WRITE:
    # python app.py
