#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Use Promise.all to ensure correct order
    const characterPromises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
            return;
          }

          try {
            const characterData = JSON.parse(charBody);
            resolve(characterData.name);
          } catch (parseError) {
            reject(parseError);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((err) => console.error('Error fetching character data:', err));
  } catch (parseError) {
    console.error('Error parsing movie data:', parseError);
  }
});
