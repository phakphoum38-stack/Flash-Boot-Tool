import React from "react";

export default function ProgressBar({ percent }) {
  return (
    <div style={{ background: "#eee", borderRadius: 20 }}>
      <div
        style={{
          width: `${percent}%`,
          padding: 10,
          background: "linear-gradient(90deg,#4facfe,#00f2fe)",
          borderRadius: 20,
          color: "#fff",
          textAlign: "center"
        }}
      >
        {percent.toFixed(1)}%
      </div>
    </div>
  );
}
