import { useState } from "react";
import { askAI } from "../services/weatherService";

export default function AgentChat() {
  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);

  const send = async () => {
    if (!msg) return;

    const res = await askAI(msg);

    setChat([...chat, { user: msg, ai: res.reply }]);
    setMsg("");
  };

  return (
    <div className="chat-box">
      <h3>AI Weather Agent</h3>

      {chat.map((c, i) => (
        <div key={i}>
          <p><b>You:</b> {c.user}</p>
          <p><b>AI:</b> {c.ai}</p>
          <hr />
        </div>
      ))}

      <input
        value={msg}
        onChange={(e) => setMsg(e.target.value)}
        placeholder="Ask weather..."
      />
      <button onClick={send}>Send</button>
    </div>
  );
}
