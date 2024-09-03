#!/usr/bin/node

const fetch = require('node-fetch');

const getCharacterNames = async (urls) => {
    for (const url of urls) {
        try {
            const response = await fetch(url);
            const data = await response.json();
            console.log(data.name);
        } catch (err) {
            console.error('Error:', err);
        }
    }
};

(async () => {
    try {
        const response = await fetch(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`);
        const data = await response.json();
        await getCharacterNames(data.characters);
    } catch (err) {
        console.error('Error:', err);
    }
})();
