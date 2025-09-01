import { useState } from "react";
import EmailCard from "../EmailCard";
import "./EmailHistory.css";

export default function EmailHistory({ emails }) {
  const [filter, setFilter] = useState("todos"); // "todos", "produtivo", "improdutivo"

  // Filtra emails de acordo com o filtro selecionado
  const filteredEmails = emails.filter(email => {
    if (filter === "todos") return true;
    return email.category.toLowerCase() === filter;
  });

  return (
    <div className="email-history-container">
      <h1 className="history-title">Histórico de Emails</h1>

      {/* Filtros */}
      <div className="history-filters">
        <button 
          onClick={() => setFilter("todos")}
          className={filter === "todos" ? "active" : ""}
        >
          Todos
        </button>
        <button 
          onClick={() => setFilter("produtivo")}
          className={filter === "produtivo" ? "active" : ""}
        >
          Produtivo
        </button>
        <button 
          onClick={() => setFilter("improdutivo")}
          className={filter === "improdutivo" ? "active" : ""}
        >
          Improdutivo
        </button>
      </div>

      {/* Grid de emails */}
      {filteredEmails.length === 0 ? (
        <p className="no-emails">Nenhum email no histórico.</p>
      ) : (
        <div className="email-history-grid">
          {filteredEmails.map((email, index) => (
            <EmailCard key={index} email={email} />
          ))}
        </div>
      )}
    </div>
  );
}
