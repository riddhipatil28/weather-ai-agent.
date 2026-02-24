import { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./App.css";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  // ===============================
  // LOAD FIRST 4 MESSAGES ON START
  // ===============================
  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:5000/history");
      setMessages(res.data);
    } catch {
      console.log("No history yet");
    }
  };

  // ===============================
  // SEND MESSAGE
  // ===============================
  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", text: input };
    setMessages(prev => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:5000/chat", {
        message: userMsg.text
      });

      const botMsg = { role: "assistant", text: res.data.reply };
      setMessages(prev => [...prev, botMsg]);

    } catch {
      setMessages(prev => [...prev, {
        role: "assistant",
        text: "Server not responding"
      }]);
    }

    setLoading(false);
  };

  // ===============================
  // AUTO SCROLL
  // ===============================
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  // ===============================
  return (
    <div className="app">

      <div className="header">
        AI Weather Assistant
      </div>

      <div className="chat">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            {msg.text}
          </div>
        ))}

        {loading && (
          <div className="message assistant typing">
            Thinking...
          </div>
        )}

        <div ref={bottomRef}></div>
      </div>

      <div className="inputArea">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && sendMessage()}
          placeholder="Message AI assistant..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>

    </div>
  );
}
