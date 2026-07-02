import Layout from "../components/Layout";

export default function Upload() {
  return (
    <Layout>
      <h1
        style={{
          marginBottom: "20px",
        }}
      >
        Upload Judgment
      </h1>

      <div
        style={{
          background: "white",
          padding: "40px",
          borderRadius: "15px",
          border: "2px dashed #94a3b8",
          textAlign: "center",
        }}
      >
        <h2>📄 Drop PDF Here</h2>

        <input
          type="file"
          style={{
            marginTop: "20px",
          }}
        />

        <br />

        <button
          style={{
            marginTop: "20px",
            padding:
              "10px 24px",
            background: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "8px",
          }}
        >
          Upload
        </button>
      </div>
    </Layout>
  );
}