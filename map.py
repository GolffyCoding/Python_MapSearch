import tkinter as tk
from tkinter import messagebox
import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

def search_location():
    location_name = entry.get()
    if not location_name:
        messagebox.showerror("Input Error", "Please enter a location.")
        return
    
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(location_name)
    
    if location:
        latitude = location.latitude
        longitude = location.longitude
        
        # Create a map centered on the user's location
        map_object = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], popup=location_name).add_to(map_object)
        
        # Save map to an HTML file
        map_file = "map.html"
        map_object.save(map_file)
        
        # Display map in browser
        import webbrowser
        webbrowser.open(map_file)
    else:
        messagebox.showerror("Location Error", "Location not found. Please try again.")

# Create a simple GUI using tkinter
root = tk.Tk()
root.title("Location Map Search")

# Create an input field and button
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Enter a location:")
label.grid(row=0, column=0, pady=5)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, pady=5)

search_button = tk.Button(frame, text="Search", command=search_location)
search_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
