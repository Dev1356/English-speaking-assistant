const userEl = document.getElementById("user");
const botEl = document.getElementById("bot");

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = "en-US";
recognition.interimResults = false;

function startRecognition() {
  recognition.start();
}

recognition.onresult = async function(event) {
  const speech = event.results[0][0].transcript;
  userEl.textContent = "You: " + speech;

  // Send to backend
  const response = await fetch("/get-response", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: speech }),
  });

  const data = await response.json();
  const reply = data.reply;
  botEl.textContent = "Bot: " + reply;

  // Speak the response
  const utter = new SpeechSynthesisUtterance(reply);
  speechSynthesis.speak(utter);
};
