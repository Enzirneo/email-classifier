import "./ChatResponse.css";

export default function ChatResponse({ response }) {
  if (!response) return null;

  const categoryClass = response.category.toLowerCase();

  return (
    <div className={`chat-response ${categoryClass}`}>
      <div className="response-label">Resposta sugerida:</div>
      <div className="response-header">
        <span className={`response-category ${categoryClass}`}>
          {response.category}
        </span>
      </div>
      <div className="response-text">{response.suggested_reply}</div>
    </div>
  );
}
