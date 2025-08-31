import "./ChatResponse.css";

export default function ChatResponse({ response }) {
  if (!response) return null;

  return (
    <div className="chat-response">
      <div className="response-category">{response.category}</div>
      <div className="response-text">{response.suggested_reply}</div>
    </div>
  );
}
