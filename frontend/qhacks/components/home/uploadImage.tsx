"use client";
import { uploadLeafImage } from "@/lib/utils";
import React, { useEffect, useState } from "react";
import axios from "axios";

function UploadImage() {
  const [longitude, setLongitude] = useState(0);
  const [latitude, setLatitude] = useState(0);
  const [leafImage, setLeafImage] = useState<any>(null);
  const [cropLabel, setCropLabel] = useState("");
  const handleUpload = (event: any) => {
    setLeafImage(event.target.files[0]);
  };

  const submitForm = (e: any) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("leafImage", leafImage);
    formData.append("latitude", latitude.toString());
    formData.append("longitude", longitude.toString());
    formData.append("cropLabel", cropLabel);

    uploadLeafImage(formData);
  };

  useEffect(() => {
    if ("geolocation" in navigator) {
      const getLocation = () => {
        if ("geolocation" in navigator) {
          navigator.geolocation.getCurrentPosition(
            (position) => {
              // Success handler
              setLatitude(position.coords.latitude);
              setLongitude(position.coords.longitude);

              console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
              // Now you can use the latitude and longitude values
            },
            (error) => {
              // Error handler
              console.error("Error getting location: ", error);
              // Handle errors here (e.g., user denied location access)
            }
          );
        } else {
          console.log("Geolocation is not supported by this browser.");
          // Handle the case where the browser doesn't support Geolocation
        }
      };

      // Call the function to get the location
      getLocation();
    } else {
      // Geolocation API is not supported
      // Inform the user or handle the lack of support
    }
  }, []);

  return (
    <form onSubmit={submitForm}>
      <input type="text" />
      <input type="file" onChange={handleUpload} />
      <button type="submit">Upload Images</button>
    </form>
  );
}

export default UploadImage;
