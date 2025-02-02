async function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let chatbox = document.getElementById("chatbox");

    if (userInput.trim() === "") return;

    chatbox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    let response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    });

    let data = await response.json();
    chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
    document.getElementById("userInput").value = "";
}
