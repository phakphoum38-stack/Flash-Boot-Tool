import { useState } from "react";

export default function App() {
  const [device, setDevice] = useState("");
  const [iso, setIso] = useState("");

  return (
    <div style={{ padding: 30, fontFamily: "sans-serif" }}>
      <h1>⚡ FlashForge</h1>

      <div>
        <h3>Select ISO</h3>
        <input
          type="text"
          placeholder="/path/windows.iso"
          onChange={(e) => setIso(e.target.value)}
        />
      </div>

      <div>
        <h3>Select USB</h3>
        <input
          type="text"
          placeholder="/dev/sdb"
          onChange={(e) => setDevice(e.target.value)}
        />
      </div>

      <button
        style={{ marginTop: 20, padding: 10 }}
        onClick={() => window.__TAURI__.invoke("flash_dd", { iso, device })}
      >
        Flash USB (Etcher Mode)
      </button>
    </div>
  );
}
