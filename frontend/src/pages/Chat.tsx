import Layout from "../components/Layout";

export default function Chat() {
  return (
    <Layout>
      <h1>Legal Chat</h1>

      <div
        style={{
          background: "white",
          height: "500px",
          borderRadius: "15px",
          padding: "20px",
          overflowY: "auto",
        }}
      >
        <div>
          <b>You:</b> What is the final verdict?
        </div>

        <div
          style={{
            marginTop: "15px",
          }}
        >
          <b>AI:</b> The appeal was dismissed.
        </div>
      </div>

      <input
        placeholder="Ask legal question..."
        style={{
          width: "100%",
          marginTop: "15px",
          padding: "15px",
          borderRadius: "10px",
        }}
      />
    </Layout>
  );
}