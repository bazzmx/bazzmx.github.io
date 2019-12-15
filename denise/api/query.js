function findSimilar(word, sense = 'auto') {
    const options = {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        credentials: 'same-origin',
        body: JSON.stringify({ word, sense })
    };
    fetch('/find', options)
        .then(res => res.json())
        .then(({ results }) => {
            console.log(results);
        });
}
