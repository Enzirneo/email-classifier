import { useState } from "react";
import "./EmailForm.css";

export default function EmailForm({ onSubmit }) {
  const [emailText, setEmailText] = useState("");
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Cria o objeto do email incluindo arquivo e link temporário
    const emailData = {
      emailText,
      file,
      fileName: file ? file.name : null,
      fileUrl: file ? URL.createObjectURL(file) : null, // link temporário
    };

    // Chama o onSubmit do Layout
    await onSubmit(emailData);

    // Limpa os campos
    setEmailText("");
    setFile(null);
  };

  return (
    <form onSubmit={handleSubmit} className="email-form">
      <div className="input-row">
        <div className="input-wrapper">
          <textarea
            value={emailText}
            onChange={(e) => {
              setEmailText(e.target.value);
              e.target.style.height = "auto"; // reseta altura antes de ajustar
              e.target.style.height = e.target.scrollHeight + "px"; // ajusta à altura do conteúdo
            }}
            placeholder="Digite ou cole o email aqui..."
            ref={(el) => {
              if (el && emailText === "") el.style.height = "44px"; // altura mínima
            }}
          />
        </div>
        <button type="submit" className="send-btn">➤</button>
      </div>

      {/* Upload de arquivo */}
      <label className="file-upload">
        📎 Anexar arquivo (.txt, .pdf)
        <input
          type="file"
          accept=".txt,.pdf"
          onChange={(e) => setFile(e.target.files[0])}
          hidden
        />
      </label>

      {/* Mostra visualmente o arquivo anexado */}
      {file && (
        <div className="file-info">
          Arquivo anexado: {file.name}
        </div>
      )}
    </form>
  );
}
