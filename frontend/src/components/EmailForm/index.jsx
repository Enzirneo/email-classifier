import { useState } from "react";
import "./EmailForm.css";

export default function EmailForm() {
  const [emailText, setEmailText] = useState("");
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    if (file) formData.append("file", file);
    else formData.append("email_text", emailText);

    try {
      const res = await fetch("http://localhost:8000/api/classify", {
        method: "POST",
        body: file ? formData : JSON.stringify({ subject: "", body: emailText }),
        headers: file ? {} : { "Content-Type": "application/json" },
      });
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      console.error("Erro ao conectar com o backend:", err);
    }
  };

  return (
    <div className="chat-container">
      <form onSubmit={handleSubmit} className="chat-form">
        <textarea
          value={emailText}
          onChange={(e) => setEmailText(e.target.value)}
          placeholder="Digite ou cole o email aqui..."
        />
        <input
          type="file"
          accept=".txt,.pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button type="submit">Enviar</button>
      </form>

      {response && (
        <div className="chat-response">
          <div className="response-category">{response.category}</div>
          <div className="response-text">{response.suggested_reply}</div>
        </div>
      )}
    </div>
  );
}
