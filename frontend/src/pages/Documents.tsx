import Layout from "../components/Layout";

export default function Documents() {
  const docs = [
    "Civil Appeal.pdf",
    "Property Case.pdf",
    "Contract Law.pdf",
  ];

  return (
    <Layout>
      <h1>Documents</h1>

      {docs.map((doc) => (
        <div
          key={doc}
          style={{
            background: "white",
            padding: "15px",
            marginTop: "15px",
            borderRadius: "10px",
          }}
        >
          📄 {doc}
        </div>
      ))}
    </Layout>
  );
}