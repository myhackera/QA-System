async function askQuestion() {
    const question = document.getElementById('question').value;
    const response = document.getElementById('response');
    
    if (!question) {
        response.textContent = 'Please enter a question';
        return;
    }

    try {
        response.textContent = 'Loading...';
        const result = await fetch('http://localhost:5001/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question })
        });

        const data = await result.json();
        response.textContent = data.answer;
    } catch (error) {
        response.textContent = 'Error: Could not get response from server';
        console.error('Error:', error);
    }
} 