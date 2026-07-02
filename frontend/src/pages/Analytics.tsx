import Layout from "../components/Layout";

export default function Analytics() {
  return (
    <Layout>
      <h1>Analytics</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(3,1fr)",
          gap: "20px",
        }}
      >
        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          Total Documents
          <h2>24</h2>
        </div>

        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          Total Sessions
          <h2>15</h2>
        </div>

        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          Queries
          <h2>84</h2>
        </div>
      </div>
    </Layout>
  );
}