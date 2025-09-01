import "./EmailCard.css";

export default function EmailCard({ email }) {
  const formattedDate = email.date ? new Date(email.date).toLocaleString() : "";

  return (
    <div className="email-card">
      <div className="email-header">
        <span className="email-subject">{email.subject || "Sem assunto"}</span>
        <button className={`email-category ${email.category.toLowerCase()}`}>
          {email.category}
        </button>
      </div>
      <div className="email-body">{email.body}</div>
      <div className="email-footer">{formattedDate}</div>
    </div>
  );
}
