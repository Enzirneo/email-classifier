import { useState } from "react";
import "./EmailForm.css";

export default function EmailForm({ onSubmit }) {
  const [emailText, setEmailText] = useState("");
  const [file, setFile] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ emailText, file });
  };

  return (
    <form onSubmit={handleSubmit} className="email-form">
      <div className="input-row">
        <div className="input-wrapper">
          <textarea
            value={emailText}
            onChange={(e) => {
              setEmailText(e.target.value);
              e.target.style.height = "auto";
              e.target.style.height = e.target.scrollHeight + "px";
            }}
            placeholder="Digite ou cole o email aqui..."
          />
        </div>
        <button type="submit" className="send-btn">➤</button>
      </div>

      <label className="file-upload">
        📎 Anexar arquivo (.txt, .pdf)
        <input
          type="file"
          accept=".txt,.pdf"
          onChange={(e) => setFile(e.target.files[0])}
          hidden
        />
      </label>
    </form>
  );
}
