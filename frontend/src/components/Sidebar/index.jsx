import "./Sidebar.css";

export default function Sidebar({ sidebarOpen, toggleSidebar, currentPage, setCurrentPage }) {
  return (
    <aside className={`sidebar ${sidebarOpen ? "open" : "collapsed"}`}>
      {/* Botões fixos do topo */}
      <div className="top-buttons">
        {/* Botão de EmailForm */}
        <button 
          className="email-btn" 
          onClick={() => setCurrentPage("novoEmail")}
        >
          📨
        </button>

        {/* Botão de toggle */}
        <button className="toggle-btn" onClick={toggleSidebar}>
          ☰
        </button>
      </div>

      {/* Navegação */}
      <nav>
        <button 
          className={currentPage === "produtivos" ? "active" : ""} 
          onClick={() => setCurrentPage("produtivos")}
        >
          <span className="icon">✅</span>
          <span className="text">Produtivos</span>
        </button>
        <button 
          className={currentPage === "improdutivos" ? "active" : ""} 
          onClick={() => setCurrentPage("improdutivos")}
        >
          <span className="icon">❌</span>
          <span className="text">Improdutivos</span>
        </button>
        <button 
          className={currentPage === "respondidos" ? "active" : ""} 
          onClick={() => setCurrentPage("respondidos")}
        >
          <span className="icon">📬</span>
          <span className="text">Respondidos</span>
        </button>
      </nav>
    </aside>
  );
}
