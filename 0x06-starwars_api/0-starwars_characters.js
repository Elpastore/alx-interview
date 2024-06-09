#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Function to fetch movie details and characters
function fetchMovieCharacters(movieId) {
    const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

    request(filmUrl, (error, response, body) => {
        if (error) {
            console.error('Error fetching movie details:', error);
            return;
        }

        if (response.statusCode !== 200) {
            console.error('Failed to retrieve movie details. Status code:', response.statusCode);
            return;
        }

        const filmData = JSON.parse(body);
        const characters = filmData.characters;

        characters.forEach(characterUrl => {
            request(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error('Error fetching character details:', charError);
                    return;
                }

                if (charResponse.statusCode !== 200) {
                    console.error('Failed to retrieve character details. Status code:', charResponse.statusCode);
                    return;
                }

                const characterData = JSON.parse(charBody);
                console.log(characterData.name);
            });
        });
    });
}

// Call the function with the provided movie ID
fetchMovieCharacters(movieId);
