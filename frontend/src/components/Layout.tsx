import Sidebar from "./Sidebar";

interface Props {
  children: React.ReactNode;
}

export default function Layout({
  children,
}: Props) {
  return (
    <div>
      <Sidebar />

      <div
        style={{
          marginLeft: "260px",
          minHeight: "100vh",
          background: "#f8fafc",
        }}
      >
        <div
          style={{
            height: "70px",
            background: "white",
            display: "flex",
            alignItems: "center",
            padding: "0 30px",
            borderBottom: "1px solid #e2e8f0",
          }}
        >
          <h2>AI Legal Judgment Assistant</h2>
        </div>

        <div style={{ padding: "30px" }}>
          {children}
        </div>
      </div>
    </div>
  );
}