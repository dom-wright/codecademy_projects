// information to reach API
const url = 'https://api.rebrandly.com/v1/links';

// Some page elements
const apiKeyField = document.querySelector('#key');
const inputField = document.querySelector('#input');
const shortenButton = document.querySelector('#shorten');
const responseField = document.querySelector('#responseField');

// AJAX functions
// Code goes here

const shortenUrl = async () => {
    const apiKey = apiKeyField.value;
    const urlToShorten = inputField.value;
    const data = JSON.stringify({
        destination: urlToShorten,
        domain: { "fullName": "rebrand.ly" }
    })
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: data,
            headers: {
                'Content-type': 'application/json',
                'apikey': apiKey
            }
        })
        if (response.ok) {
            const jsonResponse = await response.json()
            renderResponse(jsonResponse)
        }

    } catch (error) {
        console.log(error)
    }
}

// Clear page and call AJAX functions
const displayShortUrl = (event) => {
    event.preventDefault();
    while (responseField.firstChild) {
        responseField.removeChild(responseField.firstChild);
    }
    shortenUrl();
}

shortenButton.addEventListener('click', displayShortUrl);
