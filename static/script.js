document.getElementById("chat-form").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;
  
    // Add user message to UI
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user-message">You: ${message}</div>`;
    input.value = "";
  
    // Show loading
    const loading = document.getElementById("loading-indicator");
    loading.classList.remove("hidden");
  
    try {
      const res = await fetch("/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
      });
  
      const data = await res.json();
      chatBox.innerHTML += `<div class="ai-message">AI: ${data.response}</div>`;
    } catch (err) {
      chatBox.innerHTML += `<div class="ai-message">⚠️ Error connecting to AI.</div>`;
    } finally {
      loading.classList.add("hidden");
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  });

  function appendMessage(sender, message) {
    const messageDiv = document.createElement("div");
    messageDiv.className = sender === "user" ? "user-message" : "ai-message";
    messageDiv.innerText = message.trim();  // Clean up spaces/newlines
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  