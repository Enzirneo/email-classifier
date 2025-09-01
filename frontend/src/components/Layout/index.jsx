import { useState } from "react";
import Sidebar from "../Sidebar";
import EmailForm from "../EmailForm";
import ChatResponse from "../ChatResponse";
import EmailHistory from "../EmailHistory";
import "./Layout.css";

export default function Layout() {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [response, setResponse] = useState(null);

  const [currentPage, setCurrentPage] = useState("novoEmail"); 
  const [emails, setEmails] = useState([]);

  const handleEmailSubmit = async ({ emailText, file }) => {
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

      const newEmail = {
        subject: "",
        body: emailText,
        category: data.category,
        timestamp: new Date().toLocaleString(),
      };
      setEmails(prev => [newEmail, ...prev]);
      
    } catch (err) {
      console.error("Erro ao conectar com o backend:", err);
    }
  };

  return (
    <div className="app-container">
      <Sidebar
        sidebarOpen={sidebarOpen}
        toggleSidebar={() => setSidebarOpen(!sidebarOpen)}
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
      />

      <main className="main-content">
        {currentPage === "novoEmail" && (
          <>
            <h1>Classificador de Emails</h1>
            <EmailForm onSubmit={handleEmailSubmit} />
            <ChatResponse response={response} />
          </>
        )}

        {currentPage === "history" && (
          <EmailHistory emails={emails} />
        )}
      </main>
    </div>
  );
}
