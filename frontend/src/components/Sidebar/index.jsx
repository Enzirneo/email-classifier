import "./Sidebar.css";

export default function Sidebar({ sidebarOpen, toggleSidebar, currentPage, setCurrentPage }) {
  return (
    <aside className={`sidebar ${sidebarOpen ? "open" : "collapsed"}`}>
      {/* Botões fixos do topo */}
      <div className="top-buttons">
        {/* Botão de EmailForm */}
        <button 
          className="email-btn" 
          onClick={() => setCurrentPage("novoEmail")}>
          <span>📨</span>
        </button>

        {/* Botão de toggle */}
        <button className="toggle-btn" onClick={toggleSidebar}>
          ☰
        </button>
      </div>

      {/* Navegação */}
      <nav>
        <button 
          className={currentPage === "history" ? "active" : ""} 
          onClick={() => setCurrentPage("history")}
        >
          <span className="icon">📜</span>
          <span className="text">Histórico</span>
        </button>
      </nav>
    </aside>
  );
}
