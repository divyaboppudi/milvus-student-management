import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const formatResponse = (response) => {
    if (!Array.isArray(response)) {
      return JSON.stringify(response, null, 2);
    }

    return response
      .map((item) => {
        const payload = item.payload || {};

        return `
📋 Name: ${payload.name || "N/A"}

🏷️ Type: ${payload.entity_type || "N/A"}

🎓 Grade: ${payload.grade || "N/A"}

🏢 Department: ${payload.department || "N/A"}

📚 Subjects: ${
          payload.subjects
            ? payload.subjects.join(", ")
            : "N/A"
        }

📞 Phone: ${
          payload.phone_number || "N/A"
        }

────────────────────────────
`;
      })
      .join("\n");
  };

  const handleAsk = async () => {
    if (!question.trim()) {
      return;
    }

    const currentQuestion = question;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: currentQuestion,
      },
    ]);

    setQuestion("");
    setLoading(true);

    try {
      const result = await fetch(
        `http://localhost:8000/langgraph/chat?question=${encodeURIComponent(
          currentQuestion
        )}`,
        {
          method: "POST",
        }
      );

      const data = await result.json();

      console.log("Response:", data);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: formatResponse(
            data.response
          ),
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "❌ Error communicating with backend.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "1000px",
        margin: "0 auto",
        padding: "20px",
      }}
    >
      <h1>
        🎓 Milvus Student Management System
      </h1>

      <div
        style={{
          border: "1px solid #ddd",
          borderRadius: "10px",
          padding: "20px",
          height: "550px",
          overflowY: "auto",
          marginBottom: "20px",
        }}
      >
        {messages.map((message, index) => (
          <div
            key={index}
            style={{
              marginBottom: "20px",
            }}
          >
            <h3>
              {message.role === "user"
                ? "You"
                : "Assistant"}
            </h3>

            <pre
              style={{
                whiteSpace: "pre-wrap",
                wordWrap: "break-word",
                background:
                  message.role === "user"
                    ? "#dbeafe"
                    : "#f4f4f4",
                padding: "12px",
                borderRadius: "8px",
              }}
            >
              {message.content}
            </pre>
          </div>
        ))}

        {loading && (
          <div>
            <h3>Assistant</h3>

            <div
              style={{
                background: "#f4f4f4",
                padding: "12px",
                borderRadius: "8px",
              }}
            >
              Loading...
            </div>
          </div>
        )}
      </div>

      <div>
        <input
          type="text"
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
          placeholder="Ask anything..."
          style={{
            width: "80%",
            padding: "12px",
            fontSize: "16px",
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleAsk();
            }
          }}
        />

        <button
          onClick={handleAsk}
          style={{
            marginLeft: "10px",
            padding: "12px 20px",
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;