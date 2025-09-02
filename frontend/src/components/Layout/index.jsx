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
    let classificationData = null;

    // Sempre envia o texto para o backend
    if (emailText) {
      try {
        const res = await fetch("http://localhost:8000/api/classify", {
          method: "POST",
          body: JSON.stringify({ subject: "", body: emailText }),
          headers: { "Content-Type": "application/json" },
        });
        const data = await res.json();
        setResponse(data);
        classificationData = data;
      } catch (err) {
        console.error("Erro ao conectar com o backend:", err);
      }
    }

    // Adiciona o email ao estado
    setEmails(prev => [
      {
        subject: classificationData?.subject || "",
        body: emailText,
        category: classificationData?.category || "",
        confidence: classificationData?.confidence || null,
        suggested_reply: classificationData?.suggested_reply || "",
        provider: classificationData?.provider || "",
        timestamp: new Date().toLocaleString(),
        file,
        fileName: file?.name || null,
        fileUrl: file ? URL.createObjectURL(file) : null,
      },
      ...prev
    ]);
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
