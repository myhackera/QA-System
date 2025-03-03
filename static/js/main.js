async function askQuestion() {
    const question = document.getElementById('question').value;
    const response = document.getElementById('response');
    const button = document.querySelector('button');
    
    if (!question.trim()) {
        response.textContent = 'Please enter a question';
        response.classList.add('error');
        return;
    }

    try {
        button.disabled = true;
        response.classList.remove('error');
        response.innerHTML = '<div class="loading">Getting answer</div>';

        const result = await fetch('http://localhost:5001/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question })
        });

        const data = await result.json();
        
        if (data.error) {
            throw new Error(data.error);
        }

        response.innerHTML = formatResponse(data.answer);

    } catch (error) {
        response.innerHTML = `<div class="error">
            <i class="fas fa-exclamation-circle"></i>
            Error: ${error.message || 'Could not get response from server'}
        </div>`;
    } finally {
        button.disabled = false;
    }
}

function formatResponse(text) {
    // Add basic formatting to the response
    return text
        .split('\n')
        .map(line => `<p>${line}</p>`)
        .join('');
}

// Add keyboard shortcut (Ctrl/Cmd + Enter) to submit
document.getElementById('question').addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        askQuestion();
    }
}); 