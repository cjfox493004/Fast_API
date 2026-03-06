const button = document.getElementById('generateBtn');
const numberDiv = document.getElementById('number');

button.addEventListener('click', async () => {
    try {
        const res = await fetch('/randint');
        if (!res.ok) throw new Error('Network response was not ok');
        const data = await res.json();
        numberDiv.textContent = data;
    } catch (err) {
        numberDiv.textContent = 'Error';
        console.error(err);
    }
});

// optional: fetch on load
// window.addEventListener('load', () => button.click());
