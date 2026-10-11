    const input = document.getElementById('prompt');
    const button = document.getElementById('send');
    const chat = document.getElementById('chat');

    async function sendPrompt() {
      const prompt = input.value;
      if (!prompt) return;

      chat.innerHTML += `<p><b>Ty:</b> ${prompt}</p>`;
      input.value = '';

      const response = await fetch('http://localhost:8000/ollama/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: prompt })
      });

      const data = await response.json();
      chat.innerHTML += `<p><b>Model:</b> ${data.content}</p>`;
    }

    button.addEventListener('click', sendPrompt);
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') sendPrompt();
    });