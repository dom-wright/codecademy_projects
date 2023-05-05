# 🍿 Film Finder 🍿

## What is this?
A demonstration of HTTP requests using asynchronous JavaScript and the Fetch API. The Film Finder app allows the user to select a movie genre. It will then make a HTTP request to The Movie Database (TMDB) for a random movie from that genre, and present the returned information back on the page. The user can select whether they like or dislike the movie returned. The information will then clear from the page and another random movie will be fetched.

## Setup Instructions
#### API
1. Before using the application, you must [create an account](https://www.themoviedb.org/signup) on the The Movie Database (TMDB) website. 
2. After creating your account, click on your user icon in the top right, navigate to **Settings** and then **API** within. 
3. Request an API Key to register as a Developer. You may be asked to enter some personal information like your address and phone number.
4. Your API Key will be present under the **API Key (v3 auth)** header.

#### Clone Project
1. Clone this project to a local directory.
2. Navigate to the public folder and open **script.js**. Add your API Key to the 'tmdbKey' variable in the first line. Save and exit.
3. Open `index.html` in and give it a go.