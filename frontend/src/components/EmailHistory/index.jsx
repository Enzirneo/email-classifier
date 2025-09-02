import { useState } from "react";
import EmailCard from "../EmailCard";
import "./EmailHistory.css";

export default function EmailHistory({ emails }) {
  const [filter, setFilter] = useState("todos");
  const [modalEmail, setModalEmail] = useState(null); // email atual do modal

  const filteredEmails = emails.filter(email => {
    if (filter === "todos") return true;
    return email.category?.toLowerCase() === filter;
  });

  return (
    <div className="email-history-container">
      <h1 className="history-title">Histórico de Emails</h1>

      {/* Filtros */}
      <div className="history-filters">
        <button onClick={() => setFilter("todos")} className={filter === "todos" ? "active" : ""}>Todos</button>
        <button onClick={() => setFilter("produtivo")} className={filter === "produtivo" ? "active" : ""}>Produtivo</button>
        <button onClick={() => setFilter("improdutivo")} className={filter === "improdutivo" ? "active" : ""}>Improdutivo</button>
      </div>

      {/* Grid de emails */}
      {filteredEmails.length === 0 ? (
        <p className="no-emails">Nenhum email no histórico.</p>
      ) : (
        <div className="email-history-grid">
          {filteredEmails.map((email, index) => (
            <EmailCard 
              key={index} 
              email={email} 
              onClick={() => setModalEmail(email)} // abre o modal
            />
          ))}
        </div>
      )}

      {/* Modal */}
      {modalEmail && (
        <div className="email-modal-overlay" onClick={() => setModalEmail(null)}>
          <div className="email-modal" onClick={e => e.stopPropagation()}>
            <button className="modal-close-btn" onClick={() => setModalEmail(null)}>×</button>
            <h2>{modalEmail.subject || "Sem assunto"}</h2>
            <p><strong>Categoria:</strong> {modalEmail.category || "Sem categoria"}</p>
            <p><strong>Corpo do Email:</strong></p>
            <p>{modalEmail.body || modalEmail.emailText}</p>

            {modalEmail.response && (
              <>
                <p><strong>Resposta sugerida:</strong></p>
                <p>{modalEmail.response}</p>
              </>
            )}

            {modalEmail.fileName && modalEmail.fileUrl && (
              <p>
                <strong>Anexo:</strong>{" "}
                <a href={modalEmail.fileUrl} download={modalEmail.fileName}>
                  {modalEmail.fileName}
                </a>
              </p>
            )}

            <p><strong>Data:</strong> {modalEmail.timestamp}</p>
          </div>
        </div>
      )}
    </div>
  );
}
