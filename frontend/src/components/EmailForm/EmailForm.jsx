import { useState } from "react";

export default function EmailForm() {
  const [emailText, setEmailText] = useState("");
  const [response, setResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch("http://localhost:8000/api/classify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email_text: emailText }),
      });

      const data = await res.json();
      setResponse(data);
    } catch (err) {
      console.error("Erro ao conectar com o backend:", err);
    }
  };

  return (
    <div className="p-6 max-w-md mx-auto bg-white rounded shadow">
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <textarea
          value={emailText}
          onChange={(e) => setEmailText(e.target.value)}
          placeholder="Cole o email aqui"
          className="border p-2 rounded w-full"
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Enviar
        </button>
      </form>

      {response && (
        <div className="mt-4 p-4 border rounded bg-gray-50">
          <p><strong>Categoria:</strong> {response.category}</p>
          <p><strong>Resposta sugerida:</strong> {response.suggested_reply}</p>
        </div>
      )}
    </div>
  );
}
