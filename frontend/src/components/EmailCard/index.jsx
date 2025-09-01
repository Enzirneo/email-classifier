import "./EmailCard.css";

export default function EmailCard({ email, onClick }) {
  return (
    <div className="email-card" onClick={() => onClick(email)}>
      <div className="email-header">
        <span className="email-subject">{email.subject || "Sem assunto"}</span>
        <button className={`email-category ${email.category.toLowerCase()}`}>
          {email.category}
        </button>
      </div>

      <div className="email-body">
        {email.body.length > 100 ? email.body.slice(0, 100) + "..." : email.body}
      </div>

      <div className="email-footer">
        {email.date ? new Date(email.date).toLocaleString() : ""}
      </div>
    </div>
  );
}
